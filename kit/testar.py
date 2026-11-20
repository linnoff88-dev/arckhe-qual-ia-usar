#!/usr/bin/env python3
"""Kit de testes: a mesma tarefa em várias IAs, com avaliação e custo por entrega certa.

Uso:
  python3 kit/testar.py <pasta-da-tarefa> [--motores kit/motores.json] [--so "Haiku,Sol"] [--repeticoes N]
                        [--juiz claude-cli:claude-sonnet-5-5] [--simular]

A pasta da tarefa tem um tarefa.json:
  {"nome": "comprovantes",
   "pedido": "texto do pedido"            (ou "pedido_arquivo": "pedido.md"),
   "criterio": "como é 'ficou certo'",
   "verificar": "python3 verificar.py",   (opcional: recebe o caminho da resposta; sai 0 = aprovada)
   "repeticoes": 3}

Cada motor em motores.json: {"modelo": "<nome em dados/precos-*.csv>", "via": "<via>", "id": "<id do modelo>"}
Vias:
  claude-cli   Claude Code pela assinatura (claude -p, sem ferramentas)
  codex-cli    Codex pela assinatura (codex exec, sandbox só leitura)
  agy          Antigravity CLI pela assinatura Google AI Pro/Ultra (agy -p)
  gemini-cli   Gemini CLI (gemini -p): só com chave de API paga; a assinatura individual migrou para o agy
  api-anthropic / api-openai / api-google   API paga, com ANTHROPIC_API_KEY / OPENAI_API_KEY / GEMINI_API_KEY
  openrouter   API do OpenRouter, com OPENROUTER_API_KEY
Saída: resultados/<data>-<nome>/ com as respostas, tentativas.csv (lido por calcular.py) e relatorio.md.
"""
import argparse, csv, datetime as dt, json, os, re, shlex, shutil, statistics, subprocess, sys, tempfile, time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PRECOS = sorted((RAIZ / 'dados').glob('precos-*.csv'))[-1]
TIMEOUT = int(os.environ.get('KIT_TIMEOUT', '600'))
CALIBRA = 'Responda apenas: ok'


# ---------- motores ----------
def _run(cmd, entrada, cwd, env=None):
    t0 = time.time()
    r = subprocess.run(cmd, input=entrada, capture_output=True, text=True, timeout=TIMEOUT, cwd=cwd,
                       env={**os.environ, **(env or {})})
    return r, time.time() - t0


def via_claude_cli(mid, pedido, cwd):
    cmd = ['claude', '-p', '--model', mid, '--output-format', 'json', '--no-session-persistence', '--tools', '',
           '--system-prompt', 'Você é um assistente. Faça o que o usuário pedir e entregue a resposta completa.',
           '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}', '--setting-sources', '']
    r, t = _run(cmd, pedido, cwd)
    d = json.loads(r.stdout)
    if d.get('is_error'):
        raise RuntimeError(str(d.get('result'))[:300])
    u = d.get('usage', {})
    ent = u.get('input_tokens', 0) + u.get('cache_creation_input_tokens', 0) + u.get('cache_read_input_tokens', 0)
    return d.get('result', ''), ent, u.get('output_tokens', 0), t


def via_codex_cli(mid, pedido, cwd):
    out = Path(cwd) / 'ultima.txt'
    cmd = ['codex', 'exec', '-m', mid, '--skip-git-repo-check', '--ephemeral', '-s', 'read-only', '--json', '-o', str(out), '-']
    r, t = _run(cmd, pedido, cwd)
    ent = sai = 0
    for linha in r.stdout.splitlines():
        if '"turn.completed"' in linha:
            u = json.loads(linha).get('usage', {})
            ent += u.get('input_tokens', 0)
            sai += u.get('output_tokens', 0) + u.get('reasoning_output_tokens', 0)
    if not out.exists():
        raise RuntimeError((r.stderr or r.stdout)[-300:])
    return out.read_text(encoding='utf-8'), ent, sai, t


