# ⚖️ Which AI to use - GEMINI - GPT - CLAUDE

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Which AI costs less](guia/assets/banner-en.jpg)](https://inematds.github.io/qual-ia-usar/guia/en/)

## What it is

This project compares ten AI models from three companies: Google's Gemini 4 (Neon, Argon, and Hydrogen), Anthropic's Claude (Fable, Opus, Sonnet, and Haiku), and the OpenAI models used by Codex (Astra, Sol, and Luna). It brings together official pricing tables and the Agent Arena leaderboard, a public ranking that measures AI agents performing real tasks, version checked on Nov 19, 2026. It's for people who pay for AI and want to choose without wasting money. You don't need anything to read it. To test with your own task, all you need are the apps you already use (ChatGPT, Claude, or Gemini), or the testing kit, which runs the same task on every AI you enable and tells you which got the most right while spending the least.

## 📖 Guide

Complete guide, in plain language: **https://inematds.github.io/qual-ia-usar/guia/en/**

## The idea in one line

The cheapest AI in the table can end up costing more on your bill. What matters is the **cost per successful task**: everything you paid, including failed attempts, divided by the tasks that were completed correctly.

## Who wins in each tier (Nov 19, 2026)

Price in US$ per million tokens (input / output). Score and cost per task: Agent Arena.

| Tier | Google | Anthropic | OpenAI |
|---|---|---|---|
| Complex work | Gemini 4 Neon · 3 / 15 · Score 1333 · US$ 2.60 per task | Claude Opus 5.5 · 4 / 20 · 1336 · US$ 5.98 | GPT-6.2 Astra · 8 / 40 · 1291 · US$ 3.11 |
| Everyday work | Gemini 4 Argon · 2 / 10 (4 / 20 starting Dec 1) · 1229 · US$ 0.66 | Claude Sonnet 5.5 · 2 / 10 · 1296 · US$ 3.27 | GPT-6.2 Sol · 2 / 10 · 1241 · US$ 0.96 |
| High volume | Gemini 4 Hydrogen · 1.50 / 7.50 · 1271 (preliminary) · US$ 1.50 | Claude Haiku 5.5 · 0.10 / 0.50 · no score | GPT-6 Luna · 0.10 / 0.50 · no score |

Outside these tiers: **Claude Fable 5.2** (US$ 8 / 40) leads the leaderboard with a score of 1448 and costs US$ 9.16 per task.

- **Complex work:** Neon nearly ties with Opus and costs less than half as much per task.
- **Everyday work:** all three charge the same per token; per task, Argon costs less and Sonnet has the highest score.
- **High volume:** Haiku and Luna charge 15 times less per token than Hydrogen; their quality can only be determined by testing.
- **Within Google:** Hydrogen is cheaper per token than Argon, but cost more than twice as much per task.

What this comparison does not promise: the tier figures are published results (the test kit below covers one task and seven models), the leaderboard measures agent tasks in general, not yours, and everything changes over time.

## All comparisons (overview)

Four comparisons between Google, Anthropic, and OpenAI, from Nov 19 and 20, 2026. Just the numbers.

| Comparison | What was measured | Google (Gemini 4) | Anthropic (Claude) | OpenAI (GPT) |
|---|---|---|---|---|
| **1. Official pricing** (10 models) | US$ per million tokens, input / output | Neon 3 / 15 · Argon 2 / 10 · Hydrogen 1.50 / 7.50 | Fable 8 / 40 · Opus 4 / 20 · Sonnet 2 / 10 · Haiku 0.10 / 0.50 | Astra 8 / 40 · Sol 2 / 10 · Luna 0.10 / 0.50 |
| **2. Agent Arena leaderboard** (8 with scores) | score · US$ per task | Neon 1333 · 2.60 · Hydrogen 1271 · 1.50 · Argon 1229 · 0.66 | Fable 1448 · 9.16 · Opus 1336 · 5.98 · Sonnet 1296 · 3.27 | Astra 1291 · 3.11 · Sol 1241 · 0.96 |
| **3. Testing kit** (receipts, 10 × 2, by subscription) | correct · ¢ per successful task · time | 3 of 3 · 1.92–3.62 ¢ · 12–16 s (high effort) | 4 of 4 · 0.038–1.55 ¢ · 4–6 s | 3 of 3 · 0.008–0.66 ¢ · 7–11 s |
| **4. Analysis of a long document** (182 KB, same prompt, unpublished internal content) | time · incorrect counts · quality score (ours) | Neon: 5.5 min · 3 · 6.5 | Fable 5.2: 14 min · 0 · 9 | Astra: 4.5 min · 0 · 8 |

- **Quality:** in the long analysis, Fable was the most rigorous and Astra offered the best value. Neon produced the longest response, but got counts wrong and drew conclusions the other two refuted.
- **Cost:** on the simple task, all got it right and GPT-6 Luna was the cheapest. At high effort, Gemini models think more and had the highest cost per successful task.
- **Speed:** Claude Sonnet was fastest on the simple task (4 s), and Astra on the long analysis (4.5 min); Fable took three times longer.
- The analysis quality score is our evaluation: Astra and Fable checked Neon's figures against the document and found the same corrections. Neon responded first, and the other two read its analysis. One task and one document aren't enough to say which model is better overall.

### The receipts test, model by model

All ten got it right both times, with a score of 10 from the evaluator and approval from the verifier. From cheapest to most expensive per successful task:

| Model | How it ran | Correct | Median time | Output tokens | US$ per successful task* |
|---|---|---:|---:|---:|---:|
| GPT-6 Luna | subscription (Codex), default effort | 2/2 | 7 s | 104–115 | 0.00008 |
| Claude Haiku 5.5 | subscription (Claude Code), default effort | 2/2 | 6 s | 618–817 | 0.00038 |
| GPT-6.2 Sol | subscription (Codex), default effort | 2/2 | 9 s | 120–121 | 0.00155 |
| Claude Sonnet 5.5 | subscription (Claude Code), default effort | 2/2 | 4 s | 266–272 | 0.00316 |
| GPT-6.2 Astra | subscription (Codex), default effort | 2/2 | 11 s | 127–134 | 0.00656 |
| Claude Opus 5.5 | subscription (Claude Code), default effort | 2/2 | 6 s | 344–375 | 0.00813 |
| Gemini 4 Hydrogen | API, default effort | 2/2 | 6 s | 863–1,357 | 0.0087 |
| Claude Fable 5.2 | subscription (Claude Code), default effort | 2/2 | 5 s | 278–404 | 0.01552 |
| Gemini 4 Argon | subscription (Antigravity), high effort | 2/2 | 16 s | 1,645–2,097 | 0.01917 |
| Gemini 4 Hydrogen | subscription (Antigravity), high effort | 2/2 | 12 s | 2,869–2,943 | 0.02211 |
| Gemini 4 Neon | subscription (Antigravity), high effort | 2/2 | 16 s | 2,234–2,498 | 0.03616 |

\*What it would cost if paid pay-as-you-go. With a subscription, you don't pay per task; you only use up your quota.

- All 10 got it right: on a simple task, the cheapest wins. Claude and GPT took 4 to 11 s; Gemini took 12 to 16 s.
- In terms of cost, Neon (US$ 0.036) came in above even Fable (0.016) and far above Luna (0.0001). The main reason is effort: at high effort, Gemini thinks a lot before answering (2,000 to 3,000 tokens, compared with 100 to 800 for the others). Claude and GPT ran at their default effort, so the cost comparison isn't balanced. By API, at default effort, Hydrogen cost about 2.5 times less.
- Neon as a critic wasn't tested here: the test measured task execution, not review.
- Next step for a fair comparison: run Gemini at medium and low effort too, and use a harder task where some models get it wrong.

### Ranking of the long document analysis

**Fable was best, Astra came right behind, and Neon came last.** Neon produced the longest response, but also made the most mistakes. All three received the same prompt about an internal 182 KB document (unpublished content); Astra and Fable also checked Neon's analysis.

| | Fable 5.2 (Claude) | Astra (GPT-6.2, high effort) | Neon (Gemini 4, high effort) |
|---|---|---|---|
| **Time** | ~14 min (slowest) | ~4.5 min (fastest) | ~5.5 min |
| **Response length** | ~15,000 characters, the most concise | ~18,000 | ~25,000, the longest |
| **Correct figures** | Everything we checked matched. Checked 7 of Neon's figures and found 4 wrong | Everything we checked matched. Found 3 of Neon's errors | Got the basics right, but got 3 counts wrong |
| **Method** | Most rigorous: separated recurring issues from new ones and counted with a script | Explained its own method and treated each effect as a ceiling, without overpromising | Added overlapping causes without saying so and presented an assumption as fact |
| **Original findings** | Most useful: corrections that introduce a new defect and rules that exist but don't hold up | Found the exact point where the process fails and a fix made in the wrong place | Good at digging up details hidden in the data |
| **Conclusion** | Most solid, stating the limits of its own proposal | Solid and balanced | Weakest: its two main proposals were refuted by the other two |
| **Critique of Neon** | Most complete: agreements, disagreements, and what was missing, with figures | Good: checked 6 claims | — |
| **Score (ours)** | **9** | **8** | **6.5** |

- **Fable:** the most reliable and the one that best understood the problem, but took three times longer.
- **Astra:** the best value: fast, accurate, careful in its claims, and had an idea no one else came up with.
- **Neon:** great for quickly finding and organizing a lot of material. But it draws overly strong conclusions and gets counts wrong: as a critic, it needs someone to check its numbers.
- Limitations: just one analysis and one document; Neon responded first, and the other two read its analysis, which favors those who came later.

## How to get started (no programming)

Open Claude Code or Codex in one of your folders and paste:

```text
Read the "Which AI to use" project at https://github.com/inematds/qual-ia-usar (the README explains the testing kit in kit/testar.py).
I want to know which AI has the lowest cost per successful task for one of my tasks: [describe the task and what "done correctly" means].
1. In plain English, tell me which 3 or 4 models are worth testing for this task and why.
2. Propose a small test: how many times to run each model and how much it should cost.
3. Don't call any model or spend anything before I say yes.
After I say yes, set up the task in the kit format (kit/testar.py), run the test, and show me the report.
```

## Testing kit: your task across all AIs

You describe the task and what "done correctly" means. The kit runs the same task on each AI several times, evaluates each response (an AI judge and, if you want, an automatic verifier), and returns a report: how many were correct, time, and cost per successful task.

**Real test (Nov 19, 2026, receipts task, each run twice, all by subscription: Claude through Claude Code, GPT through Codex, Gemini through Google AI Pro via Antigravity CLI):**

| Model | Correct | US$ per successful task | Median time |
|---|---:|---:|---:|
| GPT-6 Luna | 2/2 | 0.00008 | 7 s |
| Claude Haiku 5.5 | 2/2 | 0.00038 | 6 s |
| GPT-6.2 Sol | 2/2 | 0.00155 | 9 s |
| Claude Sonnet 5.5 | 2/2 | 0.00316 | 4 s |
| GPT-6.2 Astra | 2/2 | 0.00656 | 11 s |
| Claude Opus 5.5 | 2/2 | 0.00813 | 6 s |
| Claude Fable 5.2 | 2/2 | 0.01552 | 5 s |
| Gemini 4 Argon (high) | 2/2 | 0.01917 | 16 s |
| Gemini 4 Hydrogen (high) | 2/2 | 0.02211 | 12 s |
| Gemini 4 Neon (high) | 2/2 | 0.03616 | 16 s |

On a simple task, all get it right, so the cheapest wins. The three Gemini models ran at **high** effort (the same as the leaderboard) and think a lot before answering (1,600 to 2,900 output tokens); Claude and GPT ran at each assistant's default effort. By API, at default effort, Hydrogen cost US$ 0.0087 per successful task (about 2.5 times less). One Fable response was initially rejected because of a verifier error, then corrected and reevaluated with `--reavaliar`. Full report: [results/2026-11-19-2317-comprovantes (in Portuguese)](resultados/2026-11-19-2317-comprovantes/relatorio.md).

## In practice: How Nei chooses

- **Luna and Haiku:** cost cents and got the simple task right. Good options for simple, long-running tasks (many repeated steps, high volume).
- **Terra and Sonnet:** in Nei's tests, the preferred models are GPT-6.1 Terra and Claude Sonnet 5.5. They cost more, but deliver good results more consistently. For OpenAI, from lowest to highest: Luna, Terra, Sol, and Astra. Terra isn't in this project's tables.
- **Neon as a critic:** Nei currently uses Claude and Codex to review each other, because models from different companies make different mistakes. Gemini 4 Neon could be the AI that validates and critiques for people who only have Claude or only have Codex (how to connect it: see the section below).

## Gemini Pro inside Claude Code or Codex

**Gemini CLI has been retired.** On Jun 18, 2026, Google stopped accepting accounts that subscribe to Google AI Pro or Ultra (and individual free usage) in Gemini CLI. Login returns: *"This client is no longer supported for Gemini Code Assist for individuals… migrate to the Antigravity suite"*. The replacement is **Antigravity CLI (`agy`)**, which uses your subscription quota. The AI Studio API key doesn't use the subscription: it has its own quota, and on the free plan Neon and Argon return 429.

**The process we followed (Nov 19, 2026):**

1. Existing Gemini API keys (free plan): Hydrogen responded; Neon and Argon returned `429 You exceeded your current quota`.
2. Gemini CLI 0.70.0 logged into the subscription account: login accepted, usage rejected (message above).
3. Antigravity CLI 1.5.13: installed, logged in with a Google account (open link → paste code back), `agy models` listed Gemini 4 Neon, Argon, and Hydrogen (low to xhigh), Gemini 3.8 Flash, Claude Opus 5.5, and Sonnet 5.5.
4. The testing kit added support for `agy` and ran the three Gemini models by subscription.

**How to do it:**

```bash
# 1. install (the script downloads the binary and checks the SHA-512)
curl -fsSL https://antigravity.google/cli/install.sh | bash      # installs to ~/.local/bin/agy

# 2. login: run with no arguments, choose "Google OAuth", open the link and sign in with the account that subscribes to Gemini
agy                                                                # then paste the authorization code

# 3. see what your account allows
agy models

# 4. use without interaction (this is how Claude Code, Codex, and the kit call it)
agy -p "Critique this text: ..." --model gemini-4-neon-high --output-format json
```

The JSON output includes `response`, `duration_seconds`, and `usage` (input, output, and reasoning tokens). In Claude Code or Codex, just ask the AI to call `agy` from the terminal. One good use is Neon as a second opinion: Claude or Codex does the work, Gemini critiques it.

In the kit, `kit/motores.json` already points the three Gemini models to the `agy` route (`gemini-4-neon-high`, `gemini-4-argon-high`, `gemini-4-hydrogen-high`).

**Cautions:** Pro quota isn't published (it renews every 5 hours, with a weekly cap); there are reports of Pro accounts marked "not eligible" in Antigravity; at high effort, Gemini thinks and writes more, which raises the equivalent "pay-as-you-go cost."

---

## Technical installation

Only Python 3 is required (no extra libraries).

```bash
git clone https://github.com/inematds/qual-ia-usar
cd qual-ia-usar
python3 calcular.py --precos                              # token price table
python3 calcular.py --arena                               # Agent Arena leaderboard + points per dollar
python3 calcular.py exemplos/tentativas-exemplo.csv       # fictional test example
```

### Testing kit

```bash
python3 kit/testar.py kit/exemplo-comprovantes --simular              # shows the plan, calls nothing
python3 kit/testar.py kit/exemplo-comprovantes --so "Claude,GPT" --repeticoes 2
python3 kit/testar.py minha-tarefa/ --juiz claude-cli:claude-sonnet-5-5
python3 kit/testar.py kit/exemplo-comprovantes --reavaliar resultados/<pasta>   # reruns verifier and judge on saved responses
python3 kit/teste_vias_api.py                                         # tests API routes against a fake server
```

**The task** is a folder with `tarefa.json`:

```json
{"nome": "comprovantes",
 "pedido_arquivo": "pedido.md",
 "criterio": "how 'done correctly' looks, point by point",
 "verificar": "python3 verificar.py",
 "repeticoes": 3}
```

`verificar` is optional: a command that receives the response path and exits with 0 when it's correct. A response counts as correct only if it passes the verifier **and** the judge.

**Models** are listed in `kit/motores.json` (`modelo` matches the name in `dados/precos-*.csv`, with `via` and `id`). Routes:

| Route | How it runs | Requires |
|---|---|---|
| `claude-cli` | `claude -p`, no tools | Claude Code logged in (subscription) |
| `codex-cli` | `codex exec`, read-only sandbox | Codex logged in (subscription) |
| `agy` | `agy -p`, Antigravity CLI | Login with the Google account that subscribes to Gemini (AI Pro/Ultra) |
| `gemini-cli` | `gemini -p` | Only with a paid API key: individual subscription migrated to `agy` |
| `api-anthropic`, `api-openai`, `api-google`, `openrouter` | HTTP API | `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY`, `OPENROUTER_API_KEY` |

Cost is calculated from measured tokens × the official price table. Claude Code, Codex, and Gemini CLI add their own instructions to each prompt; the kit measures this extra once per model and deducts it (the raw figure is in the `tokens_entrada_bruto` column). With a subscription, you don't pay per task: read the cost as "what it would cost per use." Failed calls (quota, network, login) appear as "didn't run" and don't count as model errors. The `claude-cli`, `codex-cli`, `agy`, and `api-google` routes were tested for real; `api-anthropic`, `api-openai`, `openrouter`, and `gemini-cli` were tested only against a fake server. Check each model's `id` in the company's documentation.

Output in `resultados/<data>-<nome>/`: responses, `tentativas.csv` (also read by `calcular.py), and `relatorio.md`.

### Files

| File | What it is |
|---|---|
| `calcular.py` | Calculates cost per successful task from a CSV of attempts |
| `dados/precos-2026-11-19.csv` | Official prices per million tokens, with the source for each row |
| `dados/arena-2026-11-19.csv` | Agent Arena score and median cost per task (snapshot from Nov 19, 2026) |
| `exemplos/tentativas-exemplo.csv` | **Fictional** test example (not a measurement) |
| `kit/testar.py` | Testing kit: runs the task on each AI, evaluates, and calculates cost per successful task |
| `kit/motores.json` | List of models and how to call each one |
| `kit/exemplo-comprovantes/` | Example task with an automatic verifier |
| `resultados/` | Reports from tests already run |
| `guia/` | Guide in PT, EN, and ES (GitHub Pages) |

### Attempts CSV format

One row per attempt:

| Column | What it contains |
|---|---|
| `modelo` | Same as the name in `dados/precos-2026-11-19.csv` (e.g., `Gemini 4 Argon`) |
| `execucao` | Label for each time you gave the task from scratch (1, 2, 3…). Corrections within the same run add to its cost and count as one task |
| `tokens_entrada`, `tokens_saida` | Tokens used in the attempt |
| `custo_usd` | Amount charged, if shown in the dashboard. Blank = calculated from tokens and the table |
| `aprovada` | `sim` or `nêo`. The run counts as a successful task if any of its attempts was approved |

Missing cost never becomes zero: the model appears as "no cost" and is excluded from the comparison.

### How the calculation works

`cost per successful task = sum of the cost of all attempts ÷ number of approved runs`

To test with ready-made tasks and fictional data, use the Gemini 4 lab protocol: [protocolo.md (in Portuguese)](https://github.com/inematds/gemini-4-na-pratica/blob/main/laboratorio/protocolo.md).

## Sources

- Google: [pricing](https://aistudio.google.com/docs/pricing) · [Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) · [Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/) · [Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)
- Anthropic: [pricing](https://platform.claude.com/docs/en/about-claude/pricing) · [Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)
- OpenAI: [pricing](https://developers.openai.com/api/docs/pricing) · [GPT-6.2](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna)
- [Agent Arena](https://arena.ai/leaderboard/agent): Google at High effort, Anthropic and OpenAI at Max; cost = median per task over the last 14 days; score is not an accuracy percentage.

## The process, from start to finish

| # | Step | Command | Who |
|---|---|---|---|
| 1 | Check prices and leaderboard against official sources and update `dados/*.csv` | — | 🧠 session with Nei |
| 2 | Check the tables and calculation | `python3 calcular.py --precos` / `--arena` / `exemplos/tentativas-exemplo.csv` | ⚙️ script |
| 3 | Write the PT guide (`guia/index.html`) and generate the cover and banners | `gerar-capa.cjs`, `gerar-banner.sh` | 🧠 + ⚙️ Codex image_gen |
| 4 | Translate the guide and README into EN/ES | `traduz-pagina-codex.py html` / `readme` | ⚙️ central translator |
| 5 | Independent guide review | `revisor-nota.py registra --fluxo guia` | 🤖 new reviewer |
| 6 | Publish: commit + push (GitHub Pages via Actions) | `git push` | 🧠 |
| 7 | Portal, search, and PRO catalog | `atualiza-portal` skill | 🧠 |
| 8 | Topic on INEMA.LLMS | `postar-telegram` skill | 🧠 |
| 9 | Comparison video on lives4 and embed in the guide (3 languages) | `yt-pub-x3` | ⚙️ x3 + 🧠 |

Free on inema.club, available directly on the internet. MIT License.
