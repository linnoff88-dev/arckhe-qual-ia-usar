### CSV dos comprovantes válidos (sem duplicatas e com valor)

```csv
id,data,valor_centavos
C-101,2026-11-19,1240
C-102,2026-11-19,930
C-103,2026-11-20,1000
```

### Duplicatas identificadas
- **`C-101`** (`2026-11-19`, `1240` centavos / `R$ 12,40`): aparece 2 vezes na tabela original (1ª e 3ª linhas). Apenas uma ocorrência foi mantida nos registros válidos.

### Itens sem valor (separados)
```csv
id,data,valor_centavos
C-104,2026-11-20,
```
- **`C-104`** (`2026-11-20`): valor informado como `ausente`.

### Total válido
- **Total válido em centavos:** `3170` centavos (`1240 + 930 + 1000`, equivalente a R$ 31,70).
