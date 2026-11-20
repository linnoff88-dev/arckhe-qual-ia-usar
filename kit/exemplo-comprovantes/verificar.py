#!/usr/bin/env python3
"""Verificador da tarefa dos comprovantes. Recebe o arquivo da resposta; sai 0 se estiver certa."""
import re, sys

txt = open(sys.argv[1], encoding='utf-8').read()
esperado = {'C-101': ('2026-11-19', 1240), 'C-102': ('2026-11-19', 930), 'C-103': ('2026-11-20', 1000)}
# só o primeiro CSV conta (a resposta pode listar a duplicata ou o item sem valor em blocos à parte)
blocos = re.findall(r'```(?:csv)?\n(.*?)```', txt, re.S)
LINHA = re.compile(r'^\s*"?(C-\d{3})"?\s*[,;]\s*"?(\d{4}-\d{2}-\d{2})"?\s*[,;]\s*"?(\d+)"?\s*$')
def primeiro_grupo(t):
    """Primeiro trecho de linhas seguidas no formato de CSV (para resposta sem bloco de código)."""
    grupo = []
    for l in t.splitlines():
        if LINHA.match(l) or (grupo == [] and re.match(r'^\s*id\s*[,;]', l, re.I)):
            grupo.append(l)
        elif any(LINHA.match(x) for x in grupo):
            break
        else:
            grupo = []
    return '\n'.join(grupo)
principal = next((b for b in blocos if LINHA.search(b) or re.search(r'^\s*"?C-\d{3}', b, re.M)), None) or primeiro_grupo(txt)
linhas = re.findall(r'^\s*"?(C-\d{3})"?\s*[,;]\s*"?(\d{4}-\d{2}-\d{2})"?\s*[,;]\s*"?(\d+)"?\s*$', principal, re.M)
erros = []
achadas = {}
for i, d, v in linhas:
    achadas.setdefault(i, []).append((d, int(v)))
for i, (d, v) in esperado.items():
    if achadas.get(i, [None])[0] != (d, v):
        erros.append(f'{i} esperado {d},{v} achado {achadas.get(i)}')
if len(achadas.get('C-101', [])) > 1:
    erros.append('C-101 repetido no CSV')
if 'C-104' in achadas:
    erros.append('C-104 (sem valor) entrou no CSV')
if not re.search(r'3\.?170', txt):
    erros.append('total 3170 não aparece')
if not re.search(r'duplicad|duplicat|repetid', txt, re.I):
    erros.append('não aponta a duplicata')
print('ok' if not erros else '; '.join(erros))
sys.exit(1 if erros else 0)
