## CSV (registros válidos e únicos)

```csv
id,data,valor
C-101,2026-11-19,1240
C-102,2026-11-19,930
C-103,2026-11-20,1000
```

## Duplicatas

| ID | Data | Valor | Situaçêo |
| --- | --- | --- | --- |
| C-101 | 2026-11-19 | 1240 | Aparece 2 vezes com dados idênticos. Mantive 1 ocorrência e descartei a outra. |

## Itens sem valor (separados)

```csv
id,data,valor
C-104,2026-11-20,
```

O campo de valor de C-104 está "ausente". Por isso o item ficou fora do total. Ele só pode voltar ao total depois que o valor for confirmado.

## Total válido

**3170 centavos** (R$ 31,70), calculado como 1240 + 930 + 1000.