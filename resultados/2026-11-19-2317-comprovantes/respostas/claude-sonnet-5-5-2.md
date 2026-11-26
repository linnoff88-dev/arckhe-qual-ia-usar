## CSV (itens válidos, sem duplicatas)

```csv
id,data,valor_centavos
C-101,2026-11-19,1240
C-102,2026-11-19,930
C-103,2026-11-20,1000
```

## Duplicatas

- **C-101** aparece 2 vezes (linhas 1 e 3), com mesma data e mesmo valor (2026-11-19, 1240). Mantive a primeira ocorrência e descartei a repetiçêo.

## Itens sem valor (separados)

```csv
id,data,valor_centavos
C-104,2026-11-20,
```

- **C-104**: valor "ausente", excluído do total válido.

## Total válido

**3170 centavos** (1240 + 930 + 1000), ou seja, R$ 31,70.