### CSV (itens válidos e sem duplicatas)

```csv
id,data,valor_centavos
C-101,2026-11-19,1240
C-102,2026-11-19,930
C-103,2026-11-20,1000
```

### Duplicatas identificadas

- **C-101** (`2026-11-19`, `1240` centavos / R$ 12,40): aparece 2 vezes (linhas 1 e 3 da tabela original). A ocorrência duplicada foi desconsiderada no CSV acima e no total.

### Itens sem valor

```csv
id,data,valor_centavos
C-104,2026-11-20,
```

- **C-104** (`2026-11-20`): valor `ausente`.

### Total válido

- **3170 centavos** (R$ 31,70), correspondente a `1240 + 930 + 1000`.
