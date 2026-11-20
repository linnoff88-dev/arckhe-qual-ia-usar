## CSV (itens válidos, sem duplicatas)

```csv
id,data,valor_centavos
C-101,2026-11-19,1240
C-102,2026-11-19,930
C-103,2026-11-20,1000
```

## Duplicatas

- **C-101** aparece duas vezes (linhas 1 e 3), com a mesma data (19/11/2026) e o mesmo valor (R$ 12,40). Mantive a primeira ocorrência e descartei a segunda.

## Itens sem valor (separados, fora do total)

```csv
id,data,valor_centavos
C-104,2026-11-20,
```

- **C-104**: valor marcado como "ausente", por isso não entra no total.

## Total válido

1240 + 930 + 1000 = **3170 centavos** (R$ 31,70)