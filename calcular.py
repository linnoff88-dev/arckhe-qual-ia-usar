#!/usr/bin/env python3
"""Custo por entrega certa: quanto cada modelo custou até entregar o que você pediu.

Uso:
  python3 calcular.py exemplos/tentativas-exemplo.csv      # seu teste (ou o exemplo fictício)
  python3 calcular.py --arena                              # recorte do Agent Arena de 19/11/2026
  python3 calcular.py --precos                             # tabela de preços por token

CSV de tentativas: uma linha por tentativa, com as colunas
  modelo, execucao, tokens_entrada, tokens_saida, custo_usd, aprovada
- modelo: igual ao nome em dados/precos-2026-11-19.csv (ex.: "Gemini 4 Argon").
- execucao: um rótulo para cada vez que você deu a tarefa do zero (ex.: 1, 2, 3).
  Várias tentativas da mesma execução (correções) somam custo e contam UMA entrega.
- custo_usd: se o painel mostrar o valor cobrado, use ele. Vazio = calcula pelos tokens.
- aprovada: sim/não. A execução conta como entrega se alguma tentativa dela foi aprovada.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PRECOS = AQUI / "dados" / "precos-2026-11-19.csv"
ARENA = AQUI / "dados" / "arena-2026-11-19.csv"
SIM = {"sim", "s", "yes", "y", "si", "sí", "1", "true", "ok"}


def ler(caminho):
    with open(caminho, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def precos():
    return {l["modelo"]: l for l in ler(PRECOS)}


def num(v):
    v = (v or "").strip().replace(",", ".")
    return float(v) if v else None


def custo_tentativa(l, tabela):
    direto = num(l.get("custo_usd"))
    if direto is not None:
        return direto
    p = tabela.get(l["modelo"].strip())
    te, ts = num(l.get("tokens_entrada")), num(l.get("tokens_saida"))
    if p is None or te is None or ts is None:
        return None
    return te / 1e6 * float(p["usd_entrada_por_milhao"]) + ts / 1e6 * float(p["usd_saida_por_milhao"])


def calcular(caminho):
    tabela = precos()
    gasto = defaultdict(float)
    sem_custo = defaultdict(int)
    execs = defaultdict(dict)  # modelo -> execucao -> aprovada?
    for l in ler(caminho):
        if (l.get("aprovada") or "").strip().lower() == "erro":
            continue  # a chamada falhou: não é erro do modelo
        m = l["modelo"].strip()
        c = custo_tentativa(l, tabela)
        if c is None:
            sem_custo[m] += 1
        else:
            gasto[m] += c
        e = (l.get("execucao") or "").strip() or str(len(execs[m]) + 1)
        ok = (l.get("aprovada") or "").strip().lower() in SIM
        execs[m][e] = execs[m].get(e, False) or ok
    linhas = []
    for m in execs:
        entregas = sum(execs[m].values())
        total = gasto[m]
        por = total / entregas if entregas and not sem_custo[m] else None
        linhas.append((m, len(execs[m]), entregas, total, por, sem_custo[m]))
    linhas.sort(key=lambda x: (x[4] is None, x[4] or 0))
    print(f"{'Modelo':<22}{'Execuções':>10}{'Entregas':>10}{'Gasto US$':>11}{'US$/entrega certa':>19}")
    for m, n, ent, tot, por, falta in linhas:
        txt = f"{por:.4f}" if por is not None else ("sem custo" if falta else "sem entrega")
        print(f"{m:<22}{n:>10}{ent:>10}{tot:>11.4f}{txt:>19}")
    faltas = [m for m, *_, f in linhas if f]
    if faltas:
        print("\nSem custo em alguma tentativa (não contei como zero):", ", ".join(faltas))
    if linhas and linhas[0][4] is not None:
        print(f"\nMais barato por entrega certa neste teste: {linhas[0][0]}")


def arena():
    print(f"{'Modelo':<20}{'Esforço':>8}{'Índice':>8}{'US$/tarefa':>12}{'Pontos por US$':>16}")
    for l in sorted(ler(ARENA), key=lambda x: -int(x["indice_agent_arena"])):
        i, u = int(l["indice_agent_arena"]), float(l["usd_mediano_por_tarefa"])
        nota = " (preliminar)" if l["observacao"] else ""
        print(f"{l['modelo']:<20}{l['esforco']:>8}{i:>8}{u:>12.2f}{i / u:>16.0f}{nota}")
    print("\nFonte: Agent Arena, recorte de 19/11/2026. Custo = mediana por tarefa; sessões variam.")


def tabela_precos():
    print(f"{'Faixa':<15}{'Empresa':<11}{'Modelo':<20}{'Entrada':>9}{'Saída':>8}  Obs.")
    for l in ler(PRECOS):
        print(f"{l['faixa']:<15}{l['empresa']:<11}{l['modelo']:<20}{float(l['usd_entrada_por_milhao']):>9.2f}"
              f"{float(l['usd_saida_por_milhao']):>8.2f}  {l['observacao']}")
    print("\nUS$ por milhão de tokens, sem cache, consultado em 19/11/2026.")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
    elif a[0] == "--arena":
        arena()
    elif a[0] == "--precos":
        tabela_precos()
    else:
        calcular(a[0])
