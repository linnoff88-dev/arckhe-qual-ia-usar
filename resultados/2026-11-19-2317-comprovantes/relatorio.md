# Teste: comprovantes

19/11/2026 23:41 · juiz: claude-cli:claude-sonnet-5-5 · com verificador automático

| Modelo | Certas | Taxa | US$ por entrega certa | Tempo mediano | Nota média |
|---|---:|---:|---:|---:|---:|
| GPT-6 Luna | 2/2 | 100% | 0.0001 | 7 s | 10.0 |
| Claude Haiku 5.5 | 2/2 | 100% | 0.0004 | 6 s | 10.0 |
| GPT-6.2 Sol | 2/2 | 100% | 0.0015 | 9 s | 10.0 |
| Claude Sonnet 5.5 | 2/2 | 100% | 0.0032 | 4 s | 10.0 |
| GPT-6.2 Astra | 2/2 | 100% | 0.0066 | 11 s | 10.0 |
| Claude Opus 5.5 | 2/2 | 100% | 0.0081 | 6 s | 10.0 |
| Claude Fable 5.2 | 2/2 | 100% | 0.0155 | 5 s | 10.0 |
| Gemini 4 Argon | 2/2 | 100% | 0.0192 | 16 s | 10.0 |
| Gemini 4 Hydrogen | 2/2 | 100% | 0.0221 | 12 s | 10.0 |
| Gemini 4 Neon | 2/2 | 100% | 0.0362 | 16 s | 10.0 |

**Mais barato por entrega certa:** GPT-6 Luna

Custo = tokens medidos × tabela oficial (dados/precos-*.csv), já descontadas as instruções fixas de cada assistente. Pela assinatura você nêo paga isso por tarefa: leia como "quanto custaria por uso".

## Tentativas

| Modelo | # | Certa | Nota | Tempo | Motivo |
|---|---:|---|---:|---:|---|
| Claude Fable 5.2 | 1 | sim | 10 | 5 s | O CSV tem exatamente as três linhas válidas com datas ISO e valores em centavos corretos, aponta C-101 como duplicata contada uma só vez, separa C-104 como item |
| Claude Fable 5.2 | 2 | sim | 10 | 4 s | O CSV tem exatamente as três linhas válidas com datas ISO e valores em centavos corretos, aponta C-101 como duplicata contada uma só vez, separa C-104 como item |
| Claude Haiku 5.5 | 1 | sim | 10 | 6 s | O CSV tem exatamente as três linhas válidas com datas ISO e valores em centavos corretos, a duplicata C-101 é apontada e contada uma vez, C-104 é separado como  |
| Claude Haiku 5.5 | 2 | sim | 10 | 6 s | O CSV tem exatamente as três linhas válidas com datas ISO e valores em centavos corretos, C-101 é apontado como duplicata contada uma vez, C-104 é separado como |
| Claude Opus 5.5 | 1 | sim | 10 | 6 s | O CSV tem exatamente as três linhas válidas corretas (C-101, C-102, C-103) com data ISO e valor em centavos, a duplicata C-101 é apontada e contada uma só vez,  |
| Claude Opus 5.5 | 2 | sim | 10 | 7 s | O CSV tem exatamente as três linhas válidas com datas ISO e valores em centavos corretos, a duplicata C-101 é apontada e contada uma só vez, C-104 é separado co |
| Claude Sonnet 5.5 | 1 | sim | 10 | 4 s | A resposta entrega o CSV com as três linhas válidas corretas (C-101, C-102, C-103) em formato AAAA-MM-DD e valores em centavos, aponta C-101 como duplicata cont |
| Claude Sonnet 5.5 | 2 | sim | 10 | 4 s | O CSV tem exatamente as três linhas válidas corretas (C-101, C-102, C-103) com datas ISO e valores em centavos, a duplicata C-101 foi apontada e contada uma vez |
| GPT-6 Luna | 1 | sim | 10 | 7 s | O CSV tem exatamente as três linhas válidas com datas ISO e valores em centavos corretos, aponta C-101 como duplicata contada uma vez, separa C-104 como sem val |
| GPT-6 Luna | 2 | sim | 10 | 7 s | O CSV tem exatamente as três linhas válidas com datas ISO e valores em centavos corretos, a duplicata C-101 é apontada (contada uma vez), C-104 é separado como  |
| GPT-6.2 Astra | 1 | sim | 10 | 12 s | O CSV tem exatamente as três linhas válidas corretas (C-101, C-102, C-103) com datas ISO e valores em centavos, a duplicata de C-101 é apontada e contada uma ve |
| GPT-6.2 Astra | 2 | sim | 10 | 11 s | O CSV tem exatamente as três linhas válidas corretas (C-101, C-102, C-103) com datas ISO e valores em centavos, a duplicata C-101 é apontada e contada uma vez,  |
| GPT-6.2 Sol | 1 | sim | 10 | 9 s | O CSV tem exatamente as três linhas válidas com datas ISO e valores em centavos corretos, aponta a duplicata de C-101 contada uma vez, separa C-104 como item se |
| GPT-6.2 Sol | 2 | sim | 10 | 9 s | O CSV tem exatamente as três linhas válidas corretas (C-101, C-102, C-103) com datas ISO e valores em centavos, a duplicata C-101 é apontada e contada uma vez,  |
| Gemini 4 Argon | 1 | sim | 10 | 17 s | O CSV tem exatamente as três linhas válidas com datas ISO e valores em centavos corretos, aponta C-101 como duplicata contada uma vez, separa C-104 como sem val |
| Gemini 4 Argon | 2 | sim | 10 | 16 s | O CSV tem exatamente as três linhas válidas com datas ISO e valores em centavos corretos, a duplicata C-101 é apontada e contada uma vez, C-104 é separado como  |
| Gemini 4 Hydrogen | 1 | sim | 10 | 12 s | O CSV tem exatamente as três linhas válidas corretas (C-101, C-102, C-103) com datas ISO e valores em centavos, a duplicata de C-101 foi apontada e contada uma  |
| Gemini 4 Hydrogen | 2 | sim | 10 | 12 s | A resposta traz o CSV com exatamente as três linhas válidas (C-101, C-102, C-103) nos formatos corretos, aponta a duplicata de C-101 mantida uma só vez, separa  |
| Gemini 4 Neon | 1 | sim | 10 | 15 s | O CSV tem exatamente as três linhas válidas corretas (C-101, C-102, C-103) com datas ISO e valores em centavos, a duplicata de C-101 é apontada e contada uma ve |
| Gemini 4 Neon | 2 | sim | 10 | 17 s | O CSV tem exatamente as três linhas válidas com datas ISO e valores em centavos corretos, a duplicata C-101 é apontada e contada uma vez, C-104 é separado como  |

## Notas

- Claude e GPT rodaram pela assinatura (Claude Code e Codex), no esforço padrêo de cada assistente. Os três Gemini rodaram pela assinatura Google AI Pro, pelo Antigravity CLI (`agy`), no esforço **high**, o mesmo do placar do Agent Arena. Nesse esforço o Gemini pensa mais antes de responder (de 1.600 a 2.900 tokens de saída), e isso pesa no custo.
- Rodada anterior do Hydrogen pela API (esforço padrêo, 860 a 1.360 tokens de saída): US$ 0,0087 por entrega certa. Arquivos `hydrogen-pela-api.csv` e `respostas/gemini-4-hydrogen-api-*.md`.
- Uma resposta do Fable foi reprovada de início por um erro do verificador (contou um bloco à parte como repetiçêo). O verificador foi corrigido e as respostas reavaliadas com `--reavaliar`.