def via_gemini_cli(mid, pedido, cwd):
    if not shutil.which('gemini'):
        raise RuntimeError('gemini CLI não instalado')
    r, t = _run(['gemini', '-m', mid, '-p', pedido, '--output-format', 'json'], '', cwd,
                {'GEMINI_CLI_TRUST_WORKSPACE': 'true', 'GOOGLE_GENAI_USE_GCA': os.environ.get('GOOGLE_GENAI_USE_GCA', 'true')})
    i = r.stdout.find('{')
    d = json.loads(r.stdout[i:]) if i >= 0 else {}
    if d.get('error') or not d:
        raise RuntimeError(str(d.get('error', {}).get('message') if d else (r.stderr or r.stdout)[-300:])[:300])
    ent = sai = 0
    for m in (d.get('stats', {}).get('models', {}) or {}).values():
        tk = m.get('tokens', {})
        ent += tk.get('prompt', 0)
        sai += tk.get('candidates', 0) + tk.get('thoughts', 0)
    return d.get('response', ''), ent, sai, t


def via_agy(mid, pedido, cwd):
    """Antigravity CLI pela assinatura Google AI Pro/Ultra (login: rodar `agy` uma vez)."""
    exe = shutil.which('agy') or os.path.expanduser('~/.local/bin/agy')
    r, t = _run([exe, '-p', pedido, '--model', mid, '--output-format', 'json', '--disable-slash-commands'], '', cwd)
    i = r.stdout.find('{')
    d = json.loads(r.stdout[i:]) if i >= 0 else {}
    if d.get('status') != 'SUCCESS':
        raise RuntimeError(str(d.get('error') or d.get('status') or (r.stderr or r.stdout)[-300:])[:300])
    u = d.get('usage', {})
    return d.get('response', ''), u.get('input_tokens', 0) + u.get('cache_read_tokens', 0), u.get('output_tokens', 0) + u.get('thinking_tokens', 0), t


def _post(url, corpo, cab):
    req = urllib.request.Request(url, data=json.dumps(corpo).encode(), headers={'content-type': 'application/json', **cab})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read()), time.time() - t0


def _chave(nome):
    v = os.environ.get(nome)
    if not v:
        raise RuntimeError(f'falta a variável {nome}')
    return v


def via_api_anthropic(mid, pedido, cwd):
    base = os.environ.get('ANTHROPIC_BASE_URL', 'https://api.anthropic.com')
    d, t = _post(f'{base}/v1/messages', {'model': mid, 'max_tokens': 16000, 'messages': [{'role': 'user', 'content': pedido}]},
                 {'x-api-key': _chave('ANTHROPIC_API_KEY'), 'anthropic-version': '2023-06-01'})
    txt = ''.join(b.get('text', '') for b in d.get('content', []) if b.get('type') == 'text')
    return txt, d['usage']['input_tokens'], d['usage']['output_tokens'], t


def _chat(url, chave, mid, pedido):
    d, t = _post(url, {'model': mid, 'messages': [{'role': 'user', 'content': pedido}]}, {'authorization': f'Bearer {chave}'})
    u = d.get('usage', {})
    return d['choices'][0]['message']['content'], u.get('prompt_tokens', 0), u.get('completion_tokens', 0), t


def via_api_openai(mid, pedido, cwd):
    base = os.environ.get('OPENAI_BASE_URL', 'https://api.openai.com')
    return _chat(f'{base}/v1/chat/completions', _chave('OPENAI_API_KEY'), mid, pedido)


def via_openrouter(mid, pedido, cwd):
    base = os.environ.get('OPENROUTER_BASE_URL', 'https://openrouter.ai/api')
    return _chat(f'{base}/v1/chat/completions', _chave('OPENROUTER_API_KEY'), mid, pedido)


