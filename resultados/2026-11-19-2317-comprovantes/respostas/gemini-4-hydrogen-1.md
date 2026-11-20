### CSV (itens válidos e únicos)

```csv
id,data,valor_centavos
C-101,2026-11-19,1240
C-102,2026-11-19,930
C-103,2026-11-20,1000
```

### Duplicatas apontadas

- **`C-101` (`2026-11-19`, `1240` centavos):** aparece 2 vezes (1ª e 3ª linhas da tabela). Apenas uma ocorrência foi mantida no CSV válido.

### Itens sem valor (separados)

```csv
id,data,valor_centavos
C-104,2026-11-20,ausente
```

### Total válido

- **Total válido em centavos:** `3170` (equivalente a R$ 31,70, somando `C-101`: 1240 + `C-102`: 930 + `C-103`: 1000).
