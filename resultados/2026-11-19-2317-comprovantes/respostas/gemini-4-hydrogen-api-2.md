### CSV de comprovantes válidos

```csv
id,data,valor_centavos
C-101,2026-11-19,1240
C-102,2026-11-19,930
C-103,2026-11-20,1000
```

---

### Duplicatas apontadas
- **C-101** (`2026-11-19`, `1240` centavos / R$ 12,40): aparece 2 vezes na tabela original (linhas 1 e 3). A segunda ocorrência foi desconsiderada para evitar contagem dupla.

---

### Itens sem valor (separados)
```csv
id,data,valor
C-104,2026-11-20,ausente
```

---

### Total válido
**3170 centavos** (equivalente a R$ 31,70, considerando apenas os itens válidos e sem duplicidade: `1240 + 930 + 1000`).