def via_api_google(mid, pedido, cwd):
    base = os.environ.get('GEMINI_BASE_URL', 'https://generativelanguage.googleapis.com')
    d, t = _post(f'{base}/v1beta/models/{mid}:generateContent', {'contents': [{'parts': [{'text': pedido}]}]},
                 {'x-goog-api-key': _chave('GEMINI_API_KEY')})
    txt = ''.join(p.get('text', '') for p in d['candidates'][0]['content']['parts'])
    u = d.get('usageMetadata', {})
    return txt, u.get('promptTokenCount', 0), u.get('candidatesTokenCount', 0) + u.get('thoughtsTokenCount', 0), t


VIAS = {'claude-cli': via_claude_cli, 'codex-cli': via_codex_cli, 'gemini-cli': via_gemini_cli, 'agy': via_agy,
        'api-anthropic': via_api_anthropic, 'api-openai': via_api_openai, 'api-google': via_api_google,
        'openrouter': via_openrouter}
# vias em que o assistente acrescenta instruções próprias a cada pedido: medimos e descontamos
COM_SOBRECARGA = {'codex-cli', 'gemini-cli', 'claude-cli', 'agy'}


def chamar(motor, pedido):
    with tempfile.TemporaryDirectory(prefix='kit-') as d:
        return VIAS[motor['via']](motor['id'], pedido, d)


# ---------- avaliação ----------
JUIZ = """Você é um avaliador rigoroso. Compare a RESPOSTA com o CRITÉRIO de "ficou certo".
Aprove só se TODOS os pontos do critério forem cumpridos. Não dê pontos por estilo.
Responda SÓ com JSON: {{"aprovada": true|false, "nota": 0-10, "motivo": "uma frase"}}

PEDIDO:
{pedido}

CRITÉRIO:
{criterio}

RESPOSTA:
{resposta}"""


def julgar(juiz, pedido, criterio, resposta):
    txt, *_ = chamar(juiz, JUIZ.format(pedido=pedido, criterio=criterio, resposta=resposta[:60000]))
    m = re.search(r'\{.*\}', txt, re.S)
    d = json.loads(m.group(0)) if m else {}
    return bool(d.get('aprovada')), d.get('nota', ''), str(d.get('motivo', txt[:200]))


def verificar(cmd, pasta, arquivo):
    r = subprocess.run(shlex.split(cmd) + [str(arquivo)], cwd=pasta, capture_output=True, text=True, timeout=120)
    return r.returncode == 0, (r.stdout + r.stderr).strip()[-300:]


# ---------- relatório ----------
def precos():
    with open(PRECOS, encoding='utf-8') as f:
        return {l['modelo']: (float(l['usd_entrada_por_milhao']), float(l['usd_saida_por_milhao'])) for l in csv.DictReader(f)}


