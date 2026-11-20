## CSV (itens válidos, sem duplicatas)

```csv
id,data,valor_centavos
C-101,2026-11-19,1240
C-102,2026-11-19,930
C-103,2026-11-20,1000
```

## Duplicatas

- **C-101** aparece 2 vezes (19/11/2026, R$ 12,40), com dados idênticos. Mantive a primeira ocorrência (linha 1) e descartei a segunda (linha 3).

## Itens sem valor (separados)

```csv
id,data,valor_centavos
C-104,2026-11-20,
```

- **C-104**: valor "ausente". Ficou fora do total.

## Total válido

12,40 + 9,30 + 10,00 = R$ 31,70

**Total válido: 3170 centavos**