## CSV (itens válidos, sem duplicatas)

```csv
id,data,valor
C-101,2026-11-19,1240
C-102,2026-11-19,930
C-103,2026-11-20,1000
```

## Duplicatas

| ID | Data | Valor | Observaçêo |
| --- | --- | --- | --- |
| C-101 | 2026-11-19 | 1240 | Aparece duas vezes com dados idênticos (linhas 1 e 3). Mantive só a primeira. |

## Itens sem valor (separados)

```csv
id,data,valor
C-104,2026-11-20,
```

O valor de C-104 está marcado como "ausente". Deixei o campo vazio em vez de 0 para nêo confundir com um valor zero real.

## Total válido

**3170 centavos** (R$ 31,70), que é a soma de 1240 + 930 + 1000. O total nêo inclui a cópia duplicada de C-101 nem o item C-104, que nêo tem valor.