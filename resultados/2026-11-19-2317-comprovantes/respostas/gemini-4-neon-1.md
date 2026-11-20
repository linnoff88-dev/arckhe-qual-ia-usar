### CSV (itens válidos e únicos)

```csv
id,data,valor_centavos
C-101,2026-11-19,1240
C-102,2026-11-19,930
C-103,2026-11-20,1000
```

### Duplicatas identificadas

- **C-101** | `2026-11-19` | `1240` centavos — registro duplicado (3ª linha da tabela original, idêntico à 1ª linha; desconsiderado no CSV válido e no total).

### Itens sem valor (separados)

```csv
id,data,valor_centavos
C-104,2026-11-20,
```

- **C-104** | `2026-11-20` | valor ausente.

### Total válido

- **3170 centavos** (`1240 + 930 + 1000`, equivalente a R$ 31,70).