def relatorio(nome, linhas, saida, juiz, tem_verificador):
    por, erro = {}, {}
    for l in linhas:
        if l['aprovada'] == 'erro':
            erro.setdefault(l['modelo'], l['motivo'])
            continue
        por.setdefault(l['modelo'], []).append(l)
    tab = []
    for m, ls in por.items():
        ok = [l for l in ls if l['aprovada'] == 'sim']
        custo = sum(float(l['custo_usd'] or 0) for l in ls)
        tempo = statistics.median(float(l['tempo_s']) for l in ls)
        notas = [float(l['nota']) for l in ls if str(l['nota']).replace('.', '', 1).isdigit()]
        tab.append((m, len(ok), len(ls), custo / len(ok) if ok else None, tempo, statistics.mean(notas) if notas else None))
    tab.sort(key=lambda x: (x[3] is None, x[3] or 0, -x[1]))
    L = [f'# Teste: {nome}', '', f'{dt.datetime.now():%d/%m/%Y %H:%M} · juiz: {juiz["via"]}:{juiz["id"]}'
         + (' · com verificador automático' if tem_verificador else ''), '',
         '| Modelo | Certas | Taxa | US$ por entrega certa | Tempo mediano | Nota média |', '|---|---:|---:|---:|---:|---:|']
    for m, k, n, c, t, nt in tab:
        L.append(f'| {m} | {k}/{n} | {100 * k / n:.0f}% | {"—" if c is None else f"{c:.4f}"} | {t:.0f} s | {"—" if nt is None else f"{nt:.1f}"} |')
    for m, mot in erro.items():
        if m not in por:
            L.append(f'| {m} | não rodou | — | — | — | — |')
    vence = next((x for x in tab if x[3] is not None), None)
    L += ['', f'**Mais barato por entrega certa:** {vence[0]}' if vence else '**Nenhum modelo entregou certo.**', '',
          'Custo = tokens medidos × tabela oficial (dados/precos-*.csv), já descontadas as instruções fixas de cada '
          'assistente. Pela assinatura você não paga isso por tarefa: leia como "quanto custaria por uso".', '']
    if erro:
        L += ['**Não rodou** (a chamada falhou, não conta como erro do modelo): ' + '; '.join(f'{m}: {mot[:120]}' for m, mot in erro.items()), '']
    L += [
          '## Tentativas', '', '| Modelo | # | Certa | Nota | Tempo | Motivo |', '|---|---:|---|---:|---:|---|']
    for l in linhas:
        L.append(f'| {l["modelo"]} | {l["execucao"]} | {l["aprovada"]} | {l["nota"]} | {float(l["tempo_s"]):.0f} s | {l["motivo"].replace("|", "/")[:160]} |')
    (saida / 'relatorio.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    return '\n'.join(L[:8 + len(tab) + 3])


def gravar(saida, linhas):
    campos = ['modelo', 'execucao', 'tokens_entrada', 'tokens_saida', 'custo_usd', 'aprovada', 'nota', 'tempo_s', 'motivo', 'tokens_entrada_bruto']
    with open(saida / 'tentativas.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, campos, extrasaction='ignore')
        w.writeheader()
        w.writerows(linhas)


# ---------- principal ----------
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('tarefa')
    ap.add_argument('--motores', default=str(RAIZ / 'kit' / 'motores.json'))
    ap.add_argument('--so', help='só estes modelos (parte do nome, separados por vírgula)')
    ap.add_argument('--repeticoes', type=int)
    ap.add_argument('--juiz', default='claude-cli:claude-sonnet-5-5')
    ap.add_argument('--paralelo', type=int, default=3)
    ap.add_argument('--simular', action='store_true', help='mostra o plano sem chamar nenhuma IA')
    ap.add_argument('--reavaliar', metavar='PASTA_RESULTADO', help='refaz verificador e juiz nas respostas já salvas (não chama os modelos testados)')
    a = ap.parse_args()

    pasta = Path(a.tarefa).resolve()
    tf = json.loads((pasta / 'tarefa.json').read_text(encoding='utf-8'))
    pedido = tf.get('pedido') or (pasta / tf['pedido_arquivo']).read_text(encoding='utf-8')
    criterio, rep = tf['criterio'], a.repeticoes or int(tf.get('repeticoes', 3))
    motores = json.loads(Path(a.motores).read_text(encoding='utf-8'))
    if a.so:
        alvo = [x.strip().lower() for x in a.so.split(',')]
        motores = [m for m in motores if any(x in m['modelo'].lower() for x in alvo)]
    jv, jid = a.juiz.split(':', 1)
    juiz = {'via': jv, 'id': jid}
    tab = precos()
    faltam = [m['modelo'] for m in motores if m['modelo'] not in tab]
    if faltam:
        sys.exit(f'modelo sem preço em {PRECOS.name}: {faltam}')
    print(f'Tarefa: {tf["nome"]} · {len(motores)} modelos × {rep} vezes = {len(motores) * rep} execuções · juiz {a.juiz}')
    for m in motores:
        print(f'  - {m["modelo"]:<20} via {m["via"]:<13} {m["id"]}')
    if a.simular:
        print('(simulação: nada foi chamado)')
        return

    if a.reavaliar:
        saida = Path(a.reavaliar).resolve()
        with open(saida / 'tentativas.csv', encoding='utf-8') as f:
            linhas = list(csv.DictReader(f))
        for lin in linhas:
            if lin['aprovada'] == 'erro':
                continue
            arq = saida / 'respostas' / f'{re.sub(r"[^a-z0-9]+", "-", lin["modelo"].lower())}-{lin["execucao"]}.md'
            txt = arq.read_text(encoding='utf-8')
            ok_v, msg_v = verificar(tf['verificar'], pasta, arq) if tf.get('verificar') else (True, '')
            ok_j, nota, mot = julgar(juiz, pedido, criterio, txt)
            lin.update(aprovada='sim' if (ok_v and ok_j) else 'não', nota=nota,
                       motivo=(f'verificador: {msg_v} · ' if tf.get('verificar') and not ok_v else '') + mot)
            print(f'  {arq.stem}: {"✅" if lin["aprovada"] == "sim" else "❌"} nota {nota}')
        gravar(saida, linhas)
        print(relatorio(tf['nome'], linhas, saida, juiz, bool(tf.get('verificar'))))
        return

    saida = RAIZ / 'resultados' / f'{dt.datetime.now():%Y-%m-%d-%H%M}-{re.sub(r"[^a-z0-9]+", "-", tf["nome"].lower())}'
    (saida / 'respostas').mkdir(parents=True, exist_ok=True)

    sobre = {}
    for m in motores:
        if m['via'] in COM_SOBRECARGA:
            try:
                _, e, _, _ = chamar(m, CALIBRA)
                sobre[m['modelo']] = max(0, e - 8)
            except Exception as ex:
                print(f'  ! calibração {m["modelo"]}: {ex}')

    def uma(arg):
        m, i = arg
        nome = f'{re.sub(r"[^a-z0-9]+", "-", m["modelo"].lower())}-{i}'
        arq = saida / 'respostas' / f'{nome}.md'
        lin = {'modelo': m['modelo'], 'execucao': i, 'tokens_entrada': '', 'tokens_saida': '', 'custo_usd': '',
               'aprovada': 'não', 'nota': '', 'tempo_s': '0', 'motivo': '', 'tokens_entrada_bruto': ''}
        try:
            txt, ent, sai, t = chamar(m, pedido)
        except Exception as ex:
            lin['motivo'] = f'falhou: {ex}'[:300]
            lin['aprovada'] = 'erro'
            print(f'  {nome}: falhou ({ex})')
            return lin
        arq.write_text(txt, encoding='utf-8')
        lin['tokens_entrada_bruto'] = ent
        ent = max(ent - sobre.get(m['modelo'], 0), len(pedido) // 4)  # piso: estimativa pelo tamanho do pedido
        pe, ps = tab[m['modelo']]
        lin.update(tokens_entrada=ent, tokens_saida=sai, custo_usd=f'{ent / 1e6 * pe + sai / 1e6 * ps:.6f}', tempo_s=f'{t:.1f}')
        ok_v, msg_v = (True, '')
        if tf.get('verificar'):
            ok_v, msg_v = verificar(tf['verificar'], pasta, arq)
        try:
            ok_j, nota, mot = julgar(juiz, pedido, criterio, txt)
        except Exception as ex:
            ok_j, nota, mot = False, '', f'juiz falhou: {ex}'
        lin.update(aprovada='sim' if (ok_v and ok_j) else 'não', nota=nota,
                   motivo=(f'verificador: {msg_v} · ' if tf.get('verificar') and not ok_v else '') + mot)
        print(f'  {nome}: {"✅" if lin["aprovada"] == "sim" else "❌"} nota {nota} · {t:.0f} s')
        return lin

    trabalhos = [(m, i) for i in range(1, rep + 1) for m in motores]
    with ThreadPoolExecutor(a.paralelo) as ex:
        linhas = list(ex.map(uma, trabalhos))
    linhas.sort(key=lambda l: (l['modelo'], int(l['execucao'])))
    gravar(saida, linhas)
    (saida / 'sobrecarga.json').write_text(json.dumps(sobre, indent=1, ensure_ascii=False), encoding='utf-8')
    print()
    print(relatorio(tf['nome'], linhas, saida, juiz, bool(tf.get('verificar'))))
    print(f'\nArquivos: {saida}')


if __name__ == '__main__':
    main()
