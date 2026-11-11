# APM Prep Sketch Notes

<!-- hero: Chapters 4 to 25 of *Crack the APM Role*, rebuilt from the reviewed **APM Prep Vault** as **22 chapter pages**. Learn the AI-product ideas, the product toolkit, estimation and case practice **without re-opening the vault**: every drawing is redrawn in Excalidraw, and every calculation was actually run. -->

These notes follow the APM Prep Vault from Chapter 4 to Chapter 25, one page per chapter. Each page has:

- **every point of the vault note**, in the vault's order, with all of its examples, numbers, practice questions and answer outlines (no video timestamps: each page is meant to be read on its own);
- **real runs**: every block with an *output* strip under it was actually run with the standard Python library;
- **Excalidraw diagrams** of every mechanism, redrawn in the same colour language on every page. Press *copy for Excalidraw* under a drawing to remix it;
- **Beyond the notes** sections: knobs and defaults, pitfalls, production checklists and interview questions;
- a **revision cheat-sheet** and a **tap-to-flip self-test** at the end of each chapter.

> [!IMPORTANT] How the notes are made
> Each page is built from one chapter of the vault, in the order the vault gives it: the chapter overview, then each subsection note. The vault is the source. Anything **not** from the vault is labelled **Beyond the notes**.
>
> Where the vault links to another chapter, the page says "Chapter 15 (Metrics)" in plain text. No links are kept.

## The big idea in one paragraph

The APM interview rewards one answer pattern: **clarify** the goal and the user, **structure** the answer out loud with a framework, **reason with numbers** (a guesstimate or a unit-economics check), and **close on a metric** with a trade-off. Part II gives the AI vocabulary that changes those answers: outputs are probabilistic, data is a product input, quality is a distribution, and every call has a cost and a latency. Part III is the toolkit. Part IV is estimation. Part V puts it all together in case practice.

![The whole prep in one picture: four parts that feed one interview answer pattern.](diagrams/l0-big-idea.svg)

## The 22 chapters

The pages are grouped by Part. The page number is the order of the notes here; the chapter number is the vault's own numbering, which is what the page headings and tabs show.

### Part II · AI products (Chapters 4-10)

| Page | Chapter | Title |
|---|---|---|
| 1 | 4 | What Makes an AI Product Different |
| 2 | 5 | AI Technology Literacy for PMs |
| 3 | 6 | AI Product Strategy and Economics |
| 4 | 7 | Designing AI Experiences |
| 5 | 8 | Evaluating and Measuring AI Products |
| 6 | 9 | Responsible AI, Risk, and Regulation |
| 7 | 10 | Launching and Iterating AI Features |

### Part III · Product thinking toolkit (Chapters 11-20)

| Page | Chapter | Title |
|---|---|---|
| 8 | 11 | Understanding Users |
| 9 | 12 | Product Design with CIRCLES |
| 10 | 13 | Product Improvement and App Critique |
| 11 | 14 | Prioritization |
| 12 | 15 | Metrics |
| 13 | 16 | Root Cause Analysis |
| 14 | 17 | Pricing and Monetization |
| 15 | 18 | Go-to-Market and Launch |
| 16 | 19 | Strategy and Market Entry |
| 17 | 20 | Execution: Roadmaps, PRDs, and Agile |

### Part IV · Estimation (Chapter 21)

| Page | Chapter | Title |
|---|---|---|
| 18 | 21 | Guesstimates |

### Part V · Case practice (Chapters 22-25)

| Page | Chapter | Title |
|---|---|---|
| 19 | 22 | Case Types and How to Approach Each |
| 20 | 23 | Worked Examples |
| 21 | 24 | AI Case Bank |
| 22 | 25 | Practice Protocol |

![Parts II to V and their chapters, in the order the notes build them.](diagrams/l0-parts-map.svg)

## How the calculators work (Beyond the notes)

The arithmetic in these notes runs on plain **Python 3 with the standard library**. Nothing is installed, no cluster is started, and no account is needed. Each calculator is a short file that prints its inputs and its results, so you can read the whole calculation in one screen.

Three rules keep the calculators honest:

- **Only where a calculation proves a point.** A few chapters carry a real-run block: latency and capacity, a threshold trade-off, a unit cost. Chapters with nothing to compute have none.
- **Placeholder numbers are labelled.** Prices, traffic and scores in the examples are illustrative. Replace them with your own before you use a number in an interview or a launch review.
- **Output is real and repeatable.** Every block with an output strip was run, and the strip is what the code printed. Nothing is typed in by hand.

A minimal example, the same arithmetic that sizes the peak in Chapter 4:

```python title="lab_intro_calc.py"
# A calculator in this project: plain Python, no installs, prints its inputs and results.
queries_per_day = 1_000_000
average = queries_per_day / 86_400
print(f"average load : {average:.1f} queries per second")
print(f"peak at 4x   : {average * 4:.1f} queries per second")
```

```output
average load : 11.6 queries per second
peak at 4x   : 46.3 queries per second
```

Capacity is set by the peak, not the average: at a 4x peak the system has to handle four times the average load.

## How to read the diagrams

The same colours mean the same things on every page.

![The colour key used in every diagram.](diagrams/l0-colour-key.svg)

## A tiny glossary

Terms are from the vault's notes or in standard use. The first column is the term the pages use.

| term | meaning |
|---|---|
| **probabilistic output** | an answer chosen as the most likely of several possible outputs; it can be right, wrong or partly right |
| **deterministic** | the same input always gives the same output, because engineers wrote the rules |
| **acceptance bar** | the minimum quality an output must reach to be shown, for example "no invented facts" |
| **error budget** | the share of failures the team agrees to live with, set per category and severity |
| **golden set** | a held-out set of inputs with agreed good answers, used to test a model before release |
| **LLM-as-judge** | another language model scores outputs against a rubric; its scores are checked against human ratings |
| **precision** | of the cases the model flagged, the share that were right |
| **recall** | of the real cases, the share the model found |
| **threshold** | the score above which the product acts; it is a decision made on top of the model, not part of it |
| **data flywheel** | a loop: usage gives feedback, feedback improves the product, the better product draws more usage |
| **calibration** | how well a model's stated confidence matches how often it is right |
| **time to first token (TTFT)** | the delay before the first visible token of an answer |
| **tokens per second** | how fast the rest of an answer arrives once it starts streaming |
| **peak-to-average factor** | peak load divided by average load, often 3 to 5x; it sizes capacity |
| **unit economics** | the money in and out of one unit (a query, a task, a seat); it shows whether the product pays |
| **graceful failure** | the product steps down (says "I don't know", falls back, hands off) instead of breaking |
| **kill switch** | a control that turns an AI feature off or rolls it back to an earlier model or prompt |
| **guardrail metric** | a metric that must not get worse (harmful outputs, latency, cost) while the main metric improves |


# Chapter 4 · What Makes an AI Product Different

<!-- lecture n="1" label="4" short="AI products differ" status="done" kind="AI foundations" -->

## At a glance

| Question | Short answer |
|---|---|
| What makes an AI feature different? | Its output is the **most likely** answer, not a fixed one, so success is a **rate**, not yes or no. |
| What is a deterministic feature? | Same input, same output. Engineers write the rules, and a bug can be reproduced and fixed in the code. |
| Why does data matter so much? | Data is a **product input**. Its quality, coverage, freshness and labels set model quality. A closed loop is a **flywheel**. |
| How do you judge quality? | As a **distribution**: by segment, by the worst tail and by severity. Not as a count of open bugs. |
| What does one AI call cost? | A real amount that grows with input, output, model choice and retries. Classic software has near-zero marginal cost per request. |
| How long does it take? | Two numbers: **time to first token** and **tokens per second**. Streaming hides most of the wait. |
| How do you size capacity? | Peak load = queries per day ÷ 86,400 × a peak-to-average factor (often 3-5x). Check it against limits. |
| What if the model is wrong? | Plan for it: calibrated confidence, transparency, user control, and a graceful way out. |
| Which error matters most? *(Beyond the notes)* | The one that costs more. Set the threshold from that cost, not from the headline accuracy. |
| How do you use this in an interview? *(Beyond the notes)* | Name the data source, signal, label, loop and consent. State the trade-off and close on a metric. |

> [!NOTE] Where this comes from
> The vault lists no outside sources for this chapter: its own notes say the content is from general product and ML knowledge, plus publicly reported incidents. The vault's further-reading list names *AI Product Reading*, *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

AI products behave differently from classic software: outputs are probabilistic, data is a core input, quality is a distribution, and every call has a cost and latency. This chapter gives you the vocabulary to talk about those differences in an APM interview.

The chapter has five sections, each one a building block for the next:

- **4.1 Probabilistic outputs vs deterministic features.** Same input, different outputs. Define acceptance bars instead of "works or doesn't."
- **4.2 Data as a product input and data flywheels.** Data as a product input, how feedback loops compound, and where they break.
- **4.3 Quality as a distribution, not a bug count.** Measure quality by segment, tail and severity.
- **4.4 Latency, cost per query, and capacity planning.** Per-call cost and latency budgets, and the levers that control them.
- **4.5 Trust, errors, and graceful failure.** Design for wrong answers, with clear fallbacks and recovery.

## Key takeaways

- AI outputs are probabilistic, so success is a rate with an agreed error budget.
- Data is a product input, and the feedback loop is the real moat if it is closed and clean.
- Quality is a distribution: check segments, the worst tail, and severity, not the average.
- Cost per query and latency are product constraints that shape the UX and pricing.
- Trust depends on calibration, transparency, control, and a graceful way out when the model fails.

> [!SIR] From the source notes
> AI outputs are probabilistic, so success is a rate with an agreed error budget.

## 4.1 Probabilistic outputs vs deterministic features

> A deterministic feature gives the same output for the same input; an AI feature gives the most likely output, which can be right, wrong, or partly right.

### Concept

- **Deterministic software:** rules are written by engineers. Input X always gives output Y. Bugs are reproducible and usually fixed by changing code.
- **Probabilistic software:** a model learns patterns from data and produces a score or distribution over possible outputs. The product shows the top result (or samples from the distribution). The same input can yield different outputs, and "correct" is a matter of degree.
- **What changes for a PM:**
  - Success is a rate, not a yes/no. "Works 92% of the time on this task" is the spec.
  - Every output needs an acceptance bar, e.g. "a summary is acceptable if no fact is invented."
  - Failures are not always bugs. Some are expected at the tail, so design must plan for them (see 4.5).
  - Reproducing a complaint may require the exact input, model version, prompt, and settings. Even at temperature 0, hosted LLMs are not guaranteed to be bit-for-bit repeatable, so log everything.
- **Practical implications:**
  - Define the output contract up front: format, length, confidence, and what happens below a threshold.
  - Separate the "decision" layer (threshold, ranking cut-off) from the model so the threshold can be tuned without retraining.
  - Expose uncertainty where it matters (see Chapter 7, User control, transparency, and confidence signals).
- **Precision vs recall framing:** most probabilistic features trade false positives against false negatives. Moving the threshold shifts the mix, so the PM picks the point based on which error costs more (a blocked genuine payment vs a missed fraud).
- **Rule of thumb:** use deterministic logic when the rules are known and stable. Use probabilistic models when the rules are too many or too fuzzy to write by hand, and accept the error budget that comes with that.

![Deterministic software gives one answer from a rule; probabilistic software gives a distribution, and the product shows the top one.](diagrams/l1-deterministic-vs-probabilistic.svg)

### Try it locally: two thresholds

*(Beyond the notes: reproduced locally with the standard library.)* Ten transactions scored by a made-up fraud model, four of them fraud. Watch what a higher and a lower threshold do to the two errors:

```python title="lab_p1_threshold.py"
# Ten transactions scored by a fraud model: (score, is_fraud)
rows = [(0.95, 1), (0.91, 0), (0.88, 1), (0.74, 0), (0.66, 1),
        (0.52, 0), (0.45, 0), (0.31, 1), (0.22, 0), (0.10, 0)]

def at(threshold):
    tp = sum(1 for s, y in rows if s >= threshold and y == 1)   # fraud blocked
    fp = sum(1 for s, y in rows if s >= threshold and y == 0)   # genuine blocked
    fn = sum(1 for s, y in rows if s < threshold and y == 1)    # fraud missed
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return tp, fp, fn, precision, recall

for th in (0.9, 0.6):
    tp, fp, fn, p, r = at(th)
    print(f"threshold {th:.1f}: blocked {tp + fp}, fraud caught {tp}, "
          f"wrongly blocked {fp}, missed {fn}, precision {p:.2f}, recall {r:.2f}")
```

```output
threshold 0.9: blocked 2, fraud caught 1, wrongly blocked 1, missed 3, precision 0.50, recall 0.25
threshold 0.6: blocked 5, fraud caught 3, wrongly blocked 2, missed 1, precision 0.60, recall 0.75
```

The higher threshold blocks only two payments, and one of them is genuine: most of the fraud gets through. Lowering the threshold to 0.6 catches three of the four frauds, at the cost of one more genuine payment blocked. Neither setting is "right" on its own. The PM picks the point from the cost of each error.

![Moving the threshold moves the mix: a high bar misses fraud, a lower bar blocks more genuine payments.](diagrams/l1-threshold.svg)

### Real-world examples

- **Gmail Smart Compose (Google, 2018):** suggests the next few words. A suggestion is only shown when the model is confident enough, so the team trades coverage (how often it suggests) against acceptance.
- **Spotify Discover Weekly:** a recommendation list generated from models. Two users get different playlists, and the product accepts that as the design.
- **Google Search ranking:** no single "right" answer. Quality is judged by human search quality raters (following Google's public rater guidelines) and by live experiments over a distribution of queries.
- **Grammarly:** every change is a suggestion the user accepts or dismisses, grouped by type (correctness, clarity, tone), which presents probabilistic output without pretending it is a fact.

### Practice questions

> [!INTERVIEW] Why can't you write unit tests for an AI feature the same way as for a checkout flow? What would you use instead?
> **Answer outline:** Unit tests still cover the deterministic shell (parsing, formatting, API contracts). For the model, replace exact assertions with an eval set scored against a rubric or reference, with a pass-rate threshold per category, plus property checks (valid JSON, no PII, length limits) that must hold 100% of the time.

> [!INTERVIEW] A PM says "the model is 95% accurate, ship it." What questions do you ask before agreeing?
> **Answer outline:** Accuracy on which slice? What is the cost of the 5% (a missed fraud vs a wrongly blocked payment)? What does the baseline (rules-only) get? Is the 95% measured on the distribution of real traffic or a curated set?

> [!INTERVIEW] Where would you put a confidence threshold in a fraud-detection product, and who should own that number?
> *(Beyond the notes: a starting point, not the vault's answer.)* Put it in the decision layer, after the model score, so it can change without retraining. Set it from the cost of each error, check it on live-like traffic, and let the owner of the fraud loss (with risk and operations) sign it off.

> [!INTERVIEW] Explain to an engineer from a payments background why "same input, same output" is no longer a valid test assertion.
> *(Beyond the notes: a starting point.)* A payments test asserts an exact result. A model returns a distribution, so the same input can give a different answer, and some answers are only partly right. Assert on a rate over a labelled set, and on hard rules (format, safety) that must never break.

*Related:* Chapter 4 (4.3 and 4.5 of this page), Chapter 7 (User control, transparency, and confidence signals), Chapter 8 (Offline evals: golden datasets, rubrics, LLM-as-judge), Chapter 12 (Adapting CIRCLES for AI features).

## 4.2 Data as a product input and data flywheels

> In AI products, data is a core input to the product, not a by-product, and a product that collects the right data can improve faster than competitors.

### Concept

- **Data is a product input.** Quality, coverage, freshness, and labelling determine model quality. A PM owns data decisions: what to log, what to label, what to retain, and what users are told.
- **Types of data a PM should map:**
  - Training data (historical examples, often labelled).
  - Evaluation data (held-out, golden sets; see Chapter 8).
  - Context data at inference (user profile, documents for RAG, session history).
  - Feedback data (accepts, edits, thumbs, corrections).
- **Data flywheel:** more users produce more usage data, which improves the model, which improves the product, which attracts more users. Works only if the feedback loop is closed and the signal is clean.
- **Conditions for a real flywheel:**
  - The feedback is captured as a by-product of normal use (e.g. the user accepts or edits a suggestion), not as a chore.
  - The data is specific to the task, not generic clicks.
  - The team actually retrains or re-tunes, and measures whether it helped.
  - Users consent to the use of their data (see Chapter 9, Privacy, consent, and data retention, and Chapter 10, Feedback loops and consented data collection).
- **Common traps:**
  - Feedback bias: users only click thumbs-down when angry, so the signal skews negative.
  - Logging without labels: lots of data, no usable ground truth.
  - Data moats that are weaker than they look, because public or licensed data is available to rivals.
  - Diminishing returns: the millionth example adds far less than the thousandth, so the advantage often comes from rare, hard cases, not raw volume.
- **Interview framing:** name the data source, the signal, the label, the loop, and the consent position.

![The flywheel turns only when feedback is a by-product of use, is closed back into the model, and is measured.](diagrams/l1-flywheel.svg)

### Real-world examples

- **Duolingo:** lesson difficulty and spaced repetition are tuned from millions of learner answers, a data loop that is hard for a new entrant to copy.
- **Google Search:** click and query-reformulation signals feed ranking. Scale of query logs is part of the moat.
- **GitHub Copilot:** accept and reject events on suggestions are a feedback signal for tuning the product. Data-use terms differ by plan: GitHub states that Business and Enterprise code is not used to train models, which shows that flywheels are constrained by customer contracts.
- **Swiggy / Zomato:** both run ML models for delivery-time estimates and restaurant ranking, trained on order and rider telemetry, a data loop that improves with order volume in each city.

### Practice questions

> [!INTERVIEW] What data would you log for an AI meeting-notes product, and what would you deliberately not log?
> *(Beyond the notes: a starting point.)* Log the transcript segments the user keeps, edits and shares, plus the timing of corrections. Do not log raw audio by default, attendee personal details beyond the workspace roster, or content from meetings the user has marked private. State the retention period in the consent screen.

> [!INTERVIEW] Design a feedback mechanism for an AI email drafting tool that produces clean training signal without annoying users.
> **Answer outline (Q2):** Implicit signal first (send as-is, edited, discarded, time to send). Explicit only on a tiny sample or after a negative event. Store edit diffs, not full emails, for privacy. State the consent and retention policy.

> [!INTERVIEW] Is "we have more data than competitors" a defensible moat? Give the conditions under which it is and is not.
> *(Beyond the notes: a starting point.)* It is defensible when the data is specific, hard to get, and fed back into the product in a loop that competitors cannot copy from public sources. It is not when the data is public or licensed to everyone, or when extra volume stops improving the model (diminishing returns).

*Related:* Chapter 4 (4.1 of this page), Chapter 6 (Defensibility: proprietary data, distribution, workflow integration, switching costs), Chapter 8 (Online metrics: task success, acceptance and edit rate, retention of AI users), Chapter 9 (Privacy, consent, and data retention, India DPDP Act 2023), Chapter 10 (Feedback loops and consented data collection), Chapter 19 (Competitive analysis and moats).

## 4.3 Quality as a distribution, not a bug count

> For AI products, quality is described as a distribution across inputs and severities, not as a count of open bugs that goes to zero.

### Concept

- **Bug count fails for AI.** A traditional bug has a repro and a fix. An AI "bug" like a wrong summary may appear on 3% of inputs, differ by language, and move when the model is updated.
- **Describe quality with a distribution:**
  - Quality score per output (rubric-based, 1-5, or pass/fail on criteria).
  - Breakdown by segment: language, input length, user type, intent.
  - Tail: the worst 1% or 5% of outputs, because they drive trust and complaints.
  - Severity: a harmful or legally risky error weighs far more than a stylistic one.
- **Define the bar, not just the average.** Example: "≥ 95% of answers are factually correct on the golden set, and 0 critical safety failures."
- **Track over time:** a single score is a snapshot. Quality must be watched across model versions, prompt changes, and new user cohorts (see Chapter 8, Regression testing, and Chapter 10).
- **Quality has layers:**
  - Model quality (offline evals).
  - Product quality (what the user sees after retrieval, formatting, and UI).
  - Business quality (task completion, retention).

  A model can score well offline and still fail in product.
- **PM's job:** agree the rubric with engineering and domain experts, decide the acceptable error budget, and say what gets shipped at each level.

![A healthy average can hide a weak segment and a red tail. The bar is set on the whole curve and on severity.](diagrams/l1-quality-distribution.svg)

### Real-world examples

- **Google Translate:** quality is judged on many language pairs with separate benchmarks; a pair can be "good" in one direction and weak in another.
- **Spotify recommendations:** quality is tracked through skip rate, save rate, and listening depth across user segments, not one number.
- **GitHub Copilot:** GitHub reports acceptance rates by language and context, and acceptance varies widely across them, so one overall number would hide weak segments.
- **Moffatt v. Air Canada (BC Civil Resolution Tribunal, February 2024):** one wrong bereavement-fare answer from the website chatbot led to a ruling against the airline, which shows why the tail and severity matter more than average accuracy.

### Practice questions

> [!INTERVIEW] A summarisation feature has 90% average quality. What else do you need to know before launch?
> **Answer outline:** Breakdown by segment and language; the tail (worst 5%); severity-weighted failures; whether quality holds on new content; how users react to failures (edits, abandonment).

> [!INTERVIEW] How would you set a quality bar for an AI tutor for school children?
> **Answer outline:** Split by severity: zero tolerance for unsafe or age-inappropriate content and for wrong answers marked as correct; a high bar (for example 95%+) for factual accuracy on the syllabus golden set, reported per subject, grade, and language; a softer bar for tone and helpfulness. Add a human expert review sample each release.

> [!INTERVIEW] Engineering says "quality is up 4%." What is your follow-up question?
> *(Beyond the notes: a starting point.)* Up on which segment, which severity and which set? Is the 4% from the tail or from the easy cases? Does the change hold on the last month of real traffic, and did any safety or refusal rate move?

*Related:* Chapter 4 (4.1 and 4.5 of this page), Chapter 8 (Offline evals; Guardrail metrics; Regression testing when models or prompts change), Chapter 15 (Guardrail and negative metrics).

## 4.4 Latency, cost per query, and capacity planning

> Every AI call costs money and time, so latency and cost per query are product design constraints, not just engineering metrics.

### Concept

- **Cost per query is variable.** Traditional software has near-zero marginal cost per request. An LLM or vision call has a real cost that scales with input size, output size, model choice, and retries.
- **Latency has a budget.** Users notice delays. For LLMs, split it into **time to first token (TTFT)** and **output speed (tokens per second)**: a 500-token answer at 50 tokens/s takes about 10 seconds to finish even if it starts in under 1 second. Common targets: first visible output in about 1 to 2 seconds for interactive features; background jobs can take minutes if the user is not waiting. Reasoning ("thinking") models add a hidden delay before the first visible token.
- **Levers the PM can pull:**
  - Model choice: a smaller model for easy cases, a larger one for hard ones (routing).
  - Context size: trim retrieved text, cap history.
  - Caching: reuse answers for repeated or near-identical queries; most API providers also offer discounted *prompt caching* for a repeated prompt prefix (such as a long system prompt).
  - Streaming: show tokens as they arrive so perceived latency drops.
  - Asynchronous UX: let the user do other things while a long job runs.
  - Limits: caps on free-tier usage, rate limits, and batch APIs for non-urgent work (major providers have priced batch jobs at roughly half the real-time rate).
- **Capacity planning:** two separate numbers.
  - *Peak load* = (queries per day ÷ 86,400) × peak-to-average factor (often 3-5x) → peak queries per second and tokens per minute. Check this against provider rate limits or GPU capacity before launch.
  - *Monthly cost* = queries per month × (input tokens × input price + output tokens × output price). Add retries, agent sub-calls, and evaluation traffic.
- **Unit economics link:** cost per query must sit well below the revenue or value per query (see Chapter 6, Unit economics: cost per task, inference cost, gross margin).
- **Trade-off statement for interviews:** "I would accept 2 seconds and higher quality for a weekly report, but not for an autocomplete."

![Latency is two numbers: the wait for the first token, then the speed of the rest. Streaming moves the first word earlier.](diagrams/l1-latency.svg)

### Try it locally: latency, peak load and monthly cost

*(Beyond the notes: reproduced locally with the standard library. The prices are placeholders to show the formula. Replace them with your provider's current list prices.)*

```python title="lab_p1_latency_cost.py"
# Latency and capacity for one AI feature. Inputs are illustrative and set below.
ttft = 0.8                      # seconds until the first token appears
answer_tokens = 500             # length of one answer in tokens
speed = 50                      # tokens per second once streaming
finish = ttft + answer_tokens / speed
print(f"first token at      : {ttft:.1f} s")
print(f"answer finished at  : {finish:.1f} s  (500 tokens at 50 tokens/s = {answer_tokens / speed:.0f} s)")

queries_per_day = 1_000_000
avg_qps = queries_per_day / 86_400
print(f"average load        : {avg_qps:.1f} queries per second")
for factor in (3, 5):
    print(f"peak at {factor}x average : {avg_qps * factor:.1f} queries per second")

# cost per query: placeholder prices, replace with your provider's current list prices
in_price, out_price = 2.00, 8.00     # dollars per 1 million input / output tokens
in_tok, out_tok = 3_000, 500         # prompt with retrieved context, answer
retry_rate = 0.10                     # 10% of calls are retried once
cost_call = (in_tok * in_price + out_tok * out_price) / 1_000_000
cost_query = cost_call * (1 + retry_rate)
monthly = cost_query * queries_per_day * 30
print(f"cost per call       : ${cost_call:.4f}")
print(f"cost per query      : ${cost_query:.4f}  (with 10% retries)")
print(f"monthly at 1M/day   : ${monthly:,.0f}")
print(f"batch at half price : ${monthly / 2:,.0f}")
```

```output
first token at      : 0.8 s
answer finished at  : 10.8 s  (500 tokens at 50 tokens/s = 10 s)
average load        : 11.6 queries per second
peak at 3x average : 34.7 queries per second
peak at 5x average : 57.9 queries per second
cost per call       : $0.0100
cost per query      : $0.0110  (with 10% retries)
monthly at 1M/day   : $330,000
batch at half price : $165,000
```

The first answer appears at 0.8 seconds, and the full answer lands at 10.8 seconds: the 500 tokens take 10 seconds at 50 tokens per second. The average load of a million queries a day is about 11.6 per second, but at three to five times that peak the system has to cope with 35 to 58 per second. Size for the peak. At the placeholder prices, each query costs about a cent, which is about $330,000 a month at a million queries a day. The batch price for work that can wait is about half of that.

![Cost per query has three parts; capacity is set by the peak, and the peak must sit under the limit.](diagrams/l1-cost-capacity.svg)

### Real-world examples

- **ChatGPT and similar assistants:** streamed responses reduce perceived wait even when total generation time is the same.
- **Google Smart Reply (launched in Inbox by Gmail in 2015, in Gmail from 2017):** short reply chips that must appear instantly, because a slow suggestion is useless once the user has started typing.
- **ChatGPT model routing (GPT-5, August 2025):** OpenAI shipped a router that sends quick questions to a fast model and harder ones to a slower reasoning model, a public example of routing for cost and latency.
- **UPI payment apps (illustrative):** fraud checks that run inside the payment path have a tight latency budget, so a typical design uses a fast model inline and heavier analysis asynchronously.

### Practice questions

> [!INTERVIEW] Your AI feature doubles the cost per user. What options do you have before you ask for a price increase?
> **Answer outline:** Route easy cases to a cheaper model; cut context; cache common answers; limit heavy features to paid tiers; measure which features drive the cost; only then change pricing.

> [!INTERVIEW] Design the latency budget for an AI voice assistant that answers questions from a knowledge base.
> **Answer outline (Q2):** Target about 1 second from end of speech to first audio. Split it: end-of-speech detection (~200 ms), speech-to-text (~200 ms), retrieval (~100 ms), LLM time to first token (~300 ms), text-to-speech first chunk (~200 ms). Stream every stage, use a smaller model, and play a short filler phrase if retrieval is slow.

> [!INTERVIEW] How would you decide whether to cache AI responses?
> *(Beyond the notes: a starting point.)* Cache when the same or near-same question recurs often, the answer does not depend on the user's private data, and a stale answer is cheap. Measure the hit rate and the cost saved, and set an expiry for answers tied to policies or prices.

*Related:* Chapter 6 (Unit economics; Pricing models: per seat, usage-based, outcome-based, bundled), Chapter 8 (Guardrail metrics: harmful outputs, latency, cost), Chapter 5 (LLM basics: tokens, context windows, prompting, temperature), Chapter 21 (AI estimates: tokens per user, inference compute, embedding storage), Chapter 4 (4.2 of this page).

## 4.5 Trust, errors, and graceful failure

> Users forgive an AI product for being wrong sometimes, but not for being wrong confidently and without a way out.

### Concept

- **Errors are expected.** Design assumes the model will sometimes be wrong, so the question is what the user experiences when it is.
- **Trust is built in layers:**
  - Calibration: the product's confidence matches its real accuracy.
  - Transparency: the user can see where an answer came from (sources, reasoning summary).
  - Control: the user can edit, reject, or undo.
  - Track record: repeated good outcomes raise trust over time; one high-visibility error can drop it fast.
- **Graceful failure patterns:**
  - Say "I don't know" or hand off to a human instead of guessing.
  - Show a confidence level and fall back to a rule-based or manual path below a threshold.
  - Offer a retry or a different phrasing.
  - Keep the rest of the product working when the AI part fails (degrade, do not break).
- **Severity matters.** A wrong movie suggestion is cheap. A wrong medical, legal, or payment answer is not. Set stricter gates and clearer warnings for high-stakes domains.
- **Measure trust, not just accuracy:** acceptance rate, edit rate, undo rate, escalation rate, and complaints per 1,000 sessions.
- **Incident readiness:** have a kill switch, a way to roll back to a previous model or prompt, and a communication plan (see Chapter 10, Staged rollouts and kill switches).

![Step down one rung at a time. The bottom rung is a kill switch, and the rest of the product keeps working on every rung.](diagrams/l1-graceful-ladder.svg)

### Real-world examples

- **Google AI Overviews (May 2024):** viral wrong answers soon after the US launch (for example, adding glue to pizza sauce) led Google to publish an explanation and restrict when overviews trigger, such as for nonsensical queries and satirical sources.
- **Moffatt v. Air Canada (February 2024):** a Canadian tribunal held the airline responsible for wrong bereavement-fare information its chatbot gave, rejecting the argument that the bot was responsible for its own statements. "The bot said it" does not limit liability.
- **GitHub Copilot:** suggestions are shown inline and can be dismissed with a keystroke, so the user keeps control and errors cost little.
- **Klarna AI assistant (2024-2025):** Klarna said its assistant handled about two-thirds of support chats in its first month (February 2024). In 2025 the CEO said the company would make sure customers can always reach a human, after concerns about service quality. Escalation to a human is part of graceful failure, not an admission of defeat.

### Practice questions

> [!INTERVIEW] An AI support bot gives a wrong refund policy to 200 customers. Walk through your first 48 hours.
> **Answer outline:** Stop or narrow the feature (kill switch); find the scope with logs; contact affected users and correct the policy; add a regression test on that policy; decide on compensation; post-mortem with owners and a launch-gate change.

> [!INTERVIEW] How would you show uncertainty in a medical-symptom checker without causing panic or false reassurance?
> **Answer outline (Q2):** Never show a raw probability. Show triage levels (self-care, see a doctor, urgent care) based on red-flag rules that always override the model, explain the main symptoms that drove the result, err toward "see a doctor" when uncertain, and add a clear emergency path. Validate calibration with clinicians before launch.

> [!INTERVIEW] What is the right escalation path when the AI is unsure in a loan-approval flow?
> *(Beyond the notes: a starting point.)* Route uncertain applications to a trained reviewer with the model's reasons and the missing evidence attached, not to a bare "declined." Set the uncertainty band with the credit-risk owner, log every escalation, and check later whether the reviewers agree with the model where it was confident.

*Related:* Chapter 7 (Handling hallucinations, errors, and recovery paths; User control, transparency, and confidence signals), Chapter 4 (4.3 of this page), Chapter 10 (Staged rollouts and kill switches), Chapter 9 (Safety, misuse, and content policy).

## Beyond the notes: the knobs on a model call

*(Beyond the notes: general API concepts. Names and defaults vary by provider, so check the provider's current documentation.)*

| Knob | What it does | The product question it answers |
|---|---|---|
| temperature | Controls how much randomness goes into choosing the next token. Lower values give more repeatable output, but not a guarantee. | How much variety does this task need? |
| top-p (nucleus sampling) | Samples only from the smallest set of likely tokens whose probabilities add up to p. | How wide a choice do we allow? |
| max output tokens | Caps the length of an answer. | What is the cost and latency ceiling? |
| context window | The total number of tokens the model can read in one call, input plus output. | How much retrieved text fits in one call? |
| seed (where offered) | Asks for repeatable sampling. Providers usually document it as best effort. | Can we reproduce a complaint? |
| stop sequences | Ends the output when a marker appears. | Does the output stop where the UI expects it to? |

A **token** is a chunk of text, often part of a word. Cost and latency are counted in tokens, not in words, so a 500-token answer is shorter than 500 words. The "temperature 0 is not bit-for-bit repeatable" warning from 4.1 is the reason to log model version, prompt and settings with every answer.

## Beyond the notes: averages hide the tail

The chapter says to look at the worst 1% to 5% of quality outputs. The same logic applies to latency. Report percentiles, not only averages:

- **p50 (median):** half of the requests are faster than this.
- **p95:** one request in twenty is slower than this. This is where complaints come from.
- **p99:** the slowest one in a hundred. Often the reason a support ticket is raised.

For an AI feature, report time to first token and total time at p50 and p95 separately. An average can look fine while one user in twenty waits far longer than the rest. The same goes for quality: a 95% average with a failing segment is still a failing segment.

## Beyond the notes: from score to threshold

The threshold is a product decision made on top of a model score. A few checks make it safer:

- **Calibration first.** A score of 0.9 should mean that about 90% of cases with that score really are fraud. Check this on held-out data, using a reliability chart, before you pick a threshold.
- **Shadow mode.** Run the model and log its decisions without acting on them. Compare with the current rule or human decision before the threshold goes live.
- **Store the score with the decision.** Then you can re-tune the threshold later without replaying the traffic.
- **Per-segment thresholds** can be right (new users and long-standing users behave differently), but each one needs its own evaluation and its own owner.
- **Re-check after every model or prompt change.** A threshold tuned on last month's model can drift.

## Beyond the notes: production checklist

- Log the model version, prompt version, input and output, retrieved document IDs, and the user's action (accept, edit, reject). Follow the consent and retention rules (see Chapter 9).
- Build dashboards by segment, and alert on the tail, not only on the average.
- Track cost per successful task, not only cost per call. Retries and failed attempts are paid for too.
- Set budget alerts and rate limits per user and per feature.
- Test the kill switch and the rollback before launch, and roll out in stages (see Chapter 10).
- Write caching rules: what may be cached, for how long, and what must never be cached (anything personal).

## Beyond the notes: pitfalls

- **The 95% trap with rare events.** If 99 of 100 transactions are genuine, a model that never flags fraud is 99% accurate and catches nothing. Ask for precision and recall, and for the base rate.
- **Reading temperature 0 as proof of repeatability.** It lowers randomness; it does not guarantee identical output.
- **Testing on a curated set, then shipping to the real traffic mix.** The distribution of real queries is usually messier.
- **Treating escalation to a human as a failure.** A designed handoff is part of the product.
- **Choosing a model from a leaderboard** and ignoring what it costs at peak load.

## Beyond the notes: interview corner

- **"Explain precision and recall to a non-technical stakeholder."** Precision: of the cases we flagged, how many were right. Recall: of the real cases, how many we found. Raising the threshold usually raises precision and lowers recall.
- **"Does streaming make the product cheaper?"** No. It changes the perceived wait, because the first word arrives sooner. The total tokens, the total cost and the total time stay about the same.
- **"How would you know a data flywheel is working?"** Evaluate the model on the same golden set before and after each retrain, and watch the live acceptance rate. If neither moves, the loop is not closed.
- **"Why is model choice a product decision?"** It sets quality, cost and speed together. Routing easy cases to a smaller model is a trade-off you can measure against the acceptance rate.

## Revision cheat-sheet

![Chapter 4 on one page: five ideas, each with the question it answers.](diagrams/l1-big-picture.svg)

- **4.1** Deterministic = same input, same output; AI = most likely output. Success is a **rate** with an **acceptance bar**. Put the threshold in a decision layer. Pick the threshold from the cost of each error.
- **4.2** Data is a **product input**: training, evaluation, context and feedback data. A **flywheel** needs a closed loop, a clean signal captured as a by-product, retraining and measurement, and consent. Traps: feedback bias, logging without labels, diminishing returns.
- **4.3** Quality is a **distribution**: per output, by segment, the worst tail, severity. Set the bar on the whole curve (for example, 95%+ on the golden set and zero critical failures). Track it across model and prompt changes.
- **4.4** Cost per query and latency are product constraints. Latency = **time to first token** + **tokens per second**. Streaming moves the first word earlier. Capacity = average × a peak factor (often 3-5x), checked against limits. Levers: routing, context, caching, streaming, async UX, limits and batch.
- **4.5** Trust = **calibration**, **transparency**, **control**, **track record**. Fail gracefully: say "I don't know", fall back below a threshold, offer a retry, keep the rest working, and keep a kill switch and rollback ready.
- **Beyond the notes:** percentiles (p50, p95, p99) report the tail; the threshold needs calibration and shadow mode; the 95% accuracy trap with rare events; cost per successful task, not per call.

## Self-test

<details class="quiz"><summary>Why is "same input, same output" no longer a valid test for an AI feature?

Because the model returns the most likely output, which can vary and can be right, wrong or partly right. Test with an eval set scored against a rubric, with a pass-rate threshold per category, plus property checks that must always hold.

</details>

<details class="quiz"><summary>What should a PM ask before accepting "the model is 95% accurate"?

On which slice of traffic it was measured, what the 5% of errors cost, what a rules-only baseline gets, and whether the 95% comes from real traffic or a curated set.

</details>

<details class="quiz"><summary>Why does a data flywheel only work when feedback is a by-product of use?

Chores produce little data, and the users who bother are not typical. Implicit signals such as accept, edit or discard are captured without effort, and they are specific to the task.

</details>

<details class="quiz"><summary>Name the four types of data a PM should map for an AI product.

Training data (historical, often labelled), evaluation data (held-out golden sets), context data at inference (profile, documents, session history) and feedback data (accepts, edits, thumbs, corrections).

</details>

<details class="quiz"><summary>Why is a bug count a poor measure of quality for an AI feature?

A wrong summary may appear on a few percent of inputs, differ by language, and change with each model update. Describe quality as a distribution: by segment, the worst tail, and severity.

</details>

<details class="quiz"><summary>What is the difference between time to first token and tokens per second?

Time to first token is the delay before the first visible token. Tokens per second sets how fast the rest arrives. A 500-token answer at 50 tokens per second takes about 10 seconds to finish, even if it starts in under one second.

</details>

<details class="quiz"><summary>How do you estimate peak load for an AI feature?

Queries per day divided by 86,400, multiplied by a peak-to-average factor (often 3 to 5x). Check the peak against provider rate limits or GPU capacity before launch.

</details>

<details class="quiz"><summary>What is the monthly cost formula, and what does it leave out?

Queries per month times (input tokens times input price, plus output tokens times output price). Add retries, agent sub-calls and evaluation traffic.

</details>

<details class="quiz"><summary>What are the four layers of trust in an AI product?

Calibration (confidence matches real accuracy), transparency (the user can see where the answer came from), control (the user can edit, reject or undo), and track record (repeated good outcomes).

</details>

<details class="quiz"><summary>(Beyond the notes) A fraud model is 99% accurate on a set where 99 of 100 payments are genuine. Why can that still be useless?

A model that never flags fraud gets 99% accuracy and catches nothing. Ask for precision and recall, and for the base rate of fraud.

</details>

<details class="quiz"><summary>(Beyond the notes) Why does raising a fraud threshold usually improve precision but lower recall?

A higher bar blocks fewer cases, so the ones it blocks are more likely fraud (precision goes up), but more real fraud slips under the bar (recall goes down).

</details>

<details class="quiz"><summary>(Beyond the notes) Why should latency be reported at p95, not only as an average?

The average can look fine while a slow tail of requests waits far longer. The p95 is the time that one request in twenty is slower than, and it is where complaints come from.

</details>


# Chapter 5 · AI Technology Literacy for PMs

<!-- lecture n="2" label="5" short="AI tech literacy" status="done" kind="AI literacy" -->

## At a glance

| Question | Short answer |
|---|---|
| How do AI, ML, deep learning and GenAI relate? | AI contains ML, ML contains deep learning, and modern GenAI is a subset of deep learning. |
| What feedback does each learning type need? | Labelled answers (supervised), no answers (unsupervised), or rewards for actions (reinforcement). |
| What are the stages of an ML lifecycle? | Problem, data, modelling, evaluation, deployment, monitoring, retraining. Most of the time goes to data and monitoring. |
| What is a token, and what is a context window? | A token is a chunk of text, about 4 characters. The context window is the most the model can handle in one call, input plus output. |
| Prompting, RAG or fine-tuning? | Prompting first, RAG for facts that change, fine-tuning for behaviour and format. Move on only when the cheaper option fails on evals. |
| What is an agent? | An LLM in a loop: it plans, calls tools, observes the result, decides the next step, and stops on success, a limit or a handoff. |
| Which product families does this chapter cover? | Computer vision, speech, and recommendation systems, each with its typical pitfalls. |
| Where do you start with any AI feature? | The simplest approach: rules, then classic ML, then LLMs, justifying each step up. |
| What do you say in an interview? *(Beyond the notes)* | Name the learning type, the labels and the failure mode, then say which metric you would watch. |
| What is the one habit to build? *(Beyond the notes)* | Ask for the data, the loop and the cost before you ask for the model. |

> [!NOTE] Where this comes from
> The vault lists no outside sources for this chapter. Its notes say the content is from general ML, LLM and product knowledge. The vault's further-reading lists name *AI Product Reading*, *Blogs & Newsletters* and *Product Teardowns*, depending on the note. No links are kept here.

## The big picture

This chapter gives you the technical vocabulary an APM needs to scope AI work: the learning types, the ML lifecycle, LLM basics, how to choose between RAG and fine-tuning, agents, and the common AI product families. The goal is to ask the right questions, not to build models.

The chapter has seven sections:

- **5.1 AI, machine learning, deep learning, and generative AI.** How the terms nest, and when each one fits.
- **5.2 Supervised, unsupervised, and reinforcement learning.** What feedback each learning type needs.
- **5.3 The ML lifecycle, from problem definition to deployment.** The stages from framing to monitoring.
- **5.4 LLM basics: tokens, context windows, prompting, temperature.** Tokens, context, prompts and temperature.
- **5.5 RAG, fine-tuning, and embeddings: when to use each.** Prompting vs RAG vs fine-tuning vs long context, with a comparison table.
- **5.6 Agents and tool use.** Agent loops vs fixed workflows, tool calls, MCP, compounding error and approval gates.
- **5.7 Computer vision, speech, and recommendation systems.** The three product families and their typical pitfalls.

## Key takeaways

- Start with the simplest approach (rules, then classic ML, then LLMs) and justify each step up.
- Labels and feedback decide which learning type is possible. LLM assistants use all three: self-supervised pre-training, supervised fine-tuning and RLHF.
- Tokens drive cost and latency. A big context window is not memory. Use prompting first, RAG for facts that change, and fine-tuning for behaviour.
- Agents multiply error and cost across steps. Add checks, and an approval step for irreversible actions.
- Computer vision, speech and recommendation products depend on their data distribution, so test on the real segments: accents, devices, languages.

> [!SIR] From the source notes
> Start with the simplest approach, and justify each step up.

## 5.1 AI, machine learning, deep learning, and generative AI

> AI is the broad field, machine learning is the approach of learning from data, deep learning uses large neural networks, and generative AI produces new content.

### Concept

- **Nesting:** AI contains ML; ML contains deep learning; modern generative AI is a subset of deep learning (transformers for text and code, diffusion models for most image and video generation).
- **AI:** any system that performs tasks usually requiring human judgement. This includes rule-based systems, which many "AI" features still are.
- **Machine learning:** the model learns a mapping from inputs to outputs from examples, instead of hand-written rules. Good when the rules are too complex to write.
- **Deep learning:** neural networks with many layers. Strong on images, speech and text when there is a lot of data and compute.
- **Generative AI:** models that produce new text, images, audio or code. Large language models (LLMs) are the main form for product teams.
- **Foundation model:** a large model pre-trained on broad data that can be adapted to many tasks by prompting or fine-tuning. Most generative AI products build on one rather than training from scratch.
- **Discriminative vs generative (one-liner):** classic ML mostly predicts a label or a number (spam or not, ETA in minutes). Generative AI produces new content. Many good products combine both, such as a classifier that routes a ticket and an LLM that drafts the reply.
- **Why a PM cares:**
  - It sets the data needs, cost, latency and failure modes (see Chapter 4).
  - It tells you whether a rule-based version may be cheaper and more predictable.
  - It sets the vocabulary for talking to engineers and vendors.
- **Test question for any "AI" feature:** could a rules engine or a simple statistical model solve 80% of this? If yes, start there.

![The terms nest: AI holds ML, ML holds deep learning, and GenAI sits inside deep learning.](diagrams/l2-ai-nesting.svg)

### Real-world examples

- **Gmail spam filtering:** a long-running ML classifier product. Google said in 2019 that adding TensorFlow models let Gmail block about 100 million extra spam messages a day.
- **Google Photos search:** uses deep learning for image recognition, so you can search "beach" without tags.
- **ChatGPT, Claude, Gemini:** generative AI products built on large transformer-based language models.
- **Uber ETA (DeepETA, described on Uber's engineering blog in 2022):** a deep learning model that corrects a routing engine's ETA estimate. It is a predictive (not generative) use of deep learning.

### Practice questions

> [!INTERVIEW] Explain the difference between AI, ML, and generative AI to a non-technical founder in 60 seconds.
> *(Beyond the notes: a starting point.)* AI is the goal of getting a machine to do judgement-type work. ML is one way to do it: the machine learns from examples. Generative AI is the part of ML that writes new content, such as text or images.

> [!INTERVIEW] For a delivery app's ETA feature, would you use rules, classic ML, or generative AI? Why?
> **Answer outline (Q2):** ETA is a numeric prediction from structured features, so classic ML (gradient-boosted trees or similar) fits, with a rules fallback. Generative AI adds cost and unpredictability without a clear gain.

> [!INTERVIEW] When is a generative model the wrong tool even though it can do the task?
> **Answer outline (Q3):** When the answer must be exact and auditable (tax calculation, pricing), when a rule or lookup already works, when latency or cost per call matters at high volume (a classifier is far cheaper), or when you need a stable, explainable decision for regulation (credit). Use generative AI where outputs are open-ended language or content.

*Related:* Chapter 5 (5.2 Supervised, unsupervised, and reinforcement learning), Chapter 5 (5.4 LLM basics), Chapter 5 (5.7 Computer vision, speech, and recommendation systems), Chapter 4 (4.4 Latency, cost per query, and capacity planning).

## 5.2 Supervised, unsupervised, and reinforcement learning

> The three main learning types differ by what feedback the model gets: labelled answers, no answers, or rewards for actions.

### Concept

- **Supervised learning:** the training data has inputs and correct labels. Used for classification (is this spam?) and regression (what will the price be?).
  - PM question: where do the labels come from, and how reliable are they?
- **Unsupervised learning:** no labels. The model finds structure: clusters, topics, anomalies.
  - Used for customer segmentation, anomaly detection and grouping similar items.
  - PM question: who checks that the clusters mean something to the business?
- **Reinforcement learning (RL):** an agent takes actions and learns from rewards over time.
  - Used in games, robotics, and some recommendation and ad-bidding systems.
  - PM question: what is the reward, and can the system game it?
- **Self-supervised learning:** labels are created from the data itself (predict the next word). This is how most LLMs are pre-trained. Worth naming in interviews.
- **How an LLM assistant is trained (all three types in one pipeline):**
  1. Pre-training: self-supervised next-token prediction on a huge text corpus.
  2. Supervised fine-tuning (SFT): human-written example conversations teach the assistant its format.
  3. Preference tuning: RLHF (reinforcement learning from human feedback, where humans rank outputs and a reward model is trained on the rankings), or related methods such as DPO. Some labs use AI feedback (RLAIF).
  4. Reasoning models add RL on tasks with checkable answers (maths, code tests), often called RL with verifiable rewards.
- **Choosing a type:**
  - Labels available and cheap: supervised.
  - Exploring patterns: unsupervised.
  - Sequential decisions with a clear reward: RL, and only with a safe simulator or guardrails.
- **Reward hacking:** RL and optimisation systems chase the metric you give them. Pair the main metric with guardrail metrics (see Chapter 15, section 15.5).

![Three learning types, each defined by its feedback, and the four steps that train an LLM assistant.](diagrams/l2-learning-types.svg)

### Real-world examples

- **Gmail spam filter:** supervised, trained on user-reported spam and labelled mail.
- **Google News story clustering:** articles about the same event are grouped together without anyone labelling them, a classic unsupervised use.
- **Google DeepMind AlphaGo:** reinforcement learning with self-play, a clear example of reward-driven learning.
- **Netflix artwork personalisation (Netflix tech blog, 2017):** contextual bandits, a simple form of RL, choose which thumbnail to show each member and learn from whether they play the title.
- **ChatGPT (2022):** built on InstructGPT-style training, where RLHF turned a raw pre-trained model into a helpful assistant.

### Practice questions

> [!INTERVIEW] You have 10 million support tickets with no labels. What learning approach would you consider first, and what would you do to create labels?
> **Answer outline (Q1):** Unsupervised clustering to find ticket types; sample and label a set with domain experts; then supervised classification on the labelled set. Check label quality with inter-annotator agreement.

> [!INTERVIEW] Why is reward design the hardest part of an RL product?
> *(Beyond the notes: a starting point.)* The system optimises exactly what you reward, so a reward that is almost right can produce the wrong behaviour at scale. Write the reward with the business owner, add guardrail metrics, and test for reward hacking in a simulator before any live traffic.

> [!INTERVIEW] A supervised model is trained on last year's labels. What changes in the world could make it wrong this year?
> *(Beyond the notes: a starting point.)* New products, new customer segments, a change in how people write or speak, a new policy or price, or a change in the labelling rules. Watch the input distribution and the error rate by segment, and refresh the labels on a schedule.

*Related:* Chapter 5 (5.1 and 5.3), Chapter 8 (8.2 Human evaluation and labeling; 8.4 Guardrail metrics: harmful outputs, latency, cost).

## 5.3 The ML lifecycle, from problem definition to deployment

> An ML product moves through problem framing, data, modelling, evaluation, deployment, and monitoring, and most of the time goes to data and monitoring, not model training.

### Concept

- **Stages:**
  1. **Problem definition:** the decision or prediction the product needs, the success metric, and the baseline (what happens today without ML).
  2. **Data:** sourcing, labelling, cleaning, and splitting into train, validation and test sets.
  3. **Modelling:** choose an approach and train; compare to the baseline.
  4. **Evaluation:** offline metrics on held-out data, plus slice analysis (see Chapter 8, 8.1).
  5. **Deployment:** serve the model, with latency and cost targets, often behind a feature flag.
  6. **Monitoring:** watch input drift, output quality and business metrics.
  7. **Retraining and iteration:** update with new data, with a regression check (see Chapter 8, 8.5).
- **The LLM-era version of the lifecycle:** for products built on a foundation model, "data and modelling" shrink and "evaluation" grows. A typical loop is: define the task and the acceptance bar, write a prompt (and retrieval), build an eval set, iterate on the prompt or retrieval against the evals, ship behind a flag, monitor, and re-run the evals on every model or prompt change. Fine-tuning comes later, if at all.
- **PM responsibilities:** problem framing, metric choice, the baseline, the launch bar, the rollout plan, and the monitoring owner.
- **Common mistakes:**
  - Skipping the baseline, so no one knows whether ML helped.
  - Choosing a metric the business does not care about (for example, accuracy on a skewed dataset).
  - Assuming the offline score predicts the online result.
  - No plan for retraining or for ownership after launch.
- **Useful checkpoint:** can you say what happens when the model is wrong, and who notices?

![Seven stages in a loop: most of the time goes to data and monitoring. The LLM-era version adds an eval loop.](diagrams/l2-ml-lifecycle.svg)

### Real-world examples

- **Uber ETA prediction (DeepETA, Uber engineering blog, 2022):** Uber described moving from tree-based models to a deep learning model, with offline evaluation followed by online experiments before rollout.
- **Spotify recommendations:** offline ranking metrics are followed by online A/B tests, since offline gains do not always hold.
- **Stripe Radar:** Stripe's fraud product learns from payments across its network. Because fraud patterns shift constantly, retraining and monitoring are part of the product, not a one-off project.

### Practice questions

> [!INTERVIEW] You are asked to "add ML to search." What do you ask before any modelling starts?
> *(Beyond the notes: a starting point.)* What decision should search improve, and how is success measured today? What is the baseline ranking, what data is logged, and who owns the result after launch? Only then ask which model fits.

> [!INTERVIEW] Offline accuracy improved by 3% but the online conversion fell. What might explain it?
> **Answer outline (Q2):** Offline data may not match live traffic (position bias, missing features, latency timeouts). The model may change ranking in ways users dislike. Check the segments and run a holdout test.

> [!INTERVIEW] Design the monitoring plan for a credit-scoring model.
> *(Beyond the notes: a starting point.)* Track the input drift of key features, the score distribution, approval and default rates by segment, and fairness metrics by group. Set alert thresholds, name an owner for each alert, and set a retraining trigger. Keep a regression check before any new model goes live.

*Related:* Chapter 5 (5.1 and 5.2 of this page), Chapter 8 (8.5 Regression testing when models or prompts change), Chapter 10 (10.2 Monitoring drift and vendor model updates; 10.1 Staged rollouts and kill switches), Chapter 4 (4.4 Latency, cost per query, and capacity planning).

## 5.4 LLM basics: tokens, context windows, prompting, temperature

> An LLM reads and writes tokens, can only use what fits in its context window, is steered by prompts, and varies its output by temperature.

### Concept

- **Tokens:** the units an LLM reads and writes. In English, one token is roughly 4 characters, or about three-quarters of a word (so 1,000 tokens is about 750 words). Usage is billed per token, with input and output priced separately, and output usually several times more expensive. Prices are usually quoted per million tokens and have fallen sharply year on year for a given capability level, so always quote prices with a date.
- **Context window:** the maximum number of tokens (input plus output) the model can handle in one call. Output also has its own, smaller cap. Anything outside the window is invisible to the model. Windows grew from a few thousand tokens (2022) to hundreds of thousands or more in 2025-26 models, but:
  - you pay for every input token on every call, so a long context is a recurring cost;
  - quality can drop for facts buried in the middle of a very long context ("lost in the middle");
  - the model has no memory between calls. Chat "memory" is the product re-sending history or saved facts in the context.
- **Prompting:** instructions and examples that shape the output.
  - System prompt: standing rules and persona.
  - User prompt: the task.
  - Few-shot examples: show the desired format or judgement.
  - Structured output: ask for JSON or a fixed schema so the product can parse it.
- **Temperature:** controls randomness in sampling. Low (near 0) for consistent extraction or classification; higher for creative drafts. It does not make the model correct, and even temperature 0 is not guaranteed to be perfectly repeatable on hosted models. Some reasoning models fix or ignore this setting.
- **Other knobs:** max output tokens, stop sequences and top-p.
- **Reasoning models:** some models "think" before answering, producing hidden reasoning tokens that are billed (usually as output) and add latency. They help on multi-step problems and are wasteful on simple ones, so routing matters (see Chapter 4, 4.4).
- **Prompt caching:** many providers charge less for a repeated prompt prefix, which rewards putting stable instructions first.
- **Limitations a PM must know:**
  - Hallucination: fluent but false output (see Chapter 7, 7.3).
  - Knowledge cut-off: the model does not know recent events unless you supply them (use RAG; see section 5.5).
  - Prompt sensitivity: small wording changes can shift outputs, so prompts need versioning and evals.
- **Interview point:** prompts are product code. Version them, test them and monitor them.

![A token is a small chunk of text, and the context window is everything one call can read, input and output together.](diagrams/l2-tokens-context.svg)

### Try it locally: how many pages fit in one call

*(Beyond the notes: reproduced locally with the standard library, using the vault's rule of thumb of 1,000 tokens = about 750 words. The 500 words a page and the 128,000-token window are assumptions to show the arithmetic, not vendor figures.)*

```python title="lab_p2_context_budget.py"
# How many pages fit in one call, using the vault's rule of thumb: 1,000 tokens = about 750 words.
words_per_token = 0.75          # 1,000 tokens = about 750 words
words_per_page = 500            # an assumption for a dense page of text
window_tokens = 128_000         # an illustrative window size, not a vendor figure
doc_pages = 300
doc_tokens = doc_pages * words_per_page / words_per_token
print(f"document: {doc_pages} pages x {words_per_page} words = {doc_pages * words_per_page:,} words")
print(f"document in tokens: about {doc_tokens:,.0f}")
print(f"window (illustrative): {window_tokens:,} tokens")
print(f"document fills {doc_tokens / window_tokens:.0%} of the window: it does not fit")
print(f"pages that fit in one call: about {window_tokens * words_per_token / words_per_page:.0f}")
```

```output
document: 300 pages x 500 words = 150,000 words
document in tokens: about 200,000
window (illustrative): 128,000 tokens
document fills 156% of the window: it does not fit
pages that fit in one call: about 192
```

A 300-page document is about 150,000 words, which is about 200,000 tokens. That does not fit a 128,000-token window in one call, and about 192 such pages would. This is the arithmetic behind the answer to the sales lead: "unlimited document length" is possible as a product feature (by chunking, retrieval or summarising), but not in one model call.

### Real-world examples

- **ChatGPT, Claude, Gemini:** consumer assistants whose "memory" and project features work by placing saved information in the context window, within its limits.
- **GitHub Copilot:** uses the surrounding code as context. The context budget decides which code the model sees.
- **Notion AI:** preset actions such as "summarise", "improve writing" and "translate" wrap a hidden prompt, so the user does not have to write one.
- **Indic-language tokenisation:** older tokenisers split Hindi, Tamil or Gujarati text into many more tokens per word than English, raising cost and shrinking the usable context. When OpenAI launched GPT-4o (May 2024) it reported a new tokeniser that cut token counts several-fold for languages such as Gujarati, Telugu, Tamil, Marathi and Hindi. Always measure tokens per message for each language you serve.

### Practice questions

> [!INTERVIEW] Explain tokens and context windows to a sales lead who wants to promise "unlimited document length."
> **Answer outline (Q1):** Tokens are chunks of text the model reads. The context window is the most it can read at once, and every token costs money on every call. "Unlimited length" is possible as a product feature (by chunking, retrieval or summarising) but not in one model call, and it raises cost and can lower accuracy. Offer a tested limit, for example "up to 300 pages", with a clear message above it.

> [!INTERVIEW] Which temperature would you choose for extracting invoice fields, and why?
> *(Beyond the notes: a starting point.)* A low temperature, near 0, because extraction should return the same fields for the same invoice. Still test the output against a labelled set, since temperature does not make the answer correct, and keep the output in a fixed schema so the product can check it.

> [!INTERVIEW] A prompt works in testing but fails for 8% of real users. What do you check first?
> **Answer outline (Q3):** Check the input distribution (length, language, format). The context budget may be exceeded. Check whether a system prompt rule conflicts with a user input. Build a failing-case set and re-run the evals.

*Related:* Chapter 5 (5.5 RAG, fine-tuning, and embeddings; 5.6 Agents and tool use), Chapter 4 (4.4 Latency, cost per query, and capacity planning), Chapter 7 (7.3 Handling hallucinations, errors, and recovery paths), Chapter 8 (8.5 Regression testing when models or prompts change).

## 5.5 RAG, fine-tuning, and embeddings: when to use each

> Use RAG to give a model fresh or private facts, fine-tuning to change how it behaves, and embeddings as the search index that makes RAG work.

### Concept

- **Embeddings:** numeric vectors that represent meaning. Similar texts sit close together, so you can search by meaning, not by keywords.
- **RAG (retrieval-augmented generation):** at query time, retrieve relevant passages (via embeddings and often keyword search), put them in the prompt, and ask the model to answer from them.
  - Pipeline: chunk documents, embed and index them, retrieve the top matches (often hybrid semantic plus keyword search), re-rank, then generate with citations.
  - Good for: company documents, policies, product catalogues, anything that changes.
  - Gives citations, and updates when the documents change, with no retraining.
  - Failure modes: poor retrieval (wrong chunks), chunks that split the context, stale or conflicting documents, and answers that ignore the retrieved text.
  - Evaluate the two halves separately: retrieval (did the right passage appear in the top results?) and generation (is the answer faithful to the passages, and does it answer the question?).
- **Fine-tuning:** further training on examples to change behaviour or style, or to teach a narrow format. Variants: supervised fine-tuning on input-output pairs, preference tuning on ranked outputs, and parameter-efficient methods such as LoRA, which train a small add-on instead of the whole model. Distillation (training a small model on a large model's outputs) is a common way to cut cost.
  - Good for: consistent tone, specialised classification, or formats that prompting cannot hold reliably.
  - Costs: data preparation, training, a new model to serve and evaluate, and a refresh when the base model changes.
  - Not a good way to add facts. Facts go stale and are hard to verify.
- **Prompting first:** start with prompting, then RAG for knowledge, then fine-tuning for behaviour. Move to the next option only when the cheaper one fails on evals.
- **Long context as an alternative:** if the whole corpus is small (a few documents), placing it directly in a long context window can beat building RAG. It gets expensive and less reliable as the corpus grows, and it does not handle per-user access control.
- **They combine:** many production systems use RAG for facts and a fine-tuned (or distilled) model for format and cost.

| | Prompting | RAG | Fine-tuning |
|---|---|---|---|
| Changes | Instructions | What the model knows at query time | How the model behaves |
| Fresh facts | No | Yes | No (goes stale) |
| Citations | No | Yes | No |
| Upfront cost | Lowest | Medium (pipeline, index) | Highest (data, training, re-evals) |
| Best for | First version | Private or changing knowledge | Tone, format, narrow tasks, cost cutting |

- **PM decision questions:**
  - Does the knowledge change weekly? RAG.
  - Do we need citations or access control on documents? RAG.
  - Is the problem "the model sounds wrong" or "the output format is inconsistent"? Consider fine-tuning.
  - What is the eval gain per unit of cost?

![The RAG pipeline with its failure modes, and the comparison of prompting, RAG and fine-tuning.](diagrams/l2-rag-pipeline.svg)

![Prompting, RAG and fine-tuning each change something different, so the choice follows the problem.](diagrams/l2-rag-ft-long.svg)

### Real-world examples

- **Intercom Fin:** a support agent that answers from a company's help-centre content and other sources, so answers change when the articles change, without retraining.
- **Perplexity:** search-based RAG. It retrieves web pages for each query and answers with numbered citations.
- **Notion AI Q&A (2023):** retrieval over a workspace's pages, respecting the user's permissions.
- **Spotify and Netflix recommendation embeddings:** item and user vectors used for similarity search, a classic embedding use outside text.
- **Meta Llama Guard:** a Llama model fine-tuned to classify prompts and responses against a safety taxonomy, a narrow, stable task that suits fine-tuning.

### Practice questions

> [!INTERVIEW] A bank wants its chatbot to answer from 5,000 policy PDFs that change monthly. RAG or fine-tuning? Why?
> **Answer outline (Q1):** RAG. Policies change monthly, answers need citations for compliance, and access may differ by customer type. Fine-tuning would go stale within a month and could not show sources. Measure retrieval quality on real customer questions, add a "no matching policy, connecting you to an agent" path, and keep document versions so you can show which policy an answer used.

> [!INTERVIEW] What are two ways a RAG product can fail even when the model is good?
> *(Beyond the notes: a starting point.)* The right passage is never retrieved (the chunks are wrong, or the query is phrased differently from the documents), or the passage is retrieved but split across two chunks, so the answer is incomplete. Check retrieval and generation separately to find which one fails.

> [!INTERVIEW] Your team proposes fine-tuning to "make the bot know our products." What is your response?
> **Answer outline (Q3):** Facts belong in retrieval, not in the weights. Fine-tuning would go stale and cannot cite. Ask what the actual failure is first, and test with better retrieval and prompting before any training.

*Related:* Chapter 5 (5.4 LLM basics; 5.6 Agents and tool use), Chapter 7 (7.2 User control, transparency, and confidence signals), Chapter 8 (8.1 Offline evals: golden datasets, rubrics, LLM-as-judge).

## 5.6 Agents and tool use

> An agent is an LLM in a loop that plans steps, calls tools such as search, databases or APIs, and acts until a goal is met or it stops.

### Concept

- **Tool use (function calling):** the model is given tool definitions (name, purpose, input schema). It can ask the product to call a tool and then use the result. The model does not run the tool itself.
- **Agent loop:** plan, act (call a tool), observe the result, decide the next step, and repeat. Stop on success, a limit, or a handoff.
- **Workflow vs agent:** in a *workflow*, the developer fixes the sequence of steps in code and the LLM fills in each step. In an *agent*, the model decides the next step itself. Workflows are cheaper, more predictable and easier to evaluate, so use an agent only when the path cannot be known in advance.
- **Model Context Protocol (MCP):** an open standard introduced by Anthropic in November 2024, now supported by many AI apps and vendors, for connecting models to tools and data sources through a common interface. Think of it as a standard plug between an agent and your systems.
- **Why it matters for PMs:**
  - Agents can complete multi-step tasks (book, file, reconcile), not just answer.
  - Each step adds latency, cost and a chance of error. Errors compound across steps.
  - Actions with side effects (send, pay, delete) need approval gates.
- **Design levers:**
  - Tool scope: fewer, well-described tools reduce mistakes.
  - Step and cost limits, plus a timeout.
  - Human confirmation before irreversible actions.
  - Logging of every tool call, for audit and debugging.
  - Least privilege: give the agent only the permissions it needs. Text it reads (web pages, emails, documents) can contain prompt-injection instructions (see Chapter 9, 9.3).
- **Evaluation:** measure task completion rate end to end, steps per task, tool-call accuracy and cost per completed task.
- **Autonomy is a dial:** suggest, draft, act with confirmation, act autonomously. Link to Chapter 6 (6.5) for the product categories.

![The agent loop: plan, act, observe, decide, and stop or repeat. Send, pay or delete goes through an approval gate first.](diagrams/l2-agent-loop.svg)

### Try it locally: the compounding error

*(Beyond the notes: reproduced locally with the standard library. It works through the vault's answer outline for the agent question below.)*

```python title="lab_p2_compounding.py"
# Per-step accuracy compounds: a task succeeds only if every step does.
for per_step in (0.95, 0.90):
    for steps in (1, 3, 5):
        print(f"per-step {per_step:.2f}, {steps} steps: task succeeds {per_step ** steps:.0%}")
print(f"five-step success of 60% needs about {0.60 ** (1 / 5):.1%} per step")
```

```output
per-step 0.95, 1 steps: task succeeds 95%
per-step 0.95, 3 steps: task succeeds 86%
per-step 0.95, 5 steps: task succeeds 77%
per-step 0.90, 1 steps: task succeeds 90%
per-step 0.90, 3 steps: task succeeds 73%
per-step 0.90, 5 steps: task succeeds 59%
five-step success of 60% needs about 90.3% per step
```

At 95% per step, five steps succeed about 77% of the time. At 90% per step, only about 59%. So an agent that completes 90% of one-step tasks but only 60% of five-step tasks is probably running at about 90% per step, with one weak step or a compounding problem. Find the failing step in the traces before you tune anything else.

### Real-world examples

- **ChatGPT with search and code tools:** the model calls search or a code runner and uses the results in its answer.
- **OpenAI Operator (January 2025, later folded into ChatGPT agent mode in July 2025):** a browser-using agent that fills in forms and books things, and hands control back to the user for logins and payments.
- **Coding agents (for example GitHub Copilot agent modes, and Claude Code):** read files, run commands and edit code in a loop, with permission prompts for risky actions.
- **Customer support automation (illustrative):** an agent looks up an order, checks the refund policy and issues a refund under a cap, with escalation above the cap. Vendors such as Intercom (Fin) and Sierra sell agents built on this pattern.

### Practice questions

> [!INTERVIEW] Design the approval rules for an agent that can issue refunds up to a limit.
> *(Beyond the notes: a starting point.)* Refunds below a low limit run automatically, with a log and a reversal path. Refunds above it wait for a human, who sees the order, the policy and the agent's reason. Set a daily cap per agent, and review a sample of automatic refunds each week.

> [!INTERVIEW] An agent completes 90% of tasks in one step, but 40% of tasks fail when they need five steps. What do you investigate?
> **Answer outline (Q2):** Per-step accuracy compounds: at 95% per step, five steps succeed about 77% of the time (0.95^5); at 90% per step, only about 59%. A 60% five-step success rate points to roughly 90% per-step accuracy, or one weak step. Find which step fails from traces, add validation between steps, reduce or clarify tool choice, convert fixed sequences into a workflow, and add a human checkpoint at the riskiest step.

> [!INTERVIEW] What is the difference between a chatbot that calls an API and an agent?
> **Answer outline (Q3):** A chatbot that calls an API follows a fixed path the developer wrote (one call, then answer). An agent decides which tools to call, in what order, and when to stop, based on intermediate results. It is more flexible, but harder to predict, test and cost-cap.

*Related:* Chapter 5 (5.4 and 5.5 of this page), Chapter 6 (6.5 Copilot vs automation vs autonomous agent), Chapter 7 (7.4 Human-in-the-loop design).

## 5.7 Computer vision, speech, and recommendation systems

> Three common AI product families: computer vision reads images, speech systems convert audio to text and back, and recommendation systems rank items for each user.

### Concept

- **Computer vision (CV):** classification (what is this?), detection (where are the objects?), segmentation, and OCR (text in images).
  - PM questions: which error costs most (a missed defect or a false alarm), and what lighting and camera conditions are real?
- **Speech:**
  - Speech-to-text (ASR): accuracy depends on accent, noise and domain vocabulary. Measure word error rate per accent and setting.
  - Text-to-speech (TTS): quality, latency and language coverage.
  - Voice products add a latency budget. A pause of over about one second feels slow in conversation.
  - Newer speech-to-speech models handle audio directly instead of chaining ASR, then an LLM, then TTS. That cuts latency and keeps tone, but is harder to inspect and log.
- **Recommendation systems:**
  - Candidate generation (pick a few hundred from millions), then ranking (order them), then re-ranking (apply business rules such as diversity or freshness).
  - Collaborative filtering uses behaviour; content-based uses item features; embeddings combine both.
  - Cold start: new users and new items have no history, so use popularity, onboarding questions or content features.
  - Metrics: click-through is easy to game, so pair it with satisfaction, retention and diversity.
- **Multimodal LLMs:** current frontier models accept images (and often audio) as input, so many CV tasks, such as reading a receipt or describing a photo, can now be prototyped with a prompt. Dedicated CV models still win on cost, latency and accuracy for high-volume narrow tasks (factory defects, face match).
- **Shared PM lesson:** these products depend on the data distribution. A model trained on one camera, accent or user segment may fail on another (see Chapter 9, 9.1).

### Real-world examples

- **Google Lens and Google Photos:** computer vision for search by image and for finding people or objects.
- **Google Translate, Apple Siri, Alexa:** speech recognition and synthesis, with accent and noise challenges.
- **Netflix and YouTube:** candidate generation and ranking from behaviour, with business rules for variety.
- **Amazon product recommendations:** "customers also bought" uses collaborative signals, a well-known retail example.
- **Video KYC in Indian banking:** since the RBI allowed video-based customer identification (V-CIP) in January 2020, banks and fintechs use OCR on ID documents and face matching during onboarding, where false rejects cost real customers.
- **Bhashini (Government of India):** a national language-technology platform offering speech recognition, translation and TTS across Indian languages. It was built because accent and language coverage were weak in global systems.

### Practice questions

> [!INTERVIEW] A factory wants defect detection on a line that changes product every week. What do you check before committing to a CV model?
> *(Beyond the notes: a starting point.)* The error costs (a missed defect against a false alarm that stops the line), the camera and lighting conditions on every product, how many labelled images exist per product, and whether a new product needs a new model or a quick re-training run.

> [!INTERVIEW] How would you launch a recommendation feed for a new app with no user history?
> **Answer outline (Q2):** Use popularity and category-based picks first; onboarding preferences; exploration slots to learn quickly; watch for filter bubbles; measure satisfaction, not just clicks.

> [!INTERVIEW] Why might a voice assistant work for urban speakers and fail for rural ones?
> **Answer outline (Q3):** Training and eval data skewed to urban accents, English or standard Hindi, and quiet settings. Rural users may speak dialects, code-mix, use local vocabulary, and call from noisy places on low-end phones and weak networks. Measure word error rate by region, dialect and noise level, collect consented data from under-served groups, and add fallbacks (buttons, IVR, human support).

*Related:* Chapter 5 (5.2 and 5.1 of this page), Chapter 9 (9.1 Bias, fairness, and representation), Chapter 4 (4.2 Data as a product input and data flywheels).

## Beyond the notes: the vocabulary behind the words

*(Beyond the notes: general definitions, stable across providers.)*

| Term | Plain meaning | Why a PM meets it |
|---|---|---|
| Training data | Examples the model learns from | Its quality and labels set the ceiling |
| Held-out (validation, test) data | Examples kept back from training | The only fair way to score a model |
| Overfitting | The model memorises its training data and fails on new data | Great offline score, poor live results |
| Inference | Running a trained model on a new input | Where latency and cost per call come from |
| Weights | The learned numbers inside a model | What fine-tuning changes |
| Distillation | Training a small model to copy a large one | A common way to cut cost |
| Hallucination | Fluent but false output | Why facts go through retrieval |

## Beyond the notes: a checklist before you pick a learning type

- Are there labels already? If yes and they are cheap, start with supervised learning.
- Can a rule or a lookup table give most of the answer? Ship that first and measure the gap.
- Is there a clear, safe reward and a simulator? Only then consider RL.
- For an LLM, have you written the acceptance bar and the eval set before the prompt?
- Do you know who reviews the labels, and how often?

## Beyond the notes: a RAG and context checklist

- **Chunk size is a trade-off.** Small chunks find precise passages but lose context. Large chunks keep context but blur the match.
- **Store the source ID and version with each chunk**, so every citation points to the document the answer really used.
- **Test retrieval with real customer questions** before you tune the model. Most "the bot is wrong" reports start with the wrong passage.
- **Keep stable instructions first** in the prompt. Repeated prefixes are cheaper where prompt caching is offered (see section 5.4).
- **Plan a no-answer path** ("no matching policy, connecting you to an agent") for questions the documents do not cover.

## Beyond the notes: agents in production

- **Set a step limit, a cost cap and a timeout** for every run, and log each tool call with its inputs and outputs.
- **Make tool errors visible** to the model and to the log. A silent failure is the hardest to debug.
- **Use idempotent actions** where you can, so a retried step does not charge a card or send an email twice.
- **Put a kill switch in front of the agent**, and test it before launch (see Chapter 10, 10.1).
- **Measure cost per completed task**, not cost per call (see Chapter 6, 6.2).

## Beyond the notes: pitfalls

- **Treating a long window as memory.** The model forgets anything outside the window, and everything inside is billed on every call.
- **Quoting prices without a date.** Token prices move, so every number needs a date and a source.
- **Reaching for RL when labels would do.** RL needs a reward you can defend and a safe way to test it.
- **Choosing an agent when a workflow fits.** Agents add cost, error and unpredictability.
- **Testing a vision or speech model on a clean set only.** Real cameras, accents and noise will differ.

## Beyond the notes: interview corner

- **"Explain RAG vs fine-tuning in 60 seconds."** RAG gives the model facts at query time, with citations, and updates with the documents. Fine-tuning changes how the model behaves, and it does not keep facts current.
- **"Why is temperature 0 not a guarantee?"** It reduces randomness. Hosted models may still vary, so log the model version, prompt and settings with each answer.
- **"What would you measure for an agent?"** End-to-end task success, steps per task, tool-call accuracy and cost per completed task, with traces for failures.
- **"Is this really AI?"** Ask whether a rules engine or a simple statistical model could solve most of it first. If it can, say so, and recommend starting there.

## Revision cheat-sheet

![Chapter 5 on one page: four groups of ideas, each with the question it answers.](diagrams/l2-big-picture.svg)

- **5.1** AI contains ML; ML contains deep learning; modern GenAI is a subset of deep learning. Test: could a rules engine or a simple model solve 80% of this?
- **5.2** Supervised (labels), unsupervised (structure, no labels), reinforcement (rewards). An LLM uses all three: pre-training, supervised fine-tuning, preference tuning (RLHF, DPO, RLAIF), and reasoning RL on checkable answers. Watch for **reward hacking**.
- **5.3** Seven stages: problem, data, modelling, evaluation, deployment, monitoring, retraining. Most time goes to data and monitoring. LLM-era: define the bar, write the prompt, build the evals, iterate, ship behind a flag, re-run evals on every change.
- **5.4** Tokens (about 4 characters, about 750 words per 1,000 tokens). The context window is input plus output, and it is not memory. Prompting: system prompt, user prompt, few-shot examples, structured output. Temperature controls randomness, not correctness.
- **5.5** Prompting first, RAG for facts that change (citations, access control), fine-tuning for behaviour and format. Long context fits a small corpus only. Evaluate retrieval and generation separately.
- **5.6** An agent loops: plan, act, observe, decide. Workflows are cheaper and more predictable. Errors compound per step (0.95 over five steps is 77%). Approval gates for irreversible actions; least privilege; log every tool call.
- **5.7** CV, speech and recommendations depend on the data distribution. Recommendations use candidate generation, ranking and re-ranking; cold start needs popularity and onboarding. Test speech and vision on the real segments.
- **Beyond the notes:** the vocabulary table (overfitting, inference, distillation); the RAG and agent checklists; the rule that facts go through retrieval.

## Self-test

<details class="quiz"><summary>What is the nesting from AI to generative AI?

AI contains machine learning, machine learning contains deep learning, and modern generative AI is a subset of deep learning, built mostly on transformers for text and code and on diffusion models for most images and video.

</details>

<details class="quiz"><summary>What feedback does each learning type need?

Supervised learning needs inputs with correct labels. Unsupervised learning needs no labels and finds structure. Reinforcement learning needs an agent that acts and receives rewards over time.

</details>

<details class="quiz"><summary>Name the three stages an LLM assistant goes through in training, in order.

Pre-training with self-supervised next-token prediction on a large text corpus, then supervised fine-tuning on example conversations, then preference tuning such as RLHF. Reasoning models add RL on tasks with checkable answers.

</details>

<details class="quiz"><summary>Why does a long context window not give the model memory?

The model has no memory between calls. Chat memory works because the product re-sends history or saved facts inside the context, and you pay for every input token on every call.

</details>

<details class="quiz"><summary>When should you choose RAG over fine-tuning?

When the knowledge changes, when answers need citations, or when access must follow the document owner. Fine-tuning changes behaviour and format, and it goes stale as the facts change.

</details>

<details class="quiz"><summary>What compounds across an agent's steps, and what does it cost you?

Per-step accuracy. At 95% per step, five steps succeed about 77% of the time; at 90%, about 59%. Find the weak step from traces, and add checks or a human checkpoint there.

</details>

<details class="quiz"><summary>What are the approval rules for an agent's irreversible actions?

Actions that send, pay or delete need a human confirmation before they run. Log every tool call, and give the agent only the permissions it needs.

</details>

<details class="quiz"><summary>What does a PM ask about a recommendation feed for a new app with no history?

How to handle cold start: popularity and category picks first, onboarding preferences, exploration slots to learn quickly, watch for filter bubbles, and measure satisfaction, not just clicks.

</details>

<details class="quiz"><summary>(Beyond the notes) What is overfitting, and why does it matter for a PM?

The model memorises its training data and fails on new data. It shows up as a strong offline score with poor live results, so keep a held-out test set and check the live numbers.

</details>

<details class="quiz"><summary>(Beyond the notes) What is the difference between training and inference?

Training is learning from examples. Inference is running the trained model on a new input. Latency and cost per call come from inference, so that is where the PM's budget lives.

</details>

<details class="quiz"><summary>(Beyond the notes) Why should you measure cost per completed task rather than cost per call for an agent?

An agent makes several calls per task, and retries and failed attempts are paid for too. Cost per completed task shows what a successful outcome really costs.

</details>


# Chapter 6 · AI Product Strategy and Economics

<!-- lecture n="3" label="6" short="AI strategy & economics" status="done" kind="AI strategy" -->

## At a glance

| Question | Short answer |
|---|---|
| Build, host or call an API? | Start with an API to learn what users want. Move down the stack only when cost, control or data needs justify it. |
| What is the unit that matters? | The cost of one completed task, not the cost per user. Gross margin depends on how many tasks a paying user triggers. |
| How do you measure cost per task? | Calls per task times (input tokens x price + output tokens x price), plus retrieval, tools and overhead, then divided by the success rate. |
| How do you price AI? | On the metric that moves with value and with cost: seat, usage, outcome, credits, bundle, or a hybrid of seat plus usage. |
| What makes an AI product defensible? | Proprietary data, distribution, workflow integration, switching costs, trust and brand, or a lower cost position. A wrapper alone is not a moat. |
| How much autonomy should you give? | Start at the lowest autonomy that delivers the value (copilot), earn the right to go higher, and gate every irreversible step. |
| Why does a higher autonomy change the economics? | More model calls per task, more checks, more human review of failures, and the cost of errors. |
| What do you say about training your own model? | Almost never, unless the model is the product, you have unique data at scale, and you have the budget to keep retraining. |
| Which metric catches cost regressions? *(Beyond the notes)* | Cost per successful task by feature and model version, with an alert on a week-over-week jump. |
| Which question comes first in a case? *(Beyond the notes)* | What does one task cost, and who is the paying user at the top 5% of usage? |

> [!NOTE] Where this comes from
> Several notes say they are written from general knowledge, with no converted source. The pricing note (6.3) draws on the Sigma PM casebook framework, and two Product Teardowns for Sportskeeda (February 2023) and Spotify (July 2022). The defensibility note (6.4) draws on the Blinkit idea from the February 2023 teardown. The vault's further-reading lists name *AI Product Reading*, *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

AI features change the economics of a product. Every request has a real marginal cost (model inference), so margins, pricing and build decisions must be reasoned about per task, not only per user. This chapter covers how to source models, how to measure and price the AI cost per unit of value, and how to position an AI product so it is defensible.

The chapter has five sections:

- **6.1 Build vs buy vs API access.** Training your own model, hosting an open model, or calling a vendor API.
- **6.2 Unit economics: cost per task, inference cost, gross margin.** Turning token and inference cost into per-task and per-user margin.
- **6.3 Pricing models: per seat, usage-based, outcome-based, bundled.** How to charge for AI when cost scales with usage.
- **6.4 Defensibility: proprietary data, distribution, workflow integration, switching costs.** Why a wrapper around a model is not a moat by itself.
- **6.5 Copilot vs automation vs autonomous agent.** The autonomy spectrum, and how it drives cost, risk and pricing.

## Key takeaways

- Model cost is a variable cost of goods sold (COGS). Price and design against it from day one.
- API access is the fastest route to market. It becomes a margin problem at scale.
- Usage-based or outcome-based pricing protects margin when cost tracks usage.
- A moat comes from data, distribution, workflow depth or switching costs, not from the model alone.
- Higher autonomy raises both value and risk. Scope it to what you can evaluate and afford.

> [!SIR] From the source notes
> Model cost is a variable cost of goods sold. Price and design against it from day one.

## 6.1 Build vs buy vs API access

> Start with a vendor API to learn what users want, then move down the stack only when cost, control or data needs justify it.

### Concept

There are three broad sourcing options for model capability:

| Option | What you do | Pros | Cons |
|---|---|---|---|
| Build (train your own) | Pretrain or heavily train a model | Full control, possible moat | Very expensive, needs scarce talent and data |
| Host an open-weight model | Fine-tune and run an open-weight model (for example the Llama, Mistral, Qwen or DeepSeek families) on your infrastructure or a cloud | Lower marginal cost at steady high volume, data stays in your VPC, no surprise deprecations | You own serving, scaling, evals and upgrades; usually behind the frontier on the hardest tasks |
| API access | Call a hosted model (OpenAI, Anthropic, Google and others), directly or via a cloud (Azure, AWS Bedrock, Google Vertex) | Fastest, best-in-class quality, no infrastructure, prices tend to fall over time | Vendor model changes and deprecations, data-handling terms, rate limits, less control |

Decision factors for a PM:

- **Differentiation:** is the model itself the product, or is it a component? Most products are the latter.
- **Data sensitivity:** regulated or confidential data may force self-hosting or a private deployment.
- **Volume and unit cost:** API cost is linear in usage. Self-hosting has a large fixed cost (GPUs, engineers) and only becomes cheaper at high, steady utilisation. Because API prices for a given capability have fallen fast, the break-even point keeps moving, so re-check it yearly.
- **Quality bar:** if a frontier API meets the eval bar, the premium for building is rarely justified.
- **Team capability:** serving and evaluating models is an ongoing platform cost, not a one-off project.

The real-world default in 2025-26 is a mix: an API for hard, low-volume tasks, and a small or open model for narrow, high-volume ones, behind a thin routing layer.

A common path: prototype on an API, measure quality and usage with evals, then consider routing high-volume, narrow tasks to a smaller or fine-tuned model. Keep the abstraction layer thin so you can switch vendors.

![Three ways to get model capability, with the factors that decide between them. Start with the API.](diagrams/l3-build-buy-api.svg)

### Real-world examples

- **GitHub Copilot:** launched on OpenAI models. Since late 2024 it has let users choose models from several vendors, including Anthropic and Google. GitHub owns the IDE integration and the product experience, so the model is a swappable component (buy and integrate).
- **Duolingo Max:** launched in 2023 on GPT-4 for features such as "Explain my answer" and roleplay, while Duolingo focused on pedagogy and UX.
- **Sarvam AI (India):** builds its own models for Indian languages and voice. In April 2025 it was selected under the government's IndiaAI Mission to build a sovereign foundation model. This is the build path, justified by language coverage and sovereignty rather than by cost.
- **Freshworks Freddy AI (India-founded SaaS):** generative features such as reply suggestions and ticket summaries, built on third-party models combined with Freshworks' own customer data: "buy the model, own the workflow".
- **BloombergGPT (2023):** Bloomberg trained its own 50-billion-parameter finance model. Later evaluations showed general frontier models matching or beating it on many finance tasks, a cautionary tale for training from scratch.

### Practice questions

> [!INTERVIEW] A healthtech startup wants AI summaries of patient notes. Build, host, or API? What would change your answer?
> **Answer outline:** Data residency and compliance push toward private hosting, or an API covered by a health-data agreement (in the US, a HIPAA Business Associate Agreement; in India, DPDP-compliant processor terms). Start with the API for quality, measure, then decide on hosting.

> [!INTERVIEW] Your API cost doubled after a vendor price change. What do you do in the next two weeks?
> **Answer outline:** Check per-task cost, route simple requests to a cheaper model, cache, and set a fallback to an open model.

> [!INTERVIEW] When would you tell leadership not to train a foundation model?
> **Answer outline:** Almost always, unless the model itself is the product, you have unique data at scale, there is a gap that APIs and open models cannot fill (language, sovereignty, on-device), and you have the budget to keep retraining as the frontier moves. Otherwise fine-tune or prompt an existing model, and invest in workflow and data.

> [!INTERVIEW] How do you keep vendor lock-in low without over-engineering?
> **Answer outline:** One internal interface for model calls, prompts stored outside vendor tools, the eval suite as the switching test, and a tested fallback model. Avoid building an abstraction over every vendor feature.

*Related:* Chapter 6 (6.2 Unit economics; 6.4 Defensibility), Chapter 8 (8.5 Regression testing when models or prompts change), Chapter 10 (10.2 Monitoring drift and vendor model updates), Chapter 5 (5.5 RAG, fine-tuning, and embeddings), Chapter 19 (19.5 Partnerships, acquisitions, and build-vs-buy strategy).

## 6.2 Unit economics: cost per task, inference cost, gross margin

> In AI products, the unit that matters is the cost of one completed task, and gross margin is set by how many tasks a paying user triggers.

### Concept

Traditional SaaS has near-zero marginal cost per user. AI features add inference cost on every call, so the unit economics must be built bottom-up:

**Cost per task** = calls per task x [(input tokens x input price) + (output tokens x output price)] + retrieval and tool costs + infrastructure overhead (plus retries and fallbacks)

Calls per task matters. An agent or a reasoning model may make many calls, or produce thousands of hidden reasoning tokens, for one user request, so a feature that looks cheap per call can be expensive per task. Measure **cost per successful task** (total cost divided by the tasks that actually succeeded), because failed attempts still cost money.

Worked example (illustrative prices): a support answer uses 3,000 input tokens and 400 output tokens. At $1 per million input tokens and $4 per million output tokens, that is $0.003 + $0.0016 ≈ $0.005 per call. With 1.3 calls per task (retries, a safety check) and an 80% success rate, cost per successful task ≈ $0.005 x 1.3 ÷ 0.8 ≈ $0.008.

**Cost per paying user** = tasks per user per month x cost per task

**Gross margin** = (revenue per user - cost of serving that user) / revenue per user, where the cost of serving (COGS) includes inference, hosting and third-party APIs.

Classic SaaS gross margins are often 75-80% or more. AI-heavy products have commonly reported lower margins, because inference is a real COGS line.

Key levers:

- **Model choice:** a smaller model can be 10x cheaper per token or more, and is often good enough for a narrow task.
- **Prompt length and context:** long retrieved context inflates input tokens. Trim it.
- **Output length:** output tokens are usually priced higher. Cap or structure responses.
- **Caching:** repeated prompts or semantic caches cut cost.
- **Routing:** send easy requests to cheap models, and hard ones to expensive models.
- **Retries:** failed or regenerated calls are hidden cost. Measure them.
- **Usage distribution:** averages hide heavy users. A small group of power users can make a plan unprofitable, so model the tail.

A PM should be able to write the sensitivity table: how margin changes if tokens per task go up 2x, if the price per token falls 50%, or if the feature's adoption doubles. The question to answer is whether the feature stays profitable at the 95th-percentile user, not the average one.

![Cost per successful task is a chain: cost per call, times calls per task, divided by the success rate.](diagrams/l3-cost-per-task.svg)

### Try it locally: cost per successful task

*(Beyond the notes: the vault's illustrative prices, worked locally with the standard library. The point is the order of the arithmetic: divide by the success rate last.)*

```python title="lab_p3_cost_per_task.py"
# Cost per successful task, with the vault's illustrative prices.
in_tok, out_tok = 3000, 400              # tokens per call
in_price, out_price = 1.00, 4.00         # dollars per 1 million tokens
calls, success = 1.3, 0.80               # calls per task (retries, safety check), success rate
per_call = in_tok * in_price / 1e6 + out_tok * out_price / 1e6
per_task = per_call * calls / success
print(f"cost per call: ${per_call:.4f}")
print(f"cost per successful task: ${per_task:.6f}")
print(f"rounded per-call route: ${0.005 * calls / success:.6f}")
```

```output
cost per call: $0.0046
cost per successful task: $0.007475
rounded per-call route: $0.008125
```

The per-call cost is $0.0046, not $0.005. Carried through unrounded, the cost per successful task is $0.0075. The vault's "about $0.008" comes from rounding the per-call cost to $0.005 first, which gives $0.0081. Both are close, but a model should keep the full precision: rounding an early step moves the answer by about 8%.

### Try it locally: the sensitivity table

*(Beyond the notes: the vault's own illustration, a Rs 499 plan with Rs 4 per summary. The 30 and 60 summaries a month, and the 120 for a power user, are illustrative assumptions.)*

```python title="lab_p3_margin_sensitivity.py"
# Gross margin on one plan: revenue, cost per summary, and summaries per month (illustrative).
price = 499                              # Rs per month
cost_per_task = 4                        # Rs per summary
cases = [("base case", 4, 30), ("tokens per task x2", 8, 30), ("price per token -50%", 2, 30),
         ("adoption x2", 4, 60), ("power user, 120 summaries", 4, 120)]
print(f"plan price: Rs {price}; base COGS is {cost_per_task * 30 / price:.0%} of the price")
for name, cost, tasks in cases:
    cogs = cost * tasks
    print(f"{name:<26} COGS Rs {cogs:>4}   gross margin {(price - cogs) / price:>4.0%}")
```

```output
plan price: Rs 499; base COGS is 24% of the price
base case                  COGS Rs  120   gross margin  76%
tokens per task x2         COGS Rs  240   gross margin  52%
price per token -50%       COGS Rs   60   gross margin  88%
adoption x2                COGS Rs  240   gross margin  52%
power user, 120 summaries  COGS Rs  480   gross margin   4%
```

Doubling the tokens per task and doubling the adoption both cut the margin from 76% to 52%. Halving the price per token lifts it to 88%. The power user at 120 summaries leaves 4% of the price before any other cost. The average user hides this: the feature looks healthy on the average and nearly consumes the plan price on the heavy tail. That is the reason to model the tail, and the 95th-percentile user, before the launch.

![Gross margin on one plan under five illustrative cases: the tail, not the average, sets the margin.](diagrams/l3-margin-sensitivity.svg)

### Real-world examples

- **GitHub Copilot:** the Wall Street Journal reported in October 2023 that GitHub was losing money on many users of its $10-a-month plan, with heavy users costing far more than they paid (the report cited unnamed sources). In 2025 GitHub added monthly allowances of "premium requests" for advanced models, with paid overage: a usage-metered layer on top of a per-seat plan.
- **Intercom Fin:** priced per resolution (launched at $0.99 per resolution in 2023), so Intercom's cost per resolution, including failed attempts that do not resolve, has to stay well below that price.
- **Indic-language products:** with older tokenisers, the same sentence in Hindi or Tamil could take several times more tokens than in English, so the cost per task differed by language. Tokeniser improvements (for example, OpenAI's GPT-4o tokeniser in 2024) narrowed the gap. Measure tokens per task for each language before setting prices.

### Practice questions

> [!INTERVIEW] Your AI summariser costs Rs 4 per summary, and users generate 30 per month on a Rs 499 plan. Is the feature profitable? What would you change?
> **Answer outline:** 30 x Rs 4 = Rs 120, about 24% of the plan price before other costs. Check the tail users, route short documents to a cheaper model, and cap the length.

> [!INTERVIEW] How would you forecast AI COGS for a launch with no usage data?
> **Answer outline:** Estimate tokens per task from prototype logs, take a range of tasks per user, then build a best, base and worst case. Plan to revisit after two weeks.

> [!INTERVIEW] Why might a feature with 70% gross margin on average still be a problem?
> **Answer outline:** The average hides heavy users, who may be margin-negative. Usage grows over time. Agent features or longer contexts can raise tokens per task. Price competition may cut revenue. And 70% is below typical SaaS margins, which affects valuation.

> [!INTERVIEW] What metric would you put on a dashboard to catch cost regressions early?
> **Answer outline:** Cost per successful task by feature and model version, tokens per task (input and output), calls per task, and the share of users whose cost exceeds their revenue, with alerts on week-over-week jumps.

*Related:* Chapter 6 (6.1 and 6.3 of this page), Chapter 4 (4.4 Latency, cost per query, and capacity planning), Chapter 8 (8.4 Guardrail metrics: harmful outputs, latency, cost), Chapter 21 (21.4 AI estimates: tokens per user, inference compute, embedding storage), Chapter 16 (16.4 AI-specific RCA: model changes, prompt regressions, data drift, cost spikes).

## 6.3 Pricing models: per seat, usage-based, outcome-based, bundled

> Pick the pricing metric that moves with the value the customer gets and with your cost, so revenue and margin grow together.

### Concept

The Sigma casebook framework lists the common non-hardware pricing options as ad-based, periodic subscription, and freemium-style tiers. AI products add two more metrics that are tied to cost:

| Model | Charge based on | Good when | Risk |
|---|---|---|---|
| Per seat | Users per month | Value scales with headcount; predictable revenue | Heavy users cost more than the seat price; light users underpay |
| Usage-based | Tokens, requests, documents, minutes | Cost tracks usage closely | Hard for buyers to budget; churn when bills spike |
| Outcome-based | Successful task or resolution | Outcome is measurable and agreed | Needs trustworthy attribution; revenue volatile |
| Credits | Prepaid credits spent on different AI actions | Many features with different costs | Opaque to buyers; credit inflation |
| Bundled | Included in a higher plan or suite | Drives upgrades; raises perceived value | Hides AI cost; hard to price-discriminate |
| Hybrid | Seat fee + usage credits | Most enterprise AI deals | More complex to explain |

Guidelines:

- Price on the metric closest to value and cost (for example, resolution, document or seat).
- Keep a free or low-cost tier only if its cost per user is bounded (rate limits, a smaller model).
- Include a usage allowance inside the seat price to avoid bill shock. Charge overage above it.
- Check the Sigma pricing step: a product that is bundled may still need a stated price anchor for the interview answer.

![Six ways to charge for AI. Each one is a bet on which metric moves with value and cost.](diagrams/l3-pricing-models.svg)

### Real-world examples

- **GitHub Copilot:** a free tier (from December 2024), individual and business per-seat plans, and monthly "premium request" allowances with paid overage for advanced models. That is per seat plus usage.
- **Microsoft 365 Copilot:** launched for enterprises in 2023 as a $30 per user per month add-on (a seat-based add-on). In January 2025 Microsoft folded Copilot into consumer Microsoft 365 Personal and Family plans and raised their prices, the bundling move. Google did the same with Gemini in Workspace business plans the same month.
- **Intercom Fin:** priced per resolution (launched at $0.99 per resolution), the outcome-based model.
- **Salesforce Agentforce:** launched in 2024 at $2 per conversation, then added credit-based and per-user options in 2025. This shows how vendors iterate on AI pricing metrics as buyers ask for predictability.
- **Spotify (from the July 2022 teardown):** Free (ad-supported) and Premium (ad-free, offline) tiers, a freemium plus subscription structure that AI features could be bundled into.
- **Sportskeeda (February 2023 teardown):** primarily advertising-funded, with premium and subscription sections added to diversify revenue. A case of ad revenue being a weak base for a new feature.

### Practice questions

> [!INTERVIEW] You are launching an AI meeting-notes feature in a collaboration tool. Seat, usage, or bundle? Justify.
> **Answer outline:** Bundle it into the paid tier to drive upgrades, with a usage cap for transcription minutes. Add a paid add-on for heavy use.

> [!INTERVIEW] A customer says your per-resolution price is unpredictable. How do you respond?
> **Answer outline:** Offer a committed monthly bundle with resolution credits and an overage rate. Show the cost-per-resolution trend.

> [!INTERVIEW] When is free the right price for an AI feature?
> **Answer outline:** When the cost per user is small and bounded (a small model, caps), when the feature drives acquisition, retention or upgrades worth more than its cost, or when competitors give it away. Cap usage and keep the expensive capability for paid tiers.

> [!INTERVIEW] How do you decide between an add-on price and folding AI into the base plan?
> **Answer outline:** Use an add-on when the value is concentrated in some users, the cost per user is high, and you need to prove willingness to pay. Fold it in when adoption is the goal, the value is broad, and the cost per user is low enough to absorb, usually with a base-price increase.

*Related:* Chapter 6 (6.2 Unit economics; 6.4 Defensibility), Chapter 17 (17.1 Cost-plus, value-based, and competitive pricing; 17.2 Monetization models: subscription, freemium, ads, take rate, razor-and-blade, bundling), Chapter 24 (24.5 Launch an AI feature in a payments app: pricing and risks).

## 6.4 Defensibility: proprietary data, distribution, workflow integration, switching costs

> If every competitor can call the same model, the moat has to come from data, distribution, the workflow you sit in, or the cost of leaving.

### Concept

Model quality is commoditising: a capability that was frontier a year ago becomes cheap and widely available. A wrapper around a model has little defensibility, so the PM must answer "why won't a well-funded competitor, or the model vendor itself, copy this in a quarter?"

Sources of defensibility for AI products:

- **Proprietary data:** unique, consented, labelled data or domain corpora that improve the product and are hard to obtain. Data alone is not a moat unless it is used to improve outcomes (see Chapter 4, 4.2 on data flywheels).
- **Distribution:** an existing user base, channel or platform that the AI feature plugs into (for example, a messaging app or an e-commerce checkout).
- **Workflow integration:** the AI sits inside a system of record, with permissions, approvals and integrations. Removing it breaks daily work.
- **Switching costs:** data gravity, retrained teams, custom configurations, integrations and contracts.
- **Trust and brand:** in regulated or high-stakes domains, a proven safety record is slow to replicate.
- **Cost position:** a lower cost per task that lets you price below rivals and still earn margin.

Test: remove the model vendor from the equation. What is left that a customer would miss? If the answer is only the prompt, the moat is weak.

![Six sources of defensibility around one test: remove the model vendor, and see what the customer would miss.](diagrams/l3-moats.svg)

### Real-world examples

- **Bloomberg:** its moat is proprietary financial data plus the Terminal workflow. It trained BloombergGPT (2023), but general frontier models soon matched it on many finance tasks. That suggests the durable moat is the data and the workflow, not the model.
- **Microsoft 365 Copilot:** draws on the Microsoft Graph of user documents and emails, and sits inside existing Office workflows. An example of distribution plus workflow integration.
- **Blinkit (February 2023 teardown):** the teardown's ideas (ingredient kits, subscriptions for daily essentials) lean on an existing dense delivery network and user habit, which is distribution-based defensibility.
- **Epic Systems (US healthcare):** deep EHR integration creates switching costs that a new AI tool must work inside rather than replace. Epic has added generative AI features (such as drafting replies to patient messages, built with Microsoft) inside its own workflow.
- **Cursor vs GitHub Copilot:** the AI code editor Cursor grew quickly despite Copilot's distribution advantage inside VS Code and GitHub. This is a reminder that distribution slows rivals but does not stop a clearly better workflow.

### Practice questions

> [!INTERVIEW] A startup offers an AI legal-drafting tool built on a frontier API. Where is its moat, and how would you test it?
> **Answer outline:** Check whether it owns firm-specific templates and clause data, integrations with document systems, and retention after a model upgrade. Run a churn-risk test with a vendor-neutral baseline.

> [!INTERVIEW] Why might a model vendor be a competitor to your product?
> **Answer outline:** Vendors see aggregate demand through their APIs, and they move up the stack into popular use cases (for example, assistants adding coding, search and document features). If your product is a thin wrapper on their model, a single launch can match it.

> [!INTERVIEW] Which defensibility lever matters most for an Indian consumer app with a large user base?
> **Answer outline:** Distribution and habit first (the user base and daily use), then proprietary behavioural data in local languages that improves the feature, and trust (payments, KYC) in regulated categories.

> [!INTERVIEW] How would you measure switching costs in a product?
> **Answer outline:** Integrations per account, data volume stored, the number of customised workflows, time to migrate, and churn after competitor launches or price increases.

*Related:* Chapter 6 (6.1, 6.3 and 6.5 of this page), Chapter 4 (4.2 Data as a product input and data flywheels), Chapter 19 (19.3 Competitive analysis and moats).

## 6.5 Copilot vs automation vs autonomous agent

> Autonomy is a dial: the more the AI acts without a human, the more value it can create, and the more risk, cost and evaluation burden you take on.

### Concept

Three product postures sit on one spectrum:

| Posture | Who decides | Example behaviour | Typical risk |
|---|---|---|---|
| Copilot (assistive) | Human; AI suggests | Drafts text, code completion, suggested replies | Low; the human catches errors |
| Automation (rules + AI) | AI executes a bounded step | Auto-tags tickets, routes a claim | Medium; errors repeat at scale |
| Autonomous agent | AI plans and executes multi-step tasks | Books, files, or resolves end to end using tools | High; wrong actions have real consequences |

Why it matters for strategy and economics:

- **Value:** autonomy removes more human effort, so it can justify higher prices (outcome-based pricing fits here).
- **Cost:** agents call models many times per task (plan, act, check), so cost per task rises. See section 6.2.
- **Evaluation:** a copilot is judged on acceptance. An agent needs end-to-end task success, step-level traces and safety evals (see Chapter 8, 8.1 and 8.4).
- **Trust:** moving down the spectrum requires earned confidence. Typically you start as a copilot, log accept and edit rates, then widen the scope.
- **Reversibility:** actions that are reversible (drafts) can be autonomous sooner than irreversible ones (payments, emails sent to customers).

Analogy that works in interviews: self-driving cars' levels of autonomy, from driver assistance to full self-driving. Waymo runs fully driverless robotaxis in limited areas, after years of testing and remote support. Most cars ship only driver assistance. AI products climb the same ladder, area by area.

A PM decision rule: start at the lowest autonomy that delivers the value, earn the right to go higher with measured acceptance and error data, and put approval gates on any irreversible step.

![One dial, three postures: value, risk and evaluation burden all rise from copilot to agent.](diagrams/l3-autonomy-spectrum.svg)

### Real-world examples

- **GitHub Copilot:** the canonical copilot. Suggestions appear in the editor, and the developer accepts or rejects them.
- **Intercom Fin:** a support agent that resolves conversations end to end for many queries, with handoff to humans for the rest (agent-like, scoped by intent).
- **Cognition's Devin:** announced in March 2024 as an autonomous software engineering agent. Independent tests reported low end-to-end success on real tasks, which shows how hard the high-autonomy end is to evaluate.
- **Ticket auto-triage in help desks (Zendesk, Freshdesk):** AI classifies and routes tickets. This is bounded automation, where an error repeats at scale but is easy to reverse.
- **Duolingo Max:** "Explain my answer" is a copilot-style feature that keeps the learner in control.

### Practice questions

> [!INTERVIEW] You are asked to add an AI agent that can issue refunds in a food delivery app. Copilot, automation, or agent? What guardrails?
> **Answer outline:** Start with a copilot that drafts the refund for agent approval. Automate small refunds under a threshold, with rollback and audit. Require approval above a limit.

> [!INTERVIEW] How does moving from copilot to agent change your metrics?
> **Answer outline:** From acceptance and edit rate to task success, escalation rate and cost per completed task.

> [!INTERVIEW] Why can a higher-autonomy product have worse unit economics?
> **Answer outline:** More model calls per task, retries and verification steps, monitoring and human review of failures, and the cost of errors (refunds, support). Together these can outweigh the higher price.

> [!INTERVIEW] What would make you say no to an autonomous feature?
> **Answer outline:** Irreversible or high-harm actions, no reliable way to evaluate end-to-end success, regulation that requires a human decision (credit, hiring), or error costs that exceed the labour saved.

*Related:* Chapter 5 (5.6 Agents and tool use), Chapter 6 (6.2 and 6.3 of this page), Chapter 7 (7.4 Human-in-the-loop design), Chapter 24 (24.6 Build a support copilot for a logistics company).

## Beyond the notes: the numbers to know

*(Beyond the notes: standard finance terms, stable across companies.)*

| Term | Plain meaning | Why it matters here |
|---|---|---|
| COGS (cost of goods sold) | The direct cost of serving a customer | Inference, hosting and third-party APIs sit here for AI |
| Gross margin | Revenue minus COGS, as a share of revenue | The number a plan has to hold at heavy usage |
| p95 (95th percentile) | The usage or cost that 95 in 100 users stay under | Where complaints and margin problems hide |
| Take rate | The share of each transaction the platform keeps | An alternative to per-seat or per-usage pricing |
| Bill shock | A customer's surprise at a higher-than-expected invoice | A common reason for churn on usage-based plans |

## Beyond the notes: a unit economics template

Write the model in this order, and keep the full precision until the last line:

1. Tokens per call (input and output), from prototype logs.
2. Price per token, with the date of the price list.
3. Calls per task, including retries and safety checks.
4. Success rate per task, from the eval set or the live acceptance data.
5. Cost per successful task = steps 1 to 3 combined, divided by step 4.
6. Tasks per paying user per month, at the average and at the 95th percentile.
7. Gross margin per plan, at both values in step 6.

If step 7 fails at the 95th percentile, the plan needs a cap, a cheaper route, or a higher price before launch.

## Beyond the notes: pricing pitfalls

- **Free tiers without a bound.** A free tier with no rate limit or cheaper model turns into a cost line that grows with the free user base.
- **Credits that look unlimited.** Opaque credits lead to surprise bills and distrust. Show the balance and the price of each action.
- **Changing the price of existing customers without notice.** Give notice, a migration path and a clear reason.
- **Bundling before the cost is known.** A bundle hides the AI cost. Measure it for a quarter before you fold it into the base plan.

## Beyond the notes: a build-vs-buy checklist

- **Data terms:** does the vendor train on your data, where is it stored, and how is deletion handled?
- **Exit plan:** can you switch to a second model within a release, and does your eval suite run on both?
- **Vendor changes:** how much notice do you get for model deprecations, and can you pin a model version?
- **Rate limits:** what is the peak your feature needs, and what does the vendor allow?

## Beyond the notes: interview corner

- **"Why not just train our own model?"** Ask what the model is for. If it is a component of a product, the data, the workflow and the cost per task usually matter more than the model.
- **"How do you know a price is right?"** Compare the price with the cost per successful task at the 95th percentile, and with what the customer would pay for the outcome.
- **"What makes you say an AI feature is defensible?"** Name the source (data, distribution, workflow, switching costs, trust, cost) and the test: what is left, if the model vendor is removed?
- **"When would you move a feature from copilot to agent?"** When the acceptance data is strong, the errors are reversible or gated, and the end-to-end success can be measured.

## Revision cheat-sheet

![Chapter 6 on one page: four ideas, each with the question it answers.](diagrams/l3-big-picture.svg)

- **6.1** Three sourcing options: build (expensive, possible moat), host an open-weight model (control, fixed cost), API (fastest, best quality). Start with the API, then route narrow high-volume tasks to a smaller model behind a thin layer.
- **6.2** Cost per task = calls x (input tokens x price + output tokens x price) + tools and overhead, plus retries. Divide by the success rate. Gross margin = (revenue - COGS) / revenue. Model the 95th-percentile user, not the average.
- **6.3** Six models: per seat, usage-based, outcome-based, credits, bundled, hybrid. Price on the metric closest to value and cost. Include an allowance and charge overage.
- **6.4** A wrapper is not a moat. Sources: proprietary data, distribution, workflow integration, switching costs, trust and brand, cost position. The test: remove the model vendor and see what is left.
- **6.5** Copilot, automation, agent: value, cost and risk all rise with autonomy. Start at the lowest autonomy that works, earn the right to go higher, and gate every irreversible step.
- **Beyond the notes:** the numbers to know (COGS, gross margin, p95, take rate); the unit economics template; the pricing and build-vs-buy checklists.

## Self-test

<details class="quiz"><summary>Why should a PM start with an API rather than train a model?

It is the fastest route to market and the best quality for most tasks, and it lets you learn what users want before you pay for infrastructure. Move down the stack only when cost, control or data needs justify it.

</details>

<details class="quiz"><summary>What is the cost per successful task, in the vault's formula?

Calls per task times (input tokens x input price + output tokens x output price), plus retrieval, tools and overhead, then divided by the success rate, so failed attempts are paid for.

</details>

<details class="quiz"><summary>Why does an average gross margin hide a problem?

The average hides heavy users, who may cost more than they pay. Usage grows over time, and agents or longer contexts can raise tokens per task. Model the tail and the 95th-percentile user.

</details>

<details class="quiz"><summary>Name the six pricing models, and the one that fits most enterprise AI deals.

Per seat, usage-based, outcome-based, credits, bundled, and hybrid. A hybrid of a seat fee plus usage credits fits most enterprise AI deals.

</details>

<details class="quiz"><summary>When is free the right price for an AI feature?

When its cost per user is small and bounded (a small model, caps), when it drives acquisition, retention or upgrades worth more than its cost, or when competitors give it away. Keep the expensive capability for paid tiers.

</details>

<details class="quiz"><summary>What is the test for a moat?

Remove the model vendor from the equation. If the only thing left is the prompt, the moat is weak. A real moat is what the customer would miss: data, distribution, the workflow, or the cost of leaving.

</details>

<details class="quiz"><summary>How do the metrics change when a copilot becomes an agent?

From acceptance and edit rate to task success, escalation rate and cost per completed task. An agent also needs step-level traces and safety evals.

</details>

<details class="quiz"><summary>What is the decision rule for autonomy?

Start at the lowest autonomy that delivers the value, earn the right to go higher with measured acceptance and error data, and put approval gates on any irreversible step.

</details>

<details class="quiz"><summary>(Beyond the notes) What is gross margin, and what counts as COGS for an AI feature?

Gross margin is revenue minus the cost of serving the customer, as a share of revenue. For an AI feature, COGS includes inference, hosting and third-party APIs.

</details>

<details class="quiz"><summary>(Beyond the notes) Why keep full precision in a unit economics model?

Rounding an early step moves the answer. In the vault's example, rounding the per-call cost to $0.005 gives about $0.008 per successful task, while the unrounded arithmetic gives $0.0075.

</details>

<details class="quiz"><summary>(Beyond the notes) What is bill shock, and how do you avoid it?

It is a customer's surprise at a higher-than-expected invoice. Include a usage allowance inside the seat price, show the balance and the price of each action, and charge overage above the allowance.

</details>


# Chapter 7 · Designing AI Experiences

<!-- lecture n="4" label="7" short="Designing AI UX" status="done" kind="AI UX" -->

## At a glance

| Question | Short answer |
|---|---|
| Where does AI add value? | Language, pattern or search-heavy work where a good-enough first draft saves effort and errors are cheap to catch. |
| What is the quick scoring grid? | Score frequency, pain, error tolerance and data available from 1 to 3 each. High, painful, error-tolerant tasks with data come first. |
| What gives users control? | Accept, edit, regenerate, dismiss, stop, undo, and a say in which data the AI can use. |
| When should a confidence signal appear? | Only when it changes what the user does. Prefer evidence cues ("based on 3 sources") to raw percentages. |
| How do you handle a wrong answer? | Prevent, detect, signal, recover, learn. Design the failure path as carefully as the success path. |
| Where does a human sit? | Pick the pattern (suggest, review before send, exception handling, sample audit, escalation) from the cost and reversibility of a wrong output. |
| How do you set expectations? | Teach capability, limits, verification, data use and control at first run, with a guided task. |
| What do you measure in the first weeks? | Activation, repeat use in week 1, acceptance and edit rate, and "this was wrong" reports, by cohort. |
| Which screen states must exist? *(Beyond the notes)* | Waiting, streaming, done with sources, low confidence, no source, error, refused and handed-to-human. |
| How do you use this in an interview? *(Beyond the notes)* | Name the task, the error cost, the review point, the failure path and the metric you will watch. |

> [!NOTE] Where this comes from
> The vault's notes say that no converted source covers this chapter; they are written from general product knowledge, with a few publicly reported product examples. The vault's further-reading list names *AI Product Reading*, *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

AI changes what a good user experience means. The model is not always right, so the interface has to help users decide when to trust the output, check it, fix it, and know what the feature can and cannot do. Good AI UX is mostly about the places where the model is wrong, and about the people who must catch those cases.

The chapter has five sections, each one a building block for the next:

- **7.1 Choosing use cases where AI adds real value.** Where AI beats the existing flow, and where it does not.
- **7.2 User control, transparency, and confidence signals.** Letting users steer the output and see why it is what it is.
- **7.3 Handling hallucinations, errors, and recovery paths.** Designing for wrong answers, not only right ones.
- **7.4 Human-in-the-loop design.** Where people review, approve or override.
- **7.5 Setting expectations and onboarding users to AI features.** First-run experience and honest capability framing.

## Key takeaways

- Pick AI use cases where a good-enough draft or suggestion saves real effort and errors are cheap to catch.
- Give users control: edit, regenerate, stop, and undo.
- Show sources and confidence where they change the decision; do not show fake precision.
- Design the failure path as carefully as the success path.
- Set expectations at first use and teach the limits, so trust is earned rather than assumed.

> [!SIR] From the source notes
> Pick AI use cases where a good-enough draft or suggestion saves real effort and errors are cheap to catch.

## 7.1 Choosing use cases where AI adds real value

> Use AI where the task is language-, pattern- or search-heavy, where a good-enough first draft is valuable, and where errors are cheap to catch.

### Concept

Not every problem needs AI. A useful screen for a candidate use case has six questions:

1. **Is the input or output unstructured?** Text, images, audio, or messy documents are good fits. Clean numeric rules are not.
2. **Is there a useful "good enough" output?** A draft email, a summary, or a ranked list can save effort even when imperfect.
3. **Is the cost of an error low or recoverable?** A wrong suggested reply is cheap; a wrong medical dosage is not.
4. **Does a human already do this task repeatedly?** Repetition gives you data, evaluation cases and a clear baseline.
5. **Is the existing solution clearly worse?** Compare against deterministic logic, search, or templates. AI should win on the user's metric, not on novelty.
6. **Can you measure success?** If you cannot define acceptance, edit rate or task success, you cannot tell whether AI helped.

Anti-patterns to avoid:

- Adding a chatbot to a flow that a dropdown or form solves better.
- Using AI for exact calculations.
- Putting AI in a high-stakes decision with no review.

**Quick scoring grid for interviews.** Score each factor from 1 to 3: **frequency** of the task, times **pain** today, times **error tolerance**, times **data available**. High-frequency, painful, error-tolerant tasks with data are the first bets. The grid below shows the idea; the run block after it does the arithmetic.

![Four scores, each from 1 to 3, multiply into one number. A low score on error tolerance pulls the whole product down.](diagrams/l4-use-case-grid.svg)

A useful framing: AI works best as a "first 80%" that a person finishes, or as a search and summarization layer over information the user would otherwise read in full.

### Try it locally: score three use cases

*(Beyond the notes: the vault's grid computed locally. The scores are illustrative, not from the vault. Each one is a judgement call that the team should agree on.)*

```python title="lab_p4_use_case_score.py"
# Score candidate AI use cases on the four factors from 7.1, each 1 to 3.
# The scores are illustrative. Each factor is a judgement call, agreed with the team.
cases = [
    ("draft replies in a support tool", 3, 3, 3, 3),
    ("loan approval decisions",         2, 3, 1, 2),
    ("monthly tax filing",              1, 2, 1, 2),
]
print("score = frequency x pain x error tolerance x data available")
ranked = sorted(cases, key=lambda c: -(c[1] * c[2] * c[3] * c[4]))
for name, freq, pain, tol, data in ranked:
    print(f"{name:<34} {freq} x {pain} x {tol} x {data} = {freq * pain * tol * data:>2}")

# the same draft replies, but error tolerance 1 instead of 3
print(f"draft replies, error tolerance 1: 3 x 3 x 1 x 3 = {3 * 3 * 1 * 3}")
print(f"range of the grid: from 1 x 1 x 1 x 1 = {1} up to 3 x 3 x 3 x 3 = {3 ** 4}")
```

```output
score = frequency x pain x error tolerance x data available
draft replies in a support tool    3 x 3 x 3 x 3 = 81
loan approval decisions            2 x 3 x 1 x 2 = 12
monthly tax filing                 1 x 2 x 1 x 2 =  4
draft replies, error tolerance 1: 3 x 3 x 1 x 3 = 27
range of the grid: from 1 x 1 x 1 x 1 = 1 up to 3 x 3 x 3 x 3 = 81
```

The top use case scores 81, the highest possible. The loan case scores 12 because its error tolerance is 1: a wrong approval is costly and hard to undo. Dropping one factor from 3 to 1 cuts the product by a factor of three (81 to 27), so a single weak factor matters more than the others. The score tells you where to look first. It does not decide the question; the cost of an error does.

### Real-world examples

- **Gmail Smart Compose (Google, 2018):** predicts short completions inside a text field, a low-stakes use case where the user accepts or ignores each suggestion.
- **GitHub Copilot:** code completion where a wrong suggestion is visible and easy to reject before it ships.
- **Grammarly:** suggests rewrites on text the user already wrote; the user remains the author.
- **Freshworks Freddy AI:** ticket summaries and suggested replies inside the support agent's workspace. High-volume text work where the agent reviews before sending.
- **Apple Intelligence notification summaries (2024-25):** a counter-example. Summarising news alerts produced false headlines (the BBC complained in December 2024), and Apple paused summaries for news apps in January 2025. Low tolerance for error plus third-party brand risk made it a poor fit.

### Practice questions

> [!INTERVIEW] A bank asks you to use AI for loan approvals. Would you? Walk through the screen.
> **Answer outline:** High-stakes, regulated, fairness risk. AI can assist with document extraction and summarizing for a human underwriter, not the final decision.

> [!INTERVIEW] How would you pick between three AI ideas for a grocery app?
> **Answer outline:** Score by user pain, error cost, data availability and measurable success. Pick the one with high volume and low error cost first.

> [!INTERVIEW] When would a rule-based feature beat an LLM?
> **Answer outline:** When the rules are known, few, and stable (tax slabs, eligibility checks), when exactness and auditability matter, or when the volume makes per-call cost and latency matter. LLMs win on open-ended language input.

> [!INTERVIEW] What would you measure in the first two weeks to decide whether a use case is working?
> **Answer outline:** Activation (first successful use), repeat use, acceptance and edit rate, task completion versus a holdout, and error reports, by segment.

*Related:* Chapter 7 (7.2 and 7.4 of this page), Chapter 14 (Value vs effort), Chapter 24 (Add generative AI to a navigation app), Chapter 24 (Should a food delivery app add an AI meal planner), Chapter 12 (Adapting CIRCLES for AI features), Chapter 11 (Identifying and prioritizing pain points).

## 7.2 User control, transparency, and confidence signals

> Users trust AI more when they can steer it, see where an answer came from, and know how much to rely on it.

### Concept

Three design levers.

**Control**

- Accept, edit, regenerate, or dismiss. Each action is a feedback signal and a trust builder.
- Tone, length, and format controls ("shorter", "more formal") let users shape output without re-prompting from scratch.
- Stop and undo for generation in progress.
- Scope control: let users choose which data the AI can use (for example, specific documents or folders).

**Transparency**

- Show sources and citations when the answer depends on facts. Link to the underlying document so users can verify.
- Label AI-generated content clearly, so readers know its origin.
- Explain why a recommendation appeared, in plain language, when the decision matters.

**Confidence signals**

- Use them only when they change behaviour. A raw percentage is often misleading to users.
- Prefer qualitative cues tied to evidence: "based on 3 sources" or "I could not find this in your files."
- Abstain or ask a clarifying question when confidence is low, rather than guessing.

Avoid fake precision, hiding uncertainty, and making the AI's reasoning look more reliable than the evals show. Over-trust and under-trust both hurt. The goal is calibrated trust.

![Confidence signals run from a raw percentage that looks precise to evidence cues and abstention. Test the score before showing it.](diagrams/l4-confidence-spectrum.svg)

### Real-world examples

- **Perplexity:** answers carry numbered source citations so users can click through and check claims.
- **Microsoft Copilot (launched as Bing Chat in 2023):** inline citations linking to the web pages behind each generated answer.
- **GitHub Copilot:** accept with Tab, dismiss with Esc; the user controls every suggestion.
- **Duolingo Max "Explain my answer":** gives the reasoning behind a correct or wrong answer, so the learner can judge the feedback.

### Practice questions

> [!INTERVIEW] Your AI shows a 92% confidence score on each answer. Users say it is misleading. What do you do?
> **Answer outline:** Test whether the score is calibrated against eval data. If it is not, replace it with evidence cues (sources, "not found") or remove it.

> [!INTERVIEW] How would you design the controls for an AI email drafter?
> **Answer outline:** Send, edit, regenerate, a tone slider, and an undo window. Log edit distance as a trust signal.

> [!INTERVIEW] When should an AI show its sources, and when does that add clutter?
> **Answer outline:** Show them when the answer is factual and the user may act on it or need to verify (policy, health, finance, research). Skip or collapse them for creative or low-stakes output such as a draft tagline.

> [!INTERVIEW] How do you test whether users understand what the AI can and cannot do?
> **Answer outline:** Usability sessions with tasks the AI cannot do, a short comprehension check, and logs of out-of-scope requests and over-reliance (accepting wrong answers on seeded cases).

*Related:* Chapter 7 (7.1, 7.3 and 7.5 of this page), Chapter 9 (Explainability and disclosure), Chapter 8 (Online metrics: task success, acceptance and edit rate, retention of AI users).

## 7.3 Handling hallucinations, errors, and recovery paths

> Assume the model will sometimes be wrong; design so that wrong output is noticed, contained, and easy to fix.

### Concept

Hallucination (confident but false output) is a property of generative models, not a rare bug. Reducing it is a model, retrieval and eval problem. The product must also handle it.

Design layers:

1. **Prevent:** ground answers in retrieved sources (RAG), constrain outputs to known schemas, and abstain when no source supports the answer.
2. **Detect:** run checks (citation verification, schema validation, rule checks, a second model as judge) before output reaches the user.
3. **Signal:** tell users when the answer is uncertain, unsourced, or partial.
4. **Recover:** offer a fast path to correct it: edit, ask again, escalate to a human, or open the source.
5. **Learn:** log user corrections and reports as labelled data for evals.

Error categories to design for:

- Factual error (wrong number, invented citation)
- Refusal or over-refusal (blocked a safe request)
- Incomplete or truncated output
- Latency timeout or tool failure
- Harmful or off-brand output

For each, decide what the user sees, what the system does, and what gets logged. Undo and "report a problem" are cheap and high-value.

![Five layers from prevent to learn, then the five error classes to design for.](diagrams/l4-recovery-layers.svg)

### Real-world examples

- **Moffatt v. Air Canada (2024):** a Canadian tribunal held the airline responsible for incorrect bereavement-fare information its chatbot gave a customer. Lesson: a company owns what its bot says, so disclosure and verification matter.
- **Google Bard launch demo (February 2023):** a promotional answer wrongly said the James Webb Space Telescope took the first picture of a planet outside our solar system. Alphabet's market value fell by about $100 billion that day. Public demos need the same error review as production.
- **Mata v. Avianca (US federal court, 2023):** lawyers were sanctioned for filing a brief with case citations that ChatGPT had invented. Users over-trust fluent output, so high-stakes products need verification built in.
- **Perplexity:** citations let users verify claims, a recovery path built into the answer itself.

### Practice questions

> [!INTERVIEW] Users report that your support bot invents refund policies. Outline your response in the first week.
> **Answer outline:** Confirm with logs and a sample. Restrict answers to retrieved policy documents. Abstain and route to a human when no source matches. Add a "not sure" path. Add an eval set for policy questions and block release until it passes.

> [!INTERVIEW] What is the difference between a hallucination and a stale answer, and does the fix differ?
> **Answer outline:** A hallucination is invented content the sources do not support. A stale answer was true once, but the world or the documents changed. Fix hallucinations with grounding, abstention, and checks. Fix staleness with fresher retrieval, document versioning, and date-aware answers.

> [!INTERVIEW] How would you design the recovery flow when a generated email is wrong and already sent?
> *(Beyond the notes: a starting point, not the vault's answer.)* Tell the recipient quickly and plainly, with a short correction that the sender approves. Offer the sender a path to a follow-up message from the same screen. Log the incident and the source of the error, and check whether the draft skipped a review step that should have caught it.

> [!INTERVIEW] Which error would you treat as a launch blocker?
> **Answer outline:** Any severe error class with a non-zero rate on the safety set (unsafe advice, data leaks, invented policy or prices), and any segment whose error rate is far above the bar.

*Related:* Chapter 7 (7.2, 7.4 and 7.5 of this page), Chapter 4 (Trust, errors, and graceful failure), Chapter 24 (Diagnose a rise in chatbot hallucination complaints), Chapter 8 (Offline evals: golden datasets, rubrics, LLM-as-judge), Chapter 5 (RAG, fine-tuning, and embeddings: when to use each).

## 7.4 Human-in-the-loop design

> Decide, step by step, where a person reviews, approves or overrides the AI, based on how costly and reversible each action is.

### Concept

Human-in-the-loop (HITL) is a design choice about where the human sits in the workflow. Common patterns:

| Pattern | Human role | When to use |
|---|---|---|
| Suggest | Chooses to accept | Low-stakes, high-volume (text completion) |
| Review before send | Approves each output | Customer-facing messages, legal or medical text |
| Exception handling | Reviews only flagged cases | High volume, with a reliable risk classifier |
| Sample audit | Spot-checks a percentage | Mature features with stable quality |
| Escalation | Takes over when the AI cannot resolve | Support, complex or emotional cases |

![Five placements, each with a human role and the cases it suits. Rubber-stamping is the failure to watch.](diagrams/l4-hitl-placements.svg)

Design questions:

- What is the cost of one wrong output, and can it be reversed?
- How much review time does the human have? Rubber-stamping is a real failure mode: if people approve everything, the review is not working.
- What does the reviewer see? Give them the source, the reasoning, and an easy edit path.
- Do reviewer corrections feed back into evals and training data (with consent)?
- Is there a clear handoff with context, so the customer does not repeat themselves?

HITL is not a permanent crutch. Use review data to find the cases the AI handles reliably, then reduce review there while keeping it where errors are costly.

### Real-world examples

- **Gmail "Undo Send":** not AI, but the pattern to copy: a short window to reverse an action before it becomes final.
- **GitHub Copilot:** the developer reviews every suggestion before it is committed.
- **Intercom Fin:** hands off to a human support agent when it cannot resolve a query or the customer asks for one. The escalation pattern.
- **Waymo remote assistance:** when a driverless car meets a situation it is unsure about, it can ask a remote human for guidance. Waymo says the humans advise and the car still drives. Exception handling at scale.
- **Indian digital lending (illustrative):** automated document and bureau checks clear simple cases and flag borderline ones for a human credit officer.

### Practice questions

> [!INTERVIEW] Design the review step for an AI tool that drafts discharge summaries for doctors.
> **Answer outline:** The doctor reviews and signs every draft. Show source notes next to each claim. Track edit rate by section to find weak areas. Never auto-file.

> [!INTERVIEW] How would you detect rubber-stamping in a review queue?
> **Answer outline:** Approval time versus edit rate, an approval rate near 100%, and random seeded errors to test reviewers.

> [!INTERVIEW] When would you move a feature from review-before-send to exception-only review?
> **Answer outline:** When review data shows a low and stable error rate in a defined segment, the risk classifier reliably flags bad cases (tested with seeded errors), errors are reversible, and you keep sample audits running.

> [!INTERVIEW] What context must travel with an escalation to a human?
> **Answer outline:** The conversation so far, what the AI tried and why it escalated, customer identity and history, and any action already taken, so the customer never repeats themselves.

*Related:* Chapter 7 (7.1 and 7.3 of this page), Chapter 6 (Copilot vs automation vs autonomous agent), Chapter 8 (Human evaluation and labeling), Chapter 10 (Feedback loops and consented data collection).

## 7.5 Setting expectations and onboarding users to AI features

> Tell users what the AI is good at, what it is not, and how to check it, before they rely on it.

### Concept

Expectations are set by the first few interactions. If the first answer is wrong and nothing explains the limits, trust drops and rarely recovers. Onboarding for AI features should cover five things:

1. **Capability:** what the feature can do, with 2-3 concrete examples that work well.
2. **Limits:** what it cannot do (no live data, no medical advice, works on English documents only), stated plainly.
3. **Verification:** how to check output (sources, edit before sending).
4. **Data:** what is stored, what is used for training, and how to opt out (ties to Chapter 9, 9.2).
5. **Control:** how to turn it off or change behaviour.

Tactics:

- Use a guided first task with a known-good example rather than an empty prompt box.
- Show example prompts and "try this" chips.
- Mark the feature as beta or AI where appropriate, and say what will change.
- Avoid overpromising in marketing. The gap between the pitch and the first output is where churn happens.
- Teach through the product, not only through a help page.

Measure activation (first successful task), repeat use in week 1, and the rate of "this was wrong" reports, by cohort.

![Five things to teach at first run, each one a step; then measure what changed.](diagrams/l4-onboarding-ladder.svg)

### Real-world examples

- **ChatGPT and Claude first-run screens:** example prompts and a notice that answers can be wrong. A common pattern for setting expectations.
- **Perplexity:** the interface shows that answers come from sources, which frames how users should read them.
- **Spotify AI DJ (February 2023):** launched in beta with an AI voice that introduces itself and explains its picks, and a curated start rather than an open prompt.
- **Apple Intelligence notification summaries:** after inaccurate news summaries in late 2024, Apple paused them for news apps (iOS 18.3, January 2025) and added clearer labelling that summaries are AI-generated and in beta. Labelling and limits are cheaper before launch than after a public complaint.
- **GitHub Copilot:** a trial period and in-editor examples help developers learn where suggestions are reliable.

### Practice questions

> [!INTERVIEW] You are launching an AI budgeting assistant. Outline the first-run experience.
> **Answer outline:** A short capability screen, one guided task using the user's own transactions with consent, a visible "check this" cue on advice, and a clear data-use note.

> [!INTERVIEW] Users expect the AI to be perfect after the launch video. What do you do?
> **Answer outline:** Review marketing claims, add limits in the product, measure the gap between expected and actual success, and add a feedback path.

> [!INTERVIEW] How would you test whether onboarding actually changed behaviour?
> **Answer outline:** A/B test onboarding variants and compare activation, week-1 repeat use, error reports, and the share of out-of-scope requests.

> [!INTERVIEW] Should AI features be labelled as beta? What are the trade-offs?
> **Answer outline:** A beta label sets expectations and buys tolerance, but can lower adoption and cannot excuse serious harm. Use it while quality is still moving, with a plan for removing it.

*Related:* Chapter 7 (7.2 and 7.3 of this page), Chapter 9 (Privacy, consent, and data retention, India DPDP Act 2023), Chapter 18 (Pre-launch, launch, and post-launch activities), Chapter 10 (Staged rollouts and kill switches), Chapter 18 (Pilots, MVPs, and phased rollouts).

## Beyond the notes: the states an AI feature must draw

*(Beyond the notes: a design habit, not the vault's content. Names of states vary by team.)*

A static screen design shows one state. An AI feature has at least eight, and each one needs a designed screen before the build starts:

![Eight states an AI feature needs on screen, from the first wait to the handoff to a person.](diagrams/l4-ui-states.svg)

| State | What the user needs | What to avoid |
|---|---|---|
| Waiting for the first token | Progress that says work is happening | A blank box that looks broken |
| Streaming | Stop and regenerate, visible partial text | Text that jumps when it is replaced |
| Done, with sources | Citations that open the source | Sources hidden behind a menu |
| Low confidence | A "not sure" path and a clarifying question | A confident-looking guess |
| No source found | A clear abstention and a route forward | An invented answer |
| Error or timeout | A retry, and the rest of the page still working | A full-page error for one failed call |
| Refused or off scope | What the feature can do instead | A bare refusal |
| Handed to a human | The context travels with the handoff | Asking the customer to repeat everything |

## Beyond the notes: writing the expectation copy

*(Beyond the notes: general product-writing habits.)*

- **Say the job in one sentence.** "Drafts replies from your last three tickets; you choose what to send." The user can then predict the feature.
- **Name one limit in plain words.** "Does not see messages older than 30 days." Limits written as a list of disclaimers get skipped.
- **Use the verb the user will use.** "Check", "edit" and "send" are clearer than "validate" and "finalise".
- **Test the copy on a task.** Show the screen to a new user and ask what it will do with their data. If the answer is wrong, the copy is wrong.
- **Date the beta label.** "Beta, feedback welcome" with a link to the feedback form is more honest than an open-ended tag.

## Beyond the notes: pitfalls

- **Showing a confidence number because it is available.** A number that is not calibrated teaches users the wrong lesson, in either direction.
- **Treating the first wrong answer as the user's fault.** If the copy does not say what to check, the user cannot know what went wrong.
- **Rubber-stamping by design.** A review step with a single "approve" button and a long queue will be approved without reading. Show the source next to the claim, and seed known errors.
- **Hiding the handoff.** Users who cannot find a person will blame the product, not the model.
- **Launching the demo flow.** The first-run example should match real usage, or the gap becomes churn.

## Beyond the notes: production checklist

- Write one screen for each state in the table above, before the first build review.
- Log, with consent: the prompt version, the sources shown, and the user's action (accept, edit, reject, undo, escalate).
- Set a target for activation and for "this was wrong" reports, and review both by cohort every week.
- Test the undo, the stop and the handoff on a real device, with slow network conditions.
- Decide who owns the copy about limits. It must change when the model changes.

## Beyond the notes: interview corner

- **"Would you show the model's confidence to users?"** Only after a calibration check on held-out data. If the number does not mean what it says, show evidence cues instead, such as the number of sources used.
- **"Where does AI UX fail most often?"** At the edges: the first run, the wrong answer, and the handoff. The happy path is usually the easiest part to design.
- **"How do you avoid over-trust?"** Show sources where the user may act, make the edit path cheap, measure edit rate by section, and seed known errors into the review queue.
- **"What is the difference between HITL and a fallback?"** HITL places a person in the workflow on purpose, for a defined set of cases. A fallback runs when the AI fails. Both need a design, an owner and a metric.

## Revision cheat-sheet

![Chapter 7 on one page: five ideas, each with the question it answers.](diagrams/l4-big-picture.svg)

- **7.1** Use AI where the task is language-, pattern- or search-heavy and a good-enough first draft is valuable. Score frequency, pain, error tolerance and data (1 to 3 each). Anti-patterns: a chatbot where a form works, exact maths, and high-stakes decisions with no review.
- **7.2** Control (accept, edit, regenerate, stop, undo, scope), transparency (sources, labels, plain-language reasons) and confidence signals (only when they change behaviour; prefer evidence cues; abstain when unsure).
- **7.3** Hallucination is a property of generative models. Prevent (grounding, schemas, abstention), detect (checks, a second model as judge), signal, recover (edit, ask again, escalate, open source) and learn (log corrections as eval data).
- **7.4** Pick the human pattern from the cost and reversibility of a wrong output: suggest, review before send, exception handling, sample audit, escalation. Watch for rubber-stamping. Reduce review where the data shows a stable low error rate.
- **7.5** Teach capability, limits, verification, data use and control at first run, with a guided task. Measure activation, week-1 repeat use and "this was wrong" reports by cohort.
- **Beyond the notes:** design eight screen states, not one; write limits in plain words; test the copy on a real user; log the action that followed each answer.

## Self-test

<details class="quiz"><summary>What two questions does the 7.1 screen ask before any AI idea is built?

Is the input or output unstructured, and is a good-enough output useful? Then: is the cost of an error low or recoverable, does a human already do the task, is the existing solution clearly worse, and can you measure success?

</details>

<details class="quiz"><summary>Why should a confidence score be tested before it is shown to users?

A raw percentage looks precise. If it is not calibrated against eval data, it misleads users. Replace it with evidence cues, such as "based on 3 sources", or remove it.

</details>

<details class="quiz"><summary>Name the five layers of the design for hallucinations and errors.

Prevent (ground answers, constrain outputs, abstain), detect (checks before output reaches the user), signal (say when the answer is uncertain or partial), recover (a fast path to fix it) and learn (log corrections as labelled data for evals).

</details>

<details class="quiz"><summary>What does the Moffatt v. Air Canada case teach a product team?

A company owns what its chatbot says. A tribunal held the airline responsible for incorrect bereavement-fare information from its bot (2024), so disclosure and verification matter.

</details>

<details class="quiz"><summary>What is rubber-stamping, and how do you detect it in a review queue?

Rubber-stamping is when people approve nearly everything, so the review is not working. Detect it with approval time against edit rate, an approval rate near 100%, and random seeded errors.

</details>

<details class="quiz"><summary>Which five things should onboarding teach before the first real use?

Capability (what works well, with 2-3 examples), limits (what it cannot do), verification (how to check output), data (what is stored and used, and how to opt out) and control (how to turn it off or change it).

</details>

<details class="quiz"><summary>What do the Apple notification summaries show about labelling and launch?

Summaries produced false news headlines (the BBC complained in December 2024). Apple paused them for news apps in January 2025 and added labels saying they are AI-generated and in beta. Labelling and limits are cheaper before launch.

</details>

<details class="quiz"><summary>What should a PM measure in the first two weeks of an AI use case?

Activation (first successful use), repeat use, acceptance and edit rate, task completion against a holdout, and error reports, all by segment.

</details>

<details class="quiz"><summary>(Beyond the notes) Why does one factor scored 1 cut the scoring grid so hard?

The four scores multiply. Dropping error tolerance from 3 to 1 takes 3 x 3 x 3 x 3 = 81 down to 27, a third of the score. A weak factor drags the whole product down.

</details>

<details class="quiz"><summary>(Beyond the notes) Why do AI features need more than a loading spinner?

An AI feature has several states: waiting for the first token, streaming, done with sources, low confidence, no source, error, refused and handed to a human. Each needs a designed screen, or the user is left guessing.

</details>

<details class="quiz"><summary>(Beyond the notes) Why is a fixed review step not the same as human-in-the-loop design?

HITL places a person on purpose, for defined cases, with an owner and a metric. A fixed step that is always approved without reading gives the look of review without the safety. Track edit rate and seed errors to check it works.

</details>


# Chapter 8 · Evaluating and Measuring AI Products

<!-- lecture n="5" label="8" short="AI evals & metrics" status="done" kind="AI evals" -->

## At a glance

| Question | Short answer |
|---|---|
| Why is an AI product harder to measure? | Traditional products ask whether users finish a flow. AI adds a second question: is the output good enough, and how do you know? |
| What is an offline eval? | Run the system on a fixed set of inputs (a golden dataset), score the outputs with a rubric, and compare versions on equal terms. |
| Can an LLM grade the outputs? | Yes, as a judge that scales. Calibrate it against human labels first, because it has known biases. |
| What do humans add? | Ground truth, calibration for automated judges, and failure modes that no metric was built to catch. |
| Which online signals matter most? | Acceptance and edit rate for generative features, plus task success and retention of AI users against a control. |
| What must a guardrail look like? | A metric with a threshold set before launch: harmful output rate, latency, cost per task, refusals, complaints. |
| How do you ship a model or prompt change? | Treat it as a release. Run the same suite, compare per category against the baseline, and pass a gate set in advance. |
| Which number is not enough? | Any single number. Averages hide segments and tails; a judge score hides disagreement with humans. |
| What does a good judge score need? *(Beyond the notes)* | A calibration sample with a chance-corrected agreement figure, not only a pass rate. |
| How do you use this in an interview? *(Beyond the notes)* | Name the golden set, the rubric, the judge check, the online metric, the guardrail threshold and the gate. |

> [!NOTE] Where this comes from
> The vault's notes say that no converted source covers most of this chapter, which is written from general knowledge. Two sections cite the *Sigma PM Concept Book, Part A (2023)*, chapter "Metrics" (retention, churn, and guardrail negative metrics). The vault's further-reading list names *AI Product Reading*, *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

Traditional products are measured by whether users complete a flow. AI products add a second question: is the output *good enough*, and how do you know before and after shipping? The chapter covers the layered approach. Offline evals come before launch. Human review provides ground truth. Online metrics show real behaviour. Guardrail metrics protect against harm. Regression tests stop a model or prompt change from quietly breaking what worked.

The chapter has five sections, each one a layer of the same stack:

- **8.1 Offline evals: golden datasets, rubrics, LLM-as-judge.** Pre-launch scoring against a fixed test set, with an LLM as a scalable but imperfect grader.
- **8.2 Human evaluation and labeling.** Human raters create ground truth, calibrate automated judges, and surface failure modes that metrics miss.
- **8.3 Online metrics: task success, acceptance and edit rate, retention of AI users.** What users actually do with AI output in production.
- **8.4 Guardrail metrics: harmful outputs, latency, cost.** The metrics that must not regress while you optimise for quality.
- **8.5 Regression testing when models or prompts change.** Treating prompts and model versions like code, with a fixed eval suite as the release gate.

![The layers of evaluation, from offline evals to guardrails, with the regression gate between them.](diagrams/l5-eval-pipeline.svg)

## Key takeaways

- Measure AI features in layers: offline evals, human review, online behaviour, and guardrails. No single number is enough.
- A golden dataset is only as good as its coverage of real user inputs, including the hard and adversarial ones.
- LLM-as-judge scales grading but must be calibrated against human labels before you trust it.
- Acceptance and edit rate are the most useful online signals for generative features, because they show whether users trusted the output.
- Every prompt or model change is a release. Run the same eval suite before shipping, and compare against the current baseline.

> [!SIR] From the source notes
> Every prompt or model change is a release. Run the same eval suite before shipping, and compare against the current baseline.

## 8.1 Offline evals: golden datasets, rubrics, LLM-as-judge

> Offline evals let you score an AI feature against a fixed test set before users ever see it, so you can compare versions on equal terms.

### Concept

- **Offline eval:** run the system on a fixed set of inputs and score the outputs. Same inputs, same scoring, so changes are comparable.
- **Golden dataset:** a curated set of inputs with reference answers or expected behaviour. Build it from real (anonymised) user queries, plus edge cases, known failures, and adversarial prompts.
- **Rubric:** a written definition of "good", broken into criteria, for example factual accuracy (0-2), completeness (0-2), and tone (0-1), with anchor examples for each score. A vague rubric produces noisy scores.
- **Scoring methods:**
  - Exact match or rule checks (cheap, good for extraction and classification).
  - Reference-based metrics (similarity to a gold answer; weak for open-ended text).
  - **LLM-as-judge:** a separate model grades outputs against the rubric. It scales well but has known biases: position bias, preference for longer or self-generated answers, and sensitivity to prompt wording.
- **Calibration:** check the judge against human labels on a sample (agreement rate, Cohen's kappa or similar). Only trust an automated judge once it agrees with humans on the criteria that matter.
- **What to evaluate depends on the system:**
  - *RAG:* retrieval (did the right passage appear in the top results?) and generation (is the answer faithful to the sources, and does it answer the question?).
  - *Agents:* end-to-end task success, plus the trajectory (right tools, right order, number of steps, cost) and safety (no unauthorised actions).
  - *Sampling variance:* the same input can pass once and fail the next time, so run important cases several times and report pass rates.
- **Public benchmarks vs product evals:** leaderboard scores (such as MMLU or SWE-bench) say how a model does on generic tasks. They are useful for shortlisting models but do not replace an eval set built from your own users' tasks. Benchmarks can also be contaminated (the test data leaked into training).

PM view: decide the rubric and the "must pass" cases with engineering and domain experts. The PM owns what "good enough to ship" means, and the eval suite is where that decision becomes testable.

Pitfalls:

- Dataset drift: the golden set reflects last quarter's users. Refresh it from production samples.
- Overfitting prompts to the test set, so offline scores rise while live quality does not.
- Averages hide tail failures. Track the share of outputs below threshold, and keep a list of severe failures to review individually.

![A golden set and a rubric feed the system; three scorers grade the outputs, and humans calibrate the judge.](diagrams/l5-golden-rubric-judge.svg)

### Try it locally: how much does a 90% judge pass rate mean?

*(Beyond the notes: reproduced locally with the standard library. The counts are illustrative, not from the vault. They show a judge that says 90% pass on 40 outputs, checked against human labels on the same 40.)*

```python title="lab_p5_judge_kappa.py"
# A judge passes 90% of 40 outputs. Compare its verdicts with human labels on the same 40.
# Illustrative counts: both pass 24, judge pass + human fail 12,
# judge fail + human pass 2, both fail 2.
both_pass, judge_pass_human_fail, judge_fail_human_pass, both_fail = 24, 12, 2, 2
n = both_pass + judge_pass_human_fail + judge_fail_human_pass + both_fail

judge_pass = (both_pass + judge_pass_human_fail) / n
human_pass = (both_pass + judge_fail_human_pass) / n
agree = (both_pass + both_fail) / n
# agreement you would expect by chance, if the two sets of verdicts were independent
chance = judge_pass * human_pass + (1 - judge_pass) * (1 - human_pass)
kappa = (agree - chance) / (1 - chance)

print(f"items labelled       : {n}")
print(f"judge says pass      : {judge_pass:.0%}")
print(f"humans say pass      : {human_pass:.0%}")
print(f"raw agreement        : {agree:.0%}")
print(f"agreement by chance  : {chance:.0%}")
print(f"Cohen's kappa        : {kappa:.2f}")
```

```output
items labelled       : 40
judge says pass      : 90%
humans say pass      : 65%
raw agreement        : 65%
agreement by chance  : 62%
Cohen's kappa        : 0.08
```

The judge's 90% looks healthy, but the humans pass only 65% of the same outputs. Raw agreement is 65%, and most of that agreement is what chance would produce (62%). Kappa is 0.08: close to zero, so the judge agrees with the humans about as often as chance alone would. Before this judge reports anything, the rubric or the judge prompt needs work, and the labels need a second look. A pass rate alone would have shipped the judge.

### Real-world examples

- **OpenAI Evals:** an open-source framework for writing and running evals against model outputs, including model-graded checks.
- **Stanford HELM:** a holistic benchmark that scores models across many scenarios and metrics, not just accuracy.
- **LMSYS Chatbot Arena (now LMArena):** crowd-sourced pairwise human preferences between models, used to rank them. A useful example of human judgement at scale, and of its limits: in 2025 researchers criticised the leaderboard for letting some labs test many private variants before release.
- **MT-Bench (LMSYS, 2023):** a multi-turn benchmark that studied LLM-as-judge agreement with humans and documented position and verbosity biases.

### Practice questions

> [!INTERVIEW] How would you build the golden dataset for an AI resume reviewer? Where does each test case come from?
> **Answer outline:** Mine real anonymised queries from beta users, add cases from support tickets and known failure categories, add adversarial and out-of-scope inputs, and have domain experts write or validate reference outputs.

> [!INTERVIEW] Your LLM judge gives 90% of outputs a pass. Why might you not believe it yet?
> **Answer outline:** The judge may be lenient, may favour verbose answers, or may not agree with humans. Check agreement on a labelled sample, examine the failures it passed, and confirm that the criteria it scores match what users care about.

> [!INTERVIEW] Design a rubric for summarising a 10-page document. What are the criteria, and how would you score them?
> *(Beyond the notes: a starting point.)* Criteria could be: covers the main points (0-2), no claims absent from the document (0-2, the most severe), keeps the author's conclusions and numbers (0-2), length and structure fit the reader (0-1), and tone (0-1). Give an anchor example for each score, and treat the "no unsupported claims" criterion as a gate rather than a weight.

> [!INTERVIEW] When is exact-match scoring better than an LLM judge, and when is it misleading?
> *(Beyond the notes: a starting point.)* Exact match suits extraction and classification with a fixed answer (a date, an invoice number, a category). It is misleading for open-ended text, where a correct answer can be worded in many ways and would fail on every word that differs from the reference. There the judge or a human rubric is needed, with calibration.

*Related:* Chapter 8 (8.2, 8.5 and 8.3 of this page), Chapter 4 (Quality as a distribution, not a bug count), Chapter 20 (AI PRD additions: eval criteria, failure modes, data requirements).

## 8.2 Human evaluation and labeling

> Human judgement is the ground truth that automated evals and online metrics are calibrated against, and it is the cheapest way to find failure modes you did not think to measure.

### Concept

- **Why humans:** automated metrics cannot tell you whether a medical summary is subtly wrong or a tutoring hint is patronising. Humans can, but they are slower and more expensive, so use them where they add the most information.
- **Types of human evaluation:**
  - **Pairwise preference:** "Which answer is better, A or B?" Easy for raters, good for comparing model versions.
  - **Absolute rating:** score on a rubric (1-5 or pass/fail per criterion).
  - **Error tagging:** label each failure (hallucination, wrong tone, missed step). This is the most useful for product decisions because it shows *what* to fix.
  - **Expert review:** domain specialists for high-stakes domains such as legal, medical, or finance.
- **Labeling for training or tuning:** labels used for supervised fine-tuning or reinforcement learning from human feedback (RLHF). They need clear guidelines, gold-standard checks, and inter-rater agreement tracking.
- **Quality control:** write guidelines with worked examples, run calibration rounds, measure inter-annotator agreement, and audit a sample of each rater's work.
- **Ethics and privacy:** raters see user data. Anonymise it, limit access, and get consent where the data came from users. Pay raters fairly.

PM view: you own the rubric and the sampling plan. Decide how many items to label, how often, and what disagreement means. Label a sample of production outputs every release, not just once.

Common mistakes:

- Vague guidelines, so raters disagree and the score reflects rater confusion.
- Labelling only easy examples.
- Treating a single average score as the decision, when error categories are more actionable.

![A labelling loop: stratify the sample, rate or tag, measure agreement, calibrate the judge, then tighten the rubric.](diagrams/l5-human-loop.svg)

### Real-world examples

- **Scale AI:** a large data-labelling and evaluation vendor used by AI labs and enterprises for human ratings and red-teaming.
- **Karya (Bengaluru):** a platform that collects speech and text data from workers across rural India and pays them for the work. Relevant for Indian language AI.
- **LMArena (LMSYS Chatbot Arena):** crowd-sourced pairwise human votes between anonymous chatbots, used to rank models.
- **Google Search Quality Rater Guidelines:** Google publishes the long guideline document its contracted raters use to judge page quality and whether results meet the searcher's need. Google says the ratings evaluate ranking changes rather than directly ranking pages, which is exactly the role of human eval.

### Practice questions

> [!INTERVIEW] You have budget to label 500 outputs per release. How do you sample them?
> **Answer outline:** Stratify rather than sample randomly. Oversample high-stakes intents, new features, languages and low-volume segments, outputs the automated judge scored as borderline, and outputs with negative user signals. Keep a random slice (say 20%) to estimate overall quality without bias. Keep the same core set across releases for comparison.

> [!INTERVIEW] Two raters agree only 55% of the time on "helpfulness". What do you do?
> **Answer outline:** Low agreement usually means the rubric is ambiguous. Tighten the definitions with anchor examples, split the criterion into narrower ones, run a calibration round, and re-measure agreement before trusting the labels.

> [!INTERVIEW] Why might human preference ratings and task success disagree? Give an example.
> **Answer outline:** Raters often prefer longer, more confident, or more polished answers, while users care about getting the job done fast. A verbose answer may win the preference vote but lower task success on mobile. Calibrate preference studies against behavioural outcomes.

> [!INTERVIEW] How would you design a red-team exercise for a customer-support copilot?
> *(Beyond the notes: a starting point.)* Give red-team testers a written scope: the product, the users, the data it can see, and the actions it can take. Ask them to try the harms that matter most (wrong refund or policy statements, leaked customer data, unauthorised actions, abusive replies, prompts that hide instructions in customer text). Log each attempt with its result, turn every success into a regression case, and re-run the set before each release.

*Related:* Chapter 8 (8.1, 8.3 and 8.4 of this page), Chapter 10 (Feedback loops and consented data collection).

## 8.3 Online metrics: task success, acceptance and edit rate, retention of AI users

> In production, the best signals are what users do with the output: did they accept it, edit it, or finish the task, and do they come back.

### Concept

Standard product metrics still apply: adoption, engagement, retention. For AI features, add metrics that show whether the output was useful.

| Metric | What it measures | Example |
|---|---|---|
| **Task success rate** | Share of sessions where the user completed the goal | Resume review ends with a downloaded file |
| **Acceptance rate** | Share of AI outputs the user keeps | Code suggestion accepted with Tab |
| **Edit rate / edit distance** | How much users change the output before using it | Share of drafted emails sent with more than 20% changed |
| **Regeneration / retry rate** | How often users ask again | High retries signal low quality or poor prompt fit |
| **Thumbs up/down rate** | Explicit feedback, with a low response rate | Use as a diagnostic, not a headline |
| **AI user retention** | Do users who try the feature keep using it, versus control | Week-4 retention of AI users vs non-AI users |
| **Time to task completion** | Speed to outcome | Minutes to get a usable first draft |

![Each stage removes users: shown, accepted, kept with little editing, finished, and still active. Read the drop-offs.](diagrams/l5-metric-funnel.svg)

Interpretation:

- High acceptance with low edit rate is strong evidence of trust.
- High acceptance but high later churn can mean users accept output they then have to fix, a hidden cost.
- Compare against a holdout or matched cohort. Without a control, lift from a launch can be confused with seasonality or other changes.
- Segment by task type, user tenure, and language. An average can hide a failing segment.

Sigma's metrics chapter defines retention as "are our activated users continuing to engage with the product?" and churn as its inverse. Use the same retention logic for AI users, but make sure the cohort is defined by feature use, not just by app use.

### Try it locally: acceptance up, clean output flat

*(Beyond the notes: reproduced locally with the standard library. The counts are illustrative, not from the vault. They show a prompt change that raises acceptance while the edits rise too.)*

```python title="lab_p5_funnel.py"
# Acceptance and edit rate for a suggestion feature, before and after a prompt change.
# Illustrative counts, not from the vault.
shown = 1000
before = {"accepted": 300, "edited": 60}
after = {"accepted": 450, "edited": 180}

for name, d in (("before the prompt change", before), ("after the prompt change", after)):
    acc, edited = d["accepted"], d["edited"]
    kept = acc - edited
    print(f"{name}:")
    print(f"  acceptance rate  {acc / shown:.0%}  ({acc} of {shown} shown)")
    print(f"  edit rate        {edited / acc:.0%}  ({edited} of {acc} accepted)")
    print(f"  kept as shown    {kept / shown:.0%}  ({kept} of {shown} shown)")

acc_move = (after["accepted"] - before["accepted"]) / shown * 100
kept_move = ((after["accepted"] - after["edited"]) - (before["accepted"] - before["edited"])) / shown * 100
print(f"acceptance moved    {acc_move:+.0f} points")
print(f"kept as shown moved {kept_move:+.0f} points")
```

```output
before the prompt change:
  acceptance rate  30%  (300 of 1000 shown)
  edit rate        20%  (60 of 300 accepted)
  kept as shown    24%  (240 of 1000 shown)
after the prompt change:
  acceptance rate  45%  (450 of 1000 shown)
  edit rate        40%  (180 of 450 accepted)
  kept as shown    27%  (270 of 1000 shown)
acceptance moved    +15 points
kept as shown moved +3 points
```

Acceptance rose by 15 points, from 30% to 45%, but the share of accepted output that people edited doubled, from 20% to 40%. The output that stayed as shown rose by only 3 points. Users are accepting more and fixing more, which is the hidden cost from the interpretation list. A dashboard that tracks acceptance alone would call this a win.

### Real-world examples

- **GitHub Copilot:** tracks suggestion acceptance as a core signal of usefulness. It is one of the most cited examples of acceptance-rate metrics.
- **Gmail Smart Compose (Google):** Google's published research on Smart Compose measured how often suggestions were accepted, which shaped how it was tuned.
- **GitHub Copilot controlled experiment (GitHub, 2022):** developers with Copilot finished a set coding task about 55% faster than a control group. An example of time-to-completion measured against a control rather than a before/after comparison.
- **Klarna AI assistant (February 2024 announcement):** Klarna reported resolution time falling from about 11 minutes to under 2, and 25% fewer repeat inquiries. Repeat inquiries are a useful quality check on "resolved", because a fast answer that does not solve the problem brings the customer back.

### Practice questions

> [!INTERVIEW] For an AI meeting-notes feature, which three metrics would you put on the dashboard, and why?
> *(Beyond the notes: a starting point.)* Task success (the user ends with a shared or filed summary), acceptance-and-edit rate (how much of the summary is kept as written), and week-4 retention of users who tried the feature against a holdout. The first shows the job is done, the second shows trust, and the third shows whether the feature changes behaviour. Add the guardrails from 8.4 beside them.

> [!INTERVIEW] Acceptance rose from 30% to 45% after a prompt change, but support tickets rose too. What do you investigate?
> **Answer outline:** Check whether the accepted outputs were later edited, reverted, or caused complaints. Segment the acceptance gain by task type to see if the change helped some tasks and hurt others. Look at support tickets by category against the release date.

> [!INTERVIEW] How would you prove that an AI feature causes better retention, not just that AI users are more engaged?
> **Answer outline:** Self-selection is the trap: engaged users try new features first. Use a randomised holdout that does not get the feature (or gets it later), compare retention for the whole assigned group (intent-to-treat), and if a holdout is impossible use a staggered rollout or matched cohorts on pre-launch engagement.

*Related:* Chapter 8 (8.1, 8.4 and 8.5 of this page), Chapter 15 (Funnel, marketplace, and retention metrics), Chapter 15 (HEART), Chapter 24 (Define success metrics for an AI resume reviewer).

## 8.4 Guardrail metrics: harmful outputs, latency, cost

> Guardrail metrics are the numbers you must not sacrifice while chasing quality gains, such as harmful output rate, latency, and cost per task.

### Concept

Guardrail metrics are the AI version of the negative metrics in Sigma's metrics chapter: things you watch so that a gain in one area does not hide damage in another. The usual set:

- **Harmful output rate:** share of outputs that are unsafe, abusive, privacy-violating, or policy-breaking. Measured by automated classifiers plus sampled human review. Track by category.
- **Factual error / hallucination rate on high-stakes answers:** a subset of evals, watched online for sensitive domains.
- **Refusal rate:** too many refusals hurt helpfulness; too few let harm through. Track both sides.
- **Latency:** p50 and p95 time to first token and time to full response. Users abandon slow AI replies, and latency also drives cost.
- **Cost per task:** tokens in and out times price, plus retrieval, tool calls, and retries. Watch cost per *successful* task and the trend as usage grows.
- **Security and privacy:** prompt-injection success rate on a red-team set, and personal-data leakage rate in outputs and logs.
- **Escalation or complaint rate:** how often users ask for a human or report a problem.

Set thresholds before launch. A guardrail with no threshold is a dashboard nobody acts on. Example: "p95 latency under 4 seconds; harmful output rate under 0.1% on the safety set; cost per task under INR 2."

Trade-offs to name in an interview: a larger model may improve quality but raise latency and cost. A stricter safety filter lowers harm but raises refusals. The PM decides where the line sits and documents it.

![Each guardrail has a threshold set before launch, and a named action when it is breached.](diagrams/l5-guardrails.svg)

### Real-world examples

- **Google Gemini image generation (February 2024):** Google paused the feature after outputs showed historically inaccurate and unbalanced images. Quality and safety guardrails had not been tested against this failure mode.
- **Microsoft Tay (March 2016):** a Twitter chatbot that users manipulated into posting abusive messages. Microsoft took it offline within about 16 hours. A classic case of missing harm guardrails.
- **OpenAI GPT-4o sycophancy rollback (April 2025):** an update made the model overly flattering and agreeable. OpenAI rolled it back within days and said it would add sycophancy checks to its launch review. A behavioural guardrail that was not being measured.
- **Meta Llama Guard (open model):** a safety classifier for scoring prompts and responses against a policy, a common building block for harm guardrails.

### Practice questions

> [!INTERVIEW] Which guardrail metrics would you set for a loan-eligibility chatbot, and what thresholds?
> **Answer outline:** Harmful or non-compliant advice rate (target 0 on a red-team set). Factual error rate on eligibility rules (for example under 1% on the golden set, and 0 on critical rules). Share of answers with a required disclaimer. Refusal rate on legitimate questions. p95 latency. Personal-data leakage (0). Escalation rate to a human. Fairness gap in answers across user groups.

> [!INTERVIEW] Your new model cuts hallucinations by half but doubles p95 latency. How do you decide?
> **Answer outline:** Quantify the user impact of each side: how much do slow responses hurt retention in this flow, and what is the value of fewer errors? Test a smaller or cached model, or route only hard queries to the large model. Ship only with a threshold that both sides agree on.

> [!INTERVIEW] Why do cost per task and latency sometimes need to be watched by segment, not overall?
> *(Beyond the notes: a starting point.)* An overall average can stay flat while one segment becomes slow or expensive: long documents, a second language that needs more tokens, or a tool that retries often. A segment view finds the cause, and a per-segment threshold keeps one group from paying for the others.

*Related:* Chapter 8 (8.3 and 8.5 of this page), Chapter 9 (Safety, misuse, and content policy), Chapter 15 (Guardrail and negative metrics), Chapter 6 (Unit economics: cost per task, inference cost, gross margin).

## 8.5 Regression testing when models or prompts change

> A model provider update or a one-line prompt edit can change behaviour across thousands of cases, so every change needs the same eval suite run before release.

### Concept

- **Why regressions happen:** model versions are updated by vendors, prompts are edited by teams, retrieval indexes are refreshed, and tool definitions change. Any of these can shift outputs in ways nobody intended.
- **Regression suite:** a fixed set of cases, including past failures, that must keep passing. Each case has an expected behaviour or a rubric score.
- **Baseline comparison:** run the candidate and the current production version on the same set. Look at the delta per category, not only the average. A small average gain can hide a big loss on one segment.
- **Release gate:** define in advance what blocks a release, for example "no drop above 2 points in any category and zero new severe failures."
- **Pinning and deprecation:** where the platform allows, pin a dated model version and log the version with every output, so you can trace a regression to its source. Vendors retire old versions on a schedule, so plan the migration and its eval run before the retirement date, not after.
- **Shadow and canary runs:** run the new version on live traffic without showing it to users, then roll out in stages (see Chapter 10, Staged rollouts and kill switches).

Process a PM can own:

1. Every prompt or model change gets a ticket with the eval run attached.
2. Failures found in production become new regression cases the same week.
3. Keep a changelog of prompt and model versions alongside metrics.

Pitfall: teams that only test the change they made, not the broader behaviour, end up fixing one case and breaking three others.

![A candidate is compared with the baseline per category; the gate blocks a drop, then the change rolls out in stages.](diagrams/l5-regression-gate.svg)

### Try it locally: the gate on per-category deltas

*(Beyond the notes: reproduced locally with the standard library. The pass rates are illustrative, not from the vault. They show a one-line prompt edit that lifts the average and breaks one category.)*

```python title="lab_p5_regression_gate.py"
# Per-category pass rates: production baseline vs a candidate prompt. Illustrative numbers.
baseline = {"factual accuracy": 80, "format": 95, "safety": 99, "tone": 90, "long answers": 70}
candidate = {"factual accuracy": 84, "format": 96, "safety": 99, "tone": 96, "long answers": 64}
MAX_DROP = 2   # gate: no category may drop by more than 2 points

for cat in baseline:
    delta = candidate[cat] - baseline[cat]
    flag = "BLOCK" if delta < -MAX_DROP else "ok"
    print(f"{cat:<16} {baseline[cat]:>3} -> {candidate[cat]:>3}  {delta:+d}  {flag}")

avg_b = sum(baseline.values()) / len(baseline)
avg_c = sum(candidate.values()) / len(candidate)
print(f"average          {avg_b:.1f} -> {avg_c:.1f}  {avg_c - avg_b:+.1f}")
blocked = [c for c in baseline if candidate[c] - baseline[c] < -MAX_DROP]
print("release gate:", "FAIL" if blocked else "pass", "| blocked by:", ", ".join(blocked))
```

```output
factual accuracy  80 ->  84  +4  ok
format            95 ->  96  +1  ok
safety            99 ->  99  +0  ok
tone              90 ->  96  +6  ok
long answers      70 ->  64  -6  BLOCK
average          86.8 -> 87.8  +1.0
release gate: FAIL | blocked by: long answers
```

The average rises by one point, which looks like a win on a summary line. The long-answers category falls by six points, and the gate blocks the release. Averaging the five categories hides the drop, because four categories improved. The gate reads each category on its own line. The candidate could still be fixed (for example, by a long-answer rule) and re-run before it ships.

### Real-world examples

- **OpenAI GPT-4o sycophancy rollback (April 2025):** OpenAI rolled back an update after users noticed responses had become excessively flattering. In its post-mortem OpenAI said offline evals and A/B tests looked positive and that it had no specific sycophancy eval, so it added behaviour checks as launch blockers.
- **Stanford and UC Berkeley study "How Is ChatGPT's Behavior Changing over Time?" (2023):** researchers measured changes in ChatGPT answers on the same tasks across model versions, showing that behaviour can drift without any announcement.
- **Open-source eval harnesses such as OpenAI Evals and EleutherAI's lm-evaluation-harness:** used to run fixed task suites on each model or checkpoint so results are comparable.

### Practice questions

> [!INTERVIEW] A vendor announces a new model version with "better reasoning." What regression process do you run before switching?
> **Answer outline:** Run the full suite on both versions and compare per category. Check severe failures, latency, cost per task, and output format (parsers often break). Read a sample of diffs by hand. Shadow-test on live traffic, then canary 1-5% with the old version as instant fallback. Re-tune prompts if needed, since prompts tuned for the old model may not transfer.

> [!INTERVIEW] You changed one line in the system prompt and the eval average went up 1 point. Should you ship?
> **Answer outline:** Not yet. Check per-category deltas and the severe-failure list. A one-point average gain can hide a drop on a high-value segment. Ship only if the gate passes, and add any newly found failures to the suite.

> [!INTERVIEW] How would you structure a regression suite for a multi-step agent?
> *(Beyond the notes: a starting point.)* Group cases by the step they test as well as the whole task: tool choice, argument format, order of steps, and the final answer. Score each step separately, so a failure points to its step. Keep a short list of safety cases that run on every change, and add the trajectory length and cost to the report for each case.

*Related:* Chapter 8 (8.1 and 8.4 of this page), Chapter 10 (Monitoring drift and vendor model updates), Chapter 20 (AI PRD additions: eval criteria, failure modes, data requirements), Chapter 16 (AI-specific RCA: model changes, prompt regressions, data drift, cost spikes).

## Beyond the notes: reading a judge score

*(Beyond the notes: general evaluation practice. Use it as a checklist, not as the vault's rule.)*

A judge score is a claim about the judge, not about the product, until it is checked. Before a judge score goes on a dashboard:

- **Ask for agreement, not only the pass rate.** Raw agreement with humans, and a chance-corrected figure such as Cohen's kappa. A kappa near zero means the judge agrees with humans no more than chance would.
- **Look at both kinds of error.** A judge that passes what humans fail is lenient. A judge that fails what humans pass is harsh. The two cost different things, so report them separately.
- **Read the disagreements.** Twenty disagreements, read in full, usually show the rubric problem faster than any statistic.
- **Re-calibrate after a change.** A new judge model or a new judge prompt is a new judge.

## Beyond the notes: keeping metric definitions honest

*(Beyond the notes: naming habits that stop two teams from reporting two different numbers.)*

- **Write the denominator.** Acceptance is accepted outputs divided by outputs shown. Edit rate is edited outputs divided by accepted outputs. Say which, every time.
- **Define the unit.** A session, a user, or an output. A user who asks ten times and a user who asks once count differently in every rate above.
- **Define the cohort for retention.** "Used the AI feature in week 1" is a different cohort from "opened the app in week 1".
- **Fix the window.** Acceptance measured in the first hour after launch is not the same as acceptance in week 4.
- **Name the owner of each guardrail.** A threshold with no owner is not enforced when it is breached.

## Beyond the notes: from failures to a suite that grows

*(Beyond the notes: a working habit that the vault describes in one line.)*

A regression suite is a living asset. The loop that keeps it useful:

1. A user reports a failure, or a reviewer tags one in the human loop.
2. Reproduce it, and write the case with the expected behaviour.
3. Add it to the suite, tagged by category and severity.
4. Re-run the suite on the current production version, to confirm the case is already failing or passing as expected.
5. Keep the case forever, unless the product no longer has that behaviour.

Small categories are noisy. Re-run important cases several times, as 8.1 advises, and treat a move of a point or two in a category with few cases as a reason to look, not as proof.

## Beyond the notes: pitfalls

- **Reporting the judge's pass rate as the product's quality.** It is the judge's verdict until it is calibrated.
- **Shipping on the average.** The gate must read categories, not the mean.
- **Measuring acceptance without edit rate.** Acceptance can rise while the work gets harder.
- **A retention chart without a holdout.** Engaged users try new features first, so the chart says more about them than about the feature.
- **Pinning a model version and forgetting the vendor's retirement date.** The migration then happens under deadline, without an eval run.

## Beyond the notes: production checklist

- Keep a golden set with a dated owner, and refresh it from production samples every quarter.
- Log the model version, prompt version and judge version with every eval result.
- Put acceptance, edit rate, task success and the guardrails on one dashboard, segmented by task and language.
- Set thresholds for each guardrail before launch, and write down the action for each breach.
- Run the suite on every prompt, model, retrieval index and tool change, and attach the result to the ticket.

## Beyond the notes: interview corner

- **"How do you know your eval is good?"** Its failures should match the failures users report, and a human sample should agree with its verdicts at a level you have measured.
- **"What is the difference between a guardrail and a goal?"** A goal is what you push up. A guardrail is a line you must not cross while pushing.
- **"A stakeholder asks for one number for AI quality. What do you say?"** That one number hides something. Offer a short set: the rate on the golden set, the acceptance and edit rate online, and the worst-segment result.
- **"Why not just use a bigger model?"** It may raise quality, but latency, cost and the new regressions come with it. Judge the change on the same suite, the same gate and the same guardrails.

## Revision cheat-sheet

![Chapter 8 on one page: five layers, each with the question it answers.](diagrams/l5-big-picture.svg)

- **8.1** Offline evals score a fixed golden set against a written rubric, with exact checks, reference metrics or an LLM judge. Judge bias is real. Calibrate the judge against human labels and read the agreement, not only the pass rate.
- **8.2** Humans give ground truth through pairwise preference, rubric ratings, error tags and expert review. Stratify the sample, keep a random slice, tighten the guidelines when agreement is low, and label every release.
- **8.3** Online: task success, acceptance rate, edit rate, retry rate, thumbs (as a diagnostic), AI user retention against a control, time to completion. Acceptance rising with edits rising is a hidden cost.
- **8.4** Guardrails: harmful output rate, factual errors on high-stakes answers, refusal rate on both sides, p50 and p95 latency, cost per successful task, security and privacy, complaints. Set each threshold before launch.
- **8.5** Every prompt or model change is a release. Run the same suite, compare per category against the baseline, pass a gate set in advance, and roll out with shadow, canary and kill switch. Failures become regression cases.
- **Beyond the notes:** report agreement with the judge, not only its pass rate; write the denominator of every rate; fix the cohort and the window; a guardrail needs an owner.

## Self-test

<details class="quiz"><summary>What does an offline eval need in order to compare two versions fairly?

A fixed set of inputs (a golden dataset), a written rubric with anchor examples, and the same scoring applied to both versions, so the changes are comparable.

</details>

<details class="quiz"><summary>Why must an LLM judge be calibrated against human labels before you trust it?

The judge has known biases (position bias, a preference for longer or self-generated answers, sensitivity to prompt wording). Check its agreement with humans on a labelled sample, and only trust it on the criteria where it agrees.

</details>

<details class="quiz"><summary>Which kind of human evaluation is most useful for product decisions, and why?

Error tagging, because it labels each failure (hallucination, wrong tone, missed step) and so shows what to fix. A single average score does not.

</details>

<details class="quiz"><summary>What is the difference between acceptance rate and edit rate?

Acceptance rate is the share of AI outputs the user keeps. Edit rate is how much the user changes the output before using it. High acceptance with a high edit rate means users accept output they then fix.

</details>

<details class="quiz"><summary>Why does a retention chart for AI users need a control group?

Engaged users try new features first, so AI users may already be more engaged. A randomised holdout, or a matched cohort, separates the feature's effect from who chose to try it.

</details>

<details class="quiz"><summary>Name four guardrail metrics that must not regress while quality improves.

Harmful output rate, factual error rate on high-stakes answers, refusal rate, p95 latency, cost per task, personal-data leakage, and complaint or escalation rate. Any four of these count.

</details>

<details class="quiz"><summary>Why should a release gate read each category, not only the average?

A small average gain can hide a large loss in one segment. The gate blocks a release when any category drops beyond the agreed limit, for example more than 2 points.

</details>

<details class="quiz"><summary>What happened with the GPT-4o sycophancy rollback in April 2025?

An update made the model overly flattering. OpenAI rolled it back within days. In its post-mortem it said offline evals and A/B tests looked positive and that it had no specific sycophancy eval, so it added behaviour checks as launch blockers.

</details>

<details class="quiz"><summary>(Beyond the notes) A judge says 90% of outputs pass. Humans pass 65% of the same outputs and kappa is 0.08. What do you conclude?

The judge agrees with humans barely more than chance. Its 90% is not a quality signal. Fix the rubric or the judge prompt, and re-check agreement before the judge reports anything.

</details>

<details class="quiz"><summary>(Beyond the notes) Why does a one-point average gain not justify shipping a prompt change?

The average can hide a category that fell by six points. The gate reads each category against its own limit, so a single breach blocks the release even when the average rose.

</details>

<details class="quiz"><summary>(Beyond the notes) Why is "acceptance up 15 points" not a full win on its own?

If edits rise at the same time, the output kept as shown may barely change. The clean-kept share in the run block rose only 3 points while acceptance rose 15, so the hidden cost is the extra editing.

</details>


# Chapter 9 · Responsible AI, Risk, and Regulation

<!-- lecture n="6" label="9" short="Responsible AI" status="done" kind="AI risk" -->

## At a glance

| Question | Short answer |
|---|---|
| Why is bias a product problem and not only a model problem? | It enters through the data, the labels, the objective, the evaluation set and the product design. Measure it by segment, and treat fairness as a design decision. |
| Which fairness definition do you pick? | None is free. The common definitions conflict when base rates differ, so the PM picks one by the harm it prevents and says why. |
| What does India's DPDP Act require? | Notice and consent (or a listed legitimate use), a stated purpose, and erasure when the purpose ends. Most duties apply from 13 May 2027 (as of November 2026). |
| How is safety built? | A written content policy, enforced by model training, input and output filters, product limits and human review, with red-teaming before launch. |
| How do you tell users about AI? | Say when AI is involved, what data it used, and how confident or limited it is. Match the depth of explanation to the stakes. |
| How do you start on EU AI Act work? | Sort the product into a tier first: prohibited, high-risk, transparency or minimal. The tier sets the duties and the dates. |
| Which EU AI Act dates apply now? | Prohibitions and AI literacy (2 Feb 2025), GPAI duties (2 Aug 2025) and Article 50 transparency generally (2 Aug 2026). High-risk duties moved to 2 Dec 2027 and 2 Aug 2028. |
| Which error matters most? *(Beyond the notes)* | The one that costs more to the people affected, not the one with the best headline accuracy. |
| How do you use this in an interview? *(Beyond the notes)* | Name the harm, the group, the rule and the owner. Close on a gate or a metric you would check before launch. |

> [!NOTE] Where this comes from
> The vault lists no outside sources for this chapter beyond the texts it names: the DPDP Act 2023, the DPDP Rules 2025, the EU AI Act (Regulation (EU) 2024/1689), the Digital Omnibus on AI, the India IT Rules amendment of February 2026, the RBI FREE-AI report of August 2025 and the NIST AI Risk Management Framework. The dates were checked against public reporting as of November 2026, so confirm them against the official text before you quote them in a compliance setting. Its further-reading list names *AI Product Reading*, *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

Responsible AI is a set of product requirements. Each one has an owner, a metric and a launch gate. The chapter covers five areas: bias and representation (9.1), privacy under India's DPDP Act 2023 (9.2), safety, misuse and content policy (9.3), explainability and disclosure (9.4), and the regulatory landscape including the EU AI Act (9.5).

For a PM, responsible AI is designed in, measured and disclosed. It is not added after a complaint.

## Key takeaways

- Responsible AI is a set of product requirements with owners, metrics, and launch gates, not a document written once.
- Bias can enter through the data, the labels, the objective, and the evaluation set. Measure performance by segment, not only overall.
- Under India's DPDP Act 2023, personal data processing needs notice and consent (or a listed legitimate use), must be limited to a stated purpose, and must be erased when no longer needed. Most duties apply from 13 May 2027 under the DPDP Rules 2025 (as of November 2026).
- Safety requires a written content policy, technical enforcement, and a way for users to report problems.
- The EU AI Act classifies systems by risk. Prohibitions (Feb 2025) and GPAI duties (Aug 2025) already apply; high-risk duties were delayed to Dec 2027 and Aug 2028. Know your tier before you design.

> [!SIR] From the source notes
> Responsible AI is a set of product requirements, not a document written once. Measure performance by segment, not only overall.

## 9.1 Bias, fairness, and representation

> Bias enters an AI product at many points, so fairness has to be measured by segment and handled as a design decision, not left to the model team alone.

### Concept

**Where bias comes from**

- **Historical data:** training data reflects past decisions, including discriminatory ones (e.g. past hiring or lending).
- **Representation:** some groups, languages, dialects, skin tones, or regions are under-represented, so the model performs worse for them.
- **Labels:** human labels carry annotator bias, and proxy labels (e.g. "clicks" as "relevance") can encode bias.
- **Objective:** optimising a single average metric can sacrifice minority groups.
- **Evaluation:** a test set that does not include the groups you serve hides the problem.
- **Product design:** defaults, prompts, and UI choices can steer users unequally.

![Six entry points for bias, each with its own test, then five practical steps.](diagrams/l6-bias-sources.svg)

**Fairness is not one number.** Common definitions conflict with each other, so the PM must choose which matters for the product and say why:

- Equal error rates across groups (e.g. false positive rate parity).
- Equal positive-outcome rates (demographic parity), which can be wrong when base rates differ.
- Calibration: a score means the same thing for every group.
- Known result worth citing: when base rates differ between groups, a model generally cannot satisfy calibration and equal error rates at the same time (the COMPAS debate, 2016, made this concrete). Choosing a definition is a values decision, not a technical one.
- Generative AI adds **representational harms**: stereotyped images, unequal quality across languages, or toxic outputs about some groups. Test prompts across groups and languages, not just accuracy.

![Three fairness definitions that cannot all hold at once when base rates differ.](diagrams/l6-fairness-conflict.svg)

**Practical steps**

1. Identify affected groups for the use case, including language and region for Indian users.
2. Build an eval set with those groups represented, and report performance per segment.
3. Set a gap threshold that blocks launch (e.g. error rate for any group no more than X points above the average).
4. Give users a way to report errors, and review those reports by segment.
5. Document known limits in the model card or product docs.

Indian context: performance often drops for Indian languages, code-mixed text (Hinglish), and regional accents in speech systems. Test for these explicitly.

### Real-world examples

- **Gender Shades (Buolamwini and Gebru, 2018):** found commercial facial-analysis systems had much higher error rates for darker-skinned women than for lighter-skinned men. Led several vendors to retrain and publish updates.
- **Amazon recruiting tool (reported by Reuters, 2018):** an experimental resume-screening model learned to penalise resumes mentioning women's colleges and was scrapped.
- **Google Photos (2015):** image labelling mislabelled Black people as gorillas. Google apologised and the labels were removed, a reminder that training-data coverage matters.
- **Apple Card credit limits (2019-2021):** viral reports that women got lower limits than their husbands led New York's financial regulator to investigate Goldman Sachs. In March 2021 it found no unlawful discrimination, but criticised the poor customer explanations. The lesson is that even a defensible model loses trust if it cannot explain decisions.
- **Google Gemini image generation (February 2024):** an attempt to correct for under-representation produced historically inaccurate images (for example, of historical figures), and Google paused image generation of people. Over-correction is also a fairness failure.

### Practice questions

> [!INTERVIEW] You are building an AI resume screener for a campus placement platform. Where could bias enter, and how would you test each point?
> *(Beyond the notes: a starting point, not the vault's answer.)* Walk the six entry points in order: historical hiring data, under-represented colleges and languages, labels from past recruiter decisions, a single accuracy objective, an eval set without rural or regional candidates, and the ranking UI. For each one, name a test: a per-group error table, a label audit, and a review of the top and bottom ranked profiles.

> [!INTERVIEW] Two fairness definitions conflict for your loan model. Which do you pick, and how do you explain the choice to leadership?
> **Answer outline (Q2):** Start from the harm. In lending, unequal false rejections usually matter more than equal approval rates, so error-rate parity is often the priority. State the trade-off explicitly, document it, and involve legal and risk teams.

> [!INTERVIEW] Your speech-to-text product has a 12% word error rate for Hinglish and 6% for English. What do you do before launch?
> **Answer outline (Q3):** Treat a 2x gap as a launch-blocking gap if Hinglish speakers are a core segment. Find the cause (training data, vocabulary, accents, noise), collect and label consented Hinglish data, and fine-tune or switch to a model built for Indian languages. If launching anyway, scope it clearly (label as beta for Hinglish), add easy correction, and set a target date to close the gap.

*Related:* Chapter 9.2 (Privacy, consent, and data retention), Chapter 9.4 (Explainability and disclosure), Chapter 8.1 (Offline evals: golden datasets, rubrics, LLM-as-judge), Chapter 9.5 (Regulatory landscape), Chapter 5.7 (Computer vision, speech, and recommendation systems), Chapter 24.3 (Define success metrics for an AI resume reviewer).

## 9.2 Privacy, consent, and data retention (India DPDP Act 2023)

> Under India's Digital Personal Data Protection Act, 2023, a product that processes personal data needs a lawful basis (usually consent), a stated purpose, and a plan to delete data when the purpose ends. Most duties bite from 13 May 2027 under the DPDP Rules, 2025.

### Concept

**Status and timeline (as of November 2026)**

- **Act:** received Presidential assent on 11 August 2023.
- **DPDP Rules, 2025:** notified on 13 November 2025, with a phased start:
  - **13 November 2025:** definitions and the Data Protection Board provisions in force.
  - **13 November 2026:** Consent Manager registration (Rule 4).
  - **13 May 2027:** the substantive duties (notice, consent, security, breach reporting, retention, children's data, rights, Significant Data Fiduciary duties).
- In January 2026 MeitY consulted industry on shortening the 18-month window to 12 months (at least for large data fiduciaries). As of the latest reports found, no amendment had been notified, so 13 May 2027 stands. Check for a Gazette amendment before quoting a date.

![The DPDP timeline: assent, Rules, Consent Manager registration and the substantive duties.](diagrams/l6-dpdp-timeline.svg)

**Core roles**

- **Data Principal:** the individual whose data is processed (for a child, includes the parent or guardian).
- **Data Fiduciary:** decides why and how data is processed (roughly the GDPR "controller").
- **Data Processor:** processes data on a fiduciary's behalf (for example, your LLM API vendor or cloud host).
- **Consent Manager:** a registered entity through which Principals give, manage, and withdraw consent. Under the Rules it must be an Indian company with a minimum net worth of ₹2 crore.
- **Significant Data Fiduciary (SDF):** designated by the government based on volume and sensitivity of data and risk to rights or the state. Extra duties: a Data Protection Officer based in India, an independent auditor, an annual data protection impact assessment and audit, checks that algorithmic software does not risk Principals' rights, and possible localisation of specified data.

**Obligations a PM designs for**

- **Notice:** clear, standalone, itemised notice of the data collected and the purpose, how to withdraw consent and exercise rights, and how to complain to the Board. Available in English or any of the 22 languages in the Eighth Schedule of the Constitution.
- **Consent:** free, specific, informed, unconditional, and unambiguous, by a clear affirmative action, limited to the data needed for the purpose. Withdrawal must be as easy as giving consent.
- **Legitimate uses (Section 7):** a short list of non-consent grounds (for example, data the user voluntarily gave for a specific purpose, employment, medical emergencies, legal duties). There is no broad GDPR-style "legitimate interests" ground.
- **Purpose limitation and retention:** use data only for the stated purpose and erase it when the purpose is served or consent is withdrawn. The Rules set a three-year inactivity erasure period (with 48 hours' notice) for large e-commerce, online gaming, and social media platforms, and require keeping processing logs for at least one year.
- **Children (under 18):** verifiable parental consent; no tracking, behavioural monitoring, or targeted advertising directed at children; some classes (such as healthcare and educational institutions) are exempted from parts of this.
- **Rights:** access, correction and erasure, grievance redressal, and nominating someone to act on the Principal's behalf.
- **Security and breaches:** reasonable safeguards (encryption, access control, logging); on a breach, inform affected Principals without delay and send the Board a detailed report within 72 hours.
- **Scope note for AI:** the Act does not apply to personal data that the Principal has themselves made publicly available. This matters for training on public web data, but it does not cover data made public by someone else, and other laws (copyright, IT Rules) still apply.
- **Penalties:** set per instance by the Data Protection Board, up to ₹250 crore for failing to take reasonable security safeguards, up to ₹200 crore for failing to notify a breach or breaching children's obligations, and up to ₹150 crore for SDF obligations.

**AI-specific questions to answer in a PRD**

1. Are prompts, uploads, or chat logs used to train or improve models? Is that a separate, optional consent?
2. How long are logs kept, and does deletion also remove them from training and eval datasets?
3. What does the LLM vendor (as your processor) retain, and for how long?
4. Can a user who withdraws consent be removed from future training runs? (Removing data from an already-trained model is technically hard; document your position.)
5. Can you state the purpose of each data flow in one sentence?

### Real-world examples

- **Samsung and ChatGPT (2023):** after engineers reportedly pasted confidential source code and meeting notes into ChatGPT, Samsung restricted employee use of generative AI tools. AI tools need data-handling rules for employees, not only for customers.
- **Google Gemini apps privacy notice (2024):** Google told users not to enter confidential information because human reviewers may read conversations to improve the service, and gave controls to turn off activity saving. Clear training-use and retention disclosure in practice.
- **Italy's Garante and OpenAI:** the Italian regulator temporarily blocked ChatGPT in March 2023 over lawful basis and age checks, then fined OpenAI €15 million in December 2024 under GDPR. A preview of how a data protection board can act on AI products.
- **Account Aggregator framework (India):** RBI-licensed Account Aggregators let users approve and revoke financial-data sharing through a consent dashboard. It is a separate RBI framework, but it is the closest working model of the consent-manager idea the DPDP Act describes.

### Practice questions

> [!INTERVIEW] Your AI study app stores students' practice-test answers to personalise recommendations. Walk through the DPDP obligations.
> **Answer outline (Q1):** Many users are under 18, so verifiable parental consent comes first, and no behavioural tracking or targeted ads aimed at them. Give an itemised notice in English and the relevant Indian languages. Collect only what personalisation needs, keep answers only while the account is active, let parents see, correct, and erase data, and offer easy withdrawal. If answers will train models, ask separately. Secure the data and have a 72-hour breach process. Plan for 13 May 2027 (or earlier if the timeline is shortened).

> [!INTERVIEW] A user withdraws consent. What must happen to their data, and to a model fine-tuned on it?
> **Answer outline (Q2):** Stop processing for that purpose and erase the data unless another law requires keeping it; tell processors (including the LLM vendor) to erase too. For a fine-tuned model the law is unsettled: exclude the data from future training runs, assess whether the model could reproduce it, retrain or filter if the risk is real, and document the decision with legal counsel.

> [!INTERVIEW] How would you decide the retention period for chat logs in an AI assistant?
> *(Beyond the notes: a starting point.)* Start from the purpose: keep logs only as long as a stated feature needs them (for example, to show history or to debug a complaint). Set separate periods for raw chats, derived data such as embeddings, and eval sets. Check the statutory minimums, such as the one-year processing-log rule in the Rules, and document the reason for each period.

> [!INTERVIEW] Are minors covered, and what extra steps apply for a learning app used by school students?
> *(Beyond the notes: a starting point.)* Yes, the Act protects anyone under 18 as a child. Plan for verifiable parental consent, no behavioural tracking or targeted advertising directed at children, parent access to data, and a check on whether the school or the app is the fiduciary. Confirm the exemptions for educational institutions with counsel before relying on them.

> [!INTERVIEW] Your team wants to train a model on public social media posts by Indian users. What does DPDP say, and what else would you check?
> *(Beyond the notes: a starting point.)* The Act does not apply to personal data that the Principal has themselves made publicly available, but it does not cover posts made public by someone else. Check copyright and the platform's terms, remove or exclude personal details, and document the lawful position for each source with counsel.

*Related:* Chapter 9.1 (Bias, fairness, and representation), Chapter 9.4 (Explainability and disclosure), Chapter 9.5 (Regulatory landscape), Chapter 10.3 (Feedback loops and consented data collection), Chapter 4.2 (Data as a product input and data flywheels), Chapter 24.1 (Design an AI study assistant for competitive exam aspirants).

## 9.3 Safety, misuse, and content policy

> A content policy states what the product will and will not do, and safety work turns that policy into enforced behaviour, monitoring, and a way for users to report failures.

### Concept

- **Harm categories:** typically include violence, self-harm, sexual content (especially involving minors), hate and harassment, fraud and scams, privacy violations, dangerous technical instructions, and misinformation in sensitive domains.
- **Misuse vs failure:** a failure is the product behaving badly on a normal request (e.g. giving wrong medical dosage). Misuse is a user deliberately trying to get harmful output (e.g. jailbreak prompts). Both need controls, but the controls differ.
- **Layers of defence:**
  1. **Model-level training** to refuse or safely complete risky requests.
  2. **Input filters** that classify prompts for policy categories.
  3. **Output filters** that check responses before display.
  4. **Product design:** limit capabilities (e.g. no outbound email without confirmation), rate limits, and account-level signals.
  5. **Human review and escalation** for borderline and high-severity cases.

![Five layers of defence, and the difference between misuse and failure.](diagrams/l6-safety-layers.svg)

- **Red-teaming:** structured attempts to break the system, run before launch and on a schedule, with findings turned into regression tests (see Chapter 8.5, Regression testing when models or prompts change).
- **Reporting and appeals:** users must be able to flag output, and users whose content is blocked need a route to appeal.
- **Tiered responses:** for self-harm or abuse, the product may show crisis resources. For minor policy issues, it may decline and offer an alternative.

PM decisions: the policy itself is a product decision with trade-offs. Over-refusing harms helpfulness, and under-refusing causes harm and reputational damage. Write the policy with examples of allowed and disallowed requests, and review it with legal, trust and safety, and domain experts.

Specific risks for generative products:

- **Jailbreaks:** users craft prompts (role-play, encoding, many-shot examples) to bypass the model's refusals. Expect new ones every week; defence is layered, not one filter.
- **Prompt injection:** content in a retrieved document, email, or web page instructs the model to do something the user did not ask for. It becomes dangerous when an agent has tools and access to private data. Treat any external text as untrusted input and limit what the agent can do without confirmation.
- **Policy as a measured trade-off:** track both harmful-output rate and over-refusal rate on fixed test sets (see Chapter 8.4).

### Real-world examples

- **Microsoft Tay (2016):** a chatbot learned abusive language from user interactions within hours and was taken offline. Showed the need for input and output safety layers.
- **Meta Llama Guard:** an open safety classifier that scores prompts and responses against a configurable harm taxonomy, used as a layer in product pipelines.
- **OpenAI usage policies:** publicly published rules on prohibited uses, showing how a company turns policy into a document that developers must follow.
- **Character.AI (2024-2025):** lawsuits filed from October 2024 alleged harm to minors from companion chatbots. The company first added teen safety features, then announced in October 2025 that it would end open-ended chat for under-18 users, effective 25 November 2025. The allegations are contested in court, so cite the product response rather than the claims.
- **Grok image generation (January 2026):** X's Grok was widely used to create sexualised edits of real people's photos; India's MeitY issued a 72-hour notice and xAI restricted the tool. A capability shipped without misuse testing becomes a regulatory incident.

### Practice questions

> [!INTERVIEW] Define the content policy for a study assistant used by school students. What is allowed, what is refused, and what is escalated?
> *(Beyond the notes: a starting point.)* Allowed: explanations of syllabus topics, worked examples, study plans. Refused: explicit content, self-harm instructions, help with cheating on graded tests, and personal data requests. Escalated: any message that suggests a child is at risk, which goes to a trained human with a crisis-resource reply shown at once. Write one example of each for every category.

> [!INTERVIEW] A user uses a jailbreak to get the assistant to write malware. Which layers should have caught it?
> *(Beyond the notes: a starting point.)* The input filter should flag the prompt as a cyber-harm request, the model training should refuse, and the output filter should catch code that matches a harmful pattern. Product limits, such as no code execution without review, would stop the damage if the first three failed. Log the attempt and add the jailbreak to the red-team suite.

> [!INTERVIEW] How would you measure whether safety filters are over-refusing?
> *(Beyond the notes: a starting point.)* Keep two fixed sets: one of risky requests that must be refused and one of benign requests that look similar and must be answered. Track the harmful-output rate on the first set and the over-refusal rate on the second, and review the cases where they disagree. Re-run both sets whenever a filter or prompt changes.

> [!INTERVIEW] A retrieved web page contains hidden instructions to exfiltrate user data. How should the system behave?
> **Answer outline (Q4):** Treat retrieved text as data, not instructions. Keep tool permissions narrow, require user confirmation for sensitive actions, and filter outputs for leakage of personal data. Log and review the attempt, and add it to the red-team suite.

*Related:* Chapter 8.4 (Guardrail metrics: harmful outputs, latency, cost), Chapter 9.1 (Bias, fairness, and representation), Chapter 7.3 (Handling hallucinations, errors, and recovery paths), Chapter 5.6 (Agents and tool use), Chapter 9 (Responsible AI, Risk, and Regulation).

## 9.4 Explainability and disclosure

> Users should know when AI is involved, what it used to produce an answer, and how confident or limited it is, and the depth of explanation should match the stakes.

### Concept

**Disclosure** answers "is this AI?" and "what data did it use?"

- Label AI-generated content and AI-driven decisions clearly.
- Say when a human is or is not in the loop.
- Disclose data sources, especially when personal data is used for personalisation.
- For synthetic media, use provenance signals such as watermarks or content credentials where feasible.

**Explainability** answers "why this output?"

- **Global:** how the system works in general, shown in model cards or product help pages.
- **Local:** why this specific output was given, e.g. "Recommended because you watched X and Y," or the top factors in a credit decision.
- Explanations can be given at different levels of depth: a one-line reason for consumers, a detailed factor list for a loan officer, and full logs for auditors.

![Disclosure answers on the left; the explanation ladder on the right, from one line to full logs.](diagrams/l6-disclosure-ladder.svg)

**Trade-offs**

- Explanations can be wrong or misleading if they are post-hoc rationalisations. Do not present a generated rationale as the real cause unless it has been validated.
- Over-explaining adds noise. Explain when the user needs it to act or to contest a decision.
- Disclosing limitations (e.g. "may be inaccurate; verify before filing") is a form of explanation and reduces overtrust.

**Regulatory hooks (as of November 2026)**:

- **EU AI Act Article 50:** tell people they are interacting with AI, mark AI-generated content in a machine-readable way, and label deepfakes; generally applicable from 2 August 2026, with a grace period to 2 December 2026 for generative systems already on the market. High-risk systems also owe deployers instructions and explanations.
- **GDPR:** meaningful information about the logic of solely automated decisions with significant effects.
- **India:** the IT Rules amendment in force since 20 February 2026 requires platforms to prominently label synthetic audio and visual content and keep provenance metadata; the DPDP Act requires clear notice of purpose.
- **Credit:** US adverse-action rules require specific reasons for a denial, even when a complex model made it.

PM check: for each AI output, ask "what would a user need to know to decide whether to trust or contest this?" Build that into the UI, not only into a policy page.

### Real-world examples

- **Google SynthID (2023):** an invisible watermarking system for AI-generated images, audio, and text, used to help identify AI content.
- **C2PA content credentials:** an open standard for attaching provenance metadata to media. Adopted by companies including Adobe and Microsoft.
- **Netflix and Spotify recommendation reasons:** products show short reasons such as "because you watched" for recommendations, an example of local explanation at low stakes.
- **Google Search "About this result" (2021 onward):** a panel that explains where a result comes from and why it was shown.
- **Meta "AI info" labels (2024):** Meta labels images detected as AI-generated or edited using C2PA and similar signals. It renamed the label from "Made with AI" after photographers complained that light edits triggered it, which shows that disclosure labels need precision too.

### Practice questions

> [!INTERVIEW] For an AI-written job description tool, what should be disclosed to the recruiter and to candidates?
> *(Beyond the notes: a starting point.)* To the recruiter: that the draft was AI-written, which inputs it used, and that a person must review it before posting. To candidates: good practice is to say that AI is part of any screening step, and how to ask for a human review. Check the exact wording with counsel.

> [!INTERVIEW] A loan applicant asks why they were rejected by an ML model. What explanation do you give, and what do you avoid saying?
> **Answer outline (Q2):** Provide the main factors that affected the decision, in plain language, with a path to contest or re-apply. Avoid implying a precise causal reason unless the explanation method supports it, and avoid exposing proprietary model details or data that would enable gaming.

> [!INTERVIEW] How would you design disclosure for an AI tutor that sometimes makes mistakes?
> **Answer outline (Q3):** A clear first-run statement that the tutor can be wrong and how to check; source or textbook references on factual answers; a visible "report a mistake" button; age-appropriate wording for students and a separate data notice for parents; stronger cues ("double-check with your teacher") on topics where evals show weak accuracy.

*Related:* Chapter 9.1 (Bias, fairness, and representation), Chapter 9.5 (Regulatory landscape), Chapter 7.2 (User control, transparency, and confidence signals), Chapter 7.5 (Setting expectations and onboarding users to AI features), Chapter 9 (Responsible AI, Risk, and Regulation).

## 9.5 Regulatory landscape: EU AI Act and sector-specific rules

> The EU AI Act sorts AI systems into risk tiers with different obligations, India regulates AI mainly through data, IT, and sector rules, and sector regulators add their own rules, so a PM must classify the product before designing it.

### Concept

**EU AI Act (Regulation (EU) 2024/1689): the four tiers**

- **Unacceptable risk (prohibited):** manipulative or subliminal techniques that cause significant harm, exploiting vulnerabilities (age, disability, economic situation), social scoring (by public *or* private actors), predicting crime from profiling alone, untargeted scraping of facial images to build face-recognition databases, emotion recognition in workplaces and schools (except medical or safety reasons), biometric categorisation to infer sensitive traits, and real-time remote biometric identification in public spaces for law enforcement (narrow exceptions).
- **High-risk:** systems listed in Annex III (biometrics, critical infrastructure, education such as admissions and exam scoring, employment such as CV screening and promotion decisions, access to essential services such as credit scoring and insurance pricing, law enforcement, migration, justice) or safety components of products already regulated under EU law (Annex I: medical devices, machinery, toys, and so on). Duties: risk management, data governance, technical documentation, logging, transparency to deployers, human oversight, accuracy and robustness, conformity assessment, and registration.
- **Transparency (Article 50, "limited risk"):** tell people they are talking to an AI, mark AI-generated content in a machine-readable way, and label deepfakes.
- **Minimal risk:** no new obligations (spam filters, most recommendation features).
- **General-purpose AI (GPAI) models** are regulated separately: technical documentation, information for downstream developers, a copyright policy, and a summary of training content. Models with systemic risk (presumed above 10^25 training FLOPs) also need evaluations, adversarial testing, incident reporting, and cybersecurity. A voluntary GPAI Code of Practice was published in July 2025.
- **Provider vs deployer:** a company that builds an app on a third-party model is usually a *deployer* or a *provider of an AI system*, not a GPAI model provider; its obligations depend on the use case's tier.
- **Fines:** up to €35 million or 7% of global annual turnover for prohibited practices, and up to €15 million or 3% for most other breaches.

![The four EU AI Act tiers, with the duties that sit under the top two.](diagrams/l6-eu-pyramid.svg)

**EU AI Act timeline (as of November 2026)**

| Date | What applies |
|---|---|
| 1 Aug 2024 | Act entered into force |
| 2 Feb 2025 | Prohibited practices and AI literacy duties |
| 2 Aug 2025 | GPAI model obligations, governance, penalties (models already on the market before this date have until 2 Aug 2027) |
| 2 Aug 2026 | Commission enforcement powers over GPAI providers; Article 50 transparency duties generally |
| 2 Dec 2026 | Grace period ends for marking AI-generated content by generative systems already on the market before 2 Aug 2026; new ban on AI that generates non-consensual intimate images (added by the Digital Omnibus) |
| 2 Dec 2027 | High-risk obligations for Annex III systems (originally 2 Aug 2026) |
| 2 Aug 2028 | High-risk obligations for AI in Annex I regulated products (originally 2 Aug 2027) |

![The EU AI Act timeline as of November 2026, with the Digital Omnibus changes marked.](diagrams/l6-eu-timeline.svg)

- **The delay:** the Commission proposed the "Digital Omnibus on AI" in November 2025. A provisional deal was reached on 7 May 2026, Parliament adopted it on 16 June 2026, and the Council approved it on 29 June 2026; reporting says it was published in the Official Journal on 24 July 2026 and entered into force on 27 July 2026. The obligations were deferred, not removed. Confirm against EUR-Lex before quoting dates in a compliance context.

**India (as of November 2026): no AI-specific law**

- **DPDP Act 2023 and DPDP Rules 2025:** personal data (see Chapter 9.2, Privacy, consent, and data retention).
- **IT Rules amendment on synthetically generated information:** notified 10 February 2026, in force 20 February 2026. Platforms must prominently label AI-generated or altered audio and visual content, ask users to declare it, carry provenance metadata, and act on unlawful content on much shorter timelines.
- **India AI Governance Guidelines (MeitY, November 2025):** principle-based guidance that relies on existing laws and sector regulators rather than a new AI Act.
- **RBI FREE-AI framework (August 2025):** a committee report setting out seven principles ("sutras") and 26 recommendations for AI in banks, NBFCs, and payment firms. Advisory until the RBI issues formal directions.

**Other frameworks to know**

- **GDPR (EU):** lawful basis, purpose limitation, data minimisation, and Article 22 rights around solely automated decisions with legal or similarly significant effects. Applies to any product serving people in the EU.
- **NIST AI Risk Management Framework 1.0 (US, January 2023):** voluntary; four functions: govern, map, measure, manage. The US has no comprehensive federal AI law; rules come from sector regulators and a changing set of state laws.
- **Sector rules:** the US FDA has authorised more than 1,000 AI-enabled medical devices through existing pathways; credit models fall under model risk management and fair-lending rules (in the US, adverse-action notices must give specific reasons); in India, the RBI, SEBI, and IRDAI regulate AI use by the entities they supervise.

**PM workflow**

1. Map the use case to the EU tier (and any Indian or sector rule) and to your role (provider or deployer).
2. List obligations, owners (legal, engineering, product), and the dates that apply.
3. Build documentation, logging, human oversight, and transparency labels into the roadmap, not the launch checklist.
4. Re-check classification when the use case, market, or model changes.

### Real-world examples

- **Clearview AI:** data protection authorities in Italy, France, and Greece (2022) and the Netherlands (2024) each fined the company €20 million or more for scraping facial images without a lawful basis. Scraping for face recognition is now a prohibited practice under the AI Act.
- **Italy and ChatGPT:** the Garante temporarily blocked ChatGPT in March 2023; it returned about a month later after OpenAI added privacy controls and age gating, and the Garante fined OpenAI €15 million in December 2024.
- **Grok and India's IT Rules (January 2026):** after X's Grok was used to create sexualised images of real women, MeitY gave X 72 hours to act and report; X removed content and blocked accounts, and xAI restricted the image tool. A month later India notified its synthetic-content labelling rules.
- **FDA-authorised AI devices:** most are in radiology, cleared under existing medical-device pathways, an example of a sector regulator handling AI without an AI-specific law.

### Practice questions

> [!INTERVIEW] Your app uses AI to shortlist job applicants for a company in Germany. What is the risk tier, and what must you build?
> **Answer outline (Q1):** CV screening is an Annex III employment use, so it is high-risk. The provider needs risk management, data governance (representative data, bias checks), technical documentation, logging, human oversight, accuracy and robustness testing, conformity assessment, and registration; the employer (deployer) must use it as instructed, assign trained human oversight, and inform candidates. GDPR applies too, including Article 22. The Annex III date is now 2 December 2027, but enterprise buyers already ask for this evidence, so build it into the architecture now.

> [!INTERVIEW] Which parts of the EU AI Act apply to a company that only calls a third-party GPAI API?
> **Answer outline (Q2):** The GPAI model duties fall on the model vendor. The company's duties depend on its use case: Article 50 transparency for a chatbot or generated content, full high-risk duties if the use case is in Annex III, nothing new if it is minimal risk. Fine-tuning or substantially modifying a model can make you a provider for that modification. Also check that the vendor's documentation supports your own obligations.

> [!INTERVIEW] How would you explain to leadership why launch in the EU needs a compliance plan before the model is final?
> *(Beyond the notes: a starting point.)* The tier and the data flows shape the model choice, the logging and the human review, so changing them late costs more than planning now. Show the dates that already apply, the dates that may move, and the evidence that enterprise buyers will ask for at procurement.

> [!INTERVIEW] What is the difference between a prohibited practice and a high-risk system?
> *(Beyond the notes: a starting point.)* A prohibited practice cannot be placed on the EU market at all, whatever the controls, such as social scoring. A high-risk system is allowed, but only after the provider meets the listed duties (risk management, documentation, logging, human oversight, conformity assessment and registration).

> [!INTERVIEW] The high-risk deadline moved to December 2027. Should your team pause compliance work?
> **Answer outline (Q5):** No. The obligations were deferred, not removed; documentation, data governance, and logging take a long time to retrofit; customers and procurement teams ask for them now; and prohibitions, AI literacy, and transparency duties already apply. Use the time to build properly rather than rushing in 2027.

*Related:* Chapter 9.2 (Privacy, consent, and data retention), Chapter 9.1 (Bias, fairness, and representation), Chapter 9.4 (Explainability and disclosure), Chapter 9.3 (Safety, misuse, and content policy), Chapter 20.5 (AI PRD additions: eval criteria, failure modes, data requirements), Chapter 24.5 (Launch an AI feature in a payments app: pricing and risks), Chapter 9 (Responsible AI, Risk, and Regulation).

## Beyond the notes: bias checks you can run this week

These checks turn the chapter's advice into a table your team can fill in before a launch review.

| Check | How to run it | What it tells you |
|---|---|---|
| Coverage | Count labelled examples per group, language and region | Whether the eval set can see the groups at all |
| Error gap | Error rate per group, next to the overall rate | Which group is worse off, and by how much |
| Feedback skew | Thumbs-down and edit rates per segment | Whether heavy or angry users dominate the signal |
| Over-correction | The same prompt across groups, with outputs read by hand | Whether a fix for one group makes another group's answers wrong |
| Language check | Results per language, including code-mixed text | Hinglish and regional-accent gaps |

## Beyond the notes: a consent checklist for the PRD

A starting point for the PRD, to check with counsel before you rely on it.

- Write one sentence per data flow that states its purpose.
- Use separate opt-ins for product improvement, evaluation, and training.
- Keep training on prompts and uploads off by default.
- Make the deletion path reach logs, embeddings and eval sets, not only the primary store.
- Write down your position on users who withdraw consent after a model is trained.
- Use a clear, affirmative action for each consent, never a pre-ticked box.

## Beyond the notes: documentation that proves responsibility

- **Model card:** intended use, data, evaluation by segment, and known limits. The idea comes from Mitchell and others, "Model Cards for Model Reporting" (2019).
- **System card for the product:** where AI appears, the owners, the launch gates, and the kill switch (see Chapter 10.1).
- **Decision log:** the fairness definition, the threshold, and the EU tier, each with the date, the owner and the reason.

## Beyond the notes: a safety test set

- Pair benign requests with near-identical risky ones, so the set tests both over-refusal and under-refusal.
- Measure the harmful-output rate and the over-refusal rate on fixed sets, as in 9.3.
- Re-run both sets after every model, prompt or filter change (Chapter 8.5).

## Beyond the notes: pitfalls

- **Treating the EU dates as final.** The vault says to confirm against the Official Journal and EUR-Lex. A deferred date can move again.
- **Using a generic privacy policy as the DPDP notice.** The notice must be clear, standalone and itemised, in English or an Eighth Schedule language.
- **Pre-ticked consent boxes.** Consent needs a clear affirmative action.
- **Disclosure labels that fire on light edits.** Meta's 2024 rename is the example to remember.
- **Confusing your duties with the vendor's.** A GPAI model provider and an app deployer have different obligations, and the tier of your use case decides yours.

## Beyond the notes: interview corner

- **"Which fairness definition would you pick for a loan model?"** Starting point: name what each error does to the applicant. If an unfair false rejection is the harm, error-rate parity is usually the first thing to measure.
- **"How would you answer a regulator's question about your AI feature?"** Starting point: the tier, the purpose of each data flow, the notice text the user saw, the owner of each decision, and the logs that show what happened.
- **"What is the one question you ask before any AI launch on responsibility?"** Starting point: "who is worse off if this is wrong, and how would we know within a day?"

## Revision cheat-sheet

![Chapter 9 on one page: five areas, each with the question it answers.](diagrams/l6-big-picture.svg)

- **9.1 Bias:** enters through data, representation, labels, objective, evaluation and product design. Fairness is not one number; choose a definition by the harm and say why. Set a gap gate and document limits.
- **9.2 Privacy (DPDP):** Act assent 11 Aug 2023; Rules notified 13 Nov 2025; Consent Manager registration 13 Nov 2026; most duties from 13 May 2027 (as of November 2026). Notice, consent, purpose, retention, children, 72-hour breach report. Roles: Principal, Fiduciary, Processor, Consent Manager, SDF.
- **9.3 Safety:** write the content policy, then enforce it in five layers. Red-team and turn findings into tests. Misuse is deliberate; failure is a bad answer on a normal request. Retrieved text is data, not instructions.
- **9.4 Explainability:** disclose AI use, data and human involvement. Explanations are local or global and match the stakes. Do not present a post-hoc rationale as the cause unless validated.
- **9.5 Regulation:** EU tiers are prohibited, high-risk, transparency and minimal, plus GPAI duties. Prohibitions (2 Feb 2025), GPAI (2 Aug 2025), Article 50 (2 Aug 2026). High-risk moved to 2 Dec 2027 and 2 Aug 2028. India: no AI-specific law yet; DPDP, IT Rules (in force 20 February 2026), RBI FREE-AI (advisory).
- **Beyond the notes:** a bias check table, a consent checklist, model cards and decision logs, a paired safety test set, and the five pitfalls.

## Self-test

<details class="quiz"><summary>Why is responsible AI a product requirement and not a model-team task?

Bias enters through data, labels, objectives, evaluation sets and product design, and each point needs an owner and a measure. It is designed in, measured and disclosed, not added after a complaint.

</details>

<details class="quiz"><summary>Why can a model usually not satisfy calibration and equal error rates at the same time?

When base rates differ between groups, a model generally cannot meet both. Choosing a definition is a values decision, so the PM picks one and says why.

</details>

<details class="quiz"><summary>What are the key DPDP dates, and when do most duties apply?

Assent on 11 August 2023. The Rules were notified on 13 November 2025. Consent Manager registration (Rule 4) follows on 13 November 2026. Most substantive duties apply from 13 May 2027 (as of November 2026).

</details>

<details class="quiz"><summary>What must happen when a user withdraws consent, and what about a fine-tuned model?

Stop processing for that purpose, erase the data unless another law requires keeping it, and tell processors to erase too. For a fine-tuned model, exclude the data from future training, assess whether the model could reproduce it, and document the decision with counsel.

</details>

<details class="quiz"><summary>Name the five layers of defence in a safety stack.

Model-level training to refuse risky requests, input filters for prompts, output filters before display, product design limits (rate limits, no outbound action without confirmation), and human review and escalation for borderline cases.

</details>

<details class="quiz"><summary>What is the difference between misuse and failure?

A failure is the product behaving badly on a normal request, such as a wrong medical dosage. Misuse is a user deliberately trying to get harmful output, such as with a jailbreak. Both need controls, but the controls differ.

</details>

<details class="quiz"><summary>What is prompt injection, and why is it dangerous for agents?

Content in a retrieved document, email or web page instructs the model to do something the user did not ask for. It is dangerous when an agent has tools and access to private data, so treat external text as untrusted and limit actions that need no confirmation.

</details>

<details class="quiz"><summary>Name the four EU AI Act tiers and one example of each.

Unacceptable (prohibited), such as social scoring. High-risk, such as CV screening. Transparency (Article 50), such as telling users they are talking to an AI. Minimal risk, such as spam filters.

</details>

<details class="quiz"><summary>Which EU AI Act duties apply now, and which high-risk dates moved?

Prohibitions and AI literacy (2 February 2025), GPAI obligations (2 August 2025) and Article 50 transparency generally (2 August 2026) apply. High-risk obligations for Annex III systems moved to 2 December 2027, and for Annex I products to 2 August 2028.

</details>

<details class="quiz"><summary>(Beyond the notes) Why does a provider vs deployer distinction matter for a company that calls a third-party GPAI API?

The GPAI model duties fall on the model vendor. The company's obligations depend on its own use case and tier, and fine-tuning or substantially modifying the model can make it a provider for that change.

</details>

<details class="quiz"><summary>(Beyond the notes) Why should explanations match the stakes, and why are post-hoc rationales risky?

A one-line reason suits a consumer, a factor list suits a loan officer, and full logs suit an auditor. A rationale generated after the fact can sound right without being the real cause, so do not present it as one unless it has been validated.

</details>

<details class="quiz"><summary>(Beyond the notes) What does a good safety test set measure?

Both sides of the trade-off: risky requests that must be refused (the harmful-output rate) and similar benign requests that must be answered (the over-refusal rate). Re-run both after every model, prompt or filter change.

</details>


# Chapter 10 · Launching and Iterating AI Features

<!-- lecture n="7" label="10" short="Launching AI features" status="done" kind="AI launch" -->

## At a glance

| Question | Short answer |
|---|---|
| How do you ship an AI feature? | Never to everyone at once. Release it in widening rings, with gates between steps and a switch that turns it off in minutes. |
| What is the rollout ladder? | Internal dogfood, closed beta or allowlist, a percentage ramp (1%, 5%, 25%, 50%, 100%) with a hold at each step, then general availability. |
| What is a kill switch? | A flag that disables the AI path in minutes, without a redeploy, and falls back to a safe state. Test it before launch. |
| Kill switch or rollback? | The kill switch stops the AI path for any incident. A rollback returns to the previous model, prompt or index and keeps the feature on. |
| What silent changes happen after launch? | Data drift (the world changes), concept drift (the right answer changes) and vendor drift (the model changes). Each needs its own monitor. |
| How do you handle a vendor model update? | Pin a dated version, run a regression eval on the new one, and set a go or no-go gate with quality, safety and cost thresholds. |
| How do you learn from users? | Design the loop: explicit, implicit and expert signals, triage with an owner, and a visible close. Use data only for purposes users agreed to. |
| Which consent rule matters most? | Default to the narrowest use. Do not train on prompts or uploads unless the user has clearly opted in. |
| Who owns the switch at 2 a.m.? *(Beyond the notes)* | A named person, with a written runbook that anyone on call can follow. |
| How do you use this in an interview? *(Beyond the notes)* | Name the rings, the gates, the kill criteria and the monitor. Say which version you pin and who decides on a rollback. |

> [!NOTE] Where this comes from
> The vault lists no outside sources for this chapter beyond general knowledge of AI feature launches and ML monitoring. Two of the vault's sources, the Sigma PM and Concept Book, have little on AI rollouts, so the chapter leans on public reporting of real launches. Its further-reading list names *AI Product Reading*, *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

Shipping an AI feature is the start of learning, not the end of building. Models, data, and user behaviour all change after launch, so the launch plan needs staged exposure, a fast off-switch, and monitoring that catches silent drift. This chapter also covers how to close the loop with user feedback while respecting consent.

The chapter has three sections:

- **10.1 Staged rollouts and kill switches.** Ramp exposure in gated steps, and keep a tested switch that turns the AI path off in minutes.
- **10.2 Monitoring drift and vendor model updates.** Watch input, outcome, and vendor-model changes, and treat a provider's model update as a release.
- **10.3 Feedback loops and consented data collection.** Design explicit and implicit feedback, and use data only for purposes users agreed to.

## Key takeaways

- Ramp AI features in gates (dogfood, allowlist, percentages) with quality, safety, and cost thresholds agreed in advance.
- Every AI feature needs a kill switch with a safe fallback, and the switch must be tested before launch.
- Pin model versions and run regression evals before any vendor model change reaches users.
- Monitor data drift, concept drift, and vendor drift separately, with alerts set against baselines.
- Collect feedback as a designed loop, and default to the narrowest consented use of user data.

> [!SIR] From the source notes
> Shipping an AI feature is the start of learning, not the end of building. Pin model versions before any vendor change reaches users.

## 10.1 Staged rollouts and kill switches

> An AI feature is never "shipped" to everyone at once; it is released in widening rings, with a switch that can turn it off in minutes.

### Concept

AI features fail in ways normal features do not. Output quality varies by input, costs scale with usage, and a model can behave differently on real traffic than on the eval set. A staged rollout limits the blast radius while you learn.

**Typical rollout ladder**

- **Internal dogfood:** employees and the PM team use it on real tasks.
- **Closed beta / allowlist:** a few hundred hand-picked users, often power users who will give candid feedback.
- **Percentage ramp:** 1% → 5% → 25% → 50% → 100%, with a hold at each step.
- **General availability:** default on, with the kill switch still wired in.

**Gates between steps** (write them down before starting)

- Quality: eval score and thumbs-down or edit rate within a threshold of the control.
- Guardrails: harmful-output rate, latency p95, and cost per task within budget (see Chapter 8.4, Guardrail metrics: harmful outputs, latency, cost).
- Business: task success or retention not regressing.

![The rollout ladder: each ring opens only when the gate passes, and the kill switch stays wired in.](diagrams/l7-rollout-ladder.svg)

**Kill switch**

- A feature flag or config value that disables the AI path in minutes, without a redeploy.
- It should fall back to a safe state: the old non-AI flow, a cached answer, or a "temporarily unavailable" message.
- Test the switch before launch. A kill switch nobody has flipped in staging is a hope, not a control.

![A kill switch stops the AI path; a rollback swaps the version and keeps the feature on.](diagrams/l7-kill-vs-rollback.svg)

**Things APMs often miss**

- Who owns the switch at 2 a.m., and is the runbook written?
- Rollback of the model is different from rollback of the prompt, the retrieval index, and the data pipeline. Version all four.
- Keep the control group running long enough to catch slow effects such as trust erosion or cost creep.
- **Shadow mode** before any user exposure: run the new model on live traffic, log its outputs, show users nothing, and compare with the current version.
- Ramp by risk, not only by percentage: start with low-stakes intents, languages with strong evals, or markets with lighter regulation, and hold back sensitive segments until data supports them.

### Real-world examples

- **Google AI Overviews:** tested for a year as the opt-in Search Generative Experience in Search Labs (from May 2023) before launching to US users in May 2024, then expanding country by country. Even so, viral errors after launch forced Google to narrow when overviews appear: staged rollouts reduce risk but do not remove it.
- **GitHub Copilot:** moved from a limited technical preview with waitlisted users to general availability in 2022, after the team had measured suggestion acceptance and safety filters on a larger base.
- **Meta:** uses an internal gating system (Gatekeeper) to turn features on for percentages or cohorts of users and to turn them off without a new release.
- **Microsoft Tay (March 2016):** a chatbot pulled offline within about 16 hours after users manipulated it into posting offensive messages. It is the textbook case of why a fast off-switch matters.
- **OpenAI GPT-4o update (April 2025):** a model update made the assistant overly flattering. OpenAI rolled the update back after user reports, which is a rollback of a model change in production.

### Practice questions

> [!INTERVIEW] You are launching an AI summarizer for a fintech app. Walk me through your rollout plan and the gate for each step.
> **Short answer outline (Q1):**
> - Dogfood, then allowlist, then 1% → 5% → 25% → 100%.
> - Gates: eval score vs control, thumbs-down or edit rate, harmful-output rate, latency, cost per task, and one business metric.
> - Pre-agree the kill criteria and the fallback experience.

> [!INTERVIEW] The AI feature's cost per task doubled after a ramp from 5% to 25%. What do you do in the next hour, and what do you do in the next week?
> **Short answer outline (Q2):**
> - Hour one: flip the flag or route to a cheaper model or cap usage; confirm the spend is contained.
> - Week one: find the cause (longer prompts, more retries, a model price change, heavier users) and decide whether to re-ramp with a cost gate.

> [!INTERVIEW] What is the difference between a kill switch and a rollback? When would you use each?
> **Short answer outline (Q3):**
> - Kill switch: turns the AI path off and falls back to a safe non-AI state, instantly, for any incident.
> - Rollback: returns to the previous version of the model, prompt, or index, keeping the feature on. Use it when the new version regressed and the old one was fine.

> [!INTERVIEW] How would you decide whether to keep a feature in the control group for three months?
> *(Beyond the notes: a starting point, not the vault's answer.)* Keep the control while the effects you are watching are slow, such as trust, retention or cost creep, and while the result still moves between weeks. Decide in advance how long the control runs, what result ends it, and who signs off. A control that never moves is a cost, so set a review date.

*Related:* Chapter 10.2 (Monitoring drift and vendor model updates), Chapter 10.3 (Feedback loops and consented data collection), Chapter 8.5 (Regression testing when models or prompts change), Chapter 8.4 (Guardrail metrics: harmful outputs, latency, cost), Chapter 18.2 (Pilots, MVPs, and phased rollouts).

## Beyond the notes: a gate sheet for the launch review

Write one row per gate before the first ring opens. The owner signs the row, and nobody widens a ring without a signed sheet.

| Gate | Metric to write down | Who signs it off |
|---|---|---|
| Quality | Eval score and thumbs-down or edit rate, against the control | Product and the eval owner |
| Safety | Harmful-output rate and over-refusal rate, on fixed sets | Trust and safety |
| Latency | p95 time to first token and total time | Engineering |
| Cost | Cost per successful task, against the budget | Finance partner and product |
| Business | Task success or retention, against the control | Product |

## Beyond the notes: a kill-switch drill

- Flip the flag in staging, and confirm the fallback screen renders for every entry point.
- Time how long the switch takes to take effect, and write the number in the runbook.
- Check that the logs show the switch was used, and who used it.
- Repeat the drill after each change to the fallback path.

## Beyond the notes: pitfalls

- **A kill switch that falls back to a broken screen.** The flag works, but the non-AI flow was never tested.
- **A rollback that restores the model but not the prompt.** The two were versioned separately, so the old behaviour does not come back.
- **Widening a ring after a cost spike, without a cost gate.** The spike returns at a larger scale.
- **Keeping the control group too short.** Slow effects such as trust erosion appear after the test has ended.

## Beyond the notes: interview corner

- **"How would you tell an incident apart from a regression?"** Starting point: an incident is a harm that needs the feature off now, so use the kill switch. A regression is a worse version than the one before, so roll back the version and keep the feature on.
- **"What do you put in a launch review?"** Starting point: the ring plan, the gate sheet, the kill criteria, the fallback, the owner of the switch and the monitors that will page someone.

## 10.2 Monitoring drift and vendor model updates

> An AI feature can get worse on Tuesday without a single line of your code changing, because the world or the model underneath it changed.

### Concept

There are three sources of silent change, and each needs its own monitor.

**1. Data drift (the world changes)**

- Input distribution shifts: new user segments, seasonality, a new app version that changes what users type or upload.
- Monitor input statistics such as length, language mix, topic clusters, and empty or malformed inputs.

**2. Concept drift (the right answer changes)**

- The meaning of a label moves: new fraud patterns, new policy rules, new product names.
- Monitor outcome metrics against a fresh labelled sample, not just against the old eval set.

**3. Vendor or model drift (the model changes)**

- The provider updates a model alias, retrains, or changes safety tuning. Your prompt that worked last month now behaves differently.
- Pin dated model versions where the API allows it; a floating alias (such as a "latest" name) can change underneath you. Track the provider's deprecation and changelog notices as product events, and budget for a forced migration each year.
- Run your golden eval set against each new candidate version before you switch traffic (see Chapter 8.5, Regression testing when models or prompts change).

![Three kinds of silent change, each with the monitor that would catch it.](diagrams/l7-drift-types.svg)

![A vendor model update treated as a release: pin, test, gate, tell people, then switch.](diagrams/l7-vendor-playbook.svg)

**What to put on the dashboard**

- Quality proxies: thumbs-down rate, edit or regenerate rate, escalation to human rate.
- Input health: token length distribution, language share, retrieval hit rate for RAG.
- Cost and latency per model version, so a silent switch to a bigger model shows up.
- Alert thresholds set on change from a baseline, not on fixed absolute numbers alone.

![The first monitoring dashboard: four panels, each one answering a different question.](diagrams/l7-dashboard.svg)

**Ownership**

- Name who gets paged when quality drops and who decides between "retune the prompt", "switch model", and "roll back". Without this, drift becomes a debate.

### Real-world examples

- **OpenAI GPT-4o sycophancy rollback (April 2025):** an update changed the assistant's personality in a way that users noticed quickly through feedback. The rollback shows why behavioural monitoring matters even when the model is a vendor's.
- **Google AI Overviews (May 2024):** launched broadly, then drew viral errors (for example, odd pizza advice) that forced Google to scale back and tune the feature. Real-traffic monitoring caught what the pre-launch evals had not.
- **Zillow Offers (2021):** the home-pricing algorithm failed when the housing market moved faster than the model's training data, leading to large losses and the shutdown of the business. A clear case of concept drift with high financial cost. (Widely reported.)
- **Instacart during COVID-19 (2020):** panic buying broke the item-availability model trained on normal shopping patterns; Instacart reported its accuracy dropped sharply and retrained on more recent data. Data drift from a sudden shift in the world.

### Practice questions

> [!INTERVIEW] Users say your AI assistant "feels worse" this week, but your eval score is flat. How do you investigate?
> **Short answer outline (Q1):**
> - Check whether the change is in user behaviour (input drift), in the vendor version, or in your own release.
> - Compare the feedback and edit metrics by segment and app version; sample and read conversations.
> - Re-run the golden set on the current pinned version and on the latest, to separate model change from data change.

> [!INTERVIEW] Your LLM provider announces that an alias will point to a new model next month. What do you do as the PM?
> **Short answer outline (Q2):**
> - Pin the current version, schedule a regression run on the new one, and set a go or no-go gate with quality, safety, and cost thresholds.
> - Communicate the timeline to support and sales before the switch.

> [!INTERVIEW] How would you tell data drift from concept drift in a support-ticket classifier?
> **Short answer outline (Q3):**
> - Data drift: input statistics change (new ticket topics, a new product name, more Hindi tickets) while the old labels are still correct; accuracy drops mainly on the new inputs.
> - Concept drift: inputs look the same but the right label changes (a policy change makes the same ticket a different category); accuracy drops on a freshly labelled sample of familiar inputs.

> [!INTERVIEW] Which three metrics would you put on the first monitoring dashboard for a RAG-based help assistant, and why?
> *(Beyond the notes: a starting point, not the vault's answer.)* Thumbs-down rate, because it is the fastest user signal of a bad answer. Retrieval hit rate, because an answer with no retrieved source is where hallucinations start. Cost and latency per model version, because a silent switch to a bigger model shows up there first.

*Related:* Chapter 10.1 (Staged rollouts and kill switches), Chapter 10.3 (Feedback loops and consented data collection), Chapter 16.4 (AI-specific RCA: model changes, prompt regressions, data drift, cost spikes), Chapter 8.3 (Online metrics: task success, acceptance and edit rate, retention of AI users), Chapter 4.3 (Quality as a distribution, not a bug count).

## Beyond the notes: a baseline for every alert

- Take the baseline from a window before the change you are watching, not from the last hour.
- Compare the same weekday or the same period a year earlier when you have it, so seasonality does not look like drift.
- Record the baseline value next to the alert, so the on-call person can see how far the number moved.
- Re-set the baseline after an intended change, and say so in the release notes.

## Beyond the notes: pitfalls

- **Watching only the eval score.** A flat eval score can hide a segment that is getting worse, so check the dashboard by segment.
- **Pinning a model and forgetting its end date.** The provider's deprecation notice becomes a forced migration at a bad time.
- **Alerting on fixed numbers.** A threshold that suits last quarter can fire every day, or never.
- **Changing the prompt without versioning it.** The rollback then has nothing to return to.

## Beyond the notes: interview corner

- **"How do you know a vendor update is safe?"** Starting point: the golden set, the safety sets and the cost per task on the candidate version, against the same gate you used for the last change. Nothing reaches users until the gate passes.
- **"What is the first thing you check when quality drops?"** Starting point: whether anything changed in the release, the model version or the input mix, in that order.

## 10.3 Feedback loops and consented data collection

> Users' feedback is the cheapest training and evaluation data you have, but you may only use it in ways they agreed to.

### Concept

A feedback loop turns everyday use into improvement: users react, the team learns, the product changes, and users react again. For AI products, the loop has to be designed on purpose.

**Types of feedback signal**

- **Explicit:** thumbs up or down, "report a problem", star ratings, corrections typed by the user.
- **Implicit:** edits to an AI draft, copy or accept actions, regenerate clicks, abandonment, escalation to a human.
- **Expert:** labels from trained reviewers on sampled outputs (covered in Chapter 8.2, Human evaluation and labeling).

Implicit signals are abundant but noisy. Explicit signals are sparse but clear. Use both, and check that they agree.

![The loop: react, collect the signals, triage with an owner, change the product, and close the loop.](diagrams/l7-feedback-loop.svg)

**Designing the loop**

- Make feedback one tap, placed right after the output, with an optional reason list.
- Close the loop visibly where you can ("we fixed this in the last update"), so users keep giving feedback.
- Route feedback into a triage queue with an owner and a time to respond.

**Consented data collection**

- Separate three uses and ask for consent for each: (a) improving the product for this user, (b) evaluation and analytics, (c) training or fine-tuning models.
- Default to the narrowest use. Do not train on prompts or uploads unless the user has clearly opted in.
- Honour deletion and withdrawal of consent, and check that retention rules apply to derived data such as embeddings and logs.
- In India, the Digital Personal Data Protection Act, 2023 requires clear notice and consent for processing personal data, with rights to withdraw and to erasure (see Chapter 9.2, Privacy, consent, and data retention).

![Three uses, three consents: the narrowest use is the default, and training needs a clear opt-in.](diagrams/l7-consent-uses.svg)

**Pitfalls**

- Feedback bias: heavy users and angry users over-represent. Weight by segment.
- Feedback as ground truth: a thumbs-down may mean "I did not like the tone", not "the answer was wrong".
- Data flywheel myths: more data helps only if the data is representative and labelled well (see Chapter 4.2, Data as a product input and data flywheels).

### Real-world examples

- **ChatGPT thumbs up and down with optional text:** a simple explicit loop attached to every response. Consumer users can opt out of their chats being used for training; OpenAI says business and API data is not used for training by default.
- **LinkedIn (September 2024):** LinkedIn began using member data to train generative AI by default, with an opt-out setting, and excluded the EU, EEA, Switzerland, and the UK. The backlash shows the trust cost of opt-out training, and how consent rules differ by market.
- **Grammarly:** uses accept and dismiss actions on suggestions as implicit feedback to tune which corrections appear.
- **Spotify:** users' skips and likes shape recommendations, a long-running implicit loop built on listening data users accepted through the product's terms.

### Practice questions

> [!INTERVIEW] Design the feedback loop for an AI tool that drafts customer-support replies. What do you collect, and what do you not collect?
> **Short answer outline (Q1):**
> - Collect: whether the agent sent the draft as is, edited it (store the diff), or discarded it; time to send; a one-tap reason on discard; customer satisfaction on the ticket.
> - Do not collect: full customer PII in training sets (redact first), or anything outside the support purpose stated in the notice.

> [!INTERVIEW] Your team wants to fine-tune on support chats to improve the model. What questions do you ask before saying yes?
> **Short answer outline (Q2):**
> - Purpose and lawful basis: is it consented, and is it the narrowest use that works?
> - Data: PII redaction, retention limits, deletion path, and whether derived artefacts are covered.
> - Value: would synthetic data or opt-in samples give most of the gain at lower risk?
> - Measurement: how will you prove the fine-tune helped, against a held-out set and a regression suite?

> [!INTERVIEW] Thumbs-down rate went up after you added a new tone setting. What could be happening, and what do you check first?
> *(Beyond the notes: a starting point, not the vault's answer.)* The new tone may suit some users and not others, so the thumbs-down comes from one segment. Check first which segment and which tone setting the thumbs-downs come from, then read a sample of the rated replies. Compare with the feedback reasons, and only then decide whether the change is a fault.

> [!INTERVIEW] How would you tell an enterprise customer that their data will not train the model, and how would you prove it?
> *(Beyond the notes: a starting point.)* State the rule in one plain sentence in the contract and the product settings, and name the data that is covered. To prove it, show the setting and the audit log of the training pipeline's inputs, and let the customer's security team review the data-processing terms. Check the wording with counsel.

*Related:* Chapter 10.1 (Staged rollouts and kill switches), Chapter 10.2 (Monitoring drift and vendor model updates), Chapter 8.2 (Human evaluation and labeling), Chapter 9.2 (Privacy, consent, and data retention), Chapter 7.2 (User control, transparency, and confidence signals).

## Beyond the notes: a feedback reason list

A short list keeps the one-tap reason useful. Keep it to a handful of options:

- Wrong facts
- Wrong tone for this user
- Missing information
- Too long or too short
- Not what I asked

## Beyond the notes: pitfalls in the loop

- **Reading a rise in thumbs-down as a fall in quality.** The rate can rise when more people bother to answer, so check the count as well as the share.
- **Fine-tuning on feedback you never validated.** Sample the signals and read them before they become training data.
- **Asking for consent once for everything.** Each use gets its own answer.

## Beyond the notes: interview corner

- **"How do you collect feedback without annoying users?"** Starting point: implicit signals first, one tap on the output, and an explicit prompt only on a small sample or after a clear negative event.
- **"Is user feedback a moat?"** Starting point: it is only a moat if the signal is specific, labelled and fed back into the product under consent (see Chapter 4.2).

## Revision cheat-sheet

![Chapter 10 on one page: three areas, each with the question it answers.](diagrams/l7-big-picture.svg)

- **10.1 Rollouts and kill switches:** dogfood, allowlist, 1% → 5% → 25% → 50% → 100%, then general availability, with a hold at each step. Gates: quality, guardrails and business. The kill switch falls back to a safe state and must be tested before launch. Rollback returns to a previous version and keeps the feature on. Shadow mode shows users nothing.
- **10.2 Drift and vendor updates:** data drift (monitor inputs), concept drift (monitor outcomes against a fresh labelled sample), vendor drift (pin dated versions, run the golden set on each candidate). Dashboard: quality proxies, input health, cost and latency per version, and ownership. Alert on change from a baseline.
- **10.3 Feedback and consent:** explicit, implicit and expert signals. Use both explicit and implicit, and check they agree. Three uses, three consents. Default to the narrowest use, and never train on prompts or uploads without a clear opt-in.
- **Beyond the notes:** a gate sheet with owners, a kill-switch drill, a baseline for every alert, and a feedback reason list.

## Self-test

<details class="quiz"><summary>Why is shipping an AI feature the start of learning, not the end of building?

Models, data and user behaviour all change after launch. The plan needs staged exposure, a fast off-switch and monitoring that catches silent drift.

</details>

<details class="quiz"><summary>What are the steps of the typical rollout ladder?

Internal dogfood, then a closed beta or allowlist, then a percentage ramp (1%, 5%, 25%, 50%, 100%) with a hold at each step, then general availability with the kill switch still wired in.

</details>

<details class="quiz"><summary>What are the three gates between rollout steps?

Quality (eval score and thumbs-down or edit rate against the control), guardrails (harmful-output rate, p95 latency and cost per task within budget), and business (task success or retention not regressing). Write them down before starting.

</details>

<details class="quiz"><summary>What is a kill switch, and what must it fall back to?

A feature flag or config value that disables the AI path in minutes, without a redeploy. It falls back to a safe state: the old non-AI flow, a cached answer, or a temporarily unavailable message.

</details>

<details class="quiz"><summary>(Beyond the notes) What does a kill-switch drill look like?

Flip the flag in staging, confirm the fallback renders for every entry point, time how long the switch takes to take effect, and record the result in the runbook.

</details>

<details class="quiz"><summary>What is the difference between a kill switch and a rollback?

The kill switch turns the AI path off and falls back to a safe non-AI state, for any incident. A rollback returns to the previous model, prompt or index and keeps the feature on, for when the new version regressed and the old one was fine.

</details>

<details class="quiz"><summary>Name the three sources of silent change and the monitor each one needs.

Data drift (the world changes): monitor input statistics. Concept drift (the right answer changes): monitor outcomes against a fresh labelled sample. Vendor drift (the model changes): run the golden eval on each new version and track cost and latency per version.

</details>

<details class="quiz"><summary>Why pin a dated model version rather than a floating alias?

A floating alias can change underneath you, so a prompt that worked last month can behave differently. A pinned version changes only when you move to it, after a regression run and a go or no-go gate.

</details>

<details class="quiz"><summary>What are the three types of feedback signal, and how do they differ?

Explicit signals (thumbs, reports, star ratings, typed corrections) are sparse but clear. Implicit signals (edits, copy or accept, regenerate, abandonment, escalation) are abundant but noisy. Expert labels come from trained reviewers on sampled outputs.

</details>

<details class="quiz"><summary>Name the three separate uses that each need their own consent.

Improving the product for this user, evaluation and analytics, and training or fine-tuning models. Default to the narrowest use, and do not train on prompts or uploads unless the user has clearly opted in.

</details>

<details class="quiz"><summary>(Beyond the notes) Why should a thumbs-down be treated as a signal rather than a verdict?

A thumbs-down may mean the user disliked the tone, not that the answer was wrong. Heavy and angry users also over-represent in feedback, so read a sample and weight by segment before you act.

</details>

<details class="quiz"><summary>(Beyond the notes) Why keep a control group running for a long time?

Slow effects, such as trust erosion or cost creep, appear after a short test has ended. Decide in advance how long the control runs, what result ends it, and who signs off.

</details>


# Chapter 11 · Understanding Users

<!-- lecture n="8" label="11" short="Understanding users" status="done" kind="users" -->

## At a glance

| Question | Short answer |
|---|---|
| Who do you design for? | **One primary persona**. Say who is secondary and who is negative, so the scope is clear. |
| What is a persona? | A fictional but research-grounded picture of one segment: goals, motivations, attitudes, behaviours, pain points. |
| What is a job to be done? | The **progress** a user wants in a situation. Your product competes with whatever they would do otherwise. |
| What is the JTBD format? | "When [situation], I want to [motivation], so I can [expected outcome]." |
| How do you map the experience? | A **user journey** stage by stage, checked against the **5Es**: Entice, Enter, Engage, Exit, Extend. |
| How do you pick what to fix? | List pain points for one persona along the journey, rate each **High, Moderate or Low**, and pick **1 to 3**. |
| What is the most common trap? | A strong persona that changes halfway through the answer. Stay with one segment to the end. |
| What is a weak persona? | A usage bucket such as "heavy, normal, low users". Interviewers expect richness tied to behaviour. |
| How do you use this in an interview? *(Beyond the notes)* | Name the persona in one sentence, state the job, point to the journey stage, then name the top pain. |
| What evidence backs a persona? *(Beyond the notes)* | Research where you have it. Without research, a proto-persona, labelled as an assumption. |

> [!NOTE] Where this comes from
> Sources named in the vault: *Sigma PM Concept Book, Part A (2023)*, *Sigma PM Casebook (2023-2024), Part B*, and *Decode and Conquer* by Lewis C. Lin. The milkshake study is from Clayton Christensen's *Competing Against Luck*. Further reading: *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

Every product answer starts with the user. This chapter covers how to segment users into personas, how to frame their needs as jobs-to-be-done, how to map their journey, and how to rank the pain points you find.

The chapter has four sections, each one feeding the next:

- **11.1 Segmentation and personas.** Pick one primary persona, and say who is secondary or negative.
- **11.2 Jobs-to-be-done.** State the progress the user wants, and the alternatives they already use.
- **11.3 User journeys and the 5Es.** Map the stages of the journey and check them against five lenses.
- **11.4 Identifying and prioritizing pain points.** List pain points, rate them High, Moderate or Low, and pick 1 to 3.

## Key takeaways

- Design for one persona; say who the negative persona is so the scope is clear.
- Frame needs as jobs-to-be-done, and remember the alternative the user already has.
- Map the journey before you list features; the problem often sits at one stage.
- Rate pain points by severity and reach, and state the reason for each rating.
- Keep the same persona from the first pain point to the final solution.

> [!SIR] From the source notes
> Design for one persona; say who the negative persona is so the scope is clear.

## 11.1 Segmentation and personas

> You cannot design for "everyone"; segment the market, then pick one persona and design for them.

### Concept

- **Segmentation** splits a broad user base into groups that share needs, behaviours or value. Common bases: demographics, usage intensity, goals, context (home, commute, work).
- **Persona** is a fictional but research-grounded representation of one segment: goals, motivations, attitudes, behaviours, pain points.
- **Primary, secondary, negative persona** (used in product improvement answers):
  - *Primary*: the person you design for first. Highest value or largest unmet need.
  - *Secondary*: served if it costs little extra; you accept that they may need convincing.
  - *Negative*: the person you explicitly will not focus on. Naming them shows scope discipline.
- **Proto-persona**: used in interviews and app critiques when you have no research. Organise it as Goals, Motivation, Attitudes, Behaviours. Say clearly that it is an assumption.
- **Choosing a persona**: weigh total addressable market against the extent of unmet need. Explain the choice in one sentence.
- **Common trap**: a strong persona that changes halfway through the answer. Stay with one segment from first pain point to final solution.
- **Weak answer**: a "persona" that is just a usage bucket ("heavy, normal, low users"). Interviewers expect demographic or psychographic richness tied to behaviour.

Quick structure for a persona in an answer: name, one-line description, behaviour, needs and goals, pain points. A 2x2 or small table makes it easy to follow.

![From the whole user base to one primary persona: segment first, then pick the roles.](diagrams/l8-segmentation-funnel.svg)

![A persona card has five parts; each persona gets a role: primary, secondary or negative.](diagrams/l8-persona-card.svg)

### Real-world examples

- **Airbnb**: separates guests (search, trust, price) from hosts (listing, pricing, payouts). The two segments often need different features even on the same platform.
- **Swiggy / Zomato**: diners, restaurant partners and delivery partners are distinct personas with different pain points, and the product trade-offs follow from that split.
- **Duolingo**: casual learners and committed language learners respond to different motivators (streaks versus progress depth). (illustrative of persona-driven feature choices)
- **Nykaa**: beauty buyers in metro cities and in smaller towns have different discovery and delivery needs. (illustrative)

### Practice questions

> [!INTERVIEW] Design a feature for a fitness app. Who is your primary persona and why?
> **Answer outline (Q1):** Segment by goal and frequency (for example, weight-loss beginners, strength-trainers, time-poor professionals). Pick the segment with the most unmet need and a clear willingness to pay. Write goals, behaviour and pain points, then design only for that persona.

> [!INTERVIEW] Your product serves both small shop owners and large retail chains. How do you segment, and which segment do you pick first?
> **Answer outline (Q2):** Segment by business size, volume, and tech maturity. Choose small shop owners if the TAM is large and current tools fail them. Justify with a size and pain comparison, and note that the chain segment can come later with a different product tier.

> [!INTERVIEW] Name a negative persona for a new budgeting app and justify leaving them out.
> *(Beyond the notes: a starting point, not the vault's answer.)* A good negative persona is someone with a real need that the app will not serve in this release, such as a small business owner who needs invoicing. Say why the core job is a poor fit for them, and what you would tell them.

> [!INTERVIEW] How would you build a proto-persona for an app critique when you have no user research?
> *(Beyond the notes: a starting point.)* Write the Goals, Motivation, Attitudes and Behaviours from the app's own evidence (reviews, the store listing, what the app asks users to do) and label the whole card as an assumption. Then test the card with the first few real users you can reach.

*Related:* Chapter 11 (11.2 Jobs-to-be-done, 11.4 Identifying and prioritizing pain points), Chapter 12 (CIRCLES), Chapter 13 (Five-step critique).

## 11.2 Jobs-to-be-done

> Users "hire" products to make progress in a situation; the product's competition is whatever they would do otherwise.

### Concept

- **Jobs-to-be-done (JTBD)** frames a user need as the progress a person wants to make in a specific context, not as a demographic or a feature wish.
- Format: "When [situation], I want to [motivation], so I can [expected outcome]."
- Core questions used in an app critique (from the Sigma casebook):
  - What is the customer trying to accomplish?
  - If the app did not exist, what would the customer do?
  - Is the alternative better or worse than the app? Why?
- **Why it helps in interviews**: JTBD gives objective criteria for judging a design. It also surfaces alternatives you might have missed (for example, a notes app competing with a pen and paper, or with a WhatsApp chat to self).
- **Relation to personas**: JTBD says *what job*; personas say *who is hiring* and *in what mood*. Use JTBD first to anchor the objective, then add persona detail.
- **Limit**: JTBD can be too abstract. Once the job is clear, move to flows and UI. The job "is different depending on context", so state the context.

Steps to apply:

1. Name the situation (when does the need arise?).
2. Name the job (what progress is sought?).
3. List current alternatives and their pains.
4. Judge the product against those alternatives.

![The JTBD format, the four steps, and the milkshake story in one row.](diagrams/l8-jtbd.svg)

### Real-world examples

- **Milkshake study** (Clayton Christensen, *Competing Against Luck*): a fast-food chain found many milkshakes were bought before 8 am by solo commuters who "hired" a thick shake to keep them full and make a long drive less boring. The competition was bagels, bananas and boredom, not other shakes, so the fix was a thicker shake and faster purchase, not new flavours.
- **Google Maps**: the job is "get me there on time with less uncertainty", which is why live traffic and ETA matter more than the map itself.
- **Splitwise**: the job is "keep shared expenses fair without awkward money conversations", competing with spreadsheets, mental tallies and "I'll pay next time".
- **PhonePe / Google Pay on UPI**: the job "pay a shop or a friend in seconds without carrying change" competes with cash, so the criteria are speed, payment success rate and trust that the money arrived.

### Practice questions

> [!INTERVIEW] Write the JTBD statement for a user who opens a food delivery app at 11 pm.
> **Answer outline (Q1):** Situation: late night, hungry, low energy, limited options in the area. Job: get a satisfying meal delivered quickly with no decision fatigue. Alternatives: cook (effort), call a restaurant (friction), go out (too much effort). Criteria: time to decision, delivery speed, reliability.

> [!INTERVIEW] A user says they want "more filters" on a shopping app. What is the underlying job?
> *(Beyond the notes: a starting point.)* Ask what the user is trying to find and how they will know they found it. "More filters" is usually a wish for a faster route to a short list. Test that with the user's current steps before you design any filter.

> [!INTERVIEW] How would you use JTBD to critique a banking app?
> **Answer outline (Q3):** Core jobs: check balance and pay bills, move money safely, get a quick answer on a failed transaction. For each job, compare with branch visits, calling support, and other apps. Judge on speed, trust, and clarity of error messages.

> [!INTERVIEW] What is the alternative (the "non-app" option) for a note-taking app, and how does it change your critique?
> *(Beyond the notes: a starting point.)* The non-app options include paper, a notebook, a message to yourself, or a document in a shared folder. Each one sets a bar the app must beat on the job: capture speed, finding a note later, and trust that nothing is lost. The critique then asks where the app is better and where it is only more complicated.

*Related:* Chapter 11 (11.1 Segmentation and personas, 11.3 User journeys and the 5Es, 11.4 Identifying and prioritizing pain points), Chapter 13 (Five-step critique).

## 11.3 User journeys and the 5Es

> Map the journey stage by stage, and check each stage against five lenses (the 5Es) to find where the product helps or fails.

### Concept

- **User journey map**: a sequence of stages a user goes through to reach an outcome (for example, discover, sign up, first use, repeat use, advocate). For each stage, note the user's actions, thoughts, emotions, pain points, and touchpoints.
- **Why it matters**: the journey shows *where* in the flow a problem sits, which is the first step of any root-cause or improvement answer.
- **The 5Es** (a journey framework originally from Conifer Research; the Sigma casebook recommends it for building the user journey in design answers):
  1. **Entice**: what gets the user to start? Awareness, first impression, reason to try.
  2. **Enter**: how easy is onboarding and sign-up? Friction, permissions, time to first value.
  3. **Engage**: is the core experience rewarding? Does the user get value in the main task?
  4. **Exit**: how do users leave or finish a task? Checkout, logout, cancelling, handoff to another channel.
  5. **Extend**: do users come back and bring others? Retention, sharing, referrals, community.
- **How to use it in an answer**: pick one persona (see 11.1), map 4 to 6 stages, mark the pain at each stage, then point to the lens where the biggest gap is.
- **Common mistake**: mapping every possible stage. The Sigma casebook warns that not every stage applies to every question: "Don't forcefit!" Include stages that happen *outside* the product (for example, deciding to order food before opening the app).

**Mini-example (Kindle reader who drops off mid-book):** Entice = sees a recommendation; Enter = searches and buys or borrows; Engage = reads, tracks progress, looks up meanings; Exit = stops reading (the problem stage); Extend = shares reviews and ratings. The pain sits at Engage/Exit, so solutions target re-engagement (progress nudges, chapter summaries), not discovery.

![The 5Es as five stages, with the Kindle example mapped under them.](diagrams/l8-5es-journey.svg)

### Real-world examples

- **Uber rider journey**: entice (needs a ride, sees upfront fare), enter (sets pickup and requests), engage (match, track driver, ride), exit (pay and rate), extend (saved places, referral credit). Uber's upfront pricing and live driver tracking target pain at the engage stage (uncertain ETA) and exit stage (fare surprises).
- **Flipkart checkout**: exit friction (address re-entry, payment failures) is a common place where journey analysis drives improvement. (illustrative)
- **Duolingo**: enter is a short goal-setting and optional placement test before sign-up, so users get value before creating an account; extend uses streaks, leagues and friend features to bring users back.

### Practice questions

> [!INTERVIEW] Map the journey for a first-time user of a ride-booking app. Where is the biggest drop-off likely?
> *(Beyond the notes: a starting point.)* Walk the five stages in order: the ad or referral that starts the trip (entice), the sign-up and first booking (enter), the match and the ride (engage), payment and rating (exit), and the return trip or referral (extend). Name the stage where you expect most users to leave, and say what evidence would confirm it.

> [!INTERVIEW] Apply the 5Es to a food delivery app. Which E would you fix first, and why?
> *(Beyond the notes: a starting point.)* Pick the stage with the largest measurable gap and the highest value at stake. For most food apps that is Enter or Exit, because a slow sign-up or a failed payment loses an order that was already decided. Say which metric would show the gap.

> [!INTERVIEW] Users sign up but never return. Which of the 5Es do you investigate first?
> **Answer outline (Q3):** Start with Engage (did the first session deliver value?), then Enter (was onboarding long or confusing?). Check whether the first-use outcome matched the promise from Entice. Retention problems usually show up as a weak Engage stage.

*Related:* Chapter 11 (11.2 Jobs-to-be-done, 11.4 Identifying and prioritizing pain points), Chapter 16 (Walking the user journey), Chapter 13 (Five-step critique).

## 11.4 Identifying and prioritizing pain points

> List pain points for one persona along the journey, then rank them by severity so you pick the 1 to 3 that matter most.

### Concept

**Five-step process** (condensed from steps 3 to 6 of the Sigma concept book's product design walkthrough):

1. **Pick the target segment.** Use one persona. Do not drift from it later in the answer.
2. **Map the journey.** Follow the user from opening the app to finishing the task. At each stage, note how the customer feels.
3. **List pain points.** Mark which parts are painful at each stage, and what the app is missing (unmet needs). Check what direct competitors offer that this app does not.
4. **Prioritize.** The list is usually too long to address. Rate each pain point on the probable severity and how badly it hurts the journey:
   - **High**: blocks the core task or causes loss (money, data, trust), and affects many users.
   - **Moderate**: slows the task or causes frustration, but the user can work around it.
   - **Low**: cosmetic or rare; note it but do not build for it.

   Choose 1 to 3 pain points, typically the High ones.
5. **Solve the chosen ones.** Move to solutions only for the prioritized list (see Chapter 12, CIRCLES).

**Rules to remember**

- Stay inside the chosen persona. Solutions must suit that persona.
- Keep the pain point list tied to the journey, so the prioritization is visibly grounded.
- Severity is a judgement, so state the reason for each rating in one line. Interviewers reward reasoning more than the label.

**Alternative ranking lenses**: how acute the problem is (depth) versus how many users have it (breadth); the Sigma casebook also lists reach, revenue, impact, cost, effort and complexity as valid reasons. For features (not pain points), Lewis Lin's CIRCLES uses customer value versus effort.

**Mini-example (grocery app, persona = working parent ordering weekly):** "Items substituted without asking" = High (breaks the core job, trust loss, frequent); "slot not available at night" = High (blocks the order); "search misses regional names like 'bhindi'" = Moderate (workaround: browse); "app icon looks dated" = Low. Pick the two Highs and say why.

![The five steps, each with the question it answers, and the grocery example below.](diagrams/l8-pain-steps.svg)

![Severity against reach. The red cell is the first pick; the yellow cell is the exception.](diagrams/l8-pain-grid.svg)

### Real-world examples

- **UPI payment apps (illustrative ranking)**: for a shopper, "money debited but payment failed" is High (money and trust at stake), while "app takes 3 seconds to open" is Moderate. RBI's turnaround-time rules (2019) require failed UPI debits to be auto-reversed by T+1, with compensation for delays, which shows how severe regulators judge this pain.
- **Spotify (Sigma concept book walkthrough)**: improving engagement for Spotify, the book narrows to one persona, lists pain points along the journey, ranks them High/Moderate/Low, and only then lists features, choosing a live-room (social listening) feature. The book notes the example is for illustration.
- **Google Docs offline mode**: offline editing exists because "I lose access to my document when the connection drops" is a High pain point for travellers and users on patchy networks; it blocks the core task outright.

### Practice questions

> [!INTERVIEW] You list 9 pain points for a grocery delivery app's user. How do you pick the top 2?
> **Answer outline (Q1):** Rate each pain point on severity (blocks the order or loses money?) and reach (how many of this persona hit it?). Choose the top two with High severity and at least moderate reach. Explain the trade-off you left out.

> [!INTERVIEW] How would you tell High from Moderate severity without data?
> *(Beyond the notes: a starting point.)* Ask whether the problem stops the core task or only slows it, and whether it costs money, data or trust. If it stops the task or costs one of those, it is High. If the user can finish with a workaround, it is Moderate. Write the reason in one line either way.

> [!INTERVIEW] A pain point affects few users but is very severe. Do you prioritize it? Why or why not?
> **Answer outline (Q3):** Yes if the severity is high enough to cause churn or harm, since rare but severe failures (lost money, safety) can outrank common annoyances. Otherwise defer. Tie the decision back to the persona and the business goal.

> [!INTERVIEW] Walk through your pain point list for a commuter app in under two minutes.
> *(Beyond the notes: a starting point.)* Say the persona in one line, then read the High items in journey order, each with its reason. End with the one you will solve and the metric it moves. Leave the Moderate items for a single sentence.

*Related:* Chapter 11 (11.1 Segmentation and personas, 11.3 User journeys and the 5Es), Chapter 14 (Choosing and defending a framework), Chapter 12 (CIRCLES).

## Beyond the notes: the persona card in one breath

When you present a persona in an interview, say it in one breath before you draw anything:

- **Who:** one line, a working description, not a demographic list.
- **Does what:** the behaviour that matters for this product, and when.
- **Needs:** the progress they want, in the job's words.
- **Hurts:** the one or two pains that the rest of the answer will address.

Then say the roles in one sentence: "Primary is X. Secondary is Y, served if it costs little. Negative is Z, because the core job does not fit them."

## Beyond the notes: from pain point to a defensible list

A short checklist that keeps the prioritization honest:

- Write each pain point as a sentence about the persona's job, not as a feature wish.
- Mark the journey stage next to each pain point, so the list is visibly tied to the path.
- Give each rating one reason in a few words: "blocks the order", "workaround exists", "rare, cosmetic".
- Keep the top two or three. Say what you left out and why.
- Check the chosen pain against the persona again before you move to solutions. This is where most answers drift.

## Beyond the notes: where a persona comes from

Interviews usually ask for personas without research. Still, a few well-known sources make a persona stronger than a guess:

- **Support tickets and app store reviews** show the language users use for their pains.
- **Usage data** shows how often the behaviour happens, which helps you separate High from Moderate.
- **Five or six short user conversations** test whether the persona card matches a real person.

Label any persona that does not come from these as an assumption, as the vault suggests for proto-personas.

## Beyond the notes: pitfalls

- **The usage bucket disguised as a persona.** "Power users" and "casual users" are a split, not a person. Add the goal and the context.
- **Two personas in one answer.** Interviewers see the switch. If the second persona matters, make it the secondary and say so.
- **A journey with every stage.** Map 4 to 6 stages that matter for the question.
- **JTBD as a feature list.** A job is a progress statement, not a button.
- **Ranking without reach.** A severe pain that only one person in a thousand hits is a different decision from one that most of the persona hits.

## Beyond the notes: interview corner

- **"Who is your primary user?"** Give one persona, the job, and the reason you picked them over the secondary: the size of the need, or the lack of a good alternative.
- **"What would the user do without your product?"** Name the real alternative first, then say whether your product is better, worse, or only faster on that alternative.
- **"Which pain would you fix first?"** Name the High pain, its stage on the journey, the persona it blocks, and the metric that will show it fixed.

## Revision cheat-sheet

![Chapter 11 on one page: four tools, each answering one question about the user.](diagrams/l8-big-picture.svg)

- **11.1** Segment the market, then pick **one primary persona**. Name a **secondary** (served if cheap) and a **negative** (out of scope on purpose). Weak personas are usage buckets.
- **11.2** A job is the **progress** a user wants in a **situation**. Use "When [situation], I want to [motivation], so I can [outcome]." Name the **alternative** the user already has.
- **11.3** Map the **journey** and check it with the **5Es**: Entice, Enter, Engage, Exit, Extend. Find the stage where the pain sits. Do not forcefit every stage.
- **11.4** Five steps: pick the segment, map the journey, list pain points, prioritize (High, Moderate, Low), solve the chosen 1 to 3. State the reason for each rating.
- **Beyond the notes:** lead with the persona in one breath, check the top pain against the persona again before solutions, and label proto-personas as assumptions.

## Self-test

<details class="quiz"><summary>Why should an answer name a negative persona?

It shows scope discipline: you state who you will not focus on, so the boundary of the answer is clear.

</details>

<details class="quiz"><summary>What is the difference between a persona and a usage bucket?

A persona is a research-grounded representation of one segment, with goals, motivations, attitudes, behaviours and pain points. A usage bucket such as "heavy, normal, low users" is too thin for a design answer.

</details>

<details class="quiz"><summary>What is the JTBD format?

"When [situation], I want to [motivation], so I can [expected outcome]."

</details>

<details class="quiz"><summary>In the milkshake study, why was the fix a thicker shake and faster purchase rather than new flavours?

Because the competition was bagels, bananas and boredom, not other shakes. The job was to stay full on a long commute, so the fix served that job.

</details>

<details class="quiz"><summary>Name the five Es of the user journey.

Entice (what gets the user to start), Enter (onboarding and sign-up), Engage (the core experience), Exit (how users leave or finish), and Extend (retention, sharing and referrals).

</details>

<details class="quiz"><summary>Why does the Kindle example place the pain at Engage and Exit?

The reader starts the book (Entice and Enter are fine) but stops mid-book. The problem is in the core reading experience and in the exit from it, so solutions target re-engagement.

</details>

<details class="quiz"><summary>What does the Sigma casebook warn about when mapping a journey?

Mapping every possible stage. It says "Don't forcefit!": include only the stages that matter for the question, and include stages that happen outside the product.

</details>

<details class="quiz"><summary>What are the three severity ratings for pain points, and what does High mean?

High, Moderate and Low. High blocks the core task or causes loss of money, data or trust, and affects many users. Moderate slows the task but can be worked around. Low is cosmetic or rare.

</details>

<details class="quiz"><summary>How many pain points should you choose to address, and what is the rule for the reason?

One to three, typically the High ones. State the reason for each rating in one line, because the reasoning is what interviewers reward.

</details>

<details class="quiz"><summary>(Beyond the notes) What makes a good negative persona?

Someone with a real need that this release will not serve, with a reason the core job does not fit them. Naming them is a deliberate scope choice, not an oversight.

</details>

<details class="quiz"><summary>(Beyond the notes) Why should you check the chosen pain point against the persona again before solutions?

Answers often drift: the top pain belongs to a different persona than the one you chose. Re-checking keeps the solution and the persona in line.

</details>

<details class="quiz"><summary>(Beyond the notes) What should a proto-persona be labelled as?

An assumption. Write it from the app's own evidence, say so clearly, and test it with real users as soon as you can.

</details>


# Chapter 12 · Product Design with CIRCLES

<!-- lecture n="9" label="12" short="CIRCLES design" status="done" kind="product design" -->

## At a glance

| Question | Short answer |
|---|---|
| What is CIRCLES? | A seven-step structure for "design a product" questions: **C**omprehend, **I**dentify, **R**eport, **C**ut, **L**ist, **E**valuate, **S**ummarize. |
| How do you clarify the question? | Lin's **3W's and H**: what it is, who it is for, why they need it, how it works. Confirm the goal and the constraints. |
| How many personas do you name? | List a few candidates, then **choose one** and keep it until the final solution. |
| How do you prioritize? | Lin's **A-C matrix** (revenue, satisfaction, ease, overall), or the quantitative check: **revenue per point of effort**. |
| How many solutions do you brainstorm? | **At least three.** Lin says idea 2 or 3 is usually the best. |
| How do you end? | Name the one product or feature you recommend, recap it, and say why you preferred it over the others. |
| What are the common mistakes? | Jumping to features, rambling, not asking questions, shallow personas, "me too" ideas, and no recommendation. |
| What changes for AI features? | Keep the skeleton, add output quality, data needs, failure recovery and cost per task. |
| How long should the answer be? *(Beyond the notes)* | Plan a 15 to 20 minute answer, and spend the most time on Cut, List and Evaluate. |
| What should you say at the start? *(Beyond the notes)* | One line naming the framework and the order, so the interviewer can follow. |

> [!NOTE] Where this comes from
> Sources named in the vault: *Decode and Conquer* by Lewis C. Lin (the CIRCLES method and its examples), and the *Sigma PM Concept Book, Part A (2023)* (the product design walkthrough and the common mistakes). The AI adaptation in 12.3 is general product knowledge, which the vault says its sources do not cover. Further reading: *AI Product Reading*, *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

CIRCLES (Lewis Lin, *Decode and Conquer*) is a seven-step structure for answering "design a product" questions. This chapter covers the framework itself, the mistakes that weaken answers, and how to adapt the framework for AI features.

The chapter has three sections:

- **12.1 CIRCLES.** The seven steps, with a worked persona example.
- **12.2 Common mistakes in design answers.** Jumping to features, rambling, not asking questions, and other common errors.
- **12.3 Adapting CIRCLES for AI features.** AI-specific checks for quality, data, failure modes and cost.

## Key takeaways

- Say the framework out loud at the start so the interviewer can follow your structure.
- Clarify with the "3W's and H" (what, who, why, how) before you name a persona.
- Pick one persona and keep it until the final solution.
- Prioritize one need and justify it (Lin's A-C matrix or revenue per point of effort); then brainstorm at least three solutions, weigh pros and cons, and recommend one.
- For AI products, add failure recovery, data needs, and cost per task to the evaluation.

> [!SIR] From the source notes
> Pick one persona and keep it until the final solution.

## 12.1 CIRCLES - Comprehend, Identify, Report, Cut, List, Evaluate, Summarize

> A seven-step structure for any product design question, so the answer is complete and easy to follow.

### Concept

| Step | What you do | Typical output |
|---|---|---|
| **C** Comprehend the situation | Use Lin's "3W's and H": what is it, who is it for, why do they need it, how does it work (a trimmed "5W's and H"; when/where are dropped). Also confirm the goal (engagement, revenue, share) and constraints. If the interviewer won't answer, state an assumption and invite correction. | 2-3 clarifying questions and stated assumptions |
| **I** Identify the customer | List a few candidate personas (Lin's examples: food lovers, soccer moms, college students, small business owners), then choose one. Make it vivid with behaviours, demographics, needs and goals (Lin uses a 2x2 persona card). | One persona card |
| **R** Report the customer's needs | Write user stories: *As a <role>, I want <goal> so that <benefit>.* | 2-3 user stories |
| **C** Cut, through prioritization | Choose one need. Lin's matrix grades each story A-C on revenue, customer satisfaction and ease of implementation, plus an overall grade; the quantitative version is "revenue per point of effort" (revenue impact / story size). | One chosen need, with the reason |
| **L** List solutions | Brainstorm **at least three** ideas (Lin: idea 2 or 3 is usually best; Sigma caps the short list at about four). Brainstorming aids: Reversal, Attribute, and "Why?" methods. Think big; avoid "me too" and lazy "integrate X with Y" ideas. | 3+ solutions |
| **E** Evaluate trade-offs | Optionally define criteria (customer satisfaction, implementation difficulty, revenue potential), then give a pros and cons list for each solution. Critiquing yourself first leaves the interviewer less to attack. | Pros/cons table |
| **S** Summarize your recommendation | Lin's three steps: (1) name the one product or feature you recommend, (2) recap what it is and why it benefits the user and/or company, (3) explain why you preferred it over the others. Adding a success metric is a good habit, though not part of Lin's definition. | 20-30 second wrap-up |

![The seven steps, one letter each, with the tool or output for each step.](diagrams/l9-circles-steps.svg)

**Worked example skeleton (Kat, the traveling reader, from the source book)**

- Persona: Kat, a 55-year-old who travels four times a year, carries four books per trip, and wants to discover new books and write one someday.
- User stories: "I want recommendations so that I read well-written books in my favourite genres" and "I want to write 500 words a day so that I can publish my memoir."
- Prioritization: the matrix grades "write a book" A on revenue, customer satisfaction, ease of implementation and overall, and "book discovery" C on all four. The quantitative check agrees: write a book = $500,000 revenue impact / story size 8 = $62,500 per point of effort; book discovery = $20,000 / 2 = $10,000. So "write a book" is priority 1.
- Solutions and trade-offs follow for the chosen story only.

![Kat: one persona card and two user stories written from the template.](diagrams/l9-kat-stories.svg)

![Lin's matrix grades the two stories; the revenue-per-effort check gives the same order.](diagrams/l9-kat-matrix.svg)

### Try it locally: the revenue-per-effort check

*(Beyond the notes: reproduced locally with the standard library. The numbers are Lin's, from the Kat example.)* The quantitative version of the Cut step is a single division per story, then a sort:

```python title="lab_p9_revenue_per_effort.py"
# Cut step: revenue per point of effort = revenue impact / story size (Lin's Kat example)
stories = [
    ("write a book", 500_000, 8),
    ("book discovery", 20_000, 2),
]
ranked = sorted(stories, key=lambda s: s[1] / s[2], reverse=True)
for name, revenue, size in stories:
    per_point = revenue / size
    print(f"{name}: ${revenue:,} / {size} = ${per_point:,.0f} per point of effort")
print(f"priority 1: {ranked[0][0]}")
```

```output
write a book: $500,000 / 8 = $62,500 per point of effort
book discovery: $20,000 / 2 = $10,000 per point of effort
priority 1: write a book
```

The check gives the same answer as the grid. "Write a book" is worth $62,500 per point of effort, about six times the $10,000 for book discovery. The grid and the ratio agree here, and that agreement is what makes the Cut step easy to defend in the room.

**Brainstorming methods (Lin)**

- *Reversal*: flip the situation. Buyers can't get to the car dealership, so the dealership brings the test drive home.
- *Attribute*: list attributes (material, shape, finish, position) and recombine them, for example a plastic laundry hamper mounted on the door.
- *Why?*: challenge the status quo. Why do coffee cups need handles? Because they are too hot, so make an insulated mug.

![Three brainstorming methods from Lin, each with its example.](diagrams/l9-brainstorm.svg)

**Interview tips**

- Say the framework out loud in one line at the start: "I'll clarify the goal, pick a persona, state the need, prioritize, then solve."
- Stay on one persona throughout.
- Use the time: in a 15 to 20 minute answer, spend the most time on Cut, List and Evaluate, not on clarifying.
- Lin's tip: it is fine to have a solution in mind early and steer the CIRCLES discussion toward it; it constrains the personas and needs you explore.

### Real-world examples

- **Google Maps (Lin's kind of design question)**: a traveller persona with a need to plan multi-stop trips; the chosen solution is a route-planning feature, with trade-offs in data load and accuracy. (illustrative)
- **Spotify engagement (Sigma concept book walkthrough)**: clarify scope (app vs web, music vs podcasts), choose one persona, list and rank pain points, then list features and choose a live-room (social listening) feature. The book flags the example as illustrative.
- **Swiggy "Track order" (illustrative)**: persona is a hungry customer at home; need is certainty on arrival time; solutions are live tracking, ETA revisions, and proactive delay alerts; trade-off is server and notification cost.

### Practice questions

> [!INTERVIEW] Design a feature for a library app. Walk through the CIRCLES steps in four minutes.
> *(Beyond the notes: a starting point, not the vault's answer.)* Spend about 30 seconds on Comprehend (one question on the goal and the user), 30 seconds on one persona, 40 seconds on two user stories, 40 seconds on the one need you cut to, 60 seconds on three solutions with pros and cons, and 30 seconds on the recommendation and its metric. Adjust the split to what the interviewer asks for.

> [!INTERVIEW] You have three user stories. How do you choose one in under a minute?
> **Answer outline (Q2):** Score each story on user impact, revenue or strategic fit, and effort. Pick the highest combined score with a clear reason. Name the story you parked and when you would come back to it.

> [!INTERVIEW] What clarifying questions do you ask before you pick a persona?
> *(Beyond the notes: a starting point.)* Ask what the product is and which market it serves, who the users are today, and what the goal is (engagement, revenue, share). Then ask about the constraints: platform, scale, and any part of the product that is fixed. Use Lin's 3W's and H to order the questions: what, who, why, how.

> [!INTERVIEW] How would you evaluate trade-offs between two solutions for the same need?
> *(Beyond the notes: a starting point.)* Agree the criteria first (customer satisfaction, implementation difficulty, revenue potential, as in Lin's list), then write the pros and cons of each solution against them. Critique your own options before the interviewer does, and end with the option you would build and why.

*Related:* Chapter 12 (12.2 Common mistakes, 12.3 Adapting CIRCLES for AI features), Chapter 11 (11.4 Identifying and prioritizing pain points), Chapter 14 (Choosing and defending a framework).

## 12.2 Common mistakes in design answers

> Most weak design answers fail on structure and context, not on creativity.

### Concept

**The three mistakes the Sigma casebook names most often**

1. **Jumping to features.** Listing features without context. The interviewer does not know who the customer is or which problem you are solving, so the answer cannot be justified against alternatives.
2. **Unstructured answer or rambling.** Improvising while speaking. Long, unfocused answers invite cross-questions and lose the listener.
3. **Not asking questions.** Vague prompts or unfamiliar products need clarifying questions first. Asking is a signal of judgement, not weakness.

**Mistakes flagged in Lewis Lin's *Decode and Conquer***

- **Not knowing the product.** If you have never used it, say so and ask what it does (the Windows 8 story below). Pulling up the app or site during the interview helps.
- **Shallow personas.** Classifying users only as heavy, normal and low usage, instead of by demographics, psychographics, needs and context.
- **Missing constraints and use cases, and no link to the goal.** Solutions must clearly explain how they hit the stated target.
- **"Me too" and integration ideas.** "Build what Facebook has" or "integrate YouTube with X" reads as unimaginative.
- **Only one idea.** Lin asks for at least three; with only one idea you get defensive when the interviewer critiques it.
- **No recommendation.** Failing to commit to one solution in the summary.

**Mistakes flagged elsewhere in the Sigma concept book walkthrough**

- **Abandoning the persona.** The solutions no longer match the persona you chose.
- **Off-scope answers.** "DO NOT PROPOSE marketing solutions, partnership/collaborations" when the question asks for product design.

**Common habit to add (general practice):** end with how you would measure success.

**Quick self-check before you answer**

- Did I clarify the goal and the product?
- Did I name one persona and say why?
- Did I state the need in a user story?
- Did I prioritize and say why?
- Did I list solutions that the persona can actually use?
- Did I name a trade-off and a metric?

![The mistakes from both sources, and the self-check to run before you answer.](diagrams/l9-mistakes.svg)

### Real-world examples

- **Windows 8 answer (Lin casebook)**: a candidate who had never used Windows 8 rambled about how it "deepens customer empowerment" and was stopped 45 seconds in. The lesson is to know the product before critiquing it.
- **Google+ "killer feature" (Lin casebook)**: the candidate's primary, secondary and negative personas were just heavy, normal and low social media users, and the ideas were integrations (Groups, Blogger, YouTube) that did not plausibly deliver the agreed 30% growth in sessions. Lin's verdict: mechanical use of the framework, missing constraints and use cases. The fix is personas defined by needs, and solutions tied to the goal.

### Practice questions

> [!INTERVIEW] What are the three most common mistakes in product design answers, and how do you avoid each?
> *(Beyond the notes: a starting point.)* Jumping to features: name the customer and the problem before any feature. Rambling: say the framework in one line, then move through it. Not asking questions: ask two or three clarifying questions before you name a persona.

> [!INTERVIEW] An interviewer asks you to design a feature for a product you have not used. What do you do?
> *(Beyond the notes: a starting point.)* Say so plainly, then ask what the product does and who uses it, as the vault advises. If the product is available to look at, use it during the interview, then build the persona from what you see.

> [!INTERVIEW] You realise halfway through that your solution does not fit your persona. What do you do?
> **Answer outline (Q3):** Say so openly, then go back to the persona or the chosen need. Either adjust the solution to fit, or switch persona with a brief explanation. Do not silently change the target.

*Related:* Chapter 12 (12.1 CIRCLES, 12.3 Adapting CIRCLES for AI features), Chapter 11 (11.1 Segmentation and personas), Chapter 25 (Peer mock interviews and a feedback rubric).

## 12.3 Adapting CIRCLES for AI features

> Keep the CIRCLES skeleton, and add AI-specific checks at each step: output quality, data, failure modes, and cost.

### Concept

*(The vault notes that its sources do not cover AI-specific CIRCLES. The adaptations below are general product knowledge, built on the AI chapters: Chapter 4 (What makes an AI product different) and Chapter 7 (Designing AI experiences).)*

| Step | Standard CIRCLES | AI addition |
|---|---|---|
| **C** Comprehend | Goal, constraints, context | Is AI the right tool? Is the task deterministic or probabilistic? What accuracy or latency is acceptable? |
| **I** Identify | Persona | Who sees AI output, and who is affected by its errors? Include the person who reviews or corrects output. |
| **R** Report | User stories | Add the trust need: "so that I can rely on the answer without checking every line." Add a failure-state story. |
| **C** Cut | Prioritize | Weigh value against data readiness, eval feasibility, and cost per task. A feature with no way to measure quality ranks lower. |
| **L** List | Solutions | Include the level of automation: suggestion, copilot, or autonomous action (see Chapter 6, Copilot vs automation vs autonomous agent). Include a human-in-the-loop option. |
| **E** Evaluate | Trade-offs | Add quality distribution, hallucination risk, latency, cost, privacy, and fallback behaviour. |
| **S** Summarize | Recommendation | Add the launch plan (staged rollout, kill switch) and the eval plan (golden set, online metrics). |

![The seven steps with the AI addition for each, and the three questions to add.](diagrams/l9-ai-circles.svg)

**Three questions to add to any AI design answer**

1. What happens when the model is wrong, and how does the user recover?
2. What data does the feature need, and do we have the right to use it?
3. What does it cost per task, and does the price fit the value?

**Example outline (AI study assistant for exam aspirants)**

- Persona: a working professional preparing for a government exam with two hours a day.
- Need: quick, correct answers to doubts with source references.
- Prioritize: explanation of wrong answers (high value, measurable through quiz accuracy).
- Solution: grounded answers with citations, a "check this" flag, and a fallback to a human tutor for low-confidence cases.
- Evaluate: hallucination rate on a golden set, cost per session, latency.

### Real-world examples

- **Perplexity and Microsoft Copilot**: answers carry numbered source citations, which addresses the trust need and lowers the cost of checking (the R and E steps).
- **GitHub Copilot**: suggestions the user can accept or reject, which keeps a human in the loop for each change.
- **Gmail Smart Compose**: grey inline suggestions accepted with Tab; a wrong suggestion costs nothing because the user just keeps typing. A good example of choosing a low-risk automation level.

### Practice questions

> [!INTERVIEW] Design an AI feature that summarizes customer support tickets. Walk through CIRCLES with the AI additions.
> **Answer outline (Q1):** Persona: support agent. Need: faster triage without missed escalations. Prioritize: summary accuracy on escalation-relevant fields. Solution: draft summary with source highlights and agent edit. Evaluate: summary accuracy on a labelled set, edit rate, cost per ticket. Summarize with a rollout to a small team first.

> [!INTERVIEW] Why does the Cut step change for AI features?
> *(Beyond the notes: a starting point.)* In a standard design answer, Cut weighs value against effort. For AI, it also weighs whether you have the data to build the feature and whether you can measure its quality at all. A high-value idea with no eval plan should rank below a smaller one you can measure.

> [!INTERVIEW] Which trade-offs matter most for an AI resume reviewer compared with a non-AI one?
> *(Beyond the notes: a starting point.)* The non-AI reviewer is a checklist, so its main trade-off is coverage. The AI reviewer adds quality distribution (does it fail on some resume formats?), fairness across candidate groups, the cost per resume, and the consent and retention of candidate data. Name the failure a candidate would feel most, and the way they can ask for a human review.

*Related:* Chapter 12 (12.1 CIRCLES, 12.2 Common mistakes), Chapter 7 (Human-in-the-loop design), Chapter 8 (Offline evals: golden datasets, rubrics, LLM-as-judge).

## Beyond the notes: a timed CIRCLES run-through

Interviewers often give 15 to 20 minutes. A simple plan for the time:

- **Two minutes:** the 3W's and H, with the goal and the constraints stated back.
- **Two minutes:** one persona card, said in one breath, and the reason for choosing them.
- **Three minutes:** two or three user stories, then the one need you cut to.
- **Five minutes:** three or more solutions, each with pros and cons against the criteria.
- **Three minutes:** the recommendation, the reason it beats the others, and one success metric.

Keep a small buffer. Most of the marks sit in Cut, List and Evaluate.

## Beyond the notes: the one-line scorecard

For a quick Cut, write three columns next to each story: impact on the persona, revenue or strategic fit, and effort. Use the same scale for every story. A grade or a ratio is only as good as the numbers behind it, so say which numbers you guessed.

## Beyond the notes: pitfalls

- **Stopping at one idea.** Lin's rule of three exists because a single idea makes you defensive under critique.
- **Asking questions and never using the answers.** Name the answer you heard in the persona, the need and the trade-offs.
- **Revenue per point of effort with made-up numbers.** The ratio is only as good as its inputs. Say what you assumed.
- **Changing the persona in the summary.** The recommendation must still fit the persona you chose at the start.
- **Adding AI for its own sake.** In 12.3, the first AI question is whether AI is the right tool at all.

## Beyond the notes: interview corner

- **"Walk me through CIRCLES in four minutes."** Say the seven letters in one line, then give one sentence per step, with the output of each.
- **"Why did you pick that need?"** Give the matrix grade or the ratio, and name the next need you parked.
- **"How would this change for AI?"** Name the AI addition for Cut (data and eval feasibility), then the three questions: what happens when it is wrong, what data it needs, and what it costs per task.

## Revision cheat-sheet

![Chapter 12 on one page: the seven CIRCLES steps and the AI checks.](diagrams/l9-big-picture.svg)

- **12.1** CIRCLES = **C**omprehend (3W's and H), **I**dentify (one persona), **R**eport (user stories), **C**ut (one need, A-C matrix or revenue per point of effort), **L**ist (3+ solutions), **E**valuate (pros and cons), **S**ummarize (recommend one, say why).
- **12.1 example:** Kat. "Write a book" is A on all four grades and $62,500 per point of effort, against $10,000 for "book discovery". Priority 1: write a book.
- **12.2** Mistakes: jumping to features, rambling, not asking questions, shallow personas, "me too" ideas, one idea, no recommendation, abandoning the persona, off-scope answers.
- **12.3** For AI, keep the skeleton and add: trust and failure stories, data and eval feasibility in Cut, the automation level in List, quality and hallucination risk in Evaluate, and the launch and eval plan in Summarize.
- **Beyond the notes:** time the answer, keep a one-line scorecard, and state which numbers you guessed.

## Self-test

<details class="quiz"><summary>What does the C in CIRCLES stand for, and what does Comprehend produce?

Comprehend the situation. It produces two or three clarifying questions and the stated assumptions, using Lin's 3W's and H (what, who, why, how).

</details>

<details class="quiz"><summary>What is the output of the Identify step?

One persona card, chosen from a few candidates and made vivid with behaviours, demographics, needs and goals.

</details>

<details class="quiz"><summary>What is the template for a user story in CIRCLES?

As a <role>, I want <goal> so that <benefit>.

</details>

<details class="quiz"><summary>In Lin's Kat example, why is "write a book" priority 1?

It is graded A on revenue, customer satisfaction, ease of implementation and overall, and its revenue per point of effort is $62,500, against $10,000 for "book discovery".

</details>

<details class="quiz"><summary>How is revenue per point of effort calculated?

Revenue impact divided by story size. The Kat example is $500,000 / 8 = $62,500 for "write a book" and $20,000 / 2 = $10,000 for "book discovery".

</details>

<details class="quiz"><summary>What are Lin's three brainstorming methods?

Reversal (flip the situation), Attribute (list attributes and recombine them) and "Why?" (challenge the status quo).

</details>

<details class="quiz"><summary>What are the three steps of a good Summarize, in Lin's definition?

Name the one product or feature you recommend, recap what it is and why it benefits the user or company, and explain why you preferred it over the others.

</details>

<details class="quiz"><summary>What are the three mistakes the Sigma casebook names most often?

Jumping to features without context, an unstructured or rambling answer, and not asking clarifying questions.

</details>

<details class="quiz"><summary>What does the AI adaptation add to the Cut step?

Weigh value against data readiness, eval feasibility and cost per task. A feature with no way to measure quality ranks lower.

</details>

<details class="quiz"><summary>What are the three questions to add to any AI design answer?

What happens when the model is wrong and how the user recovers; what data the feature needs and whether you have the right to use it; and what it costs per task and whether the price fits the value.

</details>

<details class="quiz"><summary>(Beyond the notes) How would you split four minutes across the CIRCLES steps?

A starting point: about 30 seconds each on Comprehend and Identify, 40 seconds each on Report and Cut, 60 seconds on List and Evaluate together, and 30 seconds on the recommendation.

</details>

<details class="quiz"><summary>(Beyond the notes) Why is revenue per point of effort only as good as its inputs?

The ratio uses your estimates of revenue and size. If those are guesses, say so, because the ranking depends on them.

</details>


# Chapter 13 · Product Improvement and App Critique

<!-- lecture n="10" label="13" short="App critique" status="done" kind="critique" -->

## At a glance

| Question | Short answer |
|---|---|
| What is an app critique? | A structured walk through an app against objectives you set yourself, not a list of random complaints. |
| What do you set first? | **Context** (why this app) and **goals** (the business objective, the user's aim, and what you will cover). |
| What are the five lenses? | Jobs to be done, personas, user familiarity, inclusivity, and zooming in and out. |
| How do you use JTBD? | Compare the app with the alternative the user would otherwise use: objective criteria. |
| Which users do you cover? | **New, intermediate and expert** users. Each has different needs. |
| What does inclusivity cover? | Vision, hearing, motor and cognitive barriers. Accessibility is a user need and a risk. |
| What does a critique end with? | A prioritized list of **2 to 3 improvements**, each tied to a lens and a metric. |
| What is the favourite-product answer? | Name the user goal, explain the "neat" part, compare with alternatives, then improve it. |
| What are the common pitfalls? | Rambling, and a favourite product you cannot discuss in depth. |
| How long should the answer run? *(Beyond the notes)* | About 15 minutes for a critique; stop a favourite-product answer after 2 to 3 minutes and invite follow-ups. |
| What does a good answer show? *(Beyond the notes)* | The user side and the business side at the same time, with a metric. |

> [!NOTE] Where this comes from
> Sources named in the vault: *Sigma PM Concept Book, Part A (2023)* (the app critique chapter), *Cracking the PM Interview* (the favourite-product type), and *Decode and Conquer* by Lewis C. Lin (the Dieter Rams criteria and the iPhone answer). Further reading: *Product Teardowns* and *Blogs & Newsletters*. No links are kept here.

## The big picture

This chapter covers two interview staples: critiquing an existing app and explaining why you love a product. Both test whether you can see a product from the user's side and the business side at once. Good answers are structured, goal-led, and specific.

The chapter has two sections:

- **13.1 Five-step critique.** A five-lens framework (JTBD, personas, user familiarity, inclusivity, zoom levels) for critiquing any app.
- **13.2 Favourite product answers that show depth.** A four-step structure for favourite-product answers, with the common pitfalls.

## Key takeaways

- Set context and goals before critiquing. Ask what the business objective is.
- Use JTBD to create objective criteria, and compare the app with the user's alternative.
- Cover new, intermediate and expert users. Each has different needs.
- Include accessibility and inclusivity. It is both a user need and a risk.
- For a favourite product, name the user goal, explain the "neat" part, compare with alternatives, then improve it.

> [!SIR] From the source notes
> Set context and goals before critiquing. Ask what the business objective is.

## 13.1 Five-step critique - JTBD, personas, familiarity, inclusivity, zoom levels

> A critique is a structured walk through an app against objectives you set yourself, not a list of random complaints.

### Concept

An app critique is one of the more approachable PM interviews, but it is easy to ramble. Start by setting **context** (why this app) and **goals** (the business objective, the user's aim, and what you will cover in the next 20 minutes). Then apply five lenses:

| # | Lens | Question it answers |
|---|------|---------------------|
| 1 | Jobs to be done | What is the user really hiring the app to do? What would they do without it? |
| 2 | Personas | Who uses it, and what are their goals, motivations and scenarios? |
| 3 | User familiarity | How does the experience differ for new, intermediate and expert users? |
| 4 | Inclusivity | Who is excluded by vision, hearing, motor or cognitive barriers? |
| 5 | Zooming in and out | How do the aesthetic (how it looks), functional (how it works) and strategic (why it exists) layers line up? |

![The five lenses in order, with the question each one asks.](diagrams/l10-five-lenses.svg)

Key points for the candidate:

- **JTBD gives objective criteria.** Compare the app against the alternative the user would otherwise use.
- **Proto-personas** are built on the fly, since you have no research. Pair one with a short scenario (a mini journey).
- **New users** judge value proposition, sign-up friction and onboarding. **Intermediate users** ask how the app guides them, where the shortcuts are, and how it grows with their needs. **Experts** look for advanced functionality and missing power tools (most relevant for task-heavy apps like Photoshop or Visual Studio).

![The same app, judged at three familiarity levels, with a Maps example.](diagrams/l10-familiarity.svg)

- **Inclusivity** covers four impairment types: **vision** (low vision, colour blindness, screen glare), **hearing** (captions, backup cues, a noisy train station), **motor** (tap target size, intricate gestures, using the app while walking) and **cognitive** (memory load, complex operations). The source notes accessibility is not a nice-to-have; in many places it is the law.

![Four kinds of barrier to check, and the benchmark settings to compare against.](diagrams/l10-inclusivity.svg)

- **Zoom out** to strategy (value proposition, business model) and **zoom in** to a specific screen or micro-interaction. The aesthetic layer is visible (brand, visual, motion, sound, touch); functional and strategic layers are invisible. Move between them deliberately.

![Three layers from strategy to looks, with the Google Maps example for each.](diagrams/l10-zoom.svg)

**Mini-example (critiquing Google Maps for a commuter):** JTBD = "reach the office on time with no surprises"; alternative = asking colleagues, fixed routine. Familiarity: a new user needs to set home and work; an expert wants departure-time alarms. Inclusivity: voice guidance helps while driving, but small map labels hurt low-vision users. Zoom: strategic layer is local search and ads; functional is routing and live traffic; aesthetic is colour-coded traffic lines (a colour-blindness risk).

Finish with a prioritised list of 2-3 improvements, each tied to a lens and a metric. Connect them to the interviewer's stated goal.

### Real-world examples

- **Duolingo** - a strong critique case for new-user onboarding (lesson before sign-up, short first lesson, streak mechanics) and for habit-forming notifications. (the critique angles are illustrative, not a company statement)
- **Google Maps** - good for zoom levels: strategic layer (local discovery and ads), functional layer (routing, live traffic), and aesthetic layer (map styling, traffic colours and contrast).
- **Swiggy / Zomato** - useful for JTBD ("decide what to eat tonight" vs. "order something specific") and for comparing new-user and repeat-user flows.
- **Apple iOS accessibility settings** - a benchmark when you critique inclusivity for another app (VoiceOver, Dynamic Type, Reduce Motion).

### Practice questions

> [!INTERVIEW] Pick an app you use daily. Walk through a five-step critique in 15 minutes. Which lens gives the most insight, and why?
> *(Beyond the notes: a starting point, not the vault's answer.)* Spend one minute on context and goals, then about two minutes on each lens, and keep two minutes for the list of improvements. The lens that gives the most insight is the one where the alternative is most different from the app, because the JTBD comparison then shows the clearest gap.

> [!INTERVIEW] How would you critique an app for a new user versus a power user without re-running the whole analysis?
> *(Beyond the notes: a starting point.)* Keep the one journey and the one JTBD comparison, then change only the familiarity lens. For the new user, check value, sign-up friction and onboarding. For the power user, check the advanced functions and the missing power tools, and say which of them would make the product stickier.

> [!INTERVIEW] Your critique finds an accessibility gap in a checkout flow. How do you prioritise it against a revenue improvement?
> **Short answer outline (Q3):** Accessibility gaps often block a whole segment and may carry legal risk, so they can outrank a revenue idea. Size both: the number of users affected and the revenue at stake. Propose a low-cost fix (larger tap targets, labels) and a metric (checkout completion by segment).

*Related:* Chapter 13 (13.2 Favourite product answers), Chapter 11 (11.1 Segmentation and personas, 11.2 Jobs-to-be-done, 11.3 User journeys and the 5Es), Chapter 12 (CIRCLES), Chapter 22 (Product improvement cases).

## 13.2 Favourite product answers that show depth

> A favourite product answer works when it reveals your user thinking, your passion and your critical eye at the same time.

### Concept

"What is your favourite product and why?" is the reverse of an improvement question. Interviewers use it to test whether you can explain why something works, not just list features.

A structure that works (from *Cracking the PM Interview*):

1. **What problems does the product solve for the user?** Name the goal, not the feature. The book's example: Mint.com analyses your finances, but the goal is "save money by understanding how you spend it". Stick to one or two goals, or you drift into features.
2. **How does it accomplish these goals, and what makes it "neat"?** A data advantage, an excellent interface, a clever win-win revenue model, a cost advantage (for example crowdsourcing), or emotional pull.
3. **How does it compare to the alternatives?** Include direct competitors and indirect substitutes. Explain why you do not use them.
4. **How would you improve it?** Expect this as a follow-up. Use the same improvement approach as in 13.1.

![The four steps of a favourite-product answer, with the Mint.com example.](diagrams/l10-favourite.svg)

Choosing the product:

- Pick something you personally connect with. Do not pick a product only because it is "impressive to discuss". It can even be a product you love but don't use yourself (a parent admiring a child's toy).
- Avoid products you cannot discuss in depth.
- Prepare a set (per the book): one online product, one physical "offline" product, one recent purchase, your favourite, one well-designed product, and the company's own product. Know each one's key metrics: users, conversion, referral, engagement, retention, revenue.

Lin's *Decode and Conquer* gives a complementary frame drawn from Dieter Rams' ten principles of good design: reveal up to **three criteria** (Lin's picks are usefulness, innovation and ease of use, with honesty as another option), show how the product meets them, and back it with evidence and a contrast with peer products. Use it as a three-point skeleton when time is short.

Keep the answer structured and concrete. Use one specific example of you using the product. Stop after 2-3 minutes and invite follow-ups.

### Real-world examples

- **Quora** - Gayle McDowell's own example in *Cracking the PM Interview*. Goal: answers to specific questions from experts. Neat: community trust via upvotes and comments. Alternative: keyword search, where trust rests on PageRank and many niche answers never get written.
- **Apple iPhone** - Lin's sample answer. Judged on usefulness (the device used most for communication, browsing and music), innovation (real web browsing and apps versus BlackBerry-era email and WAP sites) and ease of use (few buttons, finger navigation that matches mental models like flipping a photo album).
- **Google Maps** - a common favourite. Strong on problem-solving (getting there on time), data advantage (live traffic) and comparisons with paper maps and taxis.
- **Spotify** - often chosen. Good for discussing personalisation, discovery, and a freemium model.

### Practice questions

> [!INTERVIEW] What is your favourite product, and what user goal does it serve?
> *(Beyond the notes: a starting point.)* Name the product, then one goal in the user's words, then the one feature that serves the goal best. Keep it to one goal; a second goal is where answers drift into a feature list.

> [!INTERVIEW] Pick a product you love that you do not personally use. What makes it a strong product?
> *(Beyond the notes: a starting point.)* The vault's example is a parent admiring a child's toy. Explain the user goal from what you have seen people do with it, say where you got that evidence, and then run the same four steps. Be clear that you are describing it from outside.

> [!INTERVIEW] How would you improve your favourite product, and what trade-off would you accept?
> **Short answer outline (Q3):** Name one improvement that deepens the core value (e.g. a feature that solves the user's main goal better). State the trade-off explicitly: complexity, cost, or a risk to what users love. Give one metric to validate it.

*Related:* Chapter 13 (13.1 Five-step critique), Chapter 12 (CIRCLES, Common mistakes in design answers), Chapter 11 (11.2 Jobs-to-be-done), Chapter 22 (Product improvement cases).

## Beyond the notes: the critique in fifteen minutes

A time plan that keeps the critique structured:

- **One minute:** restate the context and the business objective you were given, or ask for it.
- **Two minutes:** the JTBD and its alternative.
- **Six minutes:** the other four lenses, roughly a minute and a half each.
- **Three minutes:** zoom out to strategy, then zoom in to one screen.
- **Three minutes:** the two or three improvements, each with a lens, a metric and a trade-off.

Say the lens name when you move to it. The interviewer can then follow the structure, and you can return to it if they cut you off.

## Beyond the notes: making the critique testable

A critique finding is strongest when it can be checked. For each improvement, write:

- **The user and the lens:** "new user, onboarding friction".
- **The evidence you can see:** a screen, a tap count, a step that asks for something the user does not have yet.
- **The metric:** the one number that would move if the fix worked, such as completion rate for the step.
- **The risk:** what could get worse, such as a lower sign-up quality or a slower checkout.

## Beyond the notes: pitfalls

- **A list of complaints.** Without objectives and lenses, the critique looks like a rant. Set the goals first.
- **Judging only as an expert.** A critique for a new user and one for an expert are different. Check the familiarity lens on purpose.
- **Treating accessibility as an afterthought.** It can block a whole segment, so size it like any other pain point.
- **Favourite-product answers built on features.** Name the goal first; the feature comes after.
- **Choosing a product you cannot discuss.** A favourite you cannot take apart in follow-ups costs more than it earns.

## Beyond the notes: interview corner

- **"Where would you start the critique?"** With the context and the business objective. Ask what the company wants before you list any screen.
- **"What is the user's alternative?"** Name it first. The JTBD comparison then gives you criteria for every other lens.
- **"Why this favourite product?"** Give the user goal, the neat part, the alternative you rejected, and one personal example of using it.

## Revision cheat-sheet

![Chapter 13 on one page: the critique lenses and the four-step favourite-product answer.](diagrams/l10-big-picture.svg)

- **13.1** Set context and goals. Five lenses: **JTBD** (compare with the alternative), **personas**, **user familiarity** (new, intermediate, expert), **inclusivity** (vision, hearing, motor, cognitive), **zoom levels** (strategic, functional, aesthetic). Finish with 2-3 improvements, each with a metric.
- **13.2** Favourite product: (1) the user goal, not the feature; (2) what makes it "neat"; (3) the alternatives, direct and indirect; (4) how you would improve it. Lin's skeleton: up to three criteria, with evidence and a peer contrast.
- **Beyond the notes:** time the critique, make each finding testable, and avoid lists of complaints and features-first answers.

## Self-test

<details class="quiz"><summary>What should you set before you start an app critique?

Context (why this app) and goals (the business objective, the user's aim, and what you will cover).

</details>

<details class="quiz"><summary>What are the five lenses of the critique?

Jobs to be done, personas, user familiarity, inclusivity, and zooming in and out (the aesthetic, functional and strategic layers).

</details>

<details class="quiz"><summary>Why does JTBD give objective criteria?

Because you compare the app with the alternative the user would otherwise use, rather than with your own opinion of the screens.

</details>

<details class="quiz"><summary>What does a new user judge, and what does an expert look for?

A new user judges the value proposition, sign-up friction and onboarding. An expert looks for advanced functionality and missing power tools, most relevant for task-heavy apps.

</details>

<details class="quiz"><summary>What are the four impairment types in the inclusivity lens?

Vision (low vision, colour blindness, screen glare), hearing (captions, backup cues, a noisy train station), motor (tap target size, intricate gestures, using the app while walking) and cognitive (memory load, complex operations).

</details>

<details class="quiz"><summary>What is the difference between the visible and invisible layers when you zoom?

The aesthetic layer is visible (brand, visual, motion, sound, touch). The functional and strategic layers are invisible, so you move between them deliberately.

</details>

<details class="quiz"><summary>What should a critique finish with?

A prioritized list of 2 to 3 improvements, each tied to a lens and a metric, and connected to the interviewer's stated goal.

</details>

<details class="quiz"><summary>What are the four steps of a favourite-product answer?

Name the problem the product solves for the user (the goal, not the feature); explain how it accomplishes the goal and what makes it "neat"; compare it with the alternatives; and explain how you would improve it.

</details>

<details class="quiz"><summary>Which three criteria does Lin suggest for a favourite-product answer, and where do they come from?

Usefulness, innovation and ease of use, with honesty as another option. They draw on Dieter Rams' ten principles of good design.

</details>

<details class="quiz"><summary>(Beyond the notes) Why should a critique include a metric for each improvement?

So the improvement can be checked. A metric shows whether the fix worked, and it lets the interviewer test the finding rather than the opinion.

</details>

<details class="quiz"><summary>(Beyond the notes) What is the risk of a favourite product you have not used?

You may not know its details well enough to answer follow-up questions. Say where your evidence comes from, and describe the product from outside.

</details>


# Chapter 14 · Prioritization

<!-- lecture n="11" label="14" short="Prioritization" status="done" kind="prioritization" -->

## At a glance

| Question | Short answer |
|---|---|
| What is RICE? | Reach x Impact x Confidence / Effort. One comparable number per idea, from Intercom. |
| What does the Impact scale look like? | 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal. |
| What is value vs effort? | A 2x2: quick wins, big bets, fill-ins and money pits. A simplified RICE. |
| What does Kano measure? | How features change satisfaction: expected, performance, exciting, indifferent (and reverse). |
| What is MoSCoW? | Must, Should, Could, Won't for one release. The Must list takes about 60% of effort. |
| What is ICE? | Impact, Confidence and Ease, each 1 to 10. Fast, and used for growth experiments. |
| Which framework should I use? | The one that fits the question. Many items: RICE. Scope: MoSCoW. Workshop: value vs effort. |
| What do I say in an interview? | Name the decision, pick a framework, show the inputs, and say how you would revisit it. |
| What is the weakest part of most scores? | Confidence, which is often a guess. Always state the weakest assumption. *(Beyond the notes)* |
| How do I stop a stakeholder's pet feature winning? | Ask for the evidence, then lower the confidence, not the argument. *(Beyond the notes)* |

> [!NOTE] Where this comes from
> The vault draws this chapter from the *Sigma PM Concept Book* (Part A, 2023, Chapter 4 "Feature Prioritization") and, for the choosing section, from *Cracking the PM Interview*. The vault notes say that Intercom's RICE origin, the Kano categories and the MoSCoW and ICE histories are general knowledge. Its further-reading list names *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

A product manager turns many ideas into one decision. Frameworks make the reasoning visible, so stakeholders can agree on what to build next and why. This chapter covers five scoring and sorting tools and how to choose and defend one.

The chapter has six sections, each one a building block for the next:

- **14.1 RICE.** Score reach, impact, confidence and effort into one comparable number.
- **14.2 Value vs effort.** A 2x2 matrix that sorts ideas into quick wins, big bets, fill-ins and money pits.
- **14.3 Kano model.** Classify features as expected (must-be), performance, exciting (attractive) or indifferent.
- **14.4 MoSCoW.** Sort scope into Must, Should, Could and Won't for a release.
- **14.5 ICE.** A fast Impact, Confidence and Ease score, suited to growth experiments.
- **14.6 Choosing and defending a framework.** Match a framework to the decision and explain the trade-off.

## Key takeaways

- A framework makes trade-offs visible. It does not replace judgement.
- RICE = Reach x Impact x Confidence / Effort (Intercom). It is the most precise for a large backlog. ICE is the fastest.
- Kano explains satisfaction; MoSCoW defines scope; value vs effort gives a quick visual.
- Always state the weakest assumption behind a score, especially confidence.
- In an interview, name the decision, pick a framework, show the inputs, and say how you would revisit it.

> [!SIR] From the source notes
> A framework makes trade-offs visible. It does not replace judgement.

## 14.1 RICE

> RICE turns four judgments (reach, impact, confidence, effort) into one comparable score.

### Concept

RICE was introduced by Intercom's product team (Sean McBride, 2016) to replace gut-feel roadmaps. It scores each initiative as:

**RICE score = (Reach x Impact x Confidence) / Effort**

| Factor | Question | Typical scale |
|--------|----------|---------------|
| Reach | How many people or events will this affect in a fixed period? | Customers or transactions per quarter |
| Impact | How much does it move the goal for each person reached? | 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal |
| Confidence | How sure are we of reach, impact and effort? | 100% = high, 80% = medium, 50% = low (below 50% is a moonshot) |
| Effort | Total team time across product, design and engineering | Person-months (whole numbers, or 0.5 for tiny work) |

Points to remember:

- **Reach and impact are different.** Reach is breadth (how many); impact is depth (how much for each person). Do not double-count.
- **Confidence discounts weak evidence.** A bold idea with no data gets a lower score, which keeps the list honest.
- **Effort is the denominator.** A cheap, moderate-value item can beat an expensive, large one.
- RICE gives a standard number, so it helps when many stakeholders compare very different features.

![RICE scores four judgments, each with a scale; confidence and effort both pull the score down.](diagrams/l11-rice-formula.svg)

**Worked mini-example (food delivery app, one quarter):**

| Idea | Reach | Impact | Confidence | Effort | Score |
|---|---|---|---|---|---|
| Reorder last meal in one tap | 200,000 | 1 | 80% | 2 | 80,000 |
| Group ordering for offices | 20,000 | 2 | 50% | 4 | 5,000 |
| Dark mode | 500,000 | 0.25 | 80% | 3 | 33,333 |

One-tap reorder wins despite dark mode's larger reach, because impact and effort dominate. Say this out loud: the ranking flips if group ordering's confidence rises after a pilot.

![On the worked example, one-tap reorder scores 80,000, dark mode 33,333 and group ordering 5,000.](diagrams/l11-rice-ranking.svg)

> [!PEN] Check the claim
> The scores can be checked in a few lines (the run block below). With these numbers, group ordering would need more than 100% confidence to reach dark mode's score, so a pilot that raises its confidence cannot flip the ranking on its own. A pilot could still change the impact or the effort estimate, which would change the score.

Limits: scores can look more precise than they are. RICE ignores dependencies, strategic bets and table-stakes work (a legal or security fix may score low but must ship). Use RICE to structure debate, not to end it.

### Try it locally: RICE scores

*(Beyond the notes: reproduced locally with the standard library, using the vault's worked example and its Q2 numbers.)*

```python title="lab_p11_rice.py"
# RICE scores for the vault's food-delivery example (one quarter)
ideas = [
    # name, reach per quarter, impact (0.25 to 3), confidence (0 to 1), effort (person-months)
    ("reorder last meal in one tap", 200_000, 1.0, 0.80, 2),
    ("group ordering for offices", 20_000, 2.0, 0.50, 4),
    ("dark mode", 500_000, 0.25, 0.80, 3),
]

def rice(reach, impact, confidence, effort):
    return reach * impact * confidence / effort

scores = {name: rice(r, i, c, e) for name, r, i, c, e in ideas}
for name, score in sorted(scores.items(), key=lambda kv: -kv[1]):
    print(f"{name:<30} {score:>10,.0f}")

# the vault's Q2 example: 10,000 users, impact 0.5, 80% confidence, 2 person-months
print(f"vault Q2 example: {rice(10_000, 0.5, 0.8, 2):,.0f}")

# what would group ordering need to match dark mode?
needed = scores["dark mode"] * 4 / (20_000 * 2.0)
print(f"confidence needed to match dark mode: {needed:.0%}")
print(f"group ordering at 100% confidence: {rice(20_000, 2.0, 1.0, 4):,.0f}")
```

```output
reorder last meal in one tap       80,000
dark mode                          33,333
group ordering for offices          5,000
vault Q2 example: 2,000
confidence needed to match dark mode: 333%
group ordering at 100% confidence: 10,000
```

The ranking matches the vault table: one-tap reorder first with 80,000, dark mode second, and group ordering last. The Q2 answer is 2,000. The last two lines test the claim above: group ordering would need about 333% confidence to match dark mode, and even at 100% it scores 10,000.

### Real-world examples

- **Intercom:** created RICE and published the method, the impact and confidence scales, and a scoring spreadsheet on its company blog. It remains the canonical definition.
- **Growth or onboarding backlogs:** a typical use: a tooltip (high reach, low effort) scored against a new payments integration (lower reach, high effort). *(illustrative)*
- **Indian fintech roadmap:** comparing a UPI payment-failure fix (large reach, high confidence) against a new lending feature (smaller reach, low confidence, high effort). *(illustrative)*

### Practice questions

> [!INTERVIEW] Score three features with RICE and explain why the top one wins.
> *(Beyond the notes: a starting point, not the vault's answer.)* Write each judgment as a number with a reason, compute reach x impact x confidence / effort, and rank. Say which input drives the winner (often impact and effort, not reach) and which input you are least sure of.

> [!INTERVIEW] A feature reaches 10,000 users per quarter with impact 0.5, 80% confidence, and 2 person-months effort. What is its RICE score?
> **Answer (from the vault):** 10,000 x 0.5 x 0.8 / 2 = 2,000.

> [!INTERVIEW] How would you handle a stakeholder who gives a feature an impact of 3 without evidence?
> **Answer outline (Q3):** Ask what the evidence is, then lower confidence rather than arguing about impact. Show the score with confidence visible. Invite them to run a test that raises confidence.

*Related:* Chapter 14 (Value vs effort, ICE, Choosing and defending a framework), Chapter 15 (North Star metric), Chapter 20 (Theme-based roadmaps and OKRs).

## 14.2 Value vs effort

> A 2x2 matrix that sorts ideas into quick wins, big bets, fill-ins and money pits.

### Concept

Value vs effort (also called value and complexity) is a simplified RICE. Each idea is scored on two axes:

- **Value:** the benefit to users and the business.
- **Effort:** the implementation difficulty and cost.

Plot the ideas on a 2x2:

| | Low effort | High effort |
|---|---|---|
| **High value** | Quick wins: do first | Big bets (major projects): plan, slice, de-risk |
| **Low value** | Fill-ins: do if idle | Money pits (time sinks): avoid |

![Value vs effort splits ideas into four quadrants, each with its own decision.](diagrams/l11-value-effort.svg)

Tips for the candidate:

- Agree on the scoring guidelines with the team before scoring, so the debate is about evidence.
- Use a simple scale (1-5 or T-shirt sizes) and say what each level means.
- The matrix is good for a quick visual alignment. It is weaker than RICE for comparing many items precisely, because it folds reach into "value" and ignores confidence.
- Ranking inside a quadrant: use value / effort as a ratio (this is Lin's "revenue per point of effort" idea from CIRCLES).

**Mini-example (ride-hailing app):** "Show driver's photo on booking" = high value, low effort (quick win); "in-app wallet with cashback" = high value, high effort (big bet); "new splash animation" = low value, low effort (fill-in); "build own maps stack" = low near-term value, very high effort (money pit for most startups).

### Real-world examples

- **Burbn to Instagram (2010):** Kevin Systrom and Mike Krieger's check-in app Burbn had check-ins, plans, points and photo sharing. Usage showed photos were the valued part, so they cut almost everything else and relaunched as Instagram (photos, filters, likes, comments). A real case of dropping low-value, high-effort features to focus on the high-value core. The value and effort labels are the vault's framing, not the founders'.
- **Error messages in a checkout flow:** rewriting a vague "Something went wrong" into "Payment declined by bank, try UPI" is a classic quick win: copy-only effort, measurable lift in retry rate. *(illustrative)*
- **Payments apps (Paytm, PhonePe):** small flow fixes are typical quick wins, while lending and credit products are big bets that need partners, risk models and regulatory work. *(illustrative classification)*

### Practice questions

> [!INTERVIEW] You have 10 ideas to plot. How would you run the scoring session so it does not become a debate about opinions?
> *(Beyond the notes: a starting point, not the vault's answer.)* Agree on the scale and what each level means before anyone scores. Have each person score silently, then compare the gaps, not the averages. Ask for the evidence behind every outlier, and write it next to the dot on the grid.

> [!INTERVIEW] An idea is high value but very high effort. Would you do it now? What would change your answer?
> **Answer outline (Q2):** Big bets can be worth doing if the value is strategic and the effort can be broken down. Break the work into a smaller slice, test the riskiest assumption, and re-score. Revisit if the market changes.

> [!INTERVIEW] How does value vs effort differ from RICE, and when would you use each?
> *(Beyond the notes: a starting point.)* Value vs effort is a two-axis picture for a short list or a workshop. RICE is one number with an explicit confidence input, so it orders a long backlog more precisely. Use the grid to agree on the shape of the work, then RICE to order the list inside it.

*Related:* Chapter 14 (RICE, MoSCoW, Choosing and defending a framework), Chapter 20 (Theme-based roadmaps and OKRs).

## 14.3 Kano model

> Customer satisfaction depends on how well a feature is built and whether it is expected, so not all features earn the same payoff.

### Concept

The Kano model (Noriaki Kano, 1984) plots two dimensions:

- **Functionality:** from "not done at all" to "done very well".
- **Satisfaction:** from total dissatisfaction (frustrated, disgusted) to total satisfaction (delighted, excited).

The Sigma concept book sorts features into four categories (Kano's original paper uses the names in brackets):

| Category | Also called | Effect on satisfaction |
|----------|-------------|------------------------|
| Expected | Must-be, basic | Absence causes strong dissatisfaction; presence earns little praise |
| Normal | One-dimensional, performance | More is better, roughly linearly |
| Exciting | Attractive, delighter | Absence is fine; presence delights |
| Indifferent | (none) | Users barely notice either way |

Kano also defines a fifth category, **Reverse**: features some users actively dislike (for example autoplay video with sound). Mentioning it shows depth.

![Kano's five categories as five curves: how satisfaction moves as the feature is built better.](diagrams/l11-kano-curves.svg)

Practical uses:

- **Expected features** protect you from churn. Fix them before adding delighters.
- **Performance features** are where you compete on specs or speed.
- **Exciting features** drive word of mouth but decay: today's delighter becomes tomorrow's performance or expected feature as competitors copy it.
- Survey with paired functional and dysfunctional questions ("How would you feel if the app had X?" and "...if it did not?"), each answered on five options: I like it, I expect it, I'm neutral, I can tolerate it, I dislike it. The answer pair maps to a category (for example, "neutral" if present + "dislike" if absent = Must-be).

**Mini-example (food delivery):** order arrives correct and hot = Expected; delivery time (faster is better) = Performance; free dessert on your birthday = Exciting; choice of app icon = Indifferent.

### Real-world examples

- **Battery life on a smartphone:** a classic performance feature. More hours means proportionally more satisfaction.
- **Apple's original iPhone:** touch-driven browsing and visual voicemail were widely cited as delighters when first released.
- **UPI payment confirmation:** an expected feature. Users assume an instant success screen and SMS, and only notice when it is missing.
- **Live order tracking (Swiggy, Zomato, Uber):** a delighter when first introduced, now an expected feature in every delivery and ride app. *(illustrative of Kano decay; exact timelines vary)*

### Practice questions

> [!INTERVIEW] Classify five features of a food delivery app using Kano. What changes over time?
> *(Beyond the notes: a starting point.)* Use the five-feature list in the mini-example and add three of your own, such as a refund button, real-time tracking and a loyalty stamp. Place each on the expected, performance, exciting or indifferent row, then say which ones decay into expected features as rivals copy them.

> [!INTERVIEW] Why might fixing an expected feature be a better use of sprint time than adding an exciting one?
> *(Beyond the notes: a starting point.)* An expected feature that is missing causes strong dissatisfaction and churn, while an exciting feature earns extra delight on top of a product that may still be failing its basics. Fix the basics first, then spend the sprint on delighters.

> [!INTERVIEW] How would you validate Kano categories with users?
> **Answer outline (Q3):** Run a functional and dysfunctional survey pair per feature. Compute the category from the answer matrix. Check the result with a small set of interviews to confirm the classification.

*Related:* Chapter 14 (MoSCoW, Choosing and defending a framework), Chapter 11 (Identifying and prioritizing pain points), Chapter 15 (Guardrail and negative metrics).

## 14.4 MoSCoW

> MoSCoW sorts requirements into Must, Should, Could and Won't, so a release has a clear and defensible scope.

### Concept

MoSCoW was created by Dai Clegg at Oracle (1994) and popularised by the DSDM agile method. The lower-case o's are only for pronunciation. It stands for:

- **Must-have:** essential. Without them the product cannot launch. The most time-sensitive bucket.
- **Should-have:** important, but not time-critical for launch; painful to leave out, yet a workaround exists.
- **Could-have:** desirable, but can wait for a later timeframe.
- **Won't-have (this time):** the least critical. Kept for future releases, not dropped forever.

![MoSCoW buckets for one release, the 60% rule for Musts, and the example items from the vault.](diagrams/l11-moscow.svg)

Uses:

- Scope a release or MVP. Agree on the Must list first and protect it.
- Make trade-offs visible when deadlines slip. Move items from Should or Could before touching Must.
- Works well with stakeholders who mark everything "must". Ask: "If we launch without this, does the product still work?"

Watch-outs:

- It classifies but does not rank within a bucket. Pair it with a score (for example RICE) if you need order.
- DSDM's rule of thumb: Must-haves should take no more than about 60% of the effort, leaving Should and Could items as contingency. If nearly everything is a Must, nothing is prioritised.
- Always say what the Won't list is for *this* release. It is the most useful line for managing expectations.

### Real-world examples

- **Sigma concept book's own examples:** user login = Must, reset password = Should (support can reset manually at first), single sign-on = Could.
- **Context changes the bucket:** SSO is a Could for an early consumer app but a Must for an enterprise SaaS product, because IT buyers require it. *(illustrative)*
- **Razorpay or Paytm checkout MVP:** the Must list is card or UPI payment and receipts; advanced analytics and saved-card features are later buckets. *(illustrative)*

### Practice questions

> [!INTERVIEW] Build a MoSCoW list for a first version of a ride-hailing app. Defend your Must list in two sentences.
> *(Beyond the notes: a starting point.)* Musts are the booking, the driver match, the fare and the payment, because the product does not work without them. Should items are the ride-history screen and fare estimates, which have workarounds. Could items are favourite drivers and in-app tipping. Won't this time is scheduled rides. The defence: a rider can complete one trip with only the Musts.

> [!INTERVIEW] A senior stakeholder says everything is a Must. What do you do?
> **Answer outline (Q2):** Ask what the user cannot do at launch without this item. Show the list and the consequence of dropping each Must. Offer to negotiate Should items first and invite a decision on the trade-off.

> [!INTERVIEW] How does MoSCoW differ from RICE or Kano, and when would you combine them?
> *(Beyond the notes: a starting point.)* MoSCoW sets the scope; RICE orders the work inside it; Kano explains why a feature matters to customers. Combine MoSCoW with RICE when the release has a fixed scope but a long list of Should and Could items to order.

*Related:* Chapter 14 (RICE, Kano, Choosing and defending a framework), Chapter 18 (Pilots, MVPs, and phased rollouts), Chapter 20 (PRD structure).

## 14.5 ICE

> ICE is a fast, lightweight score for Impact, Confidence and Ease, often used for growth experiments.

### Concept

ICE scores each idea on three factors, usually from 1 to 10:

- **Impact:** how much the initiative moves the target metric if it works.
- **Confidence:** how sure you are that it will work and that you can prove it.
- **Ease:** how easy it is to implement.

**ICE score = average of the three** (the Sigma concept book's convention). Many growth teams multiply instead (I x C x E), which punishes a single low score more. State which you use.

**Mini-example (onboarding experiments, averaged):** add social login (I 7, C 8, E 6 = 7.0); personalised first-week emails (I 6, C 5, E 8 = 6.3); redesign the whole onboarding flow (I 9, C 4, E 2 = 5.0). Run social login first.

![ICE scores for three onboarding experiments: the average ranks them, and the table shows each factor.](diagrams/l11-ice.svg)

It is a "minimum viable prioritisation framework": quick to fill in, good for a backlog of small experiments. Compared with RICE, ICE drops Reach and uses Ease instead of Effort, so it is faster but less precise on scale.

Tips:

- Score in a group, then discuss the outliers rather than averaging opinions.
- Keep the score tied to one metric, otherwise impact estimates drift.
- Re-score after each experiment result, since confidence should change.

### Try it locally: ICE scores

*(Beyond the notes: reproduced locally with the standard library, using the vault's three onboarding experiments.)*

```python title="lab_p11_ice.py"
# ICE scores for the vault's onboarding example (each factor 1 to 10)
experiments = [
    ("add social login", 7, 8, 6),
    ("personalised first-week emails", 6, 5, 8),
    ("redesign the whole onboarding flow", 9, 4, 2),
]

def ice_average(impact, confidence, ease):
    return (impact + confidence + ease) / 3

def ice_product(impact, confidence, ease):
    return impact * confidence * ease

for name, i, c, e in experiments:
    print(f"{name:<36} average {ice_average(i, c, e):.1f}   product {ice_product(i, c, e)}")

ranked = sorted(experiments, key=lambda x: -ice_average(*x[1:]))
print("run order by average:", " > ".join(name for name, *_ in ranked))
```

```output
add social login                     average 7.0   product 336
personalised first-week emails       average 6.3   product 240
redesign the whole onboarding flow   average 5.0   product 72
run order by average: add social login > personalised first-week emails > redesign the whole onboarding flow
```

The averages match the vault: 7.0, 6.3 and 5.0, so social login goes first. The multiplied version gives 336, 240 and 72. It punishes the redesign's low ease more, but this set of numbers ranks the three experiments in the same order either way. Say which convention you use, because the two can disagree on a closer set.

### Real-world examples

- **Growth teams in consumer apps:** ICE is common for weekly A/B tests such as button copy or onboarding steps. *(illustrative)*
- **Email subject-line tests:** high ease, moderate impact, and confidence that rises after the first test. *(illustrative)*
- **Sean Ellis and GrowthHackers:** Ellis, who coined "growth hacking", popularised ICE for ranking growth experiments. It is built into the experiment backlog he describes in *Hacking Growth* (2017).
- **Itamar Gilad's critique:** a known caveat. Confidence is often a guess, so Gilad's "Confidence Meter" ties it to evidence (opinion = low, A/B test result = high). Mention it to show you know ICE's weak spot.

### Practice questions

> [!INTERVIEW] Score five growth experiments using ICE. Which do you run first and why?
> *(Beyond the notes: a starting point.)* Write five rows with three 1-10 scores and a reason for each score, take the average, and run the top one. Explain the top pick in terms of the metric it moves and the cheapest way to learn whether it works.

> [!INTERVIEW] How is ICE different from RICE, and which would you use for a weekly experiment backlog?
> *(Beyond the notes: a starting point.)* ICE uses Ease where RICE uses Effort, and it has no Reach. For a weekly backlog of small tests, ICE is faster to fill in and easy to re-score. RICE suits a long roadmap where reach differs a lot between items.

> [!INTERVIEW] Two items have the same ICE score. How do you break the tie?
> **Answer outline (Q3):** Look at the metric each item moves and the cost of being wrong. Prefer the item that tests the biggest assumption at the lowest cost. Document the reason so the decision can be revisited.

*Related:* Chapter 14 (RICE, Value vs effort, Choosing and defending a framework), Chapter 10 (Staged rollouts and kill switches).

## 14.6 Choosing and defending a framework

> The best framework is the one that fits the decision and that you can explain. A framework is a tool for trade-offs, not a substitute for judgement.

### Concept

Prioritisation frameworks give transparency and build stakeholder consensus. Without them, decisions drift toward whoever is loudest. The Sigma concept book lists RICE, Value vs Effort, Kano, MoSCoW and ICE, and notes others: story mapping, opportunity scoring, the product tree, cost of delay, affinity grouping, buy-a-feature and weighted shortest job first (WSJF = cost of delay / job duration).

Choose based on the question:

| Question you are answering | Good fit |
|----------------------------|----------|
| Many competing features, need a comparable score | RICE |
| Quick visual alignment in a workshop | Value vs Effort |
| Which features drive satisfaction? | Kano |
| What is in or out of this release? | MoSCoW |
| Fast ranking of growth experiments | ICE |
| Time-sensitive work where delay has a cost | Cost of Delay |

![Match the question you are answering to a framework: the decision picks the tool.](diagrams/l11-which-framework.svg)

Defending a choice in an interview:

1. **State the decision.** "We need to pick the next three features for a release."
2. **Name the framework and why.** "I used RICE because we have many items with different reach."
3. **Show the inputs and their weakest assumption.** Interviewers reward honest limits.
4. **Explain how you would override the score.** Strategic or legal items may need to jump the queue.
5. **Say how you would revisit it.** Re-score after new data.

Common mistakes: using a framework to hide a preference; scoring without shared definitions; treating a score as final.

### Real-world examples

- **Intercom:** built RICE because it needed a consistent way to compare very different ideas across teams. The explicit Confidence factor was meant to stop pet ideas winning on enthusiasm.
- **Basecamp's Shape Up:** rejects scored backlogs altogether. Leadership holds a "betting table" each six-week cycle and chooses among shaped pitches, each with a fixed time "appetite". A real example that a framework is a choice you defend, not a law.
- **SAFe enterprises:** large organisations using the Scaled Agile Framework rank features by WSJF so that cost of delay, not seniority, drives order.
- **Combining frameworks (illustrative):** MoSCoW for release scope, RICE to order the Should and Could items, and ICE for weekly growth experiments.

### Practice questions

> [!INTERVIEW] You have a quarter's backlog of 40 items and a fixed team. Which framework would you use, and how would you defend it?
> *(Beyond the notes: a starting point.)* RICE, because 40 items need one comparable number and the team can estimate reach and effort. Defend it by naming the weakest input (confidence) and saying which items you would override by hand, such as a legal fix.

> [!INTERVIEW] A stakeholder wants their pet feature ranked first. How do you respond using a framework?
> *(Beyond the notes: a starting point.)* Put the feature through the same scoring with the same definitions, and show the score next to the others. If it wins, it wins on the numbers. If it does not, ask which input they think is wrong and what evidence would change it.

> [!INTERVIEW] How would you combine two frameworks for a single decision?
> **Answer outline (Q2):** State the decision and its constraints. Explain why the framework fits. Show a sensitivity check: if one assumption changes, does the ranking change? Name the trade-off you are accepting.

*Related:* Chapter 14 (RICE, Value vs effort, Kano, MoSCoW, ICE), Chapter 20 (Theme-based roadmaps and OKRs).

## Beyond the notes: the five frameworks side by side

*(Beyond the notes: a summary of this chapter's own notes, with no new facts.)*

| Framework | Inputs | Output | Best for | Watch out for |
|---|---|---|---|---|
| RICE | Reach, impact, confidence, effort | One score | Many items, one comparable number | Scores can look more precise than they are |
| Value vs effort | Value and effort on two axes | Quadrant | A quick visual in a workshop | Folds reach into value; ignores confidence |
| Kano | Survey pairs (functional and dysfunctional) | A category per feature | Which features drive satisfaction | Categories decay as features become expected |
| MoSCoW | Judgement about launch needs | Four buckets | Release scope | No ranking inside a bucket |
| ICE | Impact, confidence, ease (1 to 10) | An average (or product) | Fast ranking of experiments | Confidence is often a guess |

## Beyond the notes: running a scoring session

- **Agree the definitions first.** Write what 1 and 10 mean, what "massive" reach is for this product, and what counts as evidence.
- **Score silently, then compare.** Each person scores alone; the gaps between scores start the discussion.
- **Attach the weakest assumption to each score.** Write it next to the number, so the next re-score targets it.
- **Date the scores.** A score from last quarter is a hypothesis about this quarter.
- **Record the override.** When a legal fix or a strategic bet jumps the queue, write why, so the framework stays honest.

## Beyond the notes: pitfalls

- **Reach counted twice.** Reach and impact measure different things. Scoring a broad feature as "massive" impact and also "huge" reach can double-count the same benefit.
- **Confidence at 100% for shipped features.** Confidence should fall when the evidence is thin, not when the team is excited.
- **Precision theatre.** A score of 33,333 looks more exact than an estimate of "about 30,000" that the team actually agreed on.
- **Using a framework to win an argument.** If the chosen framework always produces the answer the leader wanted, the framework is being used as a shield.
- **Scoring a shared roadmap item with one team's numbers.** Effort split across teams needs one shared estimate, or the denominator is wrong.

## Beyond the notes: interview corner

- **"Why does RICE divide by effort?"** Because the value of an idea has to be weighed against the cost of building it. A cheap, moderate idea should be able to beat an expensive, large one.
- **"What do you do when RICE and gut feel disagree?"** Look at the input that separates them. Usually it is confidence or effort. Go and get the evidence, rather than picking the answer you prefer.
- **"Why can't you just use MoSCoW for everything?"** It sorts scope but does not rank inside a bucket. A long Should list still needs an order, so pair it with RICE or ICE.
- **"What does a Kano survey tell you that a RICE score cannot?"** Which features customers expect, which they reward and which they ignore. RICE measures the size of the benefit, Kano shows its shape.

## Revision cheat-sheet

![Chapter 14 on one page: six tools, one habit.](diagrams/l11-big-picture.svg)

- **14.1** RICE = (Reach x Impact x Confidence) / Effort. Impact scale 3 to 0.25; confidence 100%, 80%, 50%. Effort is the denominator. Reach and impact are not the same.
- **14.2** Value vs effort is a 2x2: quick wins, big bets, fill-ins, money pits. A simplified RICE for a workshop.
- **14.3** Kano: expected, performance, exciting, indifferent, plus reverse. Use functional and dysfunctional survey pairs. Delighters decay into expected features.
- **14.4** MoSCoW: Must, Should, Could, Won't. Musts take about 60% of effort. Say what the Won't list is for this release.
- **14.5** ICE = the average of impact, confidence and ease (1 to 10). Fast, for experiments. Confidence is often a guess.
- **14.6** Name the decision, name the framework, show the inputs and the weakest assumption, override where needed, and say how you will revisit it.
- **Beyond the notes:** score silently then compare; attach the weakest assumption; date and record every score; watch for reach counted twice.

## Self-test

<details class="quiz"><summary>What does the RICE formula divide by, and why?

Effort. A cheap, moderate-value item can beat an expensive, large one, because the score is a value-per-cost number.

</details>

<details class="quiz"><summary>In the vault's worked example, which idea scores highest in RICE, and why does dark mode lose?

Reorder last meal in one tap, at 80,000. Dark mode has larger reach but low impact (0.25) and higher effort, so it scores 33,333.

</details>

<details class="quiz"><summary>What is the Q2 RICE score for 10,000 users, impact 0.5, 80% confidence and 2 person-months?

2,000, from 10,000 x 0.5 x 0.8 / 2.

</details>

<details class="quiz"><summary>Where does value vs effort fold in a factor that RICE keeps separate?

Reach goes into "value", and confidence is left out entirely. That is why the matrix is weaker than RICE for comparing many items precisely.

</details>

<details class="quiz"><summary>What are the four Kano categories named in the Sigma concept book?

Expected (must-be), normal (one-dimensional, performance), exciting (attractive, delighter) and indifferent. Kano also defines a fifth, reverse.

</details>

<details class="quiz"><summary>Why do exciting features decay, according to the vault?

Today's delighter becomes tomorrow's performance or expected feature as competitors copy it.

</details>

<details class="quiz"><summary>What is the 60% rule in MoSCoW?

DSDM's rule of thumb: Must-haves should take no more than about 60% of the effort, leaving Should and Could items as contingency.

</details>

<details class="quiz"><summary>How is an ICE score calculated in the Sigma concept book?

The average of Impact, Confidence and Ease, each scored 1 to 10. Many growth teams multiply instead, so state which you use.

</details>

<details class="quiz"><summary>(Beyond the notes) What do you do when a stakeholder gives a feature an impact of 3 with no evidence?

Ask for the evidence, then lower confidence rather than arguing about impact. Show the score with confidence visible, and invite a test that raises it.

</details>

<details class="quiz"><summary>(Beyond the notes) What is the difference between Must and Won't in a MoSCoW list?

Must means the product cannot launch without it. Won't (this time) means the least critical item, kept for a future release and not dropped forever.

</details>

<details class="quiz"><summary>(Beyond the notes) Why can a pilot that raises confidence fail to flip a RICE ranking?

Because confidence is a multiplier with a ceiling of 100%. In the worked example, group ordering stays below dark mode even at 100% confidence (10,000 against 33,333).

</details>

<details class="quiz"><summary>(Beyond the notes) Why should you name the weakest assumption behind any score?

Because interviewers reward honest limits, and the weakest input (often confidence) is the one a re-score should test first.

</details>


# Chapter 15 · Metrics

<!-- lecture n="12" label="15" short="Metrics" status="done" kind="metrics" -->

## At a glance

| Question | Short answer |
|---|---|
| What is a North Star? | The one metric that captures the value you deliver to customers over the long term. |
| What is an input metric? | A metric under the North Star that a team owns, such as activation or session starts. |
| What is AARRR? | Five lifecycle stages: acquisition, activation, retention, referral, revenue. One key metric per stage. |
| What is HEART? | Google's UX framework: happiness, engagement, adoption, retention, task success. Goals, signals and metrics for each. |
| How do I read a funnel? | Track the conversion between each step. The biggest drop is the first place to investigate. |
| What does a marketplace need? | Both sides (supply and demand) and the match between them, plus the economics. |
| What is a guardrail? | A metric that must not get worse while you optimise the primary one. |
| How do I diagnose a drop? | Build a metric tree, verify the data, segment, walk the branches that moved, then test. |
| Why does a metric answer need a guardrail? | Every metric you optimise invites gaming. A guardrail sets the boundary. |
| How do I pick a North Star in an interview? *(Beyond the notes)* | Name it, justify it with customer value, name two or three inputs, and add a guardrail. |
| What is the common trap with ratios? *(Beyond the notes)* | Changing the denominator, or a segment average that hides a broken channel. |

> [!NOTE] Where this comes from
> The vault draws this chapter from the *Sigma PM Concept Book* (Part A, 2023, Chapter 5 "Metrices"), the *Sigma PM Casebook* (2023-2024, Part B) and the *XLRI PM Casebook 2023*. The vault notes say that the North Star, HEART, AARRR and guardrail sources are general product knowledge, and they name the authors and papers as general knowledge. Its further-reading list names *Blogs & Newsletters*, *Product Teardowns* and *AI Product Reading*. No links are kept here.

## The big picture

Metrics are how a product manager turns "is this working?" into a number. Interviewers test whether you can pick the right metric for a product, explain why it matters, and notice when a metric is lying to you. This chapter covers the frameworks (North Star, AARRR, HEART), the funnel and marketplace metrics behind them, guardrails that stop you from winning the wrong game, and metric trees for diagnosing a movement.

The chapter has six sections, each one a building block for the next:

- **15.1 North Star metric.** The single metric that captures the value delivered to customers over the long term.
- **15.2 AARRR (pirate metrics).** A five-stage lifecycle model, from acquisition to revenue, for product-led growth.
- **15.3 HEART.** Google's framework for user experience goals, signals and metrics.
- **15.4 Funnel, marketplace and retention metrics.** Conversion funnels, two-sided marketplace health and cohort retention.
- **15.5 Guardrail and negative metrics.** Metrics that must not get worse while you optimise the primary one.
- **15.6 Metric trees and diagnosing metric movement.** Decomposing a metric into drivers to find what moved it.

## Key takeaways

- Every metric answer should name a primary metric, its reasoning, and at least one guardrail.
- A North Star is a value-delivery metric, not a revenue or vanity metric.
- AARRR and HEART are lenses, not checklists. Pick the ones that fit the product stage and goal.
- Funnels show where users leak; retention shows whether value sticks.
- Metric trees turn "the number dropped" into testable hypotheses.

> [!SIR] From the source notes
> A primary metric tells you what you are optimising. Guardrails tell you what you must not break while you do it.

## 15.1 North Star metric

> The North Star is the one metric that best captures the value you deliver to customers, and growth follows when that metric grows.

### Concept

The North Star Metric is the single number a company uses to focus growth and decision-making on long-term customer value. The underlying idea: if a company keeps delivering more value to customers, growth is assured. It aligns teams that otherwise optimise for their own local numbers.

**Good North Star properties**

- Reflects value received by the customer, not value captured by the company.
- Leading indicator of revenue, not a lagging one.
- Measurable and understandable by every team.
- Sensitive enough to move with product work, but not so noisy that it swings daily.

**Choosing one: a quick test**

1. Does an increase in this metric mean customers are getting more value?
2. Can a team outside growth move it through their work?
3. Would gaming it harm users? (If yes, reconsider.)

**Input metrics** sit under the North Star and are what teams actually own. For example, if the North Star is "weekly listening hours," input metrics could be new-user activation, playlist creation, and session starts.

![The North Star sits on top; input metrics are what teams own; guardrails must not get worse.](diagrams/l12-north-star.svg)

**North Star vs neighbours**

- Not revenue: revenue is the *result* of value delivered and lags it.
- Not a vanity count: total sign-ups or downloads only go up and say nothing about value.
- Not OKRs: the North Star is stable for years; OKRs change each quarter and push its input metrics.

**Mini-example (food delivery):** candidate North Stars are revenue (lagging, company-centric), orders placed (better, but counts late or wrong orders) and **orders delivered on time and as ordered per week** (captures customer value and both marketplace sides). Inputs: active restaurants per locality, delivery partner availability at peak, search-to-order conversion. Guardrails: cancellation rate, delivery partner earnings per hour.

**Interview framing:** state the North Star, justify it with customer value, name two or three input metrics, and add a guardrail (see Chapter 15, Guardrail and negative metrics).

### Real-world examples

- **Spotify: time spent listening.** Value is in the listening itself, and it drives subscriptions and ad inventory.
- **Airbnb: nights booked.** A booked night means a host earned money and a guest got a stay, so both sides of the marketplace win.
- **Facebook: monthly active users.** This is the example the Sigma concept book gives, and it matches Facebook's history: Mark Zuckerberg made MAU (not registered users) the internal and external growth metric, and former growth head Alex Schultz has described it as the growth team's north star (alongside the well-known "7 friends in 10 days" activation insight). Treat it as a historical example: MAU counts activity rather than value, Facebook has long reported daily actives alongside monthly actives, and in 2018 it re-ranked News Feed around "meaningful social interactions" even though time spent fell. Interviewers may push on this, so say why MAU is a weak North Star by today's standards.
- **Slack: messages sent within a team.** Slack's founder Stewart Butterfield has said teams that had exchanged about 2,000 messages almost never churned, which is why message activity, not sign-ups, became the metric teams worked on.

### Practice questions

> [!INTERVIEW] Pick a North Star for a food delivery app. Defend it against revenue and orders.
> *(Beyond the notes: a starting point, not the vault's answer.)* Use the mini-example: orders delivered on time and as ordered per week. Defend it by saying it counts value to the customer (the order arrives right and on time), not money the company takes, and that it moves both restaurant supply and rider supply.

> [!INTERVIEW] Your North Star went up 5% but retention fell. What do you do?
> **Answer outline (Q2):** Check whether the North Star counts low-value engagement (e.g., repeat opens without success). Segment by cohort. Add retention as a guardrail or a second North Star input. Decide whether the metric definition itself needs revising.

> [!INTERVIEW] Why is "daily app opens" a weak North Star for a banking app?
> *(Beyond the notes: a starting point.)* Opens can rise while customers struggle to pay a bill or find a statement. The number says the app is being used, not that a customer got a job done. A better candidate counts completed money tasks, such as payments that succeed first time.

*Related:* Chapter 15 (AARRR, HEART, Guardrail and negative metrics, Metric trees), Chapter 14 (RICE).

## 15.2 AARRR (pirate metrics)

> AARRR splits the customer lifecycle into five stages, so you track the one metric that matters at each stage instead of a pile of vanity numbers.

### Concept

AARRR comes from Dave McClure's 2007 talk "Startup Metrics for Pirates"; McClure is a Silicon Valley investor and founder of 500 Startups. It is built for product-led growth businesses. The pitch: focus on the metrics that drive company growth and avoid superficial numbers such as social-media counts.

| Stage | Question | Typical metrics |
|---|---|---|
| **Acquisition** (awareness) | How are people discovering us? | Visits, installs, CAC, channel mix |
| **Activation** | Are they doing the action that signals value? | Sign-up completion, first key action, time-to-value |
| **Retention** | Do activated users keep coming back? | D1/D7/D30 retention, churn, DAU/MAU |
| **Referral** | Do users recommend us? | Invites sent, invite conversion, NPS-linked referrals |
| **Revenue** | Will users pay? | Conversion to paid, ARPU, LTV |

![AARRR: five stages in order, with the question and the metric that gates each one (UPI payments example).](diagrams/l12-aarrr.svg)

**How to use it in an interview**

- Map the product's lifecycle to the five stages.
- Pick one primary metric per stage, with a reason.
- Find the weakest stage. Ask what the cheapest experiment is to fix it.

**Pitfall:** teams track all five stages equally and lose focus. The point is to know the single metric that gates each stage.

**Mini-example (UPI payments app):** Acquisition = installs by channel (cashback campaign vs organic); Activation = first successful payment within 7 days of install; Retention = monthly transacting users; Referral = invites that lead to a first payment; Revenue = merchant fees and lending/insurance cross-sell per user. If cashback installs activate but do not retain, the problem is the offer attracting deal-seekers, not the funnel.

**Caveat:** some teams reorder the stages (for example putting Retention first, or Revenue before Referral), and AARRR assumes a funnel-shaped journey. For products where value is collaborative or network-driven, pair it with the funnel, marketplace and retention metrics in 15.4.

### Real-world examples

- **Dropbox referral program (2008-2010):** both the inviter and the invitee got extra free storage. Dropbox grew from roughly 100,000 to about 4 million users between late 2008 and late 2009, and Drew Houston credited referrals with a lasting lift of around 60% in sign-ups, so invite conversion was a key stage metric.
- **Ride-hailing apps (illustrative):** acquisition via referral codes and promotions, activation at first completed ride, retention via repeat rides, revenue via take rate.
- **Duolingo:** activation can be framed as the first lesson completed, retention is driven by streaks and leagues, and revenue comes from Super Duolingo subscriptions and ads. *(stage mapping is illustrative)*

### Practice questions

> [!INTERVIEW] Apply AARRR to a food delivery app. Which stage is the weakest, and why?
> *(Beyond the notes: a starting point, not the vault's answer.)* Map the app to the five stages: installs, first order, repeat orders, referred orders, and commission or delivery-fee revenue. The weakest stage is the one with the lowest rate against its peers. Say which data would show it, and which cheap test would confirm it.

> [!INTERVIEW] Your acquisition is up 30% but revenue is flat. Which stage do you examine next?
> **Answer outline (Q2):** Compare activation and retention cohorts for the new acquisition channel. If new users from the new channel do not activate, the problem is quality of traffic, not volume. Check revenue per cohort.

> [!INTERVIEW] When would you not use AARRR?
> *(Beyond the notes: a starting point.)* When the product is not a funnel-shaped lifecycle. A two-sided marketplace or a collaboration tool, where value comes from other users, needs the marketplace and network metrics in 15.4 alongside, or instead of, AARRR.

*Related:* Chapter 15 (North Star metric, HEART, Funnel, marketplace and retention metrics, Guardrail and negative metrics, Metric trees).

## 15.3 HEART

> HEART turns fuzzy user-experience goals into measurable signals, one dimension at a time.

### Concept

HEART was developed by Google UX researchers (Kerry Rodden, Hilary Hutchinson and Xin Fu, in a 2010 CHI paper) to measure user experience at scale for a feature or product. It is used to decide where to focus when building or improving something. It is used with the **Goals-Signals-Metrics** process: for each dimension you keep, define three layers:

- **Goal:** a broad objective (e.g., "increase user satisfaction").
- **Signal:** an observable user behaviour or attitude that indicates progress (e.g., "users spend more time per session").
- **Metric:** a quantifiable data point (e.g., "churn rate" for retention).

| Dimension | Goal example | Signal example | Metric example |
|---|---|---|---|
| **Happiness** | Users find the feature pleasant | Positive survey responses | CSAT, NPS |
| **Engagement** | Users use the feature often | Actions per session | Sessions/user/week |
| **Adoption** | New users start using it | First-time use of feature | % of new users who try it |
| **Retention** | Users keep returning | Repeat usage | Churn rate, D30 retention |
| **Task success** | Users complete the job | Completion without errors | Completion rate, time-on-task, error rate |

![HEART as a grid: each dimension carries a goal, a signal and a metric. The WhatsApp mini-example skips Retention.](diagrams/l12-heart.svg)

**Using HEART well**

- You do not need all five. Three or four are often enough.
- Happiness, Engagement and Retention are often measured per user over time; Adoption and Task success suit a specific feature.
- HEART is for evaluating UX of a product or feature; the North Star is for company-wide value. Use HEART when the question says "measure the success of this feature".

**Mini-example (WhatsApp disappearing messages):** Adoption = % of weekly actives who turn it on in the first month; Engagement = share of chats with it enabled; Task success = % of users who set it without opening help; Happiness = in-app rating of privacy controls. Skip Retention: one feature rarely moves app-level retention measurably.

- Happiness is usually survey-based and lags. Pair it with behavioural metrics.
- Task success is the most diagnostic for UX problems: if it is low, fix the flow before worrying about engagement.

**Interview tip:** map the feature to HEART, state the goal-signal-metric chain for the two most relevant dimensions, and say why you skipped the others.

### Real-world examples

- **Search engines (illustrative):** task success is often approximated by searches that end in a click with no immediate query reformulation.
- **Mobile payments apps (illustrative):** task success is transaction completion without failure; adoption is first-time UPI or wallet use.
- **Ride-hailing apps (illustrative):** happiness via post-ride ratings; task success via booking completion.

### Practice questions

> [!INTERVIEW] Use HEART to evaluate a new in-app grocery reorder feature.
> *(Beyond the notes: a starting point, not the vault's answer.)* Pick three dimensions. Adoption: the share of weekly grocery buyers who reorder through the feature in its first month. Task success: reorders that complete with no error or edit. Happiness: a short in-app rating after the reorder. Skip Retention if the feature is one of many reasons to return.

> [!INTERVIEW] Engagement went up but happiness went down after a redesign. What does that tell you?
> **Answer outline (Q2):** Engagement may have risen because users are struggling (more taps, more searches). Check task success and error rate. Pull qualitative feedback. Consider whether the redesign added friction.

> [!INTERVIEW] Why is HEART not a replacement for a North Star?
> *(Beyond the notes: a starting point.)* HEART judges the experience of one product or feature, one dimension at a time. A North Star is one number for the whole company's value. A feature can score well on HEART and still not move the North Star, so use both for different questions.

*Related:* Chapter 15 (North Star metric, AARRR, Guardrail and negative metrics), Chapter 13 (Five-step critique: JTBD, personas, familiarity, inclusivity, zoom levels), Chapter 11 (Identifying and prioritizing pain points).

## 15.4 Funnel, marketplace, and retention metrics

> Funnels show where people leak, marketplaces show whether both sides are served, and retention shows whether value sticks.

### Concept

**Funnel metrics** measure step-by-step conversion through a flow (e.g., visit, sign-up, first action, purchase). Track the conversion rate between each step, not just the end number. The biggest drop-off is the first candidate for investigation.

- Define each step precisely, including the event that marks it.
- Segment by source, device and cohort. An average can hide a broken channel.
- Compare against a baseline period, not just last week.

### Try it locally: a funnel from visit to second order

*(Beyond the notes: reproduced locally with the standard library. The numbers are illustrative, not from any company.)*

```python title="lab_p12_funnel.py"
# Funnel conversion for one illustrative cohort of visitors
steps = [("visit", 100_000), ("sign-up", 12_000), ("first order", 5_400), ("second order", 2_160)]

print(f"{'step':<14}{'users':>9}{'from previous':>16}{'from visit':>13}")
first = steps[0][1]
prev = None
for name, n in steps:
    from_prev = "-" if prev is None else f"{n / prev:.1%}"
    print(f"{name:<14}{n:>9,}{from_prev:>16}{n / first:>13.1%}")
    prev = n

# the biggest leak: the step that converts the lowest share of the step before it
rates = [(steps[i][0], steps[i][1] / steps[i - 1][1]) for i in range(1, len(steps))]
worst = min(rates, key=lambda r: r[1])
print(f"biggest leak: {worst[0]} (converts {worst[1]:.1%} of the step before)")
```

```output
step              users   from previous   from visit
visit           100,000               -       100.0%
sign-up          12,000           12.0%        12.0%
first order       5,400           45.0%         5.4%
second order      2,160           40.0%         2.2%
biggest leak: sign-up (converts 12.0% of the step before)
```

The table shows the funnel step by step. Only 12% of visitors sign up, but 45% of sign-ups place a first order and 40% of those place a second. The sign-up step is the biggest leak, so it is the first place to investigate. The same arithmetic applies to any funnel: compare each step with the one before it, not only the first and last numbers.

![The funnel from the run block: the sign-up step is where most visitors leave.](diagrams/l12-funnel.svg)

**Marketplace metrics** cover two sides plus the match between them:

- **Supply side:** active suppliers (drivers, sellers, hosts), supply utilisation, earnings per supplier.
- **Demand side:** active buyers, orders per buyer, repeat rate.
- **Match/liquidity:** fill rate, time-to-match, search-to-booking rate.
- **Economics:** GMV, take rate (platform revenue / GMV), contribution margin per order.
- Watch for imbalance: more demand than supply raises wait times and churns buyers; the reverse starves suppliers.

![A marketplace has two sides and a match in the middle; economics sit underneath.](diagrams/l12-marketplace.svg)

**Retention metrics** show whether users come back:

- **Cohort retention curve:** share of a signup cohort still active on day 1, 7, 30, and so on. A curve that flattens at a non-zero level signals product-market fit.
- **Stickiness:** DAU/MAU ratio.
- **Churn:** share of users lost in a period (1 - retention).

**Formula cheat sheet** (from the Sigma concept book's common metrics table)

| Metric | Formula |
|---|---|
| Trial-to-paid conversion | paying customers / trial users |
| Retention rate | users active in period 2 who were active in period 1 / users active in period 1 |
| Stickiness | DAU / MAU (0.5 = the average user is active about 15 days a month) |
| CAC | marketing spend in period / customers acquired in period |
| LTV (simple) | revenue per user per period / churn rate per period |
| NPS | % promoters (9-10) - % detractors (0-6) |

Check: LTV / CAC above about 3 is a common rule of thumb for healthy unit economics.

### Try it locally: the formula cheat sheet

*(Beyond the notes: reproduced locally with the standard library. The inputs are illustrative numbers chosen to show each formula.)*

```python title="lab_p12_formulas.py"
# The vault's formula cheat sheet, with illustrative inputs
trial_users, paying = 6_000, 900
print(f"trial-to-paid conversion: {paying / trial_users:.1%}")

active_p1, still_active_p2 = 8_000, 2_800
retention = still_active_p2 / active_p1
print(f"retention rate: {retention:.1%}")
print(f"churn (1 - retention): {1 - retention:.1%}")

dau, mau = 1_200_000, 4_000_000
stickiness = dau / mau
print(f"stickiness (DAU/MAU): {stickiness:.2f}, about {stickiness * 30:.0f} active days a month")

spend, customers = 3_000_000, 15_000
cac = spend / customers
print(f"CAC: {cac:,.0f} per customer")

revenue_per_month, churn_per_month = 40, 0.10
ltv = revenue_per_month / churn_per_month
print(f"LTV (simple): {ltv:,.0f}, so LTV / CAC = {ltv / cac:.1f}")

promoters, passives, detractors = 300, 500, 200
total = promoters + passives + detractors
nps = (promoters - detractors) / total * 100
print(f"NPS: {nps:.0f} (promoters {promoters / total:.0%}, detractors {detractors / total:.0%})")
```

```output
trial-to-paid conversion: 15.0%
retention rate: 35.0%
churn (1 - retention): 65.0%
stickiness (DAU/MAU): 0.30, about 9 active days a month
CAC: 200 per customer
LTV (simple): 400, so LTV / CAC = 2.0
NPS: 10 (promoters 30%, detractors 20%)
```

Each formula is one line of arithmetic. Here a trial-to-paid rate of 15% and a retention of 35% give a churn of 65%. The stickiness of 0.30 means the average user is active about nine days a month, against the 15 days that 0.5 would mean. The LTV of 400 against a CAC of 200 gives a ratio of 2.0, which is below the rule of thumb of about 3. The NPS comes from the counts: 30% promoters minus 20% detractors is 10.

**Interview tip:** for a marketplace, always name both sides and the match metric. For a consumer app, lead with a cohort retention curve.

### Real-world examples

- **Airbnb (marketplace):** nights booked as the match-driven outcome, with host supply and guest demand tracked separately.
- **Uber / Ola (marketplace):** driver utilisation and rider wait time (ETA) are the balance pair; surge pricing exists to pull supply in when demand outruns it.
- **Consumer subscription apps (illustrative):** cohort retention curves are the standard test of whether a feature actually changes behaviour.

### Practice questions

> [!INTERVIEW] Design the funnel for an online food ordering app. Where would you look first if orders fell 10%?
> *(Beyond the notes: a starting point, not the vault's answer.)* Use the steps visit, restaurant page view, add to cart, checkout, payment and delivered order. Compare each step with the same week last year. The first step that dropped by more than the others is where to look, and you segment it by city and device before deciding the cause.

> [!INTERVIEW] A marketplace has high buyer growth but falling conversion. What are the candidate causes?
> **Answer outline (Q2):** Check supply-side fill rate and average wait time. Segment conversion by city and category. Check whether new buyers come from a channel with low intent. Compare with a matched prior cohort.

> [!INTERVIEW] How would you tell whether a retention improvement is real or a cohort artifact?
> *(Beyond the notes: a starting point.)* Compare cohorts of the same age, not calendar weeks. Check whether the new cohort came from a different channel, season or promotion. Then compare against a matched earlier cohort and check that the lift holds for a few weeks after it.

*Related:* Chapter 15 (AARRR, North Star metric, Guardrail and negative metrics, Metric trees), Chapter 19 (Partnerships, acquisitions, and build-vs-buy strategy).

## 15.5 Guardrail and negative metrics

> A primary metric tells you what you are optimising. Guardrails tell you what you must not break while you do it.

### Concept

Every metric you optimise invites gaming. A feed that maximises time spent can flood users with clickbait. A checkout that maximises conversion can hide shipping costs. **Guardrail metrics** are the things that must stay healthy: they set a boundary the primary metric cannot cross.

![The primary metric may rise; the guardrail must hold. Compare net revenue, not gross conversion.](diagrams/l12-guardrail.svg)

**Types of guardrails**

- **Experience guardrails:** complaints, crash rate, latency, uninstalls, unsubscribes.
- **Business guardrails:** refund rate, cancellation rate, support tickets, margin.
- **Trust and safety guardrails:** harmful content rate, fraud rate, opt-out rate.
- **Negative metrics:** metrics that should go down, such as errors, churn, or dark-pattern signals (accidental taps, rage clicks).

**How to set them**

1. For every primary metric, ask "how could this be gamed?" The answer is your guardrail.
2. Set a threshold before the test, not after. For example, "crash rate must not rise more than 0.1 percentage points."
3. Decide upfront what happens if a guardrail breaks. Usually the experiment stops, regardless of primary-metric wins.

**Interview tip:** always close a success-metric answer with one to three guardrails and a stated threshold. It signals maturity.

### Real-world examples

- **Facebook News Feed, 2018:** Facebook re-ranked the feed to favour "meaningful social interactions" over viral video and publisher content, and Mark Zuckerberg told investors this cut time spent by roughly 50 million hours a day. A real case of a company accepting a drop in an engagement metric to protect a user-wellbeing goal.
- **Engagement features in social feeds (illustrative):** time spent is the primary metric; hide-post and "see less" actions and reports are guardrails.
- **Promotional pricing (illustrative):** conversion is primary; margin and refund rate are guardrails.
- **Recommendation changes (illustrative):** click-through is primary; diversity and complaint rate are guardrails.

### Practice questions

> [!INTERVIEW] Pick a primary metric for a news app's new notification feature. Name three guardrails.
> *(Beyond the notes: a starting point.)* Primary: notification-led sessions that read at least one article. Guardrails: notification opt-outs, uninstalls within a week, and complaints or "mute" taps. Set each threshold before the test.

> [!INTERVIEW] A test lifts conversion 4% but cancellations rise 3%. Ship or not?
> **Answer outline (Q2):** Compare net revenue after cancellations, not just gross conversion. Check whether the cancellations come from a specific cohort (e.g., users who bought on impulse). Ship only if the net effect is positive and the cancellation cohort is acceptable, or iterate on the offer.

> [!INTERVIEW] How would you set a threshold for a guardrail with noisy data?
> *(Beyond the notes: a starting point.)* Measure the noise first, for example with an A/A test where both groups get the same experience, so you know how much a metric moves by chance. Set the threshold outside that normal range, write it down before the test, and use a longer window before you act on a small breach.

*Related:* Chapter 15 (North Star metric, HEART, Funnel, marketplace and retention metrics, Metric trees), Chapter 17 (Running pricing experiments).

## 15.6 Metric trees and diagnosing metric movement

> A metric tree breaks one number into the drivers that multiply or add up to it, so "the number dropped" becomes a set of testable hypotheses.

### Concept

A **metric tree** starts from a top-level metric and decomposes it into component drivers. For example:

Revenue = Orders x Average order value
Orders = Visitors x Conversion rate
Visitors = Organic + Paid + Referral

Each branch is either a sum or a product, so you can check which branch moved and by how much. This is the core of metric-movement questions.

**Worked mini-example:** revenue fell 10%. Orders are flat, so AOV fell 10%. Split AOV = items per order x price per item: items per order is flat, price per item fell. Segment by category: grocery's share of orders jumped after a grocery promo. Conclusion: a mix shift toward cheaper baskets, not a product bug, and possibly a healthy one.

![Revenue fell 10 percent: the tree walks down to the one branch that moved.](diagrams/l12-metric-tree.svg)

**Diagnosing a metric drop: a working sequence**

1. **Verify the metric.** Confirm the data is right: definition change, tracking bug, or a logging outage. Check whether the drop is real.
2. **Quantify.** Absolute vs percentage, sudden vs gradual, and the time window.
3. **Segment.** Geography, platform (iOS vs Android vs web), user type, acquisition channel, and cohort.
4. **Walk the tree.** Find the branch that accounts for the movement. Ignore branches that did not move.
5. **Map to causes.** Internal (releases, pricing, bugs, UX changes), external (competitors, seasonality, regulation), or instrumentation.
6. **Test.** Form the cheapest test or query that would confirm or reject each candidate.

The Sigma casebook states the same principle in its RCA framework: define the metric, confirm context (platform, OS, demographics, region), decide whether the drop is sudden or gradual, then evaluate internal and external factors. A sudden drop usually points to a release or outage. A gradual drop points to competition or behaviour shift.

**Interview tip:** draw the tree on the whiteboard first. Interviewers reward a structured decomposition more than a long list of guesses.

### Real-world examples

- **Mobile banking uninstalls (XLRI casebook):** uninstalls of a legacy private bank's app rose gradually across India, on both Android and iOS. The candidate ruled out a metric definition change, the recent UI-only update, bugs, data leaks, PR and regulation, and a neobank competitor, then found the cause: users acquired through the bank's own free-credit install campaign were uninstalling once the credit was used. The fix was cohort analysis and better activation, not a product rollback.
- **Flipkart UGC engagement down 20% (Sigma casebook):** walking the journey showed every stage before the Q&A section was stable and Q&A impressions were flat, but Q&As viewed per session fell after a release. The cause was a new Q&A text search: users found answers directly instead of scrolling. An A/B test showed conversion *improved*, so the right move was to change the metric, not fix the product.
- **Amazon order cancellations up 10% (XLRI casebook framework):** scope first (time, service, category, region, channel), then external factors, then walk the journey (search, recommendations, listing, payments, delivery) to find the stage that changed.

### Practice questions

> [!INTERVIEW] Build a metric tree for "monthly active users" for a ride-hailing app.
> *(Beyond the notes: a starting point, not the vault's answer.)* Monthly active users = riders active plus drivers active, or total unique users who open the app and book or accept a ride. Then split riders into new and returning, and each group into the channel they came from. Each branch is a sum or a product you can check against data.

> [!INTERVIEW] Average order value dropped 8%. Walk through your diagnosis.
> *(Beyond the notes: a starting point.)* Use the six-step sequence: confirm the order value field is still logged the same way, quantify the drop by week, segment by platform and category, walk items per order and price per item, map each candidate to a cause, and test the cheapest one, such as a promo check.

> [!INTERVIEW] Your dashboard shows a 40% drop in signups overnight. What do you check first?
> **Answer outline (Q3):** First check whether the tracking pipeline changed or broke. Next, check whether a release shipped in the last 24 hours and compare across platforms. Only then look at demand-side causes like campaigns or competitor moves.

*Related:* Chapter 15 (North Star metric, Funnel, marketplace and retention metrics), Chapter 16 (Scoping: clarify, verify metrics, check platforms and segments; Internal vs external causes; AI-specific RCA).

## Beyond the notes: AARRR, HEART and the North Star side by side

*(Beyond the notes: a summary of this chapter's own notes, with no new facts.)*

| Lens | The question it answers | Unit | Use it when | Trap |
|---|---|---|---|---|
| North Star | Is customer value growing? | One company-wide number | Setting direction across teams | A vanity count that only goes up |
| AARRR | Where in the lifecycle do users leak? | One metric per stage | Product-led growth | Treating all five stages equally |
| HEART | Is this feature's experience good? | Goal, signal and metric per dimension | Evaluating one feature or product | Measuring five dimensions when three are enough |
| Funnel | Which step loses the most people? | Conversion between steps | A flow with clear steps | Looking only at the end number |
| Guardrail | What must not break? | A threshold set before the test | Any optimisation | Setting the threshold after the result |

## Beyond the notes: a metric review checklist

- **Write the definition.** What event counts, which user, which time window. A metric without a definition cannot be verified.
- **Check the denominator.** A rate can rise because the bottom number shrank. Say which population the rate is over.
- **Split the average.** Look at segments (platform, city, channel, new and returning) before believing a single number.
- **Look for the lag.** Some metrics, such as NPS or churn, show the effect of a change weeks later. Use a window long enough to show it.
- **Name one guardrail and its threshold** before the next launch review.

## Beyond the notes: pitfalls

- **Changing the denominator mid-analysis.** A conversion rate moves when the definition of "visitor" changes, even though the product did not change.
- **Cohort artifacts.** A new cohort can look better because it arrived in a quiet week, through a promo, or from a different channel. Compare cohorts of the same age, from the same source.
- **Winning the primary and losing the business.** A lift in gross conversion can coincide with a fall in net revenue once cancellations and refunds are counted.
- **Using vanity numbers in a North Star.** Totals only go up, so they say nothing about whether value is growing.
- **Diagnosing without a tree.** Jumping to a favourite cause (a release, a competitor) skips the branches that did not move.

## Beyond the notes: interview corner

- **"Name a North Star for a product that is not a marketplace."** Pick a value-delivery number for the product, such as completed tasks per active user for a note-taking app. Then name two inputs and one guardrail.
- **"Explain a funnel to a non-technical stakeholder."** Each step is the share of the people who got to the previous step and went on to the next. The step with the largest share lost is where the team looks first.
- **"Why is retention the test of product-market fit?"** A retention curve that flattens at a non-zero level says that some users keep getting value. A curve that falls to zero says the value did not stick.
- **"What would make you change a guardrail's threshold?"** New evidence about the noise in the metric, or a change in what the product is for. Changing it after a result is the mistake to avoid.

## Revision cheat-sheet

![Chapter 15 on one page: six lenses, one question each.](diagrams/l12-big-picture.svg)

- **15.1** A North Star is the value delivered to customers, not revenue or sign-ups. Name two or three inputs and a guardrail. Facebook MAU, Spotify listening, Airbnb nights booked and Slack's team messages are the vault's examples.
- **15.2** AARRR: acquisition, activation, retention, referral, revenue. One primary metric per stage. Find the weakest stage and ask for the cheapest experiment.
- **15.3** HEART: happiness, engagement, adoption, retention, task success. Goals, signals and metrics for three or four dimensions. Task success is the most diagnostic.
- **15.4** Track the conversion between each funnel step. For a marketplace, name both sides and the match. Use cohort retention curves. LTV / CAC above about 3 is a rule of thumb.
- **15.5** Every primary metric invites gaming. Set guardrails and thresholds before the test, and decide what happens if one breaks.
- **15.6** Metric tree: break one number into the drivers that multiply or add up to it. Verify, quantify, segment, walk the branch that moved, map to causes, then test.
- **Beyond the notes:** write the metric definition; check the denominator; split the average; name a guardrail threshold before the launch.

## Self-test

<details class="quiz"><summary>What makes a good North Star metric?

It reflects value received by the customer, leads revenue rather than lagging it, is measurable by every team, and moves with product work without swinging daily.

</details>

<details class="quiz"><summary>What are input metrics, and how do they relate to a North Star?

Input metrics sit under the North Star and are what teams actually own, such as new-user activation, playlist creation and session starts for a listening product.

</details>

<details class="quiz"><summary>What are the five stages of AARRR?

Acquisition, activation, retention, referral and revenue. Pick one primary metric per stage and find the weakest one.

</details>

<details class="quiz"><summary>What are the three layers of the Goals-Signals-Metrics process in HEART?

A goal (a broad objective), a signal (an observable behaviour or attitude that shows progress) and a metric (a quantifiable data point).

</details>

<details class="quiz"><summary>Why does the Dropbox referral case matter for AARRR?

Both sides of a referral got extra storage, and Dropbox grew from roughly 100,000 to about 4 million users between late 2008 and late 2009. Invite conversion was a key stage metric.

</details>

<details class="quiz"><summary>What is the simple LTV formula in the vault's cheat sheet, and what rule of thumb goes with LTV / CAC?

LTV is revenue per user per period divided by the churn rate per period. LTV / CAC above about 3 is a common rule of thumb for healthy unit economics.

</details>

<details class="quiz"><summary>What is a guardrail metric, and when do you set its threshold?

A guardrail is a metric that must stay healthy while you optimise the primary one. Set the threshold before the test, not after.

</details>

<details class="quiz"><summary>What are the six steps of the diagnosing sequence for a metric drop?

Verify the metric, quantify it, segment it, walk the tree to the branch that moved, map it to causes (internal, external or instrumentation), and test the cheapest hypothesis.

</details>

<details class="quiz"><summary>(Beyond the notes) Why can a ratio rise while the business gets worse?

The bottom number may have shrunk, or the population the rate is over may have changed. Check the denominator and the segments before believing the number.

</details>

<details class="quiz"><summary>(Beyond the notes) How would you tell a real retention improvement from a cohort artifact?

Compare cohorts of the same age from the same source, check whether a promo or channel explains the change, and compare against a matched earlier cohort.

</details>

<details class="quiz"><summary>(Beyond the notes) What do you do before you act on a small guardrail breach in noisy data?

Measure the normal noise first (for example with an A/A test), set the threshold outside that range, and use a longer window before acting.

</details>


# Chapter 16 · Root Cause Analysis

<!-- lecture n="13" label="16" short="Root cause analysis" status="done" kind="RCA" -->

## At a glance

| Question | Short answer |
|---|---|
| What kind of question is this? | "A metric dropped X%. What would you do?" It tests structuring, prioritisation and convergence. |
| What is the first move? | Clarify the terms and **verify the metric**. Many "drops" are measurement errors. |
| How do you scope it? | Reach (region, platform, OS, segment) and shape (sudden or gradual, absolute or percentage, baseline). |
| How do you localise the problem? | Walk one **linear user journey** and find the first stage where the metric moved. |
| How do you split the causes? | **Internal** (your release, bug, pricing) vs **external** (competitors, seasons, sentiment). |
| What does the shape of the drop tell you? | Sudden: suspect a release, outage or bug. Gradual: suspect a behaviour or market shift. |
| What is different for AI products? | Four extra checks: **model changes, prompt regressions, data drift, cost spikes**. |
| How do you close? | One most-probable root cause with a logical path, then solutions ranked by impact and effort. |
| What is the 5 Whys? *(Beyond the notes)* | Ask "why" again and again, so each answer becomes the next question. |
| What is a fishbone? *(Beyond the notes)* | An Ishikawa diagram: the effect at the head, cause categories on the bones. |

> [!NOTE] Where this comes from
> Built from three source books: the Sigma PM concept book (Chapter 8, Root Cause Analysis), the Sigma PM casebook (2023-2024, the RCA approach slide) and the XLRI PM Casebook 2023 (Root Cause Analysis Approach). Section 16.4 is built on the general RCA sequence from the Sigma concept book and on general AI product knowledge, including two public events. The vault's further-reading list (Blogs & Newsletters, Product Teardowns, AI Product Reading) is named, but no links are kept here.

## The big picture

> A vague "metric dropped" sentence is one of the most common PM interview questions. A repeatable sequence turns it into an answer: scope the problem, walk the user journey, split internal from external causes, and add an AI layer for AI products.

The chapter has four parts:

1. Scoping: clarify, verify the metric, check platforms and segments (16.1).
2. Walking the user journey to find the stage where behaviour changed (16.2).
3. Internal vs external causes (16.3).
4. AI-specific RCA: model changes, prompt regressions, data drift and cost spikes (16.4).

![The RCA sequence on one line: scope, walk the journey, split the causes, then add the AI checks when the product is AI.](diagrams/l13-rca-sequence.svg)

**Key takeaways**

- Converge on a single most-probable root cause, with a logical path to it.
- Verify the metric first. Many "drops" are instrumentation errors.
- Use the user journey to localise the problem before you brainstorm causes.
- Sudden drops usually mean a release, outage or bug. Gradual drops usually mean behaviour or market shifts.
- Close with solutions for the root cause, prioritised by impact and effort.

## 16.1 Scoping: clarify, verify metrics, check platforms and segments

> Before you explain a drop, make sure the drop is real, define it precisely, and find out who and where it affects.

### Concept

A root-cause prompt is usually one vague sentence. Scoping turns it into a precise problem. The source material agrees on four moves:

1. **Clarify key terms.** The interviewer's "feature is not visible" could mean poor placement, a missing option or a rendering bug. Ask.
2. **Verify the metric.** Check that the number is right. Ask how it is measured, whether the definition changed, and whether the tracking tool changed. Bad data or a wrong threshold often produces the "drop."
3. **Scope the reach.** Geography, platform (web, Android, iOS), OS version, demographic and user segment. Is it everyone or a subset?
4. **Scope the shape.** Sudden or gradual? Absolute number or percentage? Compared to what baseline? A small absolute number can look like a huge percentage.

**Scoping questions to ask (checklist)**

- Is the metric per user or overall? Compared to yesterday, last week, or the average?
- Did we change how we calculate this metric?
- Which platform, OS and app version?
- Which region and which user segment?
- When was it first noticed? Did anything ship, change or get promoted around then?
- Is it internal or external users who are affected?

**Output of this step:** a restated problem in one sentence, like the Sigma worked answer: "This month we discovered an 80% drop in a key metric on mobile platforms (all devices), affecting external customers in all markets." Confirm it with the interviewer before going further.

![The scoping checklist turns one vague sentence into a restated problem. Confirm the restatement before you analyse.](diagrams/l13-scoping-checklist.svg)

### Real-world examples

- **Streaming video key metric down 80% (Sigma concept book, Chapter 8, Practice Question 1):** before any causes, the candidate confirmed it was a mature product, that the absolute number was also large, that all markets were affected, that external customers (not internal users) were hit, and that it was mobile-only but not device-specific. Only then did they restate the problem.
- **Facebook Groups usage down 15% (Sigma concept book, Practice Question 2):** the candidate first defined "usage" (post, read, connect, discuss, buy/sell), and with the interviewer narrowed it to "posts per group per user" for topic-discussion groups.
- **YouTube average view duration down 20% (Sigma concept book):** the book's example for verifying the metric. Ask how engagement is quantified, since when, and whether the measurement tool changed.
- **Mobile banking uninstalls (XLRI casebook):** scoping showed the rise was India-wide, individual (not business) customers, both Android and iOS, and gradual since last weekend.
- **Generic (Sigma casebook):** "Metric ABC dropped X%" is answered by defining the metric, confirming the context, and asking whether the drop was sudden or gradual.

### Practice questions

> [!INTERVIEW] "Our DAU dropped 12% last week. What would you do?" List your first five questions.
> *(Beyond the notes: a starting point, built from the checklist above.)* Is DAU measured the same way as before? Which platforms, OS versions and app releases are in the drop? Which regions and segments? Did the drop start on one day or build over the week? Did any release, promotion or outage land just before it?

> [!INTERVIEW] How would you tell a real drop from a logging bug?
> **Answer outline (Q2):** Compare event counts from the raw log pipeline against the dashboard. Check for a change in event names or SDK version. Check whether the drop appears across all platforms, which would suggest a shared pipeline. Check for missing days or partial data.

> [!INTERVIEW] Why does the sudden vs gradual question matter?
> *(Beyond the notes: a starting point.)* The shape points to the bucket. A sudden step usually follows a change you made (release, config, outage), so you look inside first. A slow slide usually follows a change in behaviour or the market, so you look outside first. Asking the question also rules out a measurement change that happened on one day.

*Related:* Chapter 15 (Metric trees and diagnosing metric movement), Chapter 16 (2: Walking the user journey; 3: Internal vs external causes), Chapter 22 (Root cause analysis and diagnosis cases).

## 16.2 Walking the user journey

> Draw the end-to-end journey, then find the single stage where behaviour changed. That stage holds the root cause.

### Concept

Once the problem is scoped, map the user journey as a linear sequence of steps. Every user interaction can be split into three buckets, as the Sigma concept book suggests:

- **Input:** where information enters (the user enters data, taps a button, pays).
- **Process:** what the backend does with it (validation, calculation, matching, routing).
- **Output:** what the user sees back (the screen, the confirmation, the result).

Walking the flow through these buckets narrows the problem domain step by step. Ask the interviewer for the metric at each stage and find where the change first appears. The stage where the metric changes is where you zoom in.

**How to run it**

1. Write a single linear journey, with no branches, e.g. open app, search, view item, add to cart, pay, confirm.
2. Attach the metric at each stage (conversion, drop-off, time-on-step).
3. Find the first stage where the conversion rate moved relative to the baseline.
4. Within that stage, ask what changed: layout, copy, backend logic, latency, dependency.

**Example from the Sigma concept book (streaming video, key metric down 80% on mobile):** the candidate listed download app, create account and pay subscription, log in, search, filter, find, watch and log out. Then they asked whether app downloads were also down. They were not. The drop was in paid mobile monthly subscribers, so the investigation focused on the subscription step.

**When the journey alone does not converge (Sigma's top-down approach):** build a tree with the problem at the root, split it into sub-problems, rule branches out as you get answers, and go deeper only on the branches left. The 5 Whys and fishbone (Ishikawa) diagrams are the named techniques for this.

**Pitfall:** trying to analyse every stage in parallel. Walk the chain in order and stop when you find the break.

![Walk the chain in order. The first stage where the metric falls is the one you zoom into; the stages before it are clean.](diagrams/l13-journey-walk.svg)

### Real-world examples

- **Cart abandonment (XLRI casebook, cart-drop framework):** drop-off is located by checking each step of the single linear journey, then checking for layout changes at that step.
- **Check-out failure (illustrative):** a payment-stage drop after a new UPI flow release is traced to a changed confirmation screen.
- **Flipkart UGC engagement down 20% (Sigma casebook):** metrics at every stage before the Q&A section were flat, and Q&A impressions were flat, so the change was localised inside the Q&A section. Q&As viewed per session fell after a new text-search feature shipped. Conversion actually improved.

### Practice questions

> [!INTERVIEW] A user says they cannot see the changes they made in a web portal. Use input, process and output to diagnose.
> **Answer outline (Q1):** Input: did the save request go out? Check the request log. Process: did the backend persist it? Check the write success rate. Output: did the front end fetch and render it? Check for read errors. Each stage has a different owner and fix.

> [!INTERVIEW] Walk the journey for an online food order and find the likely break for a 15% fall in completed orders.
> *(Beyond the notes: a starting point.)* Lay the stages out in order: open app, choose restaurant, add items, pay, restaurant accepts, rider assigned, delivered, rated. Attach the completion rate to each one, find the first stage where it fell against last month, then ask what changed in that stage: a new payment option, a menu change, a rider-matching change or a fee change.

> [!INTERVIEW] Why must the journey be linear for this method?
> *(Beyond the notes: a starting point.)* A single chain gives one order of stages, so the first stage where the metric moved is well defined. Branches let the same drop sit in two places at once, and you cannot say which stage broke first.

*Related:* Chapter 16 (1: Scoping; 3: Internal vs external causes), Chapter 15 (4: Funnel, marketplace and retention metrics), Chapter 13 (1: Five-step critique: JTBD, personas, familiarity, inclusivity, zoom levels), Chapter 22 (Root cause analysis and diagnosis cases).

## 16.3 Internal vs external causes

> Split candidate causes into what your team changed and what happened around you. The two lead to different fixes and different timelines.

### Concept

Root causes fall into two buckets. Name both explicitly, because the bucket changes your recommendation.

**Internal causes (your product, your company)**

- **Releases and bugs:** a new version, a broken flow, a crash. Often a sudden drop.
- **Technical factors:** downtime, latency, errors, failed dependencies.
- **Product and UX changes:** moved buttons, changed copy, removed features.
- **Business and operations:** pricing change, cost or supply problems, a marketing pause.
- **Cannibalisation:** a new free feature eats into a paid one.

**External causes (market, users, world)**

- **Competitors:** a new entrant, a discount, a free offer, a campaign.
- **Substitutes:** a new category that replaces your product.
- **Macro and regulation:** a new tax, a policy change, a strike, a pandemic.
- **Seasonality and events:** festival periods, exam seasons, weather.
- **Sentiment:** bad press, social media backlash, shifts in user behaviour.
- **Device or platform changes:** fewer devices sold, OS updates that break a flow.

**How to tell them apart**

- Sudden drop: suspect internal first (release, outage, bug).
- Gradual drop: suspect external first (competition, seasonality, behaviour shift).
- Check whether the drop is shared across competitors or only yours.

**Recommendation rule:** internal causes can be fixed by a hotfix or a rollback. External causes need escalation, strategy and more stakeholders (Sigma casebook). Either way, list several solutions and prioritise them on an impact vs effort matrix (Sigma concept book).

![Every candidate cause sits in one of two branches. The branch decides the fix: hotfix or rollback inside, escalation and strategy outside.](diagrams/l13-cause-tree.svg)

### Real-world examples

- **Free competitor on mobile (Sigma concept book, streaming case):** the candidate ruled out internal causes in order (metric definition, seasonality, incidents, a laggy release, cannibalisation by a free feature) and external ones (mobile device sales, macro factors) until the interviewer confirmed a competitor: a new entrant offering free video on mobile caused the 80% drop in paid mobile monthly subscriptions.
- **Own campaign, not the competitor (XLRI casebook, mobile banking uninstalls):** a neobank launch looked like the external cause, but the candidate argued loyal banking customers rarely switch that fast. The real cause was internal: users acquired by the bank's own free-credit install campaign uninstalled after using the credit. Lesson: a plausible external story should not stop you checking internal changes.
- **Ride-hailing price war (illustrative):** a rival's aggressive discounting causes rider drop-off in one city, an external cause.
- **Release regression (illustrative):** a checkout redesign reduces conversion the day it ships, an internal cause.

### Practice questions

> [!INTERVIEW] A streaming app's monthly subscriptions fell 30% over three weeks. Internal or external? Justify.
> **Answer outline (Q1):** A three-week decline is gradual, so start external (competitor pricing, substitutes, seasonal patterns). Still check internal changes in that window and compare against the rest of the market.

> [!INTERVIEW] Your app's crash rate jumped the morning after a release. What do you say first?
> *(Beyond the notes: a starting point.)* Internal, and a sudden step on a known date. Say the release first, then check the crash by version, device and OS, and decide whether a rollback or a hotfix stops it. Confirm the metric is measured the same way before you act.

> [!INTERVIEW] A government announces a new tax on digital services. How does it change your RCA?
> *(Beyond the notes: a starting point.)* It is an external, macro cause, so it moves the search to escalation and strategy: which of your prices, fees or regions the tax touches, and how much of it you pass on. Check the timing against your metric before you blame it, and still rule out internal changes in the same window.

*Related:* Chapter 16 (1: Scoping; 2: Walking the user journey; 4: AI-specific RCA), Chapter 19 (3: Competitive analysis and moats), Chapter 15 (6: Metric trees and diagnosing metric movement).

## 16.4 AI-specific RCA: model changes, prompt regressions, data drift, cost spikes

> AI products fail in ways that look like no code changed. Add model, prompt, data and cost checks to the standard RCA sequence.

### Concept

The standard RCA flow still applies: scope, verify, walk the journey, split internal and external. AI products add four causes that rarely show up in normal software and must be checked explicitly.

**1. Model changes (internal, but vendor-driven)**

- A provider updates the model behind an API alias, or retires a version.
- Symptoms: output style, accuracy or refusal rate shifts with no change on your side.
- Check: pin the model version and compare outputs on the same golden set before and after the change date.

**2. Prompt regressions (internal)**

- A prompt edit, a new system instruction or a changed few-shot example makes quality worse for some inputs.
- Check: diff the prompt history against the metric timeline. Re-run the offline eval suite on old and new prompts (see Chapter 8, Regression testing when models or prompts change).

**3. Data drift (internal or external)**

- Input data changes: users ask new kinds of questions, a document corpus is re-indexed, a retrieval source goes stale, or a feature changes meaning.
- Symptoms: gradual quality decline, rising "I don't know" answers, rising edit rates.
- Check: compare the distribution of inputs and retrieved context across time windows.

**4. Cost spikes (internal)**

- Token usage per request rises: longer context, a retry loop, an agent that calls tools repeatedly, or a new feature that sends too much history.
- Check: break cost into input tokens, output tokens, retries and calls per task. Compare cost per successful task, not cost per request.

**Diagnosis order I would use**

1. Verify: is the eval or telemetry pipeline itself broken?
2. Check for a vendor model change (version or alias).
3. Check for your own prompt, retrieval or data changes in the same window.
4. Check cost per successful task for a spike.
5. Separate quality issues (which need eval) from cost issues (which need routing, caching or limits).

![The four AI causes hang off the same RCA tree. Each one has its own symptom and its own check.](diagrams/l13-ai-rca-tree.svg)

![Diagnose in this order. Verify the measurement first, then the vendor, then your own changes, then cost.](diagrams/l13-ai-diagnosis-order.svg)

### Real-world examples

- **GPT-4 behaviour drift (Stanford/Berkeley study, 2023):** Lingjiao Chen, Matei Zaharia and James Zou compared the March and June 2023 versions of GPT-4 and GPT-3.5 behind the same product names, and found large shifts on some tasks (for example, identifying prime numbers and generating directly runnable code). The lesson for PMs: the same model name can behave differently over time, so pin versions and re-run evals.
- **OpenAI GPT-4o rollback (April 2025):** OpenAI rolled back a GPT-4o update in ChatGPT after users reported overly flattering, sycophantic replies. OpenAI said the update had leaned too heavily on short-term user feedback signals. A real case of a model change causing a quality regression with no change on the user's side.
- **Retrieval index refresh (illustrative):** a support copilot starts citing outdated policy pages after an index rebuild. It looks like hallucination but is a data-freshness problem.
- **Agent loop cost spike (illustrative):** a tool-calling agent retries on a malformed response, multiplying the per-task token cost.

### Practice questions

> [!INTERVIEW] Users say the AI assistant "got worse" last week, but no release shipped. What do you check?
> **Answer outline (Q1):** First confirm the eval and telemetry are sound. Next check the provider's model version or alias history. Then compare the golden set on the pinned old and new model. If the golden set is stable but live output changed, the input distribution has shifted, which points to data drift.

> [!INTERVIEW] Cost per conversation doubled while usage was flat. Walk through your diagnosis.
> *(Beyond the notes: a starting point.)* Split the cost into input tokens, output tokens, retries and calls per task. A longer prompt or extra history shows up in input tokens. A retry loop or a tool-calling agent shows up in calls per task. Compare cost per successful task, then decide between routing, caching or limits.

> [!INTERVIEW] How would you tell prompt regression from data drift?
> *(Beyond the notes: a starting point.)* Hold the input fixed and change the prompt: if the golden set drops, the prompt is the cause. If the prompt is unchanged and the golden set is stable while live quality falls, the live inputs or retrieved context have changed, which is drift.

*Related:* Chapter 16 (1: Scoping; 3: Internal vs external causes), Chapter 8 (3: Online metrics: task success, acceptance and edit rate, retention of AI users; 5: Regression testing when models or prompts change), Chapter 10 (2: Monitoring drift and vendor model updates), Chapter 6 (2: Unit economics: cost per task, inference cost, gross margin).

## Beyond the notes: 5 Whys and the fishbone in practice

*(Beyond the notes: the two named techniques from 16.2, explained in more detail than the vault gives them. Both are for converging on one cause once the journey has narrowed the stage.)*

**The 5 Whys.** Write the problem at the top, ask "why did this happen?" and write the answer. Ask why about that answer, and repeat until you reach something you can act on. Five is a rule of thumb, not a rule. The chain stops when the answer is a process or a change you can fix.

Example, a checkout drop:

1. Why did checkout conversion fall? Because the pay button was hard to find on Android.
2. Why was it hard to find? Because the new layout moved it below the fold.
3. Why did the layout move? Because the redesign was shipped without an Android screen review.
4. Why was no review done? Because the release checklist covers iOS only.
5. Why does the checklist cover iOS only? Because it was copied from an older iOS-only release.

The fix is at the bottom of the chain (the checklist), and the hotfix for the button is at the top.

**The fishbone (Ishikawa) diagram.** Write the effect at the head of a fish, then draw cause categories as bones pointing to the spine. Common categories are people, process, product, technology, data and environment, and you can rename them to suit the product. Brainstorm causes into the bones, then test each one against the data. Causes that cannot be tested are noted, not ranked.

![A fishbone holds the effect at the head and groups the candidate causes on the bones. Test each cause against data before you rank it.](diagrams/l13-fishbone.svg)

## Beyond the notes: pitfalls

- **Anchoring on the first story.** An external story that fits well can stop the search early. Check internal changes in the same window, as the XLRI uninstall case shows.
- **Treating a correlated change as the cause.** Two things that moved on the same day need a test, such as a holdout or a rollback, before one is called the cause.
- **Comparing against the wrong baseline.** A drop against last week can be a normal weekday pattern. Compare the same weekday, or the same period last year where seasonality matters.
- **Ignoring the tail of the data.** A total can hide one segment that fell sharply, which is why segments are scoped first.
- **Calling it a root cause without a fix.** Close each cause with the action that would stop it, and with the metric that would show it worked.

## Beyond the notes: interview corner

- **"Where do you start?"** Restate the problem in one sentence, then ask about the metric definition before you ask about causes.
- **"How do you know you have found it?"** The cause explains the timing (when it started), the reach (which segments) and the shape (sudden or gradual). If one of the three does not fit, keep looking.
- **"What do you recommend?"** Name the bucket first (internal or external), then the fix (hotfix, rollback, escalation, strategy), then rank the fixes on impact and effort.
- **"How is an AI RCA different?"** Verify the eval, then check the vendor and your own prompt, retrieval and data changes, then the cost. A quality drop with no release is not a mystery until the model version is pinned.

## Revision cheat-sheet

![Chapter 16 on one page: the sequence, the two cause buckets, and the four AI causes.](diagrams/l13-big-picture.svg)

- **16.1** Scope before you analyse. Clarify terms, **verify the metric**, scope the reach (region, platform, OS, segment) and the shape (sudden or gradual, absolute or percentage, baseline). Restate the problem in one sentence and confirm it.
- **16.2** Walk one **linear journey** with input, process and output. Attach a metric to each stage and find the first stage where it moved. Do not analyse stages in parallel.
- **16.3** Split causes into **internal** (releases, bugs, pricing, cannibalisation) and **external** (competitors, substitutes, macro, seasonality, sentiment). Sudden suggests internal; gradual suggests external. Internal is fixed by hotfix or rollback; external by escalation and strategy.
- **16.4** AI adds **model changes, prompt regressions, data drift and cost spikes**. Verify the eval, check the vendor version, check your own changes, check cost per successful task, then split quality from cost.
- **Beyond the notes:** 5 Whys, the fishbone, the pitfalls of anchoring and wrong baselines.

## Self-test

<details class="quiz"><summary>Why verify the metric before you explain a drop?

Many "drops" are instrumentation errors: a changed event name, an SDK update, a wrong threshold or missing days. Ask how the metric is measured and whether the definition or the tracking tool changed.

</details>

<details class="quiz"><summary>What should the output of the scoping step look like?

A restated problem in one sentence, with the metric, the platform, the reach and the shape, for example "an 80% drop in a key metric on mobile, affecting external customers in all markets." Confirm it with the interviewer.

</details>

<details class="quiz"><summary>What are the three buckets used to walk a user journey?

Input (where information enters), process (what the backend does with it) and output (what the user sees back).

</details>

<details class="quiz"><summary>Why must the journey be walked as a single linear chain?

So you can find the first stage where the metric changed and zoom in there. Analysing every stage in parallel dilutes the search, and branches let one drop sit in two places.

</details>

<details class="quiz"><summary>What does a sudden drop point to, and what does a gradual drop point to?

A sudden drop usually points to an internal cause: a release, outage or bug. A gradual drop usually points to an external cause: competition, seasonality or a shift in behaviour.

</details>

<details class="quiz"><summary>How does the Sigma streaming case show that a competitor was the cause?

After ruling out internal causes in order (metric definition, seasonality, incidents, a laggy release, cannibalisation) and external ones (device sales, macro factors), the interviewer confirmed a new entrant offering free video on mobile.

</details>

<details class="quiz"><summary>What are the four AI-specific causes to check?

Model changes (a vendor update behind an alias), prompt regressions (a prompt edit that hurts some inputs), data drift (changed inputs or retrieved context) and cost spikes (more tokens, retries or calls per task).

</details>

<details class="quiz"><summary>Why pin the model version before comparing outputs?

The same model name can behave differently over time. Pin the version and compare outputs on the same golden set before and after the change date, as the GPT-4 drift study showed.

</details>

<details class="quiz"><summary>Why does the AI diagnosis start with the eval and telemetry?

If the measurement is broken, the "quality drop" may not exist. Confirm the pipeline is sound before you blame the model, the vendor or your prompts.

</details>

<details class="quiz"><summary>(Beyond the notes) How does the 5 Whys end?

When the chain reaches a process or a change you can fix. The fix at the bottom of the chain stops the problem from recurring; a hotfix at the top only treats the symptom.

</details>

<details class="quiz"><summary>(Beyond the notes) What does a fishbone diagram do that a list does not?

It groups candidate causes into categories on the bones and shows them against one effect at the head, so you can see which category holds most of the causes and test each one against the data.

</details>

<details class="quiz"><summary>(Beyond the notes) Why can a total hide the real root cause?

A total can stay flat while one segment falls sharply and another rises. Scope the reach by segment before you read the total.

</details>


# Chapter 17 · Pricing and Monetization

<!-- lecture n="14" label="17" short="Pricing" status="done" kind="pricing" -->

## At a glance

| Question | Short answer |
|---|---|
| How do you start a pricing answer? | From the business goal (share or profit), then the customer's willingness to pay. |
| What are the three anchors? | **Cost** is the floor, **competitors** are the reference, **customer value** is the ceiling. |
| Which anchor usually leads? | **Value-based** pricing, when value is measurable and you have evidence of willingness to pay. |
| How do you choose a monetization model? | Follow where the value is created: the user, the usage, the transaction or the attention. |
| When does freemium work? | When the free tier brings users in and the paid tier serves a clear need. |
| What is a take rate? | A percentage of each transaction a marketplace facilitates. |
| How do you test a price? | Start with cheap reads (surveys, fake doors), then a controlled live cohort. |
| What do you judge a test on? | Revenue per user and retention together, not conversion alone. |
| What is a common trap? *(Beyond the notes)* | A higher price with fewer buyers can still lose money or raise churn later. |
| How do you use this in an interview? *(Beyond the notes)* | Name the goal, the three anchors, a model, then the test that proves it. |

> [!NOTE] Where this comes from
> Built mainly from the Sigma PM concept book (Monetary Strategy: Pricing Methodology and Prevalent Models). Sections 17.2 and 17.3 also use the "Dominant Revenue Models" chart in the vault's Others folder. Take rate, per-seat and outcome models, the survey methods and the Netflix and Amazon cases are general product knowledge, as the vault itself says. No links are kept here.

## The big picture

> Pricing questions ask how you would price X, which monetization model fits Y, and how you would test a price change. Strong answers start from the business goal and the customer's willingness to pay, pick a model, then describe how to validate it.

The chapter covers three things:

1. How to choose a price basis (17.1).
2. How to pick a monetization model (17.2).
3. How to test pricing safely (17.3).

**Key takeaways**

- Start from the business goal (market share or profitability) before picking a price. Triangulate cost (floor), competitors (reference) and value (ceiling).
- Value-based pricing is usually the strongest anchor, but it needs evidence of willingness to pay.
- Freemium works only when the free tier brings users in and the paid tier serves a clear need.
- Pick the monetization model that matches where value is created: seats, usage, transactions or outcomes.
- Test prices with a holdout or a limited cohort, and watch retention and churn as well as conversion.

## 17.1 Cost-plus, value-based, and competitive pricing

> Every price is an anchor: cost sets the floor, competitors set the reference point, and customer value sets the ceiling.

### Concept

There are three standard ways to set a price. Good answers name all three and say which one leads.

**Cost-based (cost-plus)**

- Add up fixed and variable costs per unit, then apply a markup percentage.
- Use breakeven quantity to check whether the price can reach market-entry volume.
- Easy to defend internally, but it ignores what the customer would actually pay.

**Value-based**

- Estimate the total value the customer gets, then price a share of it.
- Factors: the customer's opportunity cost, time value of money, what the target segment earns and saves, and the size of the problem being solved.
- Usually gives the highest margin when the value is measurable (for example, hours saved or revenue unlocked).

**Competitor-based**

- Look at the nearest competitor's price and price close to it.
- Decide whether you are pricing offensively (undercut to win share) or defensively (match and differentiate).
- Risk: a price war that erodes margin for everyone.

**Framing the decision**

1. Business goal: market share or profitability?
2. Industry trend and product lifecycle stage: early, growth or mature?
3. Competitive benchmark: can a differentiated product carry a premium?
4. Readiness to pay in the target segment.
5. Promotional discounts needed: early adopters, time-bound, or referral-based.

The Sigma concept book's advice: in an interview, use a **combination of all three** to triangulate a price range, then pick a point in it based on the goal.

![Cost sets the floor, competitors set the reference, and value sets the ceiling. Pick a point in the band from the goal.](diagrams/l14-price-anchors.svg)

**Worked mini-example (invoicing app for Indian small businesses):**

- Cost floor: hosting, support and GST e-invoicing integration come to about ₹60 per customer per month, so anything below about ₹100 loses money after CAC.
- Competitor reference: established accounting tools charge a few hundred rupees a month for basic plans, with free tiers from newer players.
- Value ceiling: if the app saves 4 hours a month of a ₹250/hour bookkeeper's time and speeds up collections, value is roughly ₹1,000+ a month.
- Decision: goal is share in a price-sensitive segment, so price near the competitor reference (say ₹249/month), well under the value ceiling, with an annual discount and a free tier capped by invoice count. (All numbers illustrative.)

For AI products, cost-plus is harder than it looks because inference cost varies per query. Value-based pricing is often the better starting point, with cost used as a floor check (see Chapter 6, Unit economics: cost per task, inference cost, gross margin).

### Real-world examples

- **Slack** charges per user per month, and its "fair billing policy" bills only for members who are actually active, tying price to the value a team gets rather than to Slack's cost.
- **Adobe Creative Cloud** sells single-app plans and an "All Apps" plan, pricing on value across a creative workflow. The marginal cost of software is near zero, so cost-plus would be meaningless.
- **Zomato and Swiggy** charge restaurants commissions in a similar range and match each other's platform fees and subscription offers, a duopoly where competitor benchmarking strongly shapes pricing. (Illustrative of the dynamic; exact rates vary by restaurant and city.)

### Practice questions

> [!INTERVIEW] A startup is pricing a new invoicing tool for small businesses in India. Which pricing basis would you start from, and why?
> *(Beyond the notes: a starting point, using the worked example above.)* Start from value, since the time and collections saved are measurable. Use cost as the floor check, so the price clears the cost of hosting, support and compliance integrations. Then compare with the competitor reference and pick a point for the goal.

> [!INTERVIEW] Your competitor just cut prices by 30%. Do you match, hold, or differentiate? What data would change your answer?
> **Answer outline (Q2):**
> - Clarify the goal: share or margin.
> - Check whether the competitor's cut is sustainable for them.
> - Decide: match only if share is the goal and margin can absorb it; otherwise differentiate on value.
> - Name the data you need: win rate, churn, and willingness to pay in the segment.

> [!INTERVIEW] How would you estimate the value a B2B analytics product creates for a customer?
> *(Beyond the notes: a starting point.)* Count the hours of analyst time it replaces, multiply by the loaded cost of that time, then add any revenue the customer can unlock from faster decisions. Check the estimate with two or three customers before you price a share of it.

*Related:* Chapter 17 (2: Monetization models; 3: Running pricing experiments), Chapter 6 (2: Unit economics: cost per task, inference cost, gross margin; 3: Pricing models: per seat, usage-based, outcome-based, bundled).

## 17.2 Monetization models: subscription, freemium, ads, take rate, razor-and-blade, bundling

> The right model follows where the value is created: the user, the usage, the transaction, or the attention.

### Concept

The Sigma concept book lists the core models. Take rate and per-seat pricing are added for marketplaces and B2B.

| Model | How it earns | Works when | Watch out for |
|---|---|---|---|
| **Freemium** | Free core, paid premium features | Free users bring network or data value; a segment has a clear paid need | Free tier so generous nobody upgrades |
| **Subscription** | Recurring fee (monthly/annual) | Value recurs; the product is used regularly | Churn; "is it worth $X per month?" |
| **Advertising** | Fees from ad impressions or clicks | High engagement, low willingness to pay | Ads hurt experience; relevance drives CTR |
| **Take rate** | % of each transaction on a marketplace | Platform facilitates payments or bookings | Sellers leave if the cut feels too high |
| **In-app purchase / add-ons** | Pay for extras on a free base | Games, content, cosmetics | Pay-to-win perception |
| **Fixed price (one-time)** | One payment, lifetime access | Low-frequency, high-value purchase | No recurring revenue |
| **Razor-and-blade** | Cheap hardware, expensive consumables or software | Locked-in ecosystem | Customers buy the razor and switch to a cheaper blade |
| **Bundling** | Multiple products sold together | Cross-sell and lower churn | Bundle feels forced; customers pay for unused features |
| **Per seat / usage / outcome** | Charge per user, per unit consumed, or per result | B2B; AI products with variable cost | Forecasting revenue; billing complexity |

**A quick way to choose (from the "Dominant revenue models" chart in the sources):** low transaction frequency with high value suits one-time purchases (hardware, licences). Recurring use suits subscriptions (Spotify, Netflix, Office 365, Prime). High frequency with low willingness to pay suits ads (Facebook, Instagram). Facilitating someone else's transaction suits a "tax" or take rate (Uber, AWS usage billing).

![Each model follows where the value sits. Ask who gets the value before you choose the model.](diagrams/l14-monetization-map.svg)

**Questions to ask before choosing**

- Who gets the value: the end user, the buyer, or a third party?
- Does value recur, or is it a one-time event?
- Does the product's cost scale with usage?
- Does the model help or hurt the core experience?

### Real-world examples

- **Spotify** uses freemium: a free tier with ads, and a paid Premium subscription with no ads and offline listening.
- **Slack** uses freemium with per-user paid plans, a product-led path to paid seats.
- **Netflix** launched "Basic with Ads" in November 2022 alongside its ad-free tiers, to serve price-sensitive viewers and add ad revenue.
- **Amazon Prime** bundles shipping, video and other benefits into one subscription, which raises switching costs.
- **Apple App Store** takes a commission on digital purchases (30% standard, 15% for small developers and for subscriptions after the first year), a take-rate model on a platform.
- **Razorpay** charges merchants a percentage fee per transaction (around 2% on its standard plan for most domestic methods), a take rate on payments. UPI person-to-merchant payments themselves carry no merchant fee in India, which is why UPI apps monetise through lending, insurance and ads instead.
- **Swiggy One and Zomato Gold** are subscriptions layered on a marketplace: a fee in exchange for free delivery and discounts, which raises order frequency and loyalty.
- **Gaming consoles** are the classic razor-and-blade case (the Sigma book's own example). Consoles are often sold near or below cost at launch, and games, royalties and subscriptions such as PlayStation Plus carry the margin. Printers and ink, and Gillette razors and blades, are the other textbook cases.

### Practice questions

> [!INTERVIEW] Pick a monetization model for a free meditation app. Justify your choice and name one risk.
> *(Beyond the notes: a starting point.)* Freemium with a subscription on top fits: the core sessions are the free hook, and recurring use suits a recurring fee. The risk is a free tier so generous that few users upgrade, so keep the paid tier to depth (longer courses, offline packs) rather than the core habit.

> [!INTERVIEW] When would you choose take rate over subscription for a marketplace?
> *(Beyond the notes: a starting point.)* Take rate fits when value is created in each transaction (a booking, an order, a payment) and sellers would accept a cut of it. A subscription fits when buyers gain value from regular access whether or not they transact. Many marketplaces combine the two, as Swiggy One and Zomato Gold do.

> [!INTERVIEW] Your product has a free tier. How would you decide which features go behind the paywall?
> **Answer outline (Q3):**
> - Identify the "magic" core that drives engagement; keep it free.
> - Place a feature behind the paywall only if heavy users need it and it does not block the core job.
> - Test the boundary with a small cohort; watch conversion and free-to-paid churn.

*Related:* Chapter 17 (1: Cost-plus, value-based and competitive pricing; 3: Running pricing experiments), Chapter 6 (3: Pricing models: per seat, usage-based, outcome-based, bundled; 4: Defensibility: proprietary data, distribution, workflow integration, switching costs).

## 17.3 Running pricing experiments

> Test price with a controlled cohort, and judge it on revenue per user and retention together, not conversion alone.

### Concept

Pricing experiments are high-stakes because a bad change can lose customers quickly and cannot be undone. Good experiments are small, reversible where possible, and measured over a long enough window.

**Before a live test: cheaper ways to read willingness to pay**

- **Van Westendorp price sensitivity survey:** ask at what price the product is too cheap to trust, a bargain, getting expensive, and too expensive. The overlaps give an acceptable price range.
- **Gabor-Granger:** ask "would you buy at ₹X?" at descending prices to draw a demand curve.
- **Conjoint analysis:** users choose between bundles of features and prices, revealing what each feature is worth.
- **Fake-door / painted-door test:** show a paid plan and measure clicks before building it (disclose and apologise gracefully).

![Start with the cheapest read of willingness to pay. Each rung costs more and risks more real money.](diagrams/l14-price-test-ladder.svg)

**Design steps**

1. **Hypothesis:** "Raising the Pro plan from $8 to $10 keeps revenue per user up without raising churn more than 2 points."
2. **Choose the variable:** price level, price framing (monthly vs annual), discount, or what each tier includes.
3. **Choose the cohort:** new users only (lower risk, cleaner read) or a random slice of existing users (more signal, more risk). Avoid showing different prices to users who can compare them.
4. **Pick metrics:**
   - Primary: revenue per visitor or per user.
   - Guardrails: conversion, churn, refund rate, support tickets, and NPS.
   - Long-term: retention at 30 to 90 days.
5. **Run long enough** to cover a full billing cycle, since annual plans and churn lag the first purchase.
6. **Decide and communicate:** have a rollback plan and a plan for existing subscribers.

![A pricing test in six steps. The primary metric is revenue per user; the guardrails and the long-term retention stop a bad win.](diagrams/l14-ab-design.svg)

**Common pitfalls**

- Reading conversion alone: a higher price with fewer buyers can still lose revenue or raise churn later.
- Ignoring existing customers: a visible price rise to current users creates trust and support costs.
- Peeking early and stopping on noise.
- Testing too many variables at once, so the result cannot be attributed.

**For AI products:** price tests should watch usage per user as well. A cheaper plan can attract heavy users whose inference cost erodes margin (see Chapter 6, Unit economics: cost per task, inference cost, gross margin).

### Try it locally: a price test read on revenue per visitor

*(Beyond the notes: reproduced locally with the standard library. The visitor count and prices are illustrative. Variant A is the control.)*

```python title="lab_p14_price_test.py"
# One month of visitors on a Pro plan. Revenue per visitor is the number to read.
visitors = 10_000
variants = {
    "A  price 8.00, 5.0% buy":  (8.00, 0.050),    # control
    "B  price 9.00, 4.5% buy":  (9.00, 0.045),    # buy rate down 10%
    "C  price 10.00, 4.5% buy": (10.00, 0.045),
}
base_rpv = 8.00 * 0.050
for name, (price, conv) in variants.items():
    buyers = visitors * conv
    revenue = buyers * price
    rpv = revenue / visitors
    change = (rpv / base_rpv - 1) * 100
    print(f"{name}: buyers {buyers:.0f}, revenue {revenue:,.0f}, "
          f"per visitor {rpv:.3f} ({change:+.1f}%)")
```

```output
A  price 8.00, 5.0% buy: buyers 500, revenue 4,000, per visitor 0.400 (+0.0%)
B  price 9.00, 4.5% buy: buyers 450, revenue 4,050, per visitor 0.405 (+1.2%)
C  price 10.00, 4.5% buy: buyers 450, revenue 4,500, per visitor 0.450 (+12.5%)
```

Read the buy rate on its own and variant B looks like a loss: 10% fewer buyers. Read revenue per visitor and B still earns slightly more, because the higher price more than covers the fewer buyers. Variant C shows the same buy rate with a bigger price rise. Neither line tells you about churn. That is why the design steps above add retention at 30 to 90 days to the readout before the decision.

![At the same buy rate, a higher price lifts revenue per visitor. Conversion alone would have called B a loss.](diagrams/l14-price-readout.svg)

### Real-world examples

- **Netflix in India:** after testing a cheaper mobile-only plan, Netflix launched it in India in 2019 at ₹199 a month, its first market for that plan. In December 2021 it cut Indian prices sharply (the mobile plan to ₹149, Basic from ₹499 to ₹199). A real case of testing and region-specific pricing for a price-sensitive market.
- **Amazon's 2000 DVD price test:** customers discovered they were being shown different prices for the same DVDs. After a backlash Jeff Bezos apologised, said the test was random rather than based on customer data, and refunded the difference. This is the cautionary tale behind "avoid showing different prices to users who can compare them".
- **SaaS annual vs monthly defaults (illustrative):** testing which billing period is pre-selected on new sign-ups only, then judging on revenue per visitor and 90-day churn.

### Practice questions

> [!INTERVIEW] How would you test whether raising your subscription price by 20% is safe?
> *(Beyond the notes: a starting point.)* Pick the cheap reads first (a survey on the new price, or a fake-door plan). Then run a live test on new users only, with a hypothesis that states the revenue and churn you would accept. Run it through a full billing cycle and keep existing subscribers out of the first round.

> [!INTERVIEW] The price test shows conversion down 10% but revenue per visitor up 5%. What do you do?
> **Answer outline (Q2):**
> - Do not call it on conversion alone; check revenue per visitor and the margin impact.
> - Check whether the drop is concentrated in one segment.
> - Look at churn and refund data over the billing cycle before deciding.
> - Keep the test running or roll out in stages if the signal is mixed.

> [!INTERVIEW] What would you monitor in the first week of a pricing experiment?
> *(Beyond the notes: a starting point.)* Watch the guardrails first: buy rate by segment, refund requests, support tickets about price, and any complaint from a user who can see both prices. Do not read revenue as final until a full billing cycle has passed.

*Related:* Chapter 17 (1: Cost-plus, value-based and competitive pricing; 2: Monetization models), Chapter 15 (5: Guardrail and negative metrics), Chapter 10 (1: Staged rollouts and kill switches).

## Beyond the notes: launch checklist for a price change

*(Beyond the notes: general practice, not from the vault.)*

- Write the hypothesis and the guardrail thresholds before the test starts, with the revenue and churn numbers you would accept.
- Decide how existing subscribers are handled before any new visitor sees the price.
- Check that the test cohort cannot compare prices with each other (a shared link, a forum, a friend's account).
- Set the readout date from the billing cycle, not from the day traffic looks good.
- Plan the rollback: which plan is restored, for whom, and how refunds or credits are handled.

## Beyond the notes: take rate in practice

*(Beyond the notes: reproduced locally with the standard library. The order count and order size are illustrative.)*

```python title="lab_p14_take_rate.py"
# A marketplace earns a share of every order. Compare take rates on the same volume.
orders = 20_000          # orders per month
avg_order = 500          # rupees of gross merchandise value (GMV) per order
gmv = orders * avg_order
print(f"GMV per month: {gmv:,} rupees")
for take in (0.02, 0.10, 0.20):
    revenue = gmv * take
    print(f"take rate {take:.0%}: platform revenue {revenue:,.0f} rupees a month")
```

```output
GMV per month: 10,000,000 rupees
take rate 2%: platform revenue 200,000 rupees a month
take rate 10%: platform revenue 1,000,000 rupees a month
take rate 20%: platform revenue 2,000,000 rupees a month
```

The same volume gives very different revenue at each take rate. The 20% row is only a comparison: a cut that high is the point where sellers start to leave (see the take-rate row of the table in 17.2). Test a change in take rate with a cohort of sellers first, and watch order volume as well as revenue, since a smaller cut on more orders can earn more.

![A take rate multiplies the same GMV. The platform wins only if the cut keeps sellers and order volume.](diagrams/l14-take-rate.svg)

## Beyond the notes: pitfalls in reading price tests

- **Novelty.** A new price can move buyers for a week and then settle. Read the whole billing cycle.
- **Anchoring.** Visitors who first see a high plan may buy the middle plan, which changes the mix more than the price does. Read the mix as well as the total.
- **Small cohorts.** A few hundred buyers can swing on one large order. Agree the minimum sample before the test starts.
- **Segment averages.** A rise that comes from one country or one plan can hide a fall elsewhere. Check the segments the test was designed for.

## Beyond the notes: interview corner

- **"What is your first pricing question?"** What is the goal, share or margin? Then the three anchors, in that order of the answer, not the order of the question.
- **"Which model would you pick?"** Name where the value is created (user, usage, transaction, attention), then the one risk of that model.
- **"How would you test it safely?"** A cheap read first (survey or fake door), then a small cohort with revenue per user and churn as the decision metrics.
- **"What would make you roll back?"** A guardrail moves beyond its threshold, or churn rises past the level agreed before the test.

## Revision cheat-sheet

![Chapter 17 on one page: three anchors, the monetization models, and a test ladder ending in a live cohort.](diagrams/l14-big-picture.svg)

- **17.1** Price between three anchors: **cost** is the floor, **competitors** the reference, **customer value** the ceiling. Value-based usually leads. Start from the goal (share or margin).
- **17.2** Follow the value: **subscription** (value recurs), **freemium** (free users bring value, paid tier serves a need), **ads** (attention), **take rate** (each transaction), **razor-and-blade**, **bundling**, and **per seat, usage or outcome** for B2B and AI.
- **17.3** Read willingness to pay cheaply first (Van Westendorp, Gabor-Granger, conjoint, fake door). Then test live with a controlled cohort, judged on **revenue per user** and **retention**, over a full billing cycle.
- **Beyond the notes:** price-test checklist, take-rate arithmetic, novelty and anchoring in readouts.

## Self-test

<details class="quiz"><summary>What are the three anchors of a price, and what does each one set?

Cost sets the floor, competitors set the reference point, and customer value sets the ceiling. Triangulate all three, then pick a point in the band based on the goal.

</details>

<details class="quiz"><summary>Why is cost-plus pricing harder for AI products?

Inference cost varies per query. Value-based pricing is often the better starting point, with cost used as a floor check.

</details>

<details class="quiz"><summary>What is the rule for choosing a monetization model?

Follow where the value is created: the user (subscription, freemium), the usage (per seat, usage-based), the transaction (take rate) or the attention (ads).

</details>

<details class="quiz"><summary>When does freemium work?

When free users bring network or data value, and a segment has a clear need the paid tier serves. It fails when the free tier is so generous that nobody upgrades.

</details>

<details class="quiz"><summary>Name the four cheaper ways to read willingness to pay before a live test.

Van Westendorp price sensitivity survey, Gabor-Granger, conjoint analysis, and the fake-door (painted-door) test.

</details>

<details class="quiz"><summary>Why avoid showing different prices to users who can compare them?

Because the comparison creates a trust problem. Amazon's 2000 DVD price test showed how a hidden price difference, once discovered, turns into a backlash and refunds.

</details>

<details class="quiz"><summary>Why should a price test run for a full billing cycle?

Annual plans and churn lag the first purchase, so a short read can call a win that later loses customers.

</details>

<details class="quiz"><summary>The test shows conversion down 10% but revenue per visitor up 5%. What do you do?

Do not call it on conversion alone. Check the margin, churn and refunds over the billing cycle, check whether the drop sits in one segment, and keep the test running or roll out in stages if the signal is mixed.

</details>

<details class="quiz"><summary>(Beyond the notes) A price rise lifts revenue per visitor by 12.5% at the same buy rate. Why still read the churn?

Revenue per visitor counts the first purchase only. If the higher price pushes existing subscribers to leave, the gain can reverse within the billing cycle.

</details>

<details class="quiz"><summary>(Beyond the notes) At a 20% take rate, why might a marketplace earn less than at 10%?

Sellers may leave when the cut feels too high, so order volume falls. A higher rate on fewer orders can earn less than a lower rate on more orders.

</details>

<details class="quiz"><summary>(Beyond the notes) What does the anchoring pitfall look like in a price readout?

Visitors who first see a high plan may move to the middle plan. The mix changes more than the headline price, so read the mix as well as the total.

</details>


# Chapter 18 · Go-to-Market and Launch

<!-- lecture n="15" label="18" short="Go-to-market" status="done" kind="GTM" -->

## At a glance

| Question | Short answer |
|---|---|
| What does a launch question ask? | Who the first users are, how you roll it out, which channels you use, and how you know it worked. |
| What is go-to-market (GTM)? | The plan for your ideal customers, messaging and launch positioning (Sigma concept book). |
| Product-led or sales-led? | Product-led: the product sells itself and users upgrade. Sales-led: marketing makes leads, sales closes them. |
| What are the six GTM stages? | Define the ICP, research competitors, develop messaging, set targets, choose tactics, build a feedback loop. |
| What are the three launch phases? | Pre-launch, launch, post-launch. The six stages map onto them. |
| How do you de-risk a launch? | Learn from a small audience first: MVP, then a pilot, then a phased rollout with a gate at each step. |
| How do you pick channels? | Where the ICP already spends time, the cost against lifetime value, and whether you can measure the channel. |
| How do you define success? | Before launch: a primary metric, a target and a stop line, guardrails, and a time window. |
| What is a common mistake? *(Beyond the notes)* | Setting the criteria after you have seen the data. |
| How do you use this in an interview? *(Beyond the notes)* | Walk the timeline, name the rollout gates, then the metrics that would stop the launch. |

> [!NOTE] Where this comes from
> Built from the Sigma PM concept book (Go-to-market (GTM) Strategy, Experimentation Framework by Spotify, and the Google product excellence measurement step with HEART and SUPER) and from the vault's copy of *Cracking the PM Interview* (Tips and Tricks for Career Advancement: "Ship great products"). The launch phases, the pre-launch checklist, the channel table, the MVP and rollout gate definitions, and the structure of success criteria are general product knowledge, as the vault itself says. No links are kept here.

## The big picture

> Launch questions in APM interviews ask you to plan how a product reaches users. A good answer covers the timeline (before, during and after launch) and the decisions at each step.

The chapter covers four things:

1. The launch timeline: what to do before, during and after a launch (18.1).
2. How to de-risk a launch with pilots and phased rollouts (18.2).
3. How to choose distribution through partners and channels (18.3).
4. How to define success before you launch (18.4).

**Key takeaways**

- A GTM strategy defines the ICP, competitors, messaging, targets, tactics and feedback loops.
- Choose product-led or sales-led GTM based on how the buyer discovers and pays for the product.
- Launch in phases: an MVP or pilot first, then a wider rollout gated on metrics.
- Set success criteria before launch, with a clear threshold for rollback.
- Partnerships and channels can accelerate distribution, but they cost margin or control.

## 18.1 Pre-launch, launch, and post-launch activities

> A launch is a sequence of work, not a single day: prepare the market, release in a controlled way, then learn and iterate.

### Concept

The Sigma concept book defines GTM as the plan for your ideal customers, messaging and launch positioning, needed when you launch a new product in an existing market, an existing product in a new market, or test a new market. It names two types:

- **Product-led:** the product sells itself and users upgrade (for example, Calendly, Slack).
- **Sales-led:** marketing generates leads, and salespeople convert them.

![Product-led growth lets users find, try and upgrade on their own. Sales-led growth routes leads through people.](diagrams/l15-led-compare.svg)

The book builds the strategy from six stages: define the ideal customer profile (ICP), research competitors, develop messaging, set targets, choose tactics, and build a feedback loop. Those six stages map onto three launch phases.

**Pre-launch**

- Define the ICP: the customer who gets large benefits and gives enough value back to make the business viable.
- Research competitors and find where the product fits.
- Develop messaging that speaks to the ICP's pain points, in their language.
- Set funnel targets and per-team goals, so sales, marketing and product share a plan.
- Prepare support, docs, pricing and internal training.
- Agree on the launch criteria and the rollback plan (see 18.4).

**Launch**

- Release to the planned audience (pilot cohort, region, or all users).
- Run the channel tactics: content, demos, partner announcements, in-product prompts.
- Watch live dashboards for errors, latency and early conversion.
- Keep a war room or on-call rota for the first days.

**Post-launch**

- Establish a feedback loop between marketing, sales and product so learnings are acted on.
- Review metrics against targets at fixed checkpoints (week 1, week 4, quarter end).
- Triage bugs and adoption gaps, then iterate.
- Spotify's "Tweak It" stage is an example: keep improving performance and cost after release.

Launch is also a career signal. Interviewers and hiring managers look at the products a PM has shipped and how they performed in the market, more than at the specs or mockups produced along the way.

![The three launch phases, with the six GTM stages mapped onto them and the checkpoints after launch.](diagrams/l15-launch-timeline.svg)

### Real-world examples

- **Gmail** launched on 1 April 2004 as an invite-only beta with 1 GB of free storage. Scarce invites created demand and let Google scale infrastructure gradually. It opened to everyone in 2007 and dropped the "beta" label in 2009.
- **Slack** is the Sigma book's example of product-led GTM: teams adopted the free tier bottom-up, and companies later paid for seats once usage spread.
- **Spotify** described a Think It, Build It, Ship It, Tweak It loop in which features are shipped to a limited audience before a full rollout.

**Mini-example (launching a budgeting feature in a banking app):** pre-launch = the ICP is salaried 25-35 year olds with card spends, messaging is "see where your salary went", targets are 15% activation in 30 days, and support scripts are ready. Launch = 5% of eligible users, an in-app banner and push, and a live dashboard on errors. Post-launch = week-1 and week-4 reviews, fix the top confusion points, then widen.

### Practice questions

> [!INTERVIEW] Walk me through how you would launch a new budgeting feature in a banking app.
> *(Beyond the notes: the mini-example above is the vault's answer shape; this is a fuller starting point.)* Start with the ICP and one message, set the activation target and the stop line, then release to 5% of eligible users with the rollback ready. Name the owners for the dashboard, the support queue and the week-1 review.

> [!INTERVIEW] What should be in place on launch day, and what would you check in the first 48 hours?
> *(Beyond the notes: a starting point.)* In place on launch day: the rollback or kill switch tested, the dashboard for errors and latency live, support scripts and docs published, and an owner for each channel tactic. In the first 48 hours, check errors and latency against the agreed threshold, then conversion by segment, then the support queue for repeated questions.

> [!INTERVIEW] Your launch hit its conversion target but support tickets tripled. What do you do?
> **Answer outline (Q3):**
> - Stop or slow the rollout if the error rate or support load crosses the agreed threshold.
> - Find the top ticket themes and check whether they point to a bug, a confusing flow, or a messaging gap.
> - Communicate to stakeholders with data and a fix timeline.
> - Set a post-launch review to decide what to change.

*Related:* Chapter 18 (2: Pilots, MVPs, and phased rollouts; 4: Launch success criteria), Chapter 10 (1: Staged rollouts and kill switches), Chapter 15 (5: Guardrail and negative metrics).

## 18.2 Pilots, MVPs, and phased rollouts

> Reduce launch risk by learning from a small audience first, then widening the release only as evidence builds.

### Concept

These three terms are related but not the same.

**MVP styles to name in an interview:** concierge (do it manually for a few users), Wizard of Oz (looks automated, humans behind it), landing page or fake door (measure demand before building), and single-feature product. Dropbox's demo video before the product was ready is a well-known landing-page style MVP.

- **MVP (minimum viable product):** the smallest version that solves the core problem well enough to test with real users. It is built to learn, not to be complete.
- **Pilot:** a time-bound test with a chosen group of users or customers, often with close support and a clear success definition.
- **Phased rollout:** the live release is widened in steps (for example, 1%, 10%, 50%, 100%, or region by region), with a gate at each step.

**Spotify's Build It and Ship It stages** follow this pattern. Teams build an MVP to test the core problem with a set of users, then release features to a limited set first. Expansion depends on feedback and results. If the feature does not meet the bar, the team redesigns it rather than launching it. This is the "fail fast, fail cheap" logic in the Spotify framework.

![A phased rollout: an MVP and a pilot first, then each widening step opens only when its gate passes.](diagrams/l15-rollout-ladder.svg)

**Choosing the rollout shape**

- Start with the users most likely to give useful feedback: early adopters, or a region with good instrumentation.
- Define the gate for each step before starting: error rate, adoption, retention, support load.
- Keep a kill switch so you can roll back without a new release (see Chapter 10, Staged rollouts and kill switches).
- Avoid widening too quickly, because problems that show up only at scale are costly to fix.

**Trade-off:** more phases mean slower time to full reach, but they cut the cost of a bad launch.

### Real-world examples

- **Spotify** described releasing new features to a limited set of users first and widening them based on results. (From the Sigma concept book.)
- **Facebook (2004-2006)** rolled out by audience: Harvard first, then other Ivy League and Boston schools, then all US colleges, high schools, workplaces, and finally anyone 13+ in 2006. Each phase proved density and engagement before widening.
- **Instagram hidden like counts (2019)** were piloted in Canada first, then extended to Australia, Brazil, Italy, Japan and others before becoming an opt-in setting in 2021. A geography-gated pilot of a risky change.
- **Gmail** started as an invite-only beta in 2004, a classic pilot-style rollout that opened to the public in 2007.
- **Google Workspace release tracks** let admins choose Rapid Release or Scheduled Release, so features reach early-adopter organisations before everyone else.

### Practice questions

> [!INTERVIEW] You have three weeks to test a new feature. What would your MVP look like?
> *(Beyond the notes: a starting point.)* Pick the cheapest style that answers the riskiest question: a concierge or Wizard of Oz version for a handful of users if the value is unproven, or a fake-door page if the question is demand. Write down the one metric that decides the next step before you build anything.

> [!INTERVIEW] How would you choose the first cohort for a phased rollout?
> *(Beyond the notes: a starting point.)* Pick users who will tell you something useful and can be reached quickly: early adopters, an internal group, or a region with good logging. Avoid a cohort that is too unusual to generalise from, and check that the cohort is large enough to show the gate metrics move.

> [!INTERVIEW] What criteria would make you pause a rollout at 10%?
> **Answer outline (Q3):**
> - Define gate metrics before the rollout starts: error rate, task success, retention, and support volume.
> - Pause if any guardrail moves beyond its threshold; roll back with the kill switch.
> - Investigate whether the issue is in the product, the cohort, or the timing before deciding next steps.

*Related:* Chapter 18 (1: Pre-launch, launch, and post-launch activities; 4: Launch success criteria), Chapter 10 (1: Staged rollouts and kill switches), Chapter 15 (5: Guardrail and negative metrics).

## 18.3 Partnerships and distribution channels

> Distribution decides how many users you reach and at what cost. Partners can buy reach quickly, but they take margin or control in return.

### Concept

A distribution channel is the route a product takes to reach users. The main options:

| Channel | Strength | Cost or risk |
|---|---|---|
| **Organic / product-led** | Low marginal cost, word of mouth | Slow to scale; needs a strong product |
| **Paid acquisition** | Fast, measurable | Expensive; CAC can exceed LTV |
| **Sales-led** | Good for high-value B2B deals | Slow, expensive per customer |
| **Partners / integrations** | Access to an existing user base | Revenue share, dependency on partner |
| **Bundles and telco or OEM deals** | Reach at scale, often in new markets | Thin margins, long negotiations |
| **Marketplaces and app stores** | Built-in discovery | Platform fees (take rate) and policy risk |

![Each channel trades reach and cost against control. Pick the channel the ICP already uses, and check its cost against lifetime value.](diagrams/l15-channels.svg)

**Questions to ask when choosing a channel**

- Where does the ICP already spend time?
- What is the acquisition cost compared with lifetime value?
- Does the partner own the customer relationship? If so, what happens if the partnership ends?
- Can the channel be measured well enough to judge it?

**Partnership types**

- Integrations: your product plugs into another product's workflow.
- Co-marketing: shared campaigns or events.
- Distribution deals: a partner sells or bundles your product.
- Platform deals: you build on someone else's platform.

For AI products, a common pattern is a platform integration (for example, a model provider or an existing workflow tool) that makes the product reachable without building a new user base.

### Real-world examples

- **Telco bundles in India:** Airtel has bundled Amazon Prime with postpaid and broadband plans, and Jio has bundled its own JioCinema and partner OTT apps with recharges. OTT apps get reach in smaller cities without paid acquisition, and the telco gets lower churn. (Specific bundles change often, so quote the pattern, not today's plan.)
- **Apple App Store and Google Play** act as distribution channels for thousands of apps, charging a platform commission on paid purchases.
- **Slack** built an app directory of integrations (Google Drive, GitHub, Jira and thousands more), which made it the hub of existing workflows and raised switching costs.
- **OpenAI via Microsoft:** OpenAI's models reach enterprises through Microsoft's Azure OpenAI Service and Copilot products, a platform partnership that gives distribution to buyers who already trust Microsoft's procurement and compliance.

### Practice questions

> [!INTERVIEW] You are launching a personal finance app in India. Which three channels would you prioritise, and why?
> *(Beyond the notes: a starting point.)* Pick channels the ICP already uses: a bank or telco partnership for reach, in-product referrals for the users already active, and a paid test on one search or social audience for measurement. Justify each by its cost per acquired user against lifetime value.

> [!INTERVIEW] A partner offers to bundle your product for free to their users. How do you evaluate it?
> **Answer outline (Q2):**
> - Compare the partner's reach and cost per acquired user with your own channels.
> - Check contract terms: exclusivity, data ownership, revenue share, and exit clauses.
> - Pilot with a small cohort, measure retention and conversion, and decide to scale only if the unit economics hold.

> [!INTERVIEW] How would you decide between building a sales team and relying on partners?
> *(Beyond the notes: a starting point.)* Compare the cost per customer of each route at the deal size you expect, and ask who owns the customer relationship. A sales team keeps the relationship and the data; partners bring reach faster but may own the customer. Test the cheaper route first with a small cohort.

*Related:* Chapter 18 (1: Pre-launch, launch, and post-launch activities; 4: Launch success criteria), Chapter 17 (2: Monetization models: subscription, freemium, ads, take rate, razor-and-blade, bundling), Chapter 19 (5: Partnerships, acquisitions, and build-vs-buy strategy).

## 18.4 Launch success criteria

> Write down what success and failure look like before launch, with numbers, a time window and a rollback rule.

### Concept

A launch without success criteria cannot be judged. Define these before the first user sees the product.

**A good success definition has four parts**

1. **Primary metric:** the one number that shows the product solves the problem (for example, activation rate, weekly active users, or tasks completed).
2. **Target and threshold:** the level that means success, and the level that means stop or rethink.
3. **Guardrails:** metrics that must not get worse (crash rate, latency, support volume, churn, and cost).
4. **Time window:** when you will check, such as week 1, week 4 and day 90.

![A launch success definition has four parts. Write all four down before the first user sees the product.](diagrams/l15-success-criteria.svg)

**Use the GTM targets as your starting point.** The Sigma concept book describes setting funnel targets so that reps and teams work toward monthly goals. Turn those into launch criteria, with each team owning its share.

**Mini-example (in-app savings goal):** primary = % of eligible users who create a goal and make a second deposit within 30 days, target 8%, stop below 3%. Guardrails = app crash rate, support tickets per 1,000 users, and no drop in core payments usage. Windows = day 7 (health), day 30 (activation), day 90 (retention of savers).

**Frameworks that help** (both from the measurement step of Google's Product Excellence Framework in the Sigma concept book)

- HEART (Happiness, Engagement, Adoption, Retention, Task success) for consumer products.
- SUPER (Serviceability and system health, User sentiment, Productivity, Engagement, Revenue) for business products.
- Keep the set small: a launch needs one primary metric and a few guardrails, not twenty dashboards.

**Common mistakes**

- Setting criteria after seeing the data.
- Using vanity metrics such as downloads or sign-ups when activation or retention matters more.
- Declaring success on week one data when retention shows up later.
- Forgetting the cost side: a successful feature that doubles infrastructure spend may not be a win.

### Try it locally: a launch gate for the savings goal

*(Beyond the notes: reproduced locally with the standard library. The user count is illustrative, and the crash limit of 2% is an example threshold, not a rule. The rules run in the order written: guardrail first, then target, then stop line.)*

```python title="lab_p15_launch_gate.py"
# Rollout exposure for an in-app savings goal, then the decision at each gate.
eligible = 200_000                  # users eligible for the savings goal
for share in (0.01, 0.10, 0.50, 1.00):
    print(f"rollout {share:>4.0%}: {round(eligible * share):>7,} users see the feature")

TARGET, STOP_BELOW = 0.08, 0.03     # primary: share of eligible users who save within 30 days
CRASH_LIMIT = 0.02                  # guardrail: largest crash-rate rise we accept (example)

def gate(activation, crash_rise):
    if crash_rise > CRASH_LIMIT:
        return "pause: guardrail breached, roll back with the kill switch"
    if activation >= TARGET:
        return "widen: primary metric at or above target"
    if activation < STOP_BELOW:
        return "stop: below the stop line, rethink"
    return "hold: between the stop line and target, read more data"

for activation, crash_rise in [(0.085, 0.030), (0.085, 0.005), (0.050, 0.000), (0.020, 0.000)]:
    print(f"activation {activation:.1%}, crash rise {crash_rise:.1%}: {gate(activation, crash_rise)}")
```

```output
rollout   1%:   2,000 users see the feature
rollout  10%:  20,000 users see the feature
rollout  50%: 100,000 users see the feature
rollout 100%: 200,000 users see the feature
activation 8.5%, crash rise 3.0%: pause: guardrail breached, roll back with the kill switch
activation 8.5%, crash rise 0.5%: widen: primary metric at or above target
activation 5.0%, crash rise 0.0%: hold: between the stop line and target, read more data
activation 2.0%, crash rise 0.0%: stop: below the stop line, rethink
```

The first row is the trap the vault warns about. Activation is above target, but crash rate has risen by 3%, which breaks the guardrail, so the gate says pause before it widens. The second row shows the same activation with a small crash rise: that one widens. Between the stop line and the target, the gate holds and asks for more data rather than deciding on noise.

![The launch gate: the guardrail is checked first, so a strong primary metric cannot hide a breached crash rate.](diagrams/l15-launch-gate.svg)

**Real-world examples (from the source and general knowledge):**

- **Google's product excellence approach** (described in the Sigma concept book) ties launch decisions to measurement across the product lifecycle, using HEART and SUPER-style metrics. (From the source.)
- **Spotify's Ship It stage** gates wider release on feedback and results from the limited rollout. (From the source.)
- **Netflix** A/B tests nearly every product change and has written on its tech blog that member retention and streaming engagement are its core decision metrics, set before the test starts.

### Practice questions

> [!INTERVIEW] Define launch success criteria for a new in-app savings goal feature.
> *(Beyond the notes: the mini-example above is the vault's answer shape.)* Write one primary metric with a target and a stop line, two or three guardrails with their limits, and the windows at day 7, day 30 and day 90. Agree the owner of each number and the rollback rule before launch.

> [!INTERVIEW] Your primary metric is up 8% but crash rate is up 3%. Do you call the launch a success?
> **Answer outline (Q2):**
> - No, not yet: a guardrail is breached.
> - Check whether the crash increase is concentrated in one device or version.
> - Set a fix target; re-evaluate the primary metric once the guardrail is back in range.

> [!INTERVIEW] How would you decide the time window for judging a B2B product launch?
> *(Beyond the notes: a starting point.)* Set the windows from the buying cycle: an early health check in the first weeks (errors, setup completion), an adoption read once the first teams are live, and a retention and expansion read after at least one renewal cycle or the first full quarter. Do not judge a B2B launch on week one sign-ups alone.

*Related:* Chapter 18 (2: Pilots, MVPs, and phased rollouts; 1: Pre-launch, launch, and post-launch activities), Chapter 15 (1: North Star metric; 3: HEART; 5: Guardrail and negative metrics).

## Beyond the notes: launch-day checklist

*(Beyond the notes: general practice, built from the sections above, not from the vault.)*

- Kill switch tested in the production environment, with the person who can flip it named.
- Dashboard for errors, latency and conversion open, with the thresholds written next to each line.
- Support queue staffed, with scripts and a known-issues page live before the first user arrives.
- Channel tactics timed to the release window, so a campaign does not drive users to a half-open feature.
- A short written update for stakeholders at each checkpoint: what moved, what did not, what happens next.

## Beyond the notes: pitfalls in launches

- **Peeking at week one.** A launch can look like a flop or a hit in the first days and settle later. Judge against the window you wrote down.
- **Widening before the gate.** A rollout that moves because the calendar says so has no evidence behind it.
- **One channel doing all the work.** A launch that depends on a single partner or ad audience can stall the day that channel changes.
- **Ignoring the support load.** Tickets are a signal of confusion. A rising queue is a launch metric, not an operations problem.

## Beyond the notes: interview corner

- **"Walk me through your launch."** Name the phase you are in (pre, launch or post), then the ICP and message, then the rollout gate and the metric that would stop it.
- **"What would make you roll back?"** A guardrail breached beyond its limit, named before the launch and tied to the kill switch.
- **"Which channel first?"** The one the ICP already uses, judged on acquisition cost against lifetime value, and measured well enough to judge.
- **"How do you know it worked?"** The primary metric reached its target, the guardrails held, and the retention read at the window you wrote down.

## Revision cheat-sheet

![Chapter 18 on one page: the three launch phases, the rollout gates, the channels and the four parts of success.](diagrams/l15-big-picture.svg)

- **18.1** GTM is the plan for the ICP, messaging and positioning. Product-led (the product sells itself) or sales-led (marketing makes leads, sales closes). Six stages (ICP, competitors, messaging, targets, tactics, feedback loop) map onto **pre-launch, launch and post-launch**. Checkpoints at week 1, week 4 and quarter end.
- **18.2** **MVP** (smallest version that tests the core problem), **pilot** (time-bound test with a chosen group), **phased rollout** (widen in steps with a gate at each). Spotify's Build It and Ship It: fail fast, fail cheap. Keep a kill switch.
- **18.3** Channels trade reach and cost against control: organic, paid, sales-led, partners, bundles, app stores. Ask where the ICP spends time, the CAC against LTV, who owns the customer, and whether you can measure it.
- **18.4** Four parts: **primary metric**, **target and threshold**, **guardrails**, **time window**. Keep the set small, set it before launch, and judge the cost side too.
- **Beyond the notes:** a launch-day checklist, pitfalls of early reads and widening without evidence, and the gate that checks guardrails first.

## Self-test

<details class="quiz"><summary>What is the difference between product-led and sales-led GTM?

Product-led: the product sells itself and users upgrade (Calendly, Slack). Sales-led: marketing generates leads and salespeople convert them.

</details>

<details class="quiz"><summary>What are the six stages of the Sigma GTM strategy?

Define the ideal customer profile (ICP), research competitors, develop messaging, set targets, choose tactics, and build a feedback loop.

</details>

<details class="quiz"><summary>Which three launch phases do the GTM stages map onto?

Pre-launch (ICP, competitors, messaging, targets, support, criteria), launch (release, channel tactics, live dashboards, on-call) and post-launch (feedback loop, checkpoints, triage and iterate).

</details>

<details class="quiz"><summary>What is the difference between an MVP, a pilot and a phased rollout?

An MVP is the smallest version that tests the core problem with real users. A pilot is a time-bound test with a chosen group and a clear success definition. A phased rollout widens the live release in steps, with a gate at each step.

</details>

<details class="quiz"><summary>What does Spotify's Build It and Ship It stage teach about expansion?

Expansion depends on feedback and results from a limited release. If a feature does not meet the bar, the team redesigns it rather than launching it: fail fast, fail cheap.

</details>

<details class="quiz"><summary>Name the four parts of a good launch success definition.

A primary metric, a target and threshold (including the stop line), guardrails that must not get worse, and a time window for each check.

</details>

<details class="quiz"><summary>Why set success criteria before launch rather than after?

Criteria set after seeing the data can be bent to fit it. Writing the numbers, the window and the rollback rule first keeps the decision honest.

</details>

<details class="quiz"><summary>The launch hit its conversion target but support tickets tripled. What is the first move?

Check the support load against the agreed threshold and slow or stop the rollout if it is crossed. Then find the top ticket themes, and decide whether they point to a bug, a confusing flow or a messaging gap.

</details>

<details class="quiz"><summary>What does a partner bundle cost you, and what should you check before accepting?

It can cost margin or control. Check the partner's reach and cost per acquired user, exclusivity, data ownership, revenue share and exit clauses, and pilot with a small cohort first.

</details>

<details class="quiz"><summary>(Beyond the notes) In the launch gate, why is the guardrail checked before the primary metric?

A strong primary metric can hide a breached guardrail. Checking the crash rate first means the gate pauses even when activation is above target.

</details>

<details class="quiz"><summary>(Beyond the notes) What is the main risk of judging a launch on week one data?

Some effects, such as retention, show up later. An early read can call a flop or a hit before the window you wrote down has passed.

</details>

<details class="quiz"><summary>(Beyond the notes) Why does a rising support queue count as a launch metric?

It is a signal that users are confused by the feature or the messaging. Treat it as a guardrail with a threshold, not as an operations problem.

</details>


# Chapter 19 · Strategy and Market Entry

<!-- lecture n="16" label="19" short="Strategy & entry" status="done" kind="strategy" -->

## At a glance

| Question | Short answer |
|---|---|
| Should a company be in this market? | Look at the **industry** first (Five Forces), then at the **company** (SWOT and the Five Cs). |
| What counts as a moat? | A **durable advantage**: network effects, switching costs, scale, proprietary data. **Features alone are not a moat.** |
| How do you size a market? | Three layers: **TAM**, **SAM** and **SOM**. Use a **top-down** and a **bottom-up** method, and cross-check them. |
| What is the entry checklist? | Seven questions on whether to enter (company fit, industry, competitors, feasibility, customers, alternatives, risks), then **timing and route**. |
| Build, partner or buy? | Ask whether the capability is **core**, how fast you must move, and how **reversible** the choice is. |
| What is a SWOT good for? | Only when each **opportunity** is matched to a **strength** and each **threat** to a **weakness**. |
| What does a competitor analysis add? | Direct, potential and substitute competitors, and their **likely next moves**. |
| What do you do when the two sizing methods disagree? | Find the weaker assumption behind each method, then pick the number with the stronger evidence. |
| Where do you start on a new-market question? *(Beyond the notes)* | Market first (Five Forces), then the company (SWOT), then the route, and a go/no-go threshold before the numbers. |
| How do you close the answer? *(Beyond the notes)* | Say which option you would pick, what you give up, and the first checkpoint. |

> [!NOTE] Where this comes from
> The vault draws on *Cracking the PM Interview* (Porter's Five Forces, SWOT, the Five Cs, company profiles) and the Sigma PM concept book, Part A (2023), section "Market Entry". The moat categories and the TAM, SAM and SOM method are general product-strategy and estimation knowledge. The vault's further-reading list names *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

Strategy questions ask whether a company should be in a market, how it would win there, and how it would get there. This chapter covers the industry view (Five Forces), the company view (SWOT and the Five Cs), the defensibility view (competition and moats), the numbers (market sizing and entry checks), and the route in (build, partner or buy).

The chapter has five sections, each one a tool for one of those questions:

- **19.1 Porter's Five Forces.** Industry profitability, through five pressures on margins.
- **19.2 SWOT and the Five Cs.** Internal and external factors for one decision, plus a wider situational scan.
- **19.3 Competitive analysis and moats.** Who the competitors are, and what durable advantage looks like.
- **19.4 Market sizing and entry decisions.** TAM, SAM, SOM, and a go/no-go checklist for entering a market.
- **19.5 Partnerships, acquisitions, and build-vs-buy strategy.** Choosing how to acquire a capability.

## Key takeaways

- Use Five Forces to judge whether an industry is worth entering, and SWOT to judge whether you should.
- A SWOT is only useful when each opportunity is matched to a strength and each threat to a weakness. The Five Cs (company, competitors, customers, collaborators, climate) give the wider scan.
- Size markets with both top-down and bottom-up methods, then check that the two agree.
- A moat is a durable advantage such as network effects, switching costs, scale, or proprietary data. Features alone are not a moat.
- Build, partner, or buy by asking whether the capability is core, how fast you must move, and how reversible the choice is.

> [!SIR] From the source notes
> A SWOT is only useful when each opportunity is matched to a strength and each threat to a weakness.

## 19.1 Porter's Five Forces

> Porter's Five Forces describes how attractive an industry is by measuring the pressure on profits from five directions.

### Concept

Michael Porter's framework looks at an industry as a whole, not at one company. It asks how much profit the industry can sustain.

**The five forces**

- **Rivalry among existing competitors:** many similar players, slow growth, and high exit costs push prices and margins down.
- **Buyer power:** few buyers, or buyers who take a large share of revenue, can demand lower prices and better terms.
- **Supplier power:** a company that depends on a few suppliers, or on one critical component, gives them leverage over cost and timing.
- **Threat of new entrants:** low capital needs, weak regulation, and easy access to distribution invite new players. Barriers include patents, scale economies, brand loyalty, and licences.
- **Threat of substitutes:** a different product that meets the same need caps the price you can charge. *Cracking the PM Interview*'s example: even if Amazon were the only e-book seller, physical books would still cap e-book prices. (WhatsApp replacing SMS is another.)

![Five pressures push on an industry's profit from five directions. Check the industry first, then the company.](diagrams/l16-five-forces.svg)

**Worked example from the source (PC market):** buyer power is high (many sales go through a few retailers); supplier power is high (few makers of key components, high switching costs); rivalry is moderated by some differentiation; substitutes are limited; entry barriers are moderate (brand). Verdict: "there are worse markets to be in, but there are also many better markets."

**How a PM uses it**

- Before entering a market, check whether the industry is structurally profitable.
- When planning a feature, ask which force it weakens. Example: building a proprietary data layer raises switching costs and reduces buyer power.
- Pair it with 19.2 (the company view, SWOT) and 19.3 (defensibility, moats).

**Interview tip:** Use Five Forces to say whether a market is worth entering. Use SWOT to say whether *you* should enter it. Cracking's own caveat: these frameworks overlap, so use them as checklists that stop you missing something, and build your own structure when none fits the question.

**Mini-example (quick-commerce in a new Indian city):** rivalry high (Blinkit, Zepto, Swiggy Instamart, discounting); buyer power high (zero switching cost between apps); supplier power moderate (FMCG brands need these channels, but dark-store landlords and delivery riders are scarce at peak); entry threat moderate (capital-heavy dark stores, but well-funded players keep entering); substitutes strong (kirana stores that deliver, scheduled grocery). Verdict: structurally low-margin; enter only with a cost or density advantage.

### Real-world examples

- **Indian telecom, 2016 onward (Reliance Jio):** Jio launched in September 2016 with free voice and data for several months, then very cheap data. Industry prices collapsed, Vodafone and Idea merged (2018), and several smaller operators exited. A clear case of new-entrant and rivalry pressure reshaping an industry.
- **Wintel PC ecosystem:** Intel (CPUs) and Microsoft (Windows) held strong supplier power over PC makers for decades, which is why PC makers' margins stayed thin while Intel's and Microsoft's were high.
- **Walmart and its suppliers:** Walmart's scale gives it strong buyer power, letting it push prices down for consumers and demand terms from suppliers.
- **Pharmaceuticals:** Patents and regulatory approvals are high entry barriers, so incumbents keep stable margins (illustrative of barriers to entry).

### Practice questions

> [!INTERVIEW] Should a fintech startup enter India's payments market? Walk through the five forces.
> *(Beyond the notes: a starting point, not the vault's answer.)* Take each force in turn: rivalry (how many apps, how much they discount), buyer power (how easily a user switches apps), supplier power (banks, network rails, device makers), entry threat (licences, capital), substitutes (cash, cards, bank transfers). End with a verdict on whether the industry pays enough margin for a new player.

> [!INTERVIEW] Why are airlines often low-margin businesses, even with many customers?
> **Answer outline (Q2):** Rivalry is intense (similar services, price transparency). Buyers can switch easily. Fuel and aircraft suppliers have strong power. Entry is capital-heavy, but fares are set by competition. Result: thin margins.

> [!INTERVIEW] Which force is most affected when a platform adds a proprietary rating system for sellers?
> *(Beyond the notes: a starting point.)* Buyer power is the usual answer: a rating system that only this platform holds makes sellers costlier to move, and it makes buyers depend more on the platform's signal. Switching costs for sellers rise, so the force on the seller side weakens. Say which side you mean.

*Related (same page):* 19.2 SWOT and the Five Cs, 19.3 Competitive analysis and moats, 19.4 Market sizing and entry decisions, 19.5 Partnerships, acquisitions, and build-vs-buy strategy.

## 19.2 SWOT and the Five Cs

> SWOT tests a specific decision against your internal strengths and the external landscape; the Five Cs describe the full environment around it.

### Concept

**SWOT** sorts factors into a 2x2 grid.

| | Helpful | Harmful |
|---|---|---|
| **Internal** | Strengths | Weaknesses |
| **External** | Opportunities | Threats |

![SWOT is a 2x2 grid. The rows are internal and external; the columns are helpful and harmful.](diagrams/l16-swot-grid.svg)

- **Strengths:** cost, features, culture, reputation, infrastructure. Example: an existing customer base.
- **Weaknesses:** gaps such as no distribution experience or a thin engineering bench.
- **Opportunities:** market growth, new technology, regulatory change, a competitor's weakness.
- **Threats:** new rivals, adverse regulation, input cost shocks.

A SWOT is only useful if it leads to action. Pair each opportunity with a strength (use it), and each threat with a weakness (fix it or avoid it).

**The Five Cs** give a wider situational view:

1. **Company:** products, culture, brand, strengths, and weaknesses.
2. **Competitors:** direct, potential, and substitute products; their share, positioning, and likely moves.
3. **Customers:** demographics, buying behaviour, size, channels, and unmet needs.
4. **Collaborators:** suppliers, distributors, and partners who make success possible.
5. **Climate:** regulation, technology trends, economic conditions, and culture. A hostile climate can kill a good idea.

![The Five Cs: a wider scan of the whole picture around a decision.](diagrams/l16-five-cs.svg)

**Use in practice:** SWOT for "should we do this?" with a bias to the company. The Five Cs for "what does the whole picture look like?" before a launch or market entry. The Sigma concept book puts SWOT (with VRIN: valuable, rare, inimitable, non-substitutable resources) under the "Company" step of its market entry checklist.

**Mini-example (should Zomato launch a paid live-cooking-class product?):** S = huge food-interested user base, restaurant relationships; W = no live video or teaching experience; O = creator economy, home-cooking interest; T = YouTube offers cooking content free. TOWS moves: use S to grab O (chef partners, sell to existing users); W + T means do not build video infra, partner instead. Recommendation: small pilot with partner chefs, judged on paid conversion.

### Real-world examples

- **Amazon and the Kindle:** *Cracking the PM Interview*'s example strength is that Amazon was already where customers bought books online. The book's matching weakness example is a web company with no experience distributing physical devices. The first Kindle (2007) was sold only on Amazon.com, which used the strength and avoided the retail distribution weakness.
- **Clean energy products:** the book's threat example is unpredictable energy-usage regulation. India's rooftop solar subsidies are a live case: changes to subsidy schemes swing demand for installers. (application illustrative)
- **Healthcare cost (opportunity):** the book's opportunity example: rising healthcare costs create room for products that give better insight into one's own health, which is the bet behind fitness wearables and health-tracking apps.
- **Ride-hailing in a new city (illustrative):** Customers (commuters), competitors (taxis, two-wheelers), collaborators (drivers, payment gateways), and climate (local rules on fares) give a quick Five Cs snapshot.

### Practice questions

> [!INTERVIEW] Use SWOT to evaluate whether an edtech company should launch a paid live-tutoring product.
> *(Beyond the notes: a starting point.)* List two or three factors in each of the four boxes, using the company's own data (learner base, teaching staff, content library, competitor offers). Then apply the matching rule from the concept above: which strength answers each opportunity, and which weakness each threat. Say whether the answer is build, partner or wait.

> [!INTERVIEW] Which of the Five Cs would you research first for a cashless-payments feature in rural India? Why?
> *(Beyond the notes: a starting point.)* Start with **customers**: who pays today, in cash or by what means, and what stops them from going digital. Customers decide whether the feature is used at all. Then check **climate** (rules and connectivity) and **collaborators** (merchants, agents, banks) before the build.

> [!INTERVIEW] How do you turn a SWOT into a recommendation rather than a list?
> **Answer outline (Q3):** Find the strength that matches each opportunity and the weakness that matches each threat. Rank by impact. End with one recommended move and the first two actions it needs.

*Related (same page):* 19.1 Porter's Five Forces, 19.3 Competitive analysis and moats, 19.4 Market sizing and entry decisions, 19.5 Partnerships, acquisitions, and build-vs-buy strategy.

## 19.3 Competitive analysis and moats

> Competitive analysis maps who you are up against and how; a moat is the durable advantage that keeps competitors from winning even when they try.

### Concept

**Competitive analysis** covers three groups:

- **Direct competitors:** same product, same customer.
- **Potential entrants:** firms with the capability to enter (adjacent players, big tech).
- **Substitutes:** different products that solve the same job.

For each, compare market share, positioning, pricing, target segment, strengths, and likely next moves. Output: a short table, plus a view on where you can win.

**Moats** are sources of durable advantage. The common ones:

- **Network effects:** the product gets more valuable as more people use it (marketplaces, messaging, social).
- **Switching costs:** data, workflows, integrations, or learning curves make leaving expensive.
- **Scale economies:** unit cost falls with volume (logistics, cloud infrastructure).
- **Proprietary data:** unique data improves the product, which attracts more users, which creates more data.
- **Brand and trust:** customers pay more or stay loyal because of reputation.
- **Distribution:** exclusive channels, bundling, or default placement.
- **Regulatory or IP protection:** patents, licences, certifications.

![Seven common moats on the left, and the Helmer list of seven powers on the right. The test on the right applies to all of them.](diagrams/l16-moats.svg)

A rigorous reference list is Hamilton Helmer's *7 Powers*: scale economies, network economies, counter-positioning, switching costs, branding, cornered resource (e.g. exclusive data, patents, talent) and process power. Citing it signals depth.

**Test a moat:** Ask "if a well-funded rival copied our product tomorrow, what would still keep customers with us?" If the answer is only features, you have no moat.

**Interview tip:** Name the competitor's *likely response* as well as the current position. This is what separates strong answers.

### Real-world examples

- **WhatsApp:** network effects. Its value grew with each contact that joined, which made switching costly for users.
- **Google Search:** scale of query data and distribution as moats. Google pays Apple and others to be the default search engine, which a US federal court in 2024 found was part of how Google illegally maintained its search monopoly.
- **Apple:** brand, ecosystem switching costs, and premium pricing power.
- **Amazon logistics:** scale economies in fulfilment that smaller retailers find hard to match.
- **Salesforce:** years of customer records, custom fields, workflows and integrations live inside each customer's CRM, so migrating is costly. Switching costs as a moat.
- **UPI payment apps (counter-example):** UPI is interoperable, so a user can switch from Google Pay to PhonePe in seconds. Payment apps there cannot rely on switching costs and compete on distribution, rewards and adjacent services instead.

### Practice questions

> [!INTERVIEW] How would you assess the competitive position of a new food-delivery app in a city dominated by two players?
> *(Beyond the notes: a starting point.)* Build the three-group view first: the two incumbents (direct), the grocery and quick-commerce players that could add restaurants (potential), and home cooking and kirana options (substitutes). Compare share, price, delivery times and segment for each, then say where the new app can win and what the incumbents would likely do in response.

> [!INTERVIEW] Which moat would you build first for an AI writing assistant? Why?
> *(Beyond the notes: a starting point.)* Proprietary data and workflow depth are the usual first choices: feedback from accepted and edited text improves the product, and documents and style rules inside the user's workflow raise switching costs. Name the one you would measure first, and how you would know it is working.

> [!INTERVIEW] A competitor just launched a free version of your core feature. What do you do?
> **Answer outline (Q3):** Separate the threat (is the free feature close to your value, or a substitute for a small segment?). Check your moats: data, switching costs, workflow depth. Decide: match, differentiate, or go deeper into the segment where you still win. Name a metric to watch (retention, conversion).

*Related (same page):* 19.1 Porter's Five Forces, 19.2 SWOT and the Five Cs, 19.4 Market sizing and entry decisions, 19.5 Partnerships, acquisitions, and build-vs-buy strategy.

## 19.4 Market sizing and entry decisions

> Before entering a market, size it realistically (TAM, SAM, SOM), check the company's fit and the industry's structure, then decide with explicit go/no-go criteria.

### Concept

**Market sizing** uses three layers:

- **TAM (total addressable market):** everyone who could ever use the product.
- **SAM (serviceable available market):** the part you can reach with your product, price, and channels.
- **SOM (serviceable obtainable market):** the share you can realistically win in 3 to 5 years.

**Two methods**

- **Top-down:** start from a known industry total and apply a share (for example, total online food spend x your target cities x a realistic share). Quick, but depends on the source number.
- **Bottom-up:** start from users and value (for example, households x purchase frequency x average order value). Slower, but easier to defend and test.

Always cross-check both. A large gap between them is a red flag.

**Worked mini-example (bottom-up, premium e-scooters in Pune; all numbers illustrative):**

- TAM: about 1.8 million households x 50% with a two-wheeler need = 900,000 households; one scooter every 6 years = 150,000 scooters a year; at ₹1.2 lakh = about ₹1,800 crore a year.
- SAM: only households that can charge at home and afford a premium model, say 30% = 45,000 scooters, about ₹540 crore.
- SOM: realistic 10% share of SAM in 3 years given Ola, Ather and TVS = 4,500 scooters, about ₹54 crore.
- Sanity check top-down: if Pune is about 3% of India's two-wheeler EV sales, does it land in the same range?

![The three layers of market size, with the bottom-up chain for Pune e-scooters. Money in pink.](diagrams/l16-market-sizing.svg)

### Try it locally: the bottom-up sizing

*(Beyond the notes: reproduced locally with the standard library. The inputs are the vault's illustrative numbers. Change one input and watch how every layer moves.)*

```python title="lab_p16_market_sizing.py"
# Bottom-up market sizing for premium e-scooters in Pune (all inputs illustrative).
households = 1_800_000
own_need = 0.50                 # share of households with a two-wheeler need
replace_years = 6               # one scooter every 6 years
price = 120_000                 # rupees (Rs 1.2 lakh)
crore = 10_000_000

tam_households = households * own_need
tam_units = tam_households / replace_years
sam_units = tam_units * 0.30    # can charge at home and afford a premium model
som_units = sam_units * 0.10    # realistic 10% share in 3 years

def show(name, units):
    value = units * price / crore
    print(f"{name}: {units:>9,.0f} scooters a year, about Rs {value:,.0f} crore")

print(f"households with a need: {tam_households:,.0f}")
show("TAM", tam_units)
show("SAM", sam_units)
show("SOM", som_units)
```

```output
households with a need: 900,000
TAM:   150,000 scooters a year, about Rs 1,800 crore
SAM:    45,000 scooters a year, about Rs 540 crore
SOM:     4,500 scooters a year, about Rs 54 crore
```

Each layer is a fixed share of the one above it: the 30% and the 10% are the only judgement calls in this chain, and the first two layers come straight from the households. The output shows the funnel the vault describes: 150,000 scooters a year at the top, 45,000 in reach, and 4,500 won in three years. Note the unit at every step (households, then scooters, then rupees). A mistake in the unit is the most common error in a market-size answer.

**Market entry checklist** (from the Sigma concept book's "Market Entry" section):

*Should we enter?*

1. **Company fit:** goals and vision, core capabilities (VRIN, SWOT, 19.2), where we excel compared with others.
2. **Industry structure:** market size, possible share, growth and trends, and the five forces (19.1).
3. **Competitors:** how many, and what they are doing.
4. **Feasibility:** operational (value chain, regulation), financial (profitability, break-even, pricing, costs), distribution (production, marketing, supplier access), and existing expertise to leverage.
5. **Customers:** target customer, overlap with competitors, other attractive segments, the value offering.
6. **Alternative strategies:** trade-offs on cost and time to market.
7. **Risks:** legal/compliance, market, operational.

![The seven questions for "should we enter", then the route: timing, and scratch, joint venture or M&A.](diagrams/l16-entry-checklist.svg)

*How should we enter?* Timing, then the route: from scratch (GTM using STP and the 4Ps), a joint venture, or M&A (see 19.5).

**Decision:** write down the go/no-go thresholds before you analyse (for example, "SOM above Rs X crore in 3 years, break-even within 24 months"). This makes the decision defensible.

### Real-world examples

- **Reliance Jio (2016):** entered a crowded telecom market with a data-first, 4G-only network and months of free service, betting that cheap data would unlock a huge latent base of mobile internet users. India's mobile data use rose many-fold within a few years. A real case of sizing the market at a much lower price point than incumbents assumed (the internal sizing itself is not public).
- **Netflix in India:** entry depended on sizing the premium-streaming segment against free and low-cost rivals (illustrative of SAM and SOM thinking).
- **Sigma casebook example:** "Should Google enter the OTT market?" is a standard entry question. Use the checklist above to structure the answer.

### Practice questions

> [!INTERVIEW] Estimate the market for electric scooters in Pune. Show TAM, SAM, and SOM.
> *(Beyond the notes: a starting point.)* Use the worked example above as the model, and state each input as an assumption with its source. Say which input you are least sure of, and show the answer as a range by varying that one input.

> [!INTERVIEW] A top-down estimate gives 10 million users and a bottom-up gives 1.5 million. What do you do?
> **Answer outline (Q2):** The gap means one input is wrong. Check the assumption behind each method (is the top-down share too high? is the bottom-up purchase frequency too low?). Pick the number with the stronger evidence and note the range in the answer.

> [!INTERVIEW] Should a bank enter the buy-now-pay-later market? Set go/no-go criteria first.
> *(Beyond the notes: a starting point.)* Set the bar before the analysis: a SOM target at year three, a break-even month, and a loss-rate limit the risk team signs off. Then run the checklist (company fit, feasibility, risks) and check the result against those three numbers.

*Related (same page):* 19.1 Porter's Five Forces, 19.2 SWOT and the Five Cs, 19.3 Competitive analysis and moats, 19.5 Partnerships, acquisitions, and build-vs-buy strategy.

## 19.5 Partnerships, acquisitions, and build-vs-buy strategy

> To enter or expand a market, a company can build the capability itself, partner for it, or buy it. Choose by speed, control, cost, and how core the capability is.

### Concept

The three routes:

- **Build:** develop in-house. Full control and IP, but slower and riskier. Right when the capability is core to your moat.
- **Partner:** share revenue, distribution, or technology through an alliance, licence, or channel deal. Fast and low-capital, but you depend on the partner and may share data.
- **Acquire:** buy a company or team. Fastest route to capability, customers, or talent, but expensive and hard to integrate.

![Three routes, each with its trade-off, and the five questions that pick between them.](diagrams/l16-build-partner-buy.svg)

**Decision lens**

1. **Is it core?** If it defines your moat, lean to build or acquire, not partner.
2. **Time to market:** if a window closes in months, partner or buy.
3. **Cost and risk:** compare total cost of ownership, not just the price.
4. **Integration load:** acquisitions fail often on culture and product fit. Partnerships fail on incentives and exclusivity terms.
5. **Reversibility:** partnerships are easier to unwind than acquisitions.

**Interview tip:** Name what you would give up in each option. A strong answer ends with a staged plan, for example "partner now to test demand, acquire later if usage clears a threshold."

**Porter link:** partnering with a dominant supplier or distributor can reduce supplier or buyer power (19.1).

### Real-world examples

- **Facebook acquires Instagram (2012):** bought a fast-growing product to add mobile photo users, rather than build a competitor.
- **Google acquires YouTube (2006):** bought a video platform with strong growth to secure a major content and ads asset.
- **JioStar (2024):** Reliance's media arm and Disney's Star India combined their streaming and broadcast businesses, a large-scale merger to pool content and reach.
- **Co-branded credit cards in India:** the Amazon Pay ICICI Bank card and the Flipkart Axis Bank card pair a bank's licence and credit underwriting with a platform's customer base and rewards. Partnering beats building for both sides.
- **Flipkart acquires PhonePe (2016) and Zomato acquires Blinkit (2022):** Flipkart bought a payments capability rather than building one; Zomato bought a quick-commerce business (all-stock deal) to enter a new category fast instead of building dark stores from scratch.

### Practice questions

> [!INTERVIEW] A fintech wants lending capability but has no licence. Build, partner, or acquire? Why?
> **Answer outline (Q1):** Lending is regulated and capital-heavy, so the time and licence hurdle favours partnering with a licensed NBFC or bank now. Set a checkpoint on loan performance and customer data quality. Revisit acquisition only if the partnership limits margin or product control.

> [!INTERVIEW] When would you tell a PM not to build a feature in-house even if the team can?
> *(Beyond the notes: a starting point.)* When a partner already runs it at scale and does it well, when the feature is not part of your moat, or when a window closes before your team could ship it. Say what you would give up: control, margin, or the data the feature would have produced.

> [!INTERVIEW] What signals would make you stop an acquisition integration?
> *(Beyond the notes: a starting point.)* Key people from the acquired team leaving, customers of either company churning after the deal, and a product roadmap that stalls for more than one quarter. Set the signals and the review date before the deal closes.

*Related (same page):* 19.1 Porter's Five Forces, 19.3 Competitive analysis and moats, 19.4 Market sizing and entry decisions, and the OKR and roadmap link in Chapter 20 (Theme-based roadmaps and OKRs).

## Beyond the notes: sizing checks before you present a number

The vault asks for two methods and a cross-check. A few habits make the number easier to defend:

- **Check the units at every step.** Households, scooters and rupees are three different units. Write the unit next to each number.
- **Keep SOM inside SAM, and SAM inside TAM.** A share of a layer cannot be bigger than the layer. If the funnel inverts, one input is wrong.
- **State the replacement or purchase cycle.** The worked example uses one scooter every 6 years. Saying that out loud shows why the annual number is a fraction of the household count.
- **Show a range, not a point.** Vary the one assumption you are least sure of, and report the low and high case.
- **Do not confuse TAM with the target.** TAM is everyone who could ever use the product. The market you want to win is the SOM.

## Beyond the notes: framework order and pitfalls

Frameworks are checklists, not answers. A clear order for a new-market question:

1. **Market:** Five Forces, to see whether the industry pays enough margin.
2. **Company:** SWOT, to see whether you should enter, using the matching rule.
3. **Numbers:** TAM, SAM and SOM with two methods, and a cross-check.
4. **Decision:** the go/no-go thresholds, written before the analysis.
5. **Route:** build, partner or buy, using the five-question lens.

Common pitfalls:

- **A list instead of a decision.** A SWOT with twenty factors and no recommendation is a list. End with one move.
- **Scoring the five forces without evidence.** A "high" or "low" needs a fact behind it (a number of players, a switching cost, a margin).
- **Treating a moat as permanent.** UPI shows how quickly a switching cost can disappear when the rails are shared. Re-check the moat as the market changes.
- **Skipping the substitutes.** Most weak market-entry answers forget the substitute that already does the job, such as the kirana store in quick-commerce.
- **Ignoring the partner's incentives.** Partnerships fail on incentives and exclusivity terms, not only on technology.

## Beyond the notes: interview corner

- **"Walk me through how you would decide whether to enter a new market."** Market first (Five Forces), company second (SWOT with the matching rule), then sizing with two methods, the go/no-go thresholds, and the route. Close with the first checkpoint.
- **"What is the difference between Porter and SWOT?"** Porter asks how profitable the industry is, from five outside pressures. SWOT asks whether this decision suits your company, given your strengths and weaknesses and the external factors. The vault's interview tip gives the same split.
- **"How do you size a market you know nothing about?"** Use both methods, write each assumption down with its source, cross-check the two results, and give a range.
- **"Why is 'features are not a moat' a useful test?"** It forces you to name what would keep customers after a copy: data, switching costs, scale, distribution or network effects.

## Revision cheat-sheet

![Chapter 19 on one page: five tools, five questions, from the industry down to the route in.](diagrams/l16-big-picture.svg)

- **19.1** Five Forces measure the pressure on an industry's profit: rivalry, buyer power, supplier power, new entrants, substitutes. Check the industry before you enter.
- **19.2** SWOT is a 2x2 grid. Match each opportunity to a strength and each threat to a weakness. The Five Cs are the wider scan: company, competitors, customers, collaborators, climate.
- **19.3** Analyse three groups of competitors: direct, potential entrants, substitutes. Moats are durable advantages (network effects, switching costs, scale, proprietary data, brand, distribution, regulation or IP). Features alone are not a moat.
- **19.4** TAM is everyone who could use it, SAM is what you can reach, SOM is what you can win in 3 to 5 years. Size with top-down and bottom-up, cross-check, and set the go/no-go thresholds first.
- **19.5** Build when the capability is core, partner when speed and low capital matter, acquire when you need the capability fast and can integrate it. Choose by core, time, cost, integration load and reversibility.
- **Beyond the notes:** check units and funnel order, state the purchase cycle, show a range, and treat moats as things that can decay.

## Self-test

<details class="quiz"><summary>What does Porter's Five Forces measure, and at what level?

It measures the pressure on profit in an industry as a whole, from five directions, not the results of one company.

</details>

<details class="quiz"><summary>Name the five forces in Porter's framework.

Rivalry among existing competitors, buyer power, supplier power, threat of new entrants, and threat of substitutes.

</details>

<details class="quiz"><summary>When is a SWOT analysis useful?

Only when it leads to action: each opportunity is matched to a strength you can use, and each threat to a weakness you must fix or avoid.

</details>

<details class="quiz"><summary>What are the Five Cs of a situational analysis?

Company, competitors, customers, collaborators and climate. Climate covers regulation, technology trends, economic conditions and culture.

</details>

<details class="quiz"><summary>Why are features alone not a moat?

A well-funded rival can copy a feature quickly. A moat is what keeps customers after a copy: network effects, switching costs, scale, proprietary data, brand, distribution, or regulatory and IP protection.

</details>

<details class="quiz"><summary>Define TAM, SAM and SOM.

TAM is everyone who could ever use the product. SAM is the part you can reach with your product, price and channels. SOM is the share you can realistically win in 3 to 5 years.

</details>

<details class="quiz"><summary>Why cross-check top-down and bottom-up market sizes?

Each method has its own assumptions. A large gap between them is a red flag that one input is wrong, so you check the assumption behind each method.

</details>

<details class="quiz"><summary>What are the three questions that choose between build, partner and buy?

Is the capability core to the moat, how fast the market window closes, and how reversible the choice is. Compare total cost of ownership, and the integration load.

</details>

<details class="quiz"><summary>Why write the go/no-go thresholds before the analysis?

Setting the bar first stops the analysis from being bent to fit the answer you wanted. It makes the decision defensible.

</details>

<details class="quiz"><summary>(Beyond the notes) Why must SOM always sit inside SAM, and SAM inside TAM?

A share of a layer cannot be bigger than the layer itself. If the funnel inverts, one input is wrong, so check the assumptions before presenting the number.

</details>

<details class="quiz"><summary>(Beyond the notes) Why do market-size answers often go wrong on units?

Households, scooters and rupees are different units. Mixing them, or dropping the purchase cycle such as one scooter every 6 years, gives a number that looks precise and is wrong.

</details>

<details class="quiz"><summary>(Beyond the notes) Why can a network effect still be weakened?

Shared rails and interoperability can let users switch quickly. UPI, where a user can move between payment apps in seconds, shows how a switching cost can disappear, so re-check the moat as the market changes.

</details>


# Chapter 20 · Execution - Roadmaps, PRDs, and Agile

<!-- lecture n="17" label="20" short="Roadmaps, PRDs, Agile" status="done" kind="execution" -->

## At a glance

| Question | Short answer |
|---|---|
| How do you plan the work? | A **theme-based roadmap** with Current, Near term and Future columns, and **no fixed dates**. |
| How do you set goals? | **OKRs**: one qualitative **objective** with two to four measurable **key results**. Outputs are not key results. |
| How do you document a feature? | A **PRD** that follows one story from **problem to metric**, where each section leads to the next. |
| What does a user story need? | A **benefit** ("so that") and **acceptance criteria** that can be tested. |
| How does the team run the work? | **Scrum**: a Product Owner, a Scrum Master and Developers, with sprints, events and three commitments. |
| What changes for an AI feature? | The PRD adds **eval criteria**, **failure modes**, **data requirements**, and **cost and latency budgets**. |
| What is the most common roadmap mistake? | A release plan in disguise: fixed dates and features, with no themes and no link to outcomes. |
| What is the most common story mistake? | A task written as a story, with a vague benefit or criteria that describe the code, not the behaviour. |
| How do you talk about Agile in an interview? | Say that Agile reduces up-front documentation. The PRD and the acceptance criteria still exist. |
| How do you keep a PRD useful after launch? *(Beyond the notes)* | Keep it short, link to living sources (dashboards, experiment logs), and add a "what we learned" note at each review. |

> [!NOTE] Where this comes from
> The vault draws on the Sigma PM concept book, Part A (2023) for the roadmap, PRD, user story and Scrum sections, and on *Cracking the PM Interview* for the company profiles (Intel, Google, Foursquare, Amazon, Yahoo). The AI PRD additions come from Part II of the vault and general AI product practice. OKR history, INVEST, Given/When/Then and the Scrum Guide details are general knowledge. The vault's further-reading list names *AI Product Reading*, *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

Execution questions test whether you can turn strategy into shipped work. This chapter covers how to plan (theme-based roadmaps and OKRs), how to document (PRDs and user stories with acceptance criteria), how to run the work (Agile and Scrum), and what changes when the feature is AI.

The chapter has five sections, each one a step on the way from strategy to shipped work:

- **20.1 Theme-based roadmaps and OKRs.** Time-horizon roadmaps and measurable quarterly goals.
- **20.2 PRD structure.** The sections of a PRD and how they connect.
- **20.3 User stories and acceptance criteria.** The "As a... I want... so that..." format, and testable done criteria.
- **20.4 Agile and Scrum essentials.** The Agile Manifesto values, Scrum roles (Product Owner, Scrum Master, Developers), artifacts, and events.
- **20.5 AI PRD additions: eval criteria, failure modes, data requirements.** The extra PRD sections an AI feature needs.

## Key takeaways

- A theme-based roadmap uses Current, Near term, and Future columns and avoids fixed release dates.
- OKRs pair one qualitative objective with two to four measurable key results. Outputs are not key results.
- A PRD follows one story from problem to metric, and each section should lead to the next.
- Every user story needs a benefit ("so that") and acceptance criteria that can be tested.
- AI PRDs add eval criteria, failure modes, data requirements, and cost and latency budgets.

> [!SIR] From the source notes
> A PRD follows one story from problem to metric, and each section should lead to the next.

## 20.1 Theme-based roadmaps and OKRs

> A theme-based roadmap shows where the product is heading in broad themes across time horizons, and OKRs tie each theme to measurable goals.

### Concept

**A good roadmap is visual and answers three questions:** What are we doing? Why are we doing it? How does this tie back to our OKRs?

**Theme-based vs release-based**

- A **release roadmap** commits to features and dates. Useful for sales and launch planning, but brittle when priorities change.
- A **theme-based roadmap** shows broader themes (for example, "reduce first-order drop-off") with no fixed dates. It keeps room to explore how to solve each problem.

**Three columns (time horizons)**

- **Current:** what the team is working on now. Cards are detailed.
- **Near term:** what comes next. Cards are partly detailed.
- **Future:** what needs more research. Cards are thin, and get more detailed as they move left.

![Three time-horizon columns. Cards get more detailed as they move from Future to Current, and every theme answers the three questions.](diagrams/l17-roadmap.svg)

**What sits under each theme:** ideas (the problem to solve), customer feedback linked to those ideas, and user stories ("As a user, I want X so that Y", see 20.3).

**OKRs (Objectives and Key Results)**

- **Objective:** a qualitative, inspiring goal.
- **Key results:** 2 to 4 measurable outcomes that show the objective is met. John Doerr's formula: "I will [objective] as measured by [key results]."
- Example: Objective "Make first-time sellers successful." KRs: "raise first-listing completion from 40% to 60%" and "cut median time-to-first-sale to 7 days."
- OKRs are usually set per quarter and graded at the end. Google grades each KR from 0.0 to 1.0, and for ambitious ("aspirational") OKRs about 0.6-0.7 counts as success; "committed" OKRs are expected to hit 1.0. Keep them few: a team with five objectives has none.
- OKRs vs North Star: the North Star stays stable for years; OKRs are the quarterly bets that move its input metrics (Chapter 15, North Star metric).

![One objective, two measurable key results, the formula, the grading scale, and the two common mistakes.](diagrams/l17-okr.svg)

**Common mistakes:** outputs in place of outcomes ("ship X" is not a key result), too many objectives, and roadmaps that are really release plans in disguise.

### Real-world examples

- **Intel:** OKRs originated at Intel under Andy Grove in the 1970s, building on management by objectives.
- **Google:** John Doerr, who learned OKRs at Intel, introduced them to Google's founders in 1999 after Kleiner Perkins invested; Google still uses them and published its OKR grading guidance. Doerr later wrote *Measure What Matters* (2018).
- **Foursquare (per Cracking the PM Interview):** a Foursquare PM (many of its PMs came from Google) says individual OKRs were superfluous at 30 people and still felt like overhead at 150, so the company adopted team-level OKRs to track firm metric goals. Lesson: fit the OKR process to company size.
- **Theme-based roadmap tools:** ProdPad popularised the Current / Near term / Future ("Now-Next-Later") roadmap format that the Sigma concept book describes.

### Practice questions

> [!INTERVIEW] Build a three-column theme-based roadmap for a grocery app with a 6-month horizon.
> *(Beyond the notes: a starting point.)* Put two or three themes in Current, one or two in Near term, and a couple of research questions in Future. Under each theme, list the problem, the feedback it came from, and one user story. Leave out dates on the themes, and show which OKR each theme moves.

> [!INTERVIEW] Write one objective and three key results for a food-delivery app's retention goal.
> *(Beyond the notes: a starting point.)* An objective such as "make weekly ordering a habit", with three measurable key results, for example a repeat-order rate, the share of users with a second order in 14 days, and a cap on cancelled orders as a guardrail. Check that each key result is an outcome, not a feature launch.

> [!INTERVIEW] A team says its OKR is "launch the new home screen." How do you rewrite it?
> **Answer outline (Q3):** Move from the output to the outcome. Rewrite as "increase weekly active users who open the app at least 3 times a week from 30% to 40%." Add a guardrail if needed, such as "keep order-error rate below 1%."

*Related (other chapters):* Chapter 14 (RICE), 20.2 and 20.3 of this page, 20.4 of this page.

## 20.2 PRD structure

> A Product Requirements Document tells cross-functional teams the problem, why it matters, what to build, and how success will be measured, in one connected story.

### Concept

A PRD is the document that keeps engineering, design, sales, and leadership on the same page. The PM owns it and gathers input from each team. Each section should follow from the one before, so the reader can trace a line from problem to metric.

**Typical structure**

1. **Problem definition:** the problem in plain words. State assumptions and gaps early so nobody is surprised later.
2. **Market research and opportunity:** competitors, market size if relevant, and why now.
3. **User research:** methods (surveys, interviews, focus groups), key demographics, behaviours, and pain points. Turn them into insights.
4. **Personas and use cases:** the segments that have the problem, and the use cases each one has.
5. **Prioritised use case:** pick one, and give a data-backed reason for choosing it (the Sigma book suggests tools such as an empathy map).
6. **Proposed solution:** features, split into functional and non-functional requirements.
7. **Solution prioritisation:** impact vs effort, or MoSCoW or Kano where they fit. Do not force a model that does not suit the product.
8. **UX design:** wireframes or prototypes (Figma, Balsamiq).
9. **Roadmap:** phases and milestones, agreed with the teams involved (Sigma lists idea sourcing, screening, research, strategy, creation, testing and feedback, constant improvement).
10. **Metrics:** the North Star with the reason it was chosen, app-level metrics (Sigma suggests AARRR), and feature-specific metrics for the prioritised solution. Add the launch plan and guardrails.

![The ten sections of a PRD, in the order a reader follows one story from problem to metric.](diagrams/l17-prd-chain.svg)

**Mini-example (PRD outline: "split bill" in a UPI app):** problem = friends settle group dinners over WhatsApp and forget; opportunity = high share of P2P payments are group settle-ups; persona = college students and young professionals; prioritised use case = one payer, 3-6 friends, same app; solution = create split from a completed payment, auto-requests, reminders (functional) + requests delivered in under 2 seconds and no duplicate debits (non-functional); prioritisation = MoSCoW for v1; metrics = splits created per weekly active user, % of requests paid within 48 hours, guardrail on payment failure rate.

**Keep it tight.** A PRD is a living, shared document, not a dump of everything the team knows. Link out to research rather than pasting it in.

**Interview tip:** When asked "how would you write a PRD for X?", walk the sections in order and say which one you would spend the most time on for that product.

### Real-world examples

- **Amazon (per Cracking the PM Interview):** new proposals are written documents, not slides, because documents force precision; meetings start with everyone silently reading the document. Amazon's "working backwards" PR/FAQ (a mock press release plus FAQ written before building) is its best-known PRD-like format.
- **Basecamp's Shape Up "pitch":** a lighter alternative to a PRD with five parts: problem, appetite (time budget), solution sketch, rabbit holes, and no-gos. Useful contrast if an interviewer asks how PRDs vary.
- **Typical consumer app launch (illustrative):** a PRD for a new feature at a company like Zomato or Hotstar would cover the user problem, segments, functional list and the experiment plan for launch.

### Practice questions

> [!INTERVIEW] Which PRD section would you write first, and why? Which one last?
> **Answer outline (Q1):** Problem first, because everything depends on it. Success metrics last, once the solution is clear, though you should draft them early. Explain the story link between sections.

> [!INTERVIEW] What goes in the "non-functional requirements" part of a PRD for a payments feature?
> *(Beyond the notes: a starting point.)* Speed targets (how fast a payment or request must complete), reliability (no duplicate debits, safe retries), availability during peaks, security and data protection, audit logs, and the consent and retention rules that apply. Each one should be a number or a testable rule.

> [!INTERVIEW] How do you keep a PRD from going stale after launch?
> *(Beyond the notes: a starting point.)* Keep it short and link to living sources (the dashboard, the experiment log, the research folder). Add a short "what we learned" section at each review, and retire the parts that no longer describe the product.

*Related (other chapters and this page):* 20.1 and 20.3 of this page, 20.5 AI PRD additions (this page), Chapter 14 (Choosing and defending a framework).

## 20.3 User stories and acceptance criteria

> A user story states who wants what and why. Acceptance criteria state how the team will know the story is done.

### Concept

**The user story format**

> As a <user type>, I want <goal>, so that <benefit>.

The Sigma concept book uses the same shape: "As a user, I want X in order to Y." The "so that" part matters most, because it ties the work to a real need. A story without a benefit is a feature request.

**Acceptance criteria** define done. Two common styles:

- **Checklist:** a list of conditions the feature must meet.
- **Given / When / Then:** a scenario format that testers and engineers can turn into tests.

Example:

- Story: As a commuter, I want to save a payment card, so that I can pay in one tap next time.
- Acceptance criteria:
  - Given I have added a card, when I select "Save", then the card appears in my wallet.
  - Given the card is saved, when I open checkout, then the card is pre-selected.
  - Given the card is invalid, when I try to save it, then I see an error and nothing is stored.

![A story with its benefit, three Given / When / Then criteria, and the six INVEST letters.](diagrams/l17-user-story.svg)

**Good stories follow INVEST** (Bill Wake): **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall (fits in a sprint), **T**estable. Write them from the user's view, and mark out-of-scope items, because the gap between stories is where bugs start. Large stories are called epics and are split (by workflow step, by user type, or happy path first, edge cases later).

Given/When/Then comes from behaviour-driven development (BDD), which lets criteria be turned directly into automated tests.

**Pitfalls:** writing tasks as stories ("As a developer, I want to refactor the API"), vague criteria ("works fast"), and criteria that describe implementation rather than behaviour.

### Real-world examples

- **Agile teams at Yahoo (per Cracking the PM Interview):** many teams moved to short iterations where, instead of long, detailed specs, the PM might write a one-sentence user story and engineers make the decisions.
- **Amazon (per Cracking the PM Interview):** once a proposal is approved, many teams follow Agile, with the PM as product owner responsible for writing user stories and the team's backlog.
- **Amazon one-click checkout (illustrative):** a story such as "As a returning shopper, I want to buy with saved details, so that I can finish in one step" maps directly to checkout criteria.

### Practice questions

> [!INTERVIEW] Turn "improve search" into two user stories with acceptance criteria.
> *(Beyond the notes: a starting point.)* For example, one story for a shopper who mistypes a product name (criteria: suggestions appear after the third letter; a spelling-corrected result is shown with a "showing results for" line) and one for a shopper who searches with no results (criteria: a fallback list appears, and no blank page). Each story names a user and a benefit.

> [!INTERVIEW] What is wrong with this story: "As a PM, I want a dashboard, so that data is visible"?
> **Answer outline (Q2):** The user is not a real user, and the benefit is vague. Rewrite around the person who needs the data and the decision they make with it (for example, "As a city ops manager, I want to see late deliveries by hour, so that I can add riders before the peak").

> [!INTERVIEW] How do acceptance criteria change between a happy path and an error path?
> *(Beyond the notes: a starting point.)* The happy path says what the user gets when everything works. The error path says what the user sees and what the system stores when something fails: the message, the retry option, and the rule that nothing half-saved is left behind. Write both, with one Given / When / Then each.

*Related (other chapters and this page):* 20.1, 20.2 and 20.4 of this page, 20.5 AI PRD additions (this page).

## 20.4 Agile and Scrum essentials

> Agile delivers value in small increments and adapts to change. Scrum is the most common framework for doing it, built on roles, artifacts, and time-boxed events.

### Concept

**Agile in one line:** deliver working software in small, usable increments, get feedback fast, and adapt. Agile is a set of principles (the Agile Manifesto), not a fixed process. Teams differ in how they apply it.

The Agile Manifesto (2001) has four values: **individuals and interactions** over processes and tools; **working software** over comprehensive documentation; **customer collaboration** over contract negotiation; **responding to change** over following a plan. The items on the right still matter; the left matters more.

Key principles (out of twelve) that come up in interviews:

- Working software is the primary measure of progress.
- Welcome changing requirements, even late.
- Business people and developers work together daily.
- Teams reflect regularly and adjust.

**Other frameworks:** Kanban (flow-based, limits work in progress), Lean, Extreme Programming (pair programming, tests first), and Feature-Driven Development.

**Scrum** (per the official Scrum Guide, last revised 2020; the Sigma book groups it as Roles, Artifacts and Time Boxes)

- **Roles ("accountabilities"):** *Product Owner* (one person who maximises value and orders the product backlog; often the PM), *Scrum Master* (coaches the team on Scrum and removes impediments; not a project manager), *Developers* (everyone who builds the increment; older guides said "Development Team").
- **Artifacts and their commitments:** *Product backlog* → Product Goal; *Sprint backlog* → Sprint Goal; *Increment* → Definition of Done.
- **Events (time-boxed):** *Sprint* (one month or less, commonly 2 weeks; contains all other events), *Sprint planning* (up to 8 hours for a one-month sprint), *Daily Scrum* (15 minutes, for the developers), *Sprint review* (inspect the increment with stakeholders), *Sprint retrospective* (improve how the team works). Backlog refinement is an ongoing activity, not a formal event.

![The Scrum loop: three artifacts with their commitments, four events in order, and the three accountabilities.](diagrams/l17-scrum-loop.svg)

**Scrum vs Kanban:** Scrum uses fixed sprints and commits to a sprint goal; Kanban has continuous flow, work-in-progress limits and no required roles, which suits support or ops teams with unpredictable inflow.

**Why teams use Scrum (Sigma concept book):** higher quality deliverables, coping better with change, better estimates for less time spent estimating, and more control of the schedule. Compared with waterfall, it shortens time to benefit.

**The PM's role:** in most Scrum teams the PM is the Product Owner. Writes and orders user stories (20.3), keeps the backlog tied to the roadmap, and accepts or rejects increments.

**Interview tip:** Don't say "Agile means no documentation." Say "Agile reduces up-front documentation, but the PRD and acceptance criteria still exist."

### Real-world examples

- **Yahoo (per Cracking the PM Interview):** teams moved to short iterations and PM-written user stories instead of long specs.
- **Amazon (per Cracking the PM Interview):** after a proposal is approved, many teams follow Agile with the PM as product owner, writing user stories and owning the backlog.
- **Spotify squads:** Spotify's 2012 "squads, tribes, chapters and guilds" model is a famous adaptation of Agile for autonomy at scale. Spotify itself has said the model evolved and was never followed exactly, so cite it as inspiration, not a recipe.
- **Startups (general pattern):** small teams often adopt Scrum or Kanban and shrink the ceremonies to fit their size.

### Practice questions

> [!INTERVIEW] Who should prioritise the product backlog, and why?
> *(Beyond the notes: a starting point.)* The Product Owner, because the Scrum Guide makes that one person accountable for ordering the backlog to maximise value. In most teams that is the PM, who holds the roadmap and the customer evidence. Engineers and stakeholders give input, but one person decides the order.

> [!INTERVIEW] What would you do if a sprint's stories keep spilling over to the next sprint?
> **Answer outline (Q2):** Check story size first (stories too big for a sprint are the usual cause). Then check whether scope changes mid-sprint. Use the retrospective to fix the root cause, and split stories or cut scope at planning.

> [!INTERVIEW] How would you explain Scrum to a stakeholder in two minutes?
> *(Beyond the notes: a starting point.)* Scrum is a repeating loop of one-month-or-shorter sprints. Each sprint starts with a goal and a short list of work from the backlog, the team builds it, shows it to stakeholders, and then reviews how it worked. The product owner decides the order of work; the team decides how to build it.

*Related (other chapters and this page):* 20.1, 20.2, 20.3 and 20.5 of this page.

## 20.5 AI PRD additions: eval criteria, failure modes, data requirements

> An AI feature's PRD needs extra sections that a normal PRD skips: how quality is judged, how the feature fails, what data it needs, and what it costs to run.

### Concept

A standard PRD assumes the same input gives the same output. AI outputs vary, so the PRD must define acceptable behaviour as a range. Add these sections to the standard structure from 20.2.

**1. Eval criteria (quality bar)**

- Define what "good" means for this task, with a rubric (for example: factual accuracy, relevance, tone, format).
- Set thresholds: "at least 90% of answers rated acceptable on the golden set, and under 2% harmful outputs."
- Name the eval method: golden dataset, human review, or LLM-as-judge. See Chapter 8 (Offline evals: golden datasets, rubrics, LLM-as-judge).

**2. Failure modes**

- List the known ways the feature fails: hallucination, wrong tool call, refusal of a valid request, leakage of private data, unsafe content.
- For each, state the user-facing behaviour and the fallback (show sources, ask a clarifying question, hand off to a human).
- Link each to a guardrail metric. See Chapter 8 (Guardrail metrics: harmful outputs, latency, cost).

**3. Data requirements**

- What data the feature needs (training, retrieval corpus, user context), where it comes from, and how often it refreshes.
- Consent and retention rules, including privacy obligations (Chapter 9, Privacy, consent, and data retention (India DPDP Act 2023)).
- Labelling plan for evals and improvement.

**4. Performance and cost budgets**

- Latency target (for example, first token under 1 second; full answer under 5 seconds).
- Cost per task and gross-margin impact (Chapter 6, Unit economics: cost per task, inference cost, gross margin).

**5. Launch and monitoring**

- Rollout stages, kill-switch conditions, and the drift and regression checks to run after launch (Chapter 10, Staged rollouts and kill switches).

![The standard PRD in the centre, with the five AI sections that a normal PRD does not have.](diagrams/l17-ai-prd.svg)

**Interview tip:** Name the failure mode you worry about most, and show how the PRD changes because of it.

**Mini-example (AI reply suggestions in a support tool):** eval = 85%+ of suggestions rated "usable with minor edits" on a 300-ticket golden set, under 0.5% policy-violating; failure modes = invents refund policy (fallback: only quote from the policy knowledge base, else "escalate"), wrong language (detect and match); data = past resolved tickets with PII masked, policy docs refreshed weekly; budgets = suggestion in under 3 seconds, under ₹1 per ticket; launch = 10% of agents, kill switch if edit rate rises above 60%.

### Real-world examples

- **GitHub Copilot:** GitHub's 2022 research on Copilot found that the acceptance rate of suggestions was the best predictor of developers' perceived productivity, which is why acceptance rate is a standard success criterion for AI-assist features.
- **Customer-support copilots (illustrative):** PRDs set a target share of suggested replies accepted by agents, plus an escalation rule for low-confidence answers.
- **Search and answer features (illustrative):** teams define citation requirements and a "no answer" behaviour as explicit PRD items.

### Practice questions

> [!INTERVIEW] Write three eval criteria for an AI resume reviewer.
> *(Beyond the notes: a starting point.)* For example: the share of suggested fixes that are factually correct against the candidate's own text (no invented employers or dates), the share of reviews that name the role's required skills, and the share of outputs that stay within the length and format rules. Set a threshold for each, and name the golden set and the reviewer.

> [!INTERVIEW] Which failure mode matters most for an AI medical-information chatbot, and what does the PRD require because of it?
> **Answer outline (Q2):** Harmful or wrong medical advice is the top risk. The PRD should require source citations, a clear "consult a doctor" path for high-risk queries, a refusal policy for dosing decisions, and a human review sample each week. Add a kill switch tied to the harmful-output rate.

> [!INTERVIEW] How would you set a latency budget for a streaming chat feature?
> *(Beyond the notes: a starting point.)* Set a target for the first visible token (the wait the user feels), and a separate target for the full answer. The PRD should also say what the user sees while waiting, and what happens after the budget is missed (a shorter answer, or a fallback message). Check both numbers at the 95th percentile, not only the average.

*Related (other chapters and this page):* 20.2, 20.3 and 20.4 of this page, Chapter 8 (Offline evals: golden datasets, rubrics, LLM-as-judge).

## Beyond the notes: planning traps

- **Roadmap as a promise.** A date on a Near term card turns a theme into a commitment. Keep dates for Current work only, and say so on the roadmap.
- **Outcomes that nobody can move.** A North Star metric is usually moved by several OKRs. If no team can move a key result, it belongs to the leadership review, not to a quarter's plan.
- **Scoring the roadmap by volume.** Count the problems solved against the OKR, not the number of cards.

## Beyond the notes: documentation traps

- **The PRD that is never read.** Put the decision and the open questions at the top, and link the long research.
- **Acceptance criteria written after the code.** Writing Given / When / Then before the build gives QA and engineers the same test.
- **One story per screen.** A story that spans three screens is an epic. Split it by workflow step, then by user type.

## Beyond the notes: interview corner

- **"What is the difference between a roadmap and a backlog?"** The roadmap shows themes and outcomes over time. The backlog is the ordered list of stories the team can pick up next. The roadmap answers why; the backlog answers what next.
- **"How do you know a key result is an outcome?"** Ask whether a user or the business changes if the key result is met. "Ship the feature" fails that test; "raise repeat orders from 20% to 25%" passes.
- **"What would make you change a PRD during a sprint?"** A new fact that breaks the problem statement or a failure that the guardrail metric shows. Otherwise the change waits for the review.
- **"Why do AI PRDs need a range?"** The same input can give different outputs, so a single pass or fail rule would be wrong. A threshold on a golden set says what "good enough" means.

## Revision cheat-sheet

![Chapter 20 on one page: plan, document, run, judge.](diagrams/l17-big-picture.svg)

- **20.1** Use a **theme-based roadmap** with Current, Near term and Future, and **no fixed dates**. OKRs: one **objective**, two to four measurable **key results**, graded by Google's 0.0 to 1.0 scale. Outputs are not key results.
- **20.2** A PRD has ten sections in one story: problem, market, user research, personas, prioritised use case, solution, prioritisation, UX, roadmap, metrics. Read it from problem to metric.
- **20.3** A story is "As a... I want... so that...". Acceptance criteria are a checklist or **Given / When / Then**. Good stories follow **INVEST**. The benefit and the criteria are what make a story testable.
- **20.4** Agile is a set of principles (Manifesto, 2001). **Scrum**: the Product Owner orders the backlog, the Scrum Master coaches, the Developers build. Events: sprint planning, daily Scrum, sprint review, retrospective. Commitments: product goal, sprint goal, definition of done.
- **20.5** An AI PRD adds **eval criteria** (the quality bar), **failure modes** (with fallbacks), **data requirements**, **performance and cost budgets**, and **launch and monitoring**.
- **Beyond the notes:** dates belong to current work only; read PRDs from the decision down; write the criteria before the build; name the failure mode you worry about most.

## Self-test

<details class="quiz"><summary>What is the difference between a release roadmap and a theme-based roadmap?

A release roadmap commits to features and dates, which is useful for launches but brittle when priorities change. A theme-based roadmap shows themes with no fixed dates, and keeps room to explore how to solve each problem.

</details>

<details class="quiz"><summary>What is the OKR formula, and how many key results should an objective have?

"I will [objective] as measured by [key results]." Two to four measurable key results, and few objectives per team.

</details>

<details class="quiz"><summary>Why is "launch the new home screen" not a good key result?

It is an output, not an outcome. The rewrite moves to the outcome the launch should cause, such as a higher weekly active user share, with an error-rate guardrail if needed.

</details>

<details class="quiz"><summary>Why should a PRD follow one connected story?

Each section should follow from the one before, so a reader can trace a line from the problem to the metric. The PRD is a shared document for engineering, design, sales and leadership.

</details>

<details class="quiz"><summary>What is the "so that" part of a user story for?

It states the benefit, which ties the work to a real need. A story without a benefit is a feature request.

</details>

<details class="quiz"><summary>What does INVEST describe?

A good user story is Independent, Negotiable, Valuable, Estimable, Small (fits in a sprint) and Testable (Bill Wake).

</details>

<details class="quiz"><summary>Who orders the product backlog in Scrum, and what is the Scrum Master's job?

The Product Owner, one person who maximises value and orders the backlog; in most teams that is the PM. The Scrum Master coaches the team on Scrum and removes impediments. The Scrum Master is not a project manager.

</details>

<details class="quiz"><summary>Name the Scrum events in order, and the time-box of the sprint planning for a one-month sprint.

Sprint planning, the Daily Scrum (15 minutes), the sprint review, and the sprint retrospective. Sprint planning takes up to 8 hours for a one-month sprint. The sprint itself is one month or less, commonly two weeks.

</details>

<details class="quiz"><summary>What are the five sections an AI PRD adds to a standard PRD?

Eval criteria (the quality bar), failure modes (with fallbacks), data requirements (sources, consent, labels), performance and cost budgets, and launch and monitoring (rollout stages, kill switch, drift checks).

</details>

<details class="quiz"><summary>Why does an AI PRD need a range rather than a single pass or fail rule?

The same input can produce different outputs, so acceptable behaviour is defined as a rate on a golden set, such as at least 90% of answers rated acceptable, plus hard rules that must always hold.

</details>

<details class="quiz"><summary>(Beyond the notes) Why should dates stay on current work only?

A date on a Near term or Future card turns a theme into a promise before the research is done. Keep dates for the work in progress, and say so on the roadmap.

</details>

<details class="quiz"><summary>(Beyond the notes) What makes acceptance criteria testable?

Each one is written as a behaviour that can be checked: a given state, an action, and an observable result (Given / When / Then). Vague words such as "works fast" and implementation details are not testable.

</details>



# Chapter 21 · Guesstimates

<!-- lecture n="18" label="21" short="Guesstimates" status="done" kind="estimation" -->

## At a glance

| Question | Short answer |
|---|---|
| What is a guesstimate? | A question with a number you cannot look up, such as US gasoline spend or the bikes a bike-taxi needs. |
| What do interviewers grade? | Your **structure**, your **stated assumptions** and your **self-checks**, more than the final figure. |
| What is the loop? | **Clarify, segment, assume, compute, sanity-check.** Aim for 10-15 minutes in total. |
| Which types cover most PM questions? | **Market sizing, user counts, storage, supply and capacity.** Each has a standard equation. |
| Which anchors should I know? | India about **1.45B people** and **950M internet users**; the US about **340M people** and **133M households**. |
| How do I check my answer? | A **per-unit check**, a **cross-check** (a second method) or an **anchor check**. Agreement within 2-3x is fine. |
| How do AI estimates differ? | Count **tokens per user**, price input and output apart, then convert to GPUs and embedding bytes. |
| How do I keep the arithmetic clean? | Round to friendly numbers, keep powers of ten apart, and **write every step down**. |
| How much time should I give each step? *(Beyond the notes)* | About 1-2 minutes to clarify and 2-3 to compute. Rehearse with a timer until the whole loop fits in 15. |
| What is the most common trap? *(Beyond the notes)* | Stopping after the maths and waiting for a verdict. Check your own work before the interviewer does. |

> [!NOTE] Where this comes from
> The chapter draws on the Sigma PM ConceptBook (Part A, 2023), the Consulting Club casebook, the Sigma PM Casebook (2023-2024) and the Guesstimates chapter of the vault's Others collection. Public figures are used only as sanity checks: UN World Population Prospects, US Census Bureau, IAMAI-Kantar, ITU / DataReportal, Pew Research, IDC, NFHS-5, SIAM, NPCI and EY-FICCI. Further reading names *Blogs & Newsletters* and *Product Teardowns*. No links are kept here. Section 21.4 (AI estimates) has no vault source; its conversion factors are general knowledge and approximate.

## The big picture

Guesstimates ask for a number you cannot look up, such as US gasoline spend, the bikes a bike-taxi startup needs, or the GPUs an AI feature needs at peak. Interviewers grade your structure, stated assumptions and self-checks more than the final figure. This chapter gives one repeatable loop, the anchor numbers to feed it, the standard equation for each question type, AI-specific conversions, and the arithmetic tricks that keep you fast and error-free.

The chapter has five sections, each one a building block for the next:

- **21.1 Guesstimate structure.** The five-step loop with a time budget, three sanity checks, and worked US gas and Bangalore bike-taxi examples.
- **21.2 Demographic and digital benchmarks.** A dated, source-labelled table of population, internet and smartphone users, households, urban share, vehicles, screen time, UPI volume and metro populations.
- **21.3 Common guesstimate types.** The equation and sanity check for each type, with corrected YouTube, Google Photos (about 750 PB a year) and ping-pong-ball worked examples.
- **21.4 AI estimates.** An assumption sheet (tokens per word, price per million tokens, FLOPs per token, bytes per dimension) and worked cost, GPU and vector-storage estimates.
- **21.5 Mental math tactics.** Rounding, scientific notation, fast division, time and byte constants, lakhs and crores, and checking as you go.

## Key takeaways

- Write the equation and confirm it with the interviewer before putting in any numbers.
- Every input gets a stated reason. Never let an assumption stay implicit, for example "one ride per user per day".
- Use round numbers and powers of ten, and write every intermediate result down.
- Finish with an independent sanity check (per unit, a second method, or a known anchor) and name the most sensitive assumption.
- Keep dated anchors: India about 1.45B people and about 950M internet users, the US about 340M people and about 133M households. Stale casebook inputs (250M Americans, $1.25 gas) can be off by 6x.

> [!SIR] From the source notes
> Write the equation and confirm it with the interviewer before putting in any numbers.

## 21.1 Guesstimate structure: clarify, segment, assume, compute, sanity-check

> Every guesstimate is the same loop: pin down the question, write the equation, state assumptions out loud, compute with round numbers, then check the answer against something you know.

### Concept

A guesstimate asks for a number you cannot look up. The interviewer grades your reasoning (structure, stated assumptions, self-correction), not how close you get. Run the same five-step loop every time.

**The loop (aim for 10-15 minutes in total)**

| Step | What you do | What you say aloud | Time |
|---|---|---|---|
| 1. Clarify | Pin down the geography, time period, unit and definition. | "Road fuel only? Personal cars only? Per year, in dollars?" | 1-2 min |
| 2. Segment | Write the equation before any numbers. Build bottom-up (units x frequency x value) or top-down with a MECE issue tree. Split into 2-4 segments where behaviour differs (age, city tier, heavy or light users). | "Spend = cars x gallons per car per year x price. Does that structure work for you?" | 2-3 min |
| 3. Assume | Give one number per term, each with a reason (personal experience, or a benchmark from 21.2). | "I'll assume one fill-up a week, because that is what a typical commuter does." | 2-3 min |
| 4. Compute | Use round numbers, track powers of ten separately, and write every intermediate result on the board. | "250M x 500 = 125B gallons." | 2-3 min |
| 5. Sanity-check | Test the answer at least one independent way, then name the most sensitive assumption. | "That is about $30 a week per car, which matches a weekly tank fill." | 1-2 min |

Validate the structure after step 2. The ConceptBook warns that finding out late that the interviewer had a different model in mind is very hard to recover from.

![The five steps as a loop, with a time budget for each. Validate the structure after step 2.](diagrams/l18-five-steps.svg)

**Three sanity checks to pick from**

- **Per-unit check:** divide the answer back down to one person, household or day, and ask whether it feels right.
- **Cross-check:** estimate it a second way (supply versus demand, top-down versus bottom-up). Agreement within 2-3x is fine.
- **Anchor check:** compare with a number you know, such as population, a company's reported revenue, or a physical limit like hours in a day.

![Three independent checks around one answer. Agreement within 2-3x is fine.](diagrams/l18-sanity-triangle.svg)

**Close in four parts:** the rounded answer, a range, the assumption that moves it most, and what you would verify with real data.

**Whiteboard layout:** the equation on the top line, a column of assumptions with a reason beside each, the computation underneath, the answer boxed, and the sanity check below it.

**Common traps**

- **Stopping after the math** and waiting for a verdict. Strong candidates check their own work before the interviewer does.
- **Hiding assumptions.** The interviewer should be able to change any one number and see its effect.
- **Implicit assumptions.** "0.5% adoption = 65,000 rides" quietly assumes one ride per user per day, so say it.
- **Precision theatre.** 1,000,553 is "about a million".
- **Stale anchors.** Many casebook answers use 1990s inputs (250M Americans, $1.25 gas). Update them, or say what year they are from (see example 1).

### Real-world examples

**1. Money spent on gasoline in the US per year (Sigma ConceptBook and Consulting Club casebook, inputs updated)**

- Clarify: road gasoline for personal vehicles, US, one year, in dollars.
- Segment: households x cars per household x gallons per car per year x price per gallon.
- Assume: 340M people / 2.5 per household is about 135M households, rounded to 130M. About 2 cars per household gives about 250M cars. One fill-up of about 10 gallons a week, over 50 weeks, gives 500 gallons per car per year (about 12,000 miles at 25 mpg). The price is about $3 per gallon (the ConceptBook's own round-number suggestion; recent US averages have been $3-3.50).
- Compute: 250M x 500 = 125B gallons. 125B x $3 = about $375B, so say $350-400B a year.
- Sanity-check: per car, 500 gallons x $3 = $1,500 a year, or about $30 a week, which matches a weekly tank fill. As a cross-check, the US uses roughly 9M barrels of gasoline a day (EIA); 9M x 42 gallons is about 380M gallons a day, or 135-140B gallons a year. So 125B for personal vehicles is close.
- Lesson: the casebook's original inputs (250M people, 1 car per household, $1.25 a gallon) give about $62.5B, six times too low for today. Every input was decades old.

![The gasoline equation split into its terms. Each leaf is one assumption with its reason.](diagrams/l18-gas-tree.svg)

### Try it locally: the gasoline numbers

*(Beyond the notes: reproduced locally with the standard library. The vault's own rounding is kept, and each rounded step is printed so you can see it.)*

```python title="lab_p18_gasoline.py"
# US gasoline spend per year (21.1 example 1), its cross-checks and the stale inputs.
# The vault rounds at each step; the exact products are printed beside the rounded ones.
GAL_PER_CAR = 10 * 50                    # 10 gallons a week, 50 weeks
homes = 340e6 / 2.5                      # people / people per household
print(f"homes (340M / 2.5)     : {homes / 1e6:.0f}M, vault rounds to 130M")
print(f"cars at 2 per home     : {130e6 * 2 / 1e6:.0f}M, vault uses 250M")
for cars in (250e6, 260e6):
    print(f"spend at {cars / 1e6:.0f}M cars     : ${cars * GAL_PER_CAR * 3 / 1e9:.0f}B a year")
print(f"per car a year / week  : ${GAL_PER_CAR * 3:,} / ${GAL_PER_CAR * 3 / 52:.1f}")
gal_year = 9e6 * 42 * 365                # EIA: 9M barrels a day, 42 gallons a barrel
print(f"EIA cross-check        : {gal_year / 1e9:.0f}B gallons a year")
old = 250e6 / 2.5 * GAL_PER_CAR * 1.25   # the stale inputs: 250M people, 1 car a home, $1.25
print(f"stale inputs           : ${old / 1e9:.1f}B, today {375 / (old / 1e9):.0f}x that")
city_gal = 1e6 / 2.5 * 2 * 500           # practice question 1: a 1M-person city
print(f"city gallons a day     : {city_gal / 350 / 1e6:.2f}M (350 days)")
print(f"US gallons per person  : {380e6 / 340e6:.2f} a day")
```

```output
homes (340M / 2.5)     : 136M, vault rounds to 130M
cars at 2 per home     : 260M, vault uses 250M
spend at 250M cars     : $375B a year
spend at 260M cars     : $390B a year
per car a year / week  : $1,500 / $28.8
EIA cross-check        : 138B gallons a year
stale inputs           : $62.5B, today 6x that
city gallons a day     : 1.14M (350 days)
US gallons per person  : 1.12 a day
```

> [!WARNING] Beyond the notes: check the arithmetic
> The vault says 130M homes give about 250M cars. Two cars each is 260M, so the straight product is $390B, not $375B. The vault's $350-400B range covers both, so the answer holds, but write the 250M as a rounding of 260M, not as a product. The $3 price and the 500 gallons are the assumptions to name.

**2. Bike-taxi fleet for Bangalore (Sigma casebook, Guesstimate 1, Google PM)**

- Clarify: one city (Bangalore), the launch phase, and the number of bikes needed.
- Assume: a population of about 1.3 crore (13M). 0.5% of residents take one ride a day, giving 65,000 rides a day. Each bike completes 12-13 rides a day, allowing for traffic and waiting time.
- Compute: 65,000 / 13 = 5,000 bikes. Adding 10% for maintenance and spares gives 5,500.
- Sanity-check: 13 rides of about 25 minutes each is 5-6 hours of riding in a 10-12 hour shift, which is plausible. Peak check: if 30% of rides fall in a 3-hour morning peak and a bike does about 2 rides an hour, the peak needs 65,000 x 0.3 / (3 x 2) = about 3,250 bikes. That is under 5,000, so here the daily total is the binding constraint, not the peak.

### Try it locally: the bike-taxi fleet, Hyderabad and mechanics

*(Beyond the notes: reproduced locally. It also runs practice questions 2 and 3 of this section, with the same equation.)*

```python title="lab_p18_supply.py"
# Bangalore bike taxi (21.1 example 2), Hyderabad and mechanics (practice questions 2 and 3).
rides = 1.3e7 * 0.005                    # 0.5% of 13M residents ride once a day
bikes = rides / 13                       # 13 rides a bike a day
print(f"rides a day / bikes        : {rides:,.0f} / {bikes:,.0f}")
print(f"with 10% spares            : {bikes * 1.1:,.0f}")
peak = rides * 0.3 / (3 * 2)             # 30% in a 3-hour peak, 2 rides an hour
print(f"bikes for the 3-hour peak  : {peak:,.0f}")
print(f"binding limit              : {'the daily total' if bikes > peak else 'the peak'}")
hyd = 1.1e7 * 0.004 / 13                 # Hyderabad: 1.1 crore, 0.4% adoption
print(f"Hyderabad bikes, + spares  : {hyd:,.0f}, {hyd * 1.1:,.0f}")
top, bottom = 1e6 * 2 / 12, 2000 * 3 * 1.2 * 25
print(f"mechanics, top-down / bottom-up: {top / 1e3:.0f}K / {bottom / 1e3:.0f}K a month")
print(f"gap between the methods    : {abs(bottom - top) / top * 100:.0f}%")
```

```output
rides a day / bikes        : 65,000 / 5,000
with 10% spares            : 5,500
bikes for the 3-hour peak  : 3,250
binding limit              : the daily total
Hyderabad bikes, + spares  : 3,385, 3,723
mechanics, top-down / bottom-up: 167K / 180K a month
gap between the methods    : 8%
```

**3. One player's revenue from a market total (illustrative)**

- Size the whole market first, then apply a share assumption last and justify it. In a market with 4-5 large players, the leader often holds 20-30%. For example, a fuel retailer with 10% of the US market above would sell about $35-40B of gasoline a year.

### Practice questions

1. How many gallons of gasoline does one city consume per day? Walk through your clarifying questions first.
2. Estimate the number of bikes needed for a new bike-taxi company in one city. What changes if it expands to five cities?
3. How many cars do mechanics in your city service each month? Build a top-down estimate, then a bottom-up one.
4. Estimate annual spending on coffee in India. Which assumption would you validate first?

**Outline for question 1:** Clarify the city (say a US city of 1M people), personal vehicles only, and gasoline only. 1M / 2.5 = 400K households x 2 cars = 800K cars. 800K x 500 gallons = 400M gallons a year, and / 350 days is about 1.1M gallons a day. Sanity-check: 380M gallons a day nationally / 340M people is about 1.1 gallons per person per day, which matches. (The local run of this outline is in the gasoline block above.)

**Outline for question 2:** Bangalore needs 5,500 bikes, as in example 2. Rerun the same formula per city with that city's own population and adoption (lower adoption in smaller cities). For Hyderabad, 1.1 crore x 0.4% = 44,000 rides / 13 = about 3,400 bikes, plus 10% is about 3,700. Spares cannot be shared across cities, so apply the buffer per city, then add the cities up.

**Outline for question 3:** Top-down: a city with 1M cars x 2 services per car per year / 12 is about 170K services a month. Bottom-up: 2,000 garages x 3 bays x 1.2 cars per bay per day x 25 working days is about 180K. The two methods agree within 10%, which is the sanity check.

**Outline for question 4:** Clarify whether this means all coffee or only cafe purchases. 1.45B people x about 70% aged 15 and over is about 1B. About 20% drink coffee (concentrated in the south), giving 200M. At about 5 cups a week, 200M x 5 x 52 is about 52B cups a year. A blended price of about ₹20 per cup (a home cup ₹5-10, a filter-coffee stall ₹20-30, a cafe ₹200 or more) gives about ₹1 lakh crore (about $12B) of consumer spend. The coffee-drinker share is the most sensitive input, so validate it first. Sanity-check: 52B cups x about 2 g of coffee is about 100,000 tonnes, the same order as the Coffee Board's domestic consumption estimate of roughly 90,000-100,000 tonnes a year.

### Try it locally: coffee spend in India

*(Beyond the notes: reproduced locally with the standard library. The vault rounds 203M drinkers to 200M and 1.015B adults to about 1B; the code keeps those roundings so the numbers match the outline.)*

```python title="lab_p18_coffee.py"
# Coffee spend in India (practice question 4 of 21.1).
print(f"1.45B x 70% = {1.45e9 * 0.70 / 1e9:.3f}B, rounded to 1B")
drinkers = 1e9 * 0.20                    # about 20% drink coffee
cups = drinkers * 5 * 52                 # 5 cups a week
print(f"drinkers / cups a year     : {drinkers / 1e6:.0f}M / {cups / 1e9:.0f}B")
print(f"spend at Rs 20 a cup       : Rs {cups * 20 / 1e12:.2f} lakh crore")
print(f"in dollars at Rs 87        : ${cups * 20 / 87 / 1e9:.0f}B")
print(f"beans at 2 g a cup         : {cups * 2 / 1e6:,.0f} tonnes")
```

```output
1.45B x 70% = 1.015B, rounded to 1B
drinkers / cups a year     : 200M / 52B
spend at Rs 20 a cup       : Rs 1.04 lakh crore
in dollars at Rs 87        : $12B
beans at 2 g a cup         : 104,000 tonnes
```

*Related:* Chapter 21 (this page), 21.2 (benchmarks), 21.3 (common types), 21.5 (mental math); Chapter 19 (Market sizing and entry decisions); Chapter 22 (Metrics cases)

## 21.2 Demographic and digital benchmarks for India and the US

> Memorise a small set of round benchmarks for India and the US, say the year and that they are approximate, and you can anchor almost any sizing question.

### Concept

Guesstimates go faster when you already hold a few anchor numbers. You will not have internet access in the interview, so learn the rounded column and quote it as an assumption ("about 1.45 billion, as of 2025").

**Core benchmarks (rounded; values checked November 2026)**

| Metric | India | US | Year and source type |
|---|---|---|---|
| Population | ~1.45 billion | ~340 million | 2024-25; UN WPP 2024 (India), US Census Bureau population estimates (US) |
| Age structure | ~25% under 15; median age ~28 | ~18% under 15; median age ~39 | 2024; UN WPP 2024 |
| Internet users | ~950 million (~65%) | ~320 million (~93%) | India 2025: IAMAI-Kantar *Internet in India*; US 2024-25: ITU / DataReportal. TRAI counts subscriptions (about 1 billion), which overstates people. |
| Smartphone users | ~800 million (estimates range ~700-900M) | ~90% of adults, ~290-300 million people | India 2025: industry estimates (Deloitte, Counterpoint and others; no official count); US 2024: Pew Research |
| Smartphones shipped per year | ~150 million | ~125-135 million | 2025; IDC (India, 152M); Canalys / Counterpoint quarterly data (US, approximate) |
| Households | ~320-330 million (derived) | ~133 million | India: population / 4.4; last Census count (2011) was ~249M, and the next Census is under way. US 2025: Census Bureau CPS |
| Average household size | ~4.4 people | ~2.5 people | India: NFHS-5 (2019-21); US: Census Bureau CPS 2024-25 |
| Urban share | ~36% (national definition) | ~83% | c. 2025; UN World Urbanization Prospects (2018-revision estimates). India Census 2011: 31%. See the caveat below. |
| Two-wheelers | ~50% of households own one; ~19-20M sold a year | niche | NFHS-5 (2019-21); SIAM, FY2024-25 |
| Cars | ~7.5% of households own one; ~4.3M passenger vehicles sold a year | ~92% of households have a vehicle (~1.9 each); ~16M new light vehicles sold a year | NFHS-5; SIAM FY2024-25; US Census ACS; US auto industry sales 2024-25 |
| Daily phone screen time | ~5 hours | ~4.5-5 hours | India 2024: EY-FICCI media and entertainment report; US: third-party trackers (methods vary widely) |
| UPI payments | ~24 billion a month (~800M a day), ~₹29-30 lakh crore by value | n/a | Aug-Sep 2026; NPCI monthly statistics. The average ticket is about ₹1,200. |

**Metro populations (urban agglomeration, c. 2025, rounded)**

| India | Population | US | Population |
|---|---|---|---|
| Delhi | ~30-35M | New York metro | ~20M (city ~8.5M) |
| Mumbai | ~20-22M | Los Angeles metro | ~13M |
| Kolkata | ~15M | Chicago metro | ~9.5M |
| Bengaluru | ~13-14M (casebook uses 1.3 crore) | Dallas-Fort Worth metro | ~8M |
| Chennai | ~12M | | |
| Hyderabad | ~11M | | |

India figures are UN urban-agglomeration estimates; US figures are Census Bureau metropolitan-area (MSA) estimates for 2024. City-limit figures are much smaller, so say which one you are using.

**How to use them**

- Pick the round number (India 1.4-1.5B, US about 1/3 of a billion) and state it as an assumption with its year.
- Cross-check with a derived figure. 1.45B / 4.4 people per household is about 330M Indian households; 340M / 2.5 is about 135M US households, close to the Census count.
- **The key digital insight:** the US is near saturation, so growth comes from engagement, conversion and ARPU. India still adds users, so growth comes from new (often rural, Indic-language) users. About 950M Indians are online but only about 800M have smartphones, so many reach the internet through shared or basic devices.
- Urban share is the usual proxy for where digital products and quick logistics are reachable.
- UPI at about 800M transactions a day is a strong anchor for any Indian payments, commerce or fintech estimate.

**Caveats**

- These numbers move every year. Treat them as anchors and say so in the interview.
- Definitions differ. "Internet user" can mean any use in the last month (IAMAI) or a subscription (TRAI). "Household" can mean a dwelling or a family unit.
- Urban share depends on definition. The UN's 2025 World Urbanization Prospects uses a grid-based "Degree of Urbanisation" method that counts many Indian census villages as towns, which puts India's urban share far above 36%. In interviews, use about 36% and name the definition.
- Before a real product decision, verify against the primary datasets named in the table.

![Anchor numbers for India and the US, each with its year and source type.](diagrams/l18-benchmarks.svg)

### Real-world examples

**1. Reach for an Indian consumer app.** A PM starts with about 950M internet users (IAMAI-Kantar 2025), narrows to about 800M smartphone users, then applies the target age band and city tier. The point is the funnel, not the exact count. (illustrative)

**2. US subscription sizing.** Starting from about 133M households, a PM sizes a household subscription (such as streaming) by household, not by person, because one account serves about 2.5 people. Near-saturated internet use means the levers are conversion and ARPU, not new users. (illustrative)

**3. India versus US for a feature.** A team compares urban share (about 36% versus 83%), household size (4.4 versus 2.5) and two-wheeler versus car ownership (about 50% versus about 92% vehicle access) to argue that India needs low-data, low-end-device designs, shared-device support, and two-wheeler-first delivery logistics. (illustrative)

**4. Payments product sizing.** UPI's roughly 24 billion transactions a month at an average of about ₹1,200 gives a ceiling for any UPI-based feature: a 1% attach rate is about 240M transactions a month. (illustrative)

### Try it locally: from benchmarks to answers

*(Beyond the notes: reproduced locally. It derives the household figures, the UPI ceiling, the urban funnel from practice question 1 and the child-households check from practice question 2.)*

```python title="lab_p18_benchmarks.py"
# Benchmarks from 21.2: derived figures, the UPI ceiling, the urban funnel and homes with children.
print(f"India homes (1.45B / 4.4)  : {1.45e9 / 4.4 / 1e6:.0f}M")
print(f"UPI a day / value a month  : {24e9 / 30 / 1e6:.0f}M / Rs {24e9 * 1200 / 1e12:.1f} lakh crore")
print(f"1% attach on UPI volume    : {24e9 * 0.01 / 1e6:.0f}M a month")
young = 1.45e9 * 0.36 * 0.45             # urban, ages 18-45
print(f"urban adults 18-45         : {young / 1e6:.0f}M")
print(f"smartphones at 85-90%      : {young * 0.85 / 1e6:.0f}-{young * 0.90 / 1e6:.0f}M")
print(f"banked on UPI at 65%       : {young * 0.85 * 0.65 / 1e6:.0f}-{young * 0.90 * 0.65 / 1e6:.0f}M")
homes_kids = 340e6 * 0.22 / 1.9          # under-18s, about 1.9 children a home
print(f"US homes with children     : {homes_kids / 1e6:.1f}M, {homes_kids / 133e6 * 100:.0f}% of 133M")
```

```output
India homes (1.45B / 4.4)  : 330M
UPI a day / value a month  : 800M / Rs 28.8 lakh crore
1% attach on UPI volume    : 240M a month
urban adults 18-45         : 235M
smartphones at 85-90%      : 200-211M
banked on UPI at 65%       : 130-137M
US homes with children     : 39.4M, 30% of 133M
```

### Practice questions

1. How many smartphone users would a new Indian fintech app reach if it targets only urban adults aged 18-45? State every benchmark you use.
2. Estimate the number of US households with a child under 18. Which benchmark is weakest, and how would you tighten it?
3. Why might a launch in the US need a different sizing approach from one in India? Name two differences in the benchmarks.

**Outline for question 1:** 1.45B x 36% urban is about 520M urban residents. Ages 18-45 are about 45% of India's population (about 30% are under 18), giving about 235M. Urban smartphone penetration of about 85-90% for this age group gives about 200-210M. Then apply the target segment, such as banked UPI users (about 65%), for about 130-140M. Sanity-check: that is under a tenth of the population, which fits an urban, young, banked segment.

**Outline for question 2:** Under-18s are about 22% of 340M, or about 75M children. Households with children have about 1.9 children each, giving about 40M households, roughly 25-30% of 133M. The weakest input is children per household, so tighten it by splitting households into one, two and three-or-more children.

**Outline for question 3:** (a) The unit differs: in the US, size by household and ARPU because penetration is near 93%; in India, size by individual through an internet-to-smartphone funnel, with shared devices and 4.4 people per household. (b) Reach differs: 83% versus 36% urban changes the reachable base, delivery logistics and price points, and in India the payment rail (UPI) changes the conversion assumptions.

*Related:* Chapter 21 (this page), 21.1 (structure), 21.3 (common types), 21.5 (mental math); Chapter 19 (Market sizing and entry decisions); Chapter 11 (Segmentation and personas)

## 21.3 Common guesstimate types: market sizing, user counts, storage, supply

> Most PM guesstimates are one of four types, and each has a standard equation and a standard sanity check you can reuse.

### Concept

| Type | Equation | Typical sanity check |
|---|---|---|
| Market sizing | units (people, households, businesses) x penetration x frequency x price | spend per user per month; compare with a known company's revenue |
| User counts | population x segment share x usage share (daily or monthly) | DAU / population ratio; DAU / MAU between about 0.2 and 0.6 for most apps |
| Storage | items per user x users x size per item x replication | photos per user per day; compare with a known product's upload volume |
| Supply and capacity | peak demand per hour / throughput per unit per hour x (1 + buffer) | utilisation per unit (hours busy per shift) |

**1. Market sizing (revenue or spend)**

- Frame it as TAM (everyone who could buy), SAM (the part your product can serve, by geography, segment or channel) and SOM (what you can realistically capture in 3-5 years).
- For marketplaces, size GMV first, then revenue = GMV x take rate.

**2. User counts**

- Ask whether the target is daily, monthly or total users, because the answer changes the frequency term.
- Segment by age or city tier when usage differs sharply between groups.

**3. Storage and data volume**

- Segment users by behaviour (heavy, medium, light) and give each segment its own upload rate.
- Name the data type, because size differs by orders of magnitude: text ~1 KB, compressed photo ~2 MB, a minute of HD video ~50-100 MB.
- State whether you mean new storage per year or the total accumulated, and whether you include replication (often 3x).

**4. Supply and capacity**

- Size for the peak hour, not the daily average. Peak is often 2-3x the average hour.
- Bike-taxi and ride-hailing fleets are supply problems: rides per peak hour / rides per vehicle per hour, plus a buffer for vehicles offline.

**Choosing the decomposition**

- Start bottom-up if you can name the unit (a user, an item, a vehicle). Start top-down with an issue tree if you cannot.
- Say the choice aloud and confirm it with the interviewer before computing.

### Real-world examples

**1. Market sizing: US gasoline (worked in 21.1).** About 250M cars x 500 gallons x $3 is about $375B a year. To get one player's revenue, apply a justified share last: a retailer with 10% of the market sells about $35-40B of fuel. (Sigma ConceptBook and Consulting Club casebook, inputs updated.)

**2. User counts and revenue: YouTube ad revenue per day in the US (Sigma ConceptBook, Practice Question 2).**

- Users: the US population is about 300M, spread evenly over ages 0-80. A 10-year band is 1/8 of the population (about 40M) and a 20-year band is 1/4 (75M). Daily viewing: 0% for 0-10, 100% for 10-20 (40M) and 20-40 (75M), 75% for 40-60 (about 56M), 50% for 60-80 (about 38M). The total is about 210M, so call it about 200M daily users.
- Views: about 10 videos per user per day gives about 2B views a day.
- Ad views: if half of views start with an ad, that is about 1B ad views a day.
- Revenue: at $10 per 1,000 ad views, 1B / 1,000 x $10 = about $10M a day, or about $3.65B a year.
- Sanity-check: two-thirds of Americans watching daily is plausible. For revenue, YouTube's reported global ad revenue was about $11B in 2018 and about $36B in 2024 (Alphabet annual reports). If the US is 40-50% of that, US YouTube ads are about $15B a year today, roughly 4x this estimate. Say so, and name the weak inputs: US CPMs are often above $10, many views carry more than one ad (mid-rolls), and the US population is now about 340M. The estimate is the right order of magnitude but on the low side.

**3. Storage: new photos added to Google Photos in a year (Sigma casebook, Guesstimate 3, Google PM; arithmetic corrected).**

- Users: about 2.4B Android users (photos only, this year's uploads only).
- Clicked photos per week, by segment: heavy 20% x 5, medium 50% x 2, light 30% x 1 = 2.3 a week, or about 120 a year. (The casebook writes 260, which is 5 x 52, the heavy-user rate only.)
- Received photos at a 1:3 clicked-to-received ratio: about 360 a year.
- Storage: clicked 2.4B x 120 = about 290B photos x 2 MB = about 580 PB. Received 2.4B x 360 = about 860B photos x 0.2 MB = about 170 PB. The total is about 750 PB (0.75 EB) of new photos a year, or about 2 EB of raw disk with 3x replication.
- Correction note: the casebook's 3,750 PB swaps the two sizes (it applies 2 MB to received photos) and also uses the 260 rate, so it overstates by about 5x.
- Sanity-check: 2.4B x 480 is about 1.2 trillion photos a year. Google said in 2020 that users uploaded about 28B photos and videos a week, about 1.5 trillion a year, so the estimate is within about 25%.

**4. Volume: ping-pong balls in a 747 (Consulting Club casebook brainteaser; numbers refined).**

- Ball: a regulation ball is 4 cm across, so about 34 cm³. Random packing fills about 64% of space, so each ball takes about 50 cm³. (The casebook approximates a ball as a 3 cm cube, 27 cm³, which undercounts its size.)
- Plane: the main cabin is roughly 60 m x 6 m x 2.5 m, about 900 m³. With the upper deck, call it about 1,000 m³ (10^9 cm³), with seats removed.
- Compute: 10^9 / 50 = 20M balls, or about 30M if you also fill the cargo holds (about 1,500 m³ in total).
- Sanity-check: a 747 carries about 400-500 passengers; 20M / 450 is about 45,000 balls per passenger, about 2 m³ each, which is about right for one seat's share of cabin space. The method, not the answer, is what is graded.

### Try it locally: user counts, market sizes and storage

*(Beyond the notes: reproduced locally. The output keeps the source's rounding, so each line says what it is compared with. The YouTube bands are printed both ways.)*

```python title="lab_p18_market.py"
# Market sizing from 21.3: YouTube viewers and ad revenue, a news site (question 4),
# food-delivery TAM (question 2) and Uber drivers (question 3).
pop = 300e6                              # the source uses 300M so the splits are clean
b10, b20 = pop / 8, pop / 4
exact = b10 + b20 + 0.75 * b20 + 0.50 * b20    # 10-20, 20-40, 40-60, 60-80 (0-10 is 0%)
print(f"daily viewers, exact bands : {exact / 1e6:.0f}M (vault's 40M band: 209M)")
ad_day = 1e9 / 1000 * 10                 # 1B ad views a day at $10 per 1,000
print(f"YouTube ads a day / a year : ${ad_day / 1e6:.0f}M / ${ad_day * 365 / 1e9:.2f}B")
print(f"gap to about $15B a year   : {15 / (ad_day * 365 / 1e9):.1f}x")
news_day = 5e6 * 3 * 4 / 1000 * 2       # 3 page views x 4 ad slots, $2 CPM
print(f"news site a year, a visitor: ${news_day * 365 / 1e6:.1f}M, ${news_day * 365 / 5e6:.2f}")
tam = 2e7 * 0.25 * 4 * 400 * 12 / 1e7   # Mumbai: 25% order, 4 a month, Rs 400 an order
print(f"food TAM, SAM, SOM (crore) : {tam:,.0f}, {tam * 0.6:,.0f}, {tam * 0.06:,.0f}")
drivers = 1e7 * 0.5 * 0.1 * 0.1 * 0.4 / 2   # working age, corporate, cab at peak, 40%, 2 an hour
print(f"Uber drivers, + 15% offline: {drivers:,.0f}, {drivers * 1.15:,.0f}")
```

```output
daily viewers, exact bands : 206M (vault's 40M band: 209M)
YouTube ads a day / a year : $10M / $3.65B
gap to about $15B a year   : 4.1x
news site a year, a visitor: $43.8M, $8.76
food TAM, SAM, SOM (crore) : 9,600, 5,760, 576
Uber drivers, + 15% offline: 10,000, 11,500
```

### Try it locally: Google Photos and voice notes

*(Beyond the notes: reproduced locally. The vault's corrected figures are rounded (580 PB, 170 PB, 750 PB); the exact products are printed next to them.)*

```python title="lab_p18_storage.py"
# Google Photos new uploads (21.3 example 3) and the voice-note app (practice question 1).
users = 2.4e9
print(f"clicked a week, average    : {0.20 * 5 + 0.50 * 2 + 0.30 * 1:.1f}")
clicked, received = 120, 360             # 2.3 x 52 = 119.6, rounded; 1:3 clicked to received
c_pb = users * clicked * 2e6 / 1e15      # 2 MB per clicked photo
r_pb = users * received * 0.2e6 / 1e15   # 0.2 MB per received photo
print(f"clicked / received storage : {c_pb:.0f} PB / {r_pb:.0f} PB")
print(f"total, and with 3x copies  : {c_pb + r_pb:.0f} PB, {3 * (c_pb + r_pb) / 1000:.1f} EB")
print(f"photos a year, ours / Google: {users * 480 / 1e12:.2f}T / {28e9 * 52 / 1e12:.2f}T")
day_tb = 10e6 * 5 * 30 * 2 / 1e9         # 10M users, 5 notes a day, 60 KB a note
print(f"voice notes a day / a year : {day_tb:.0f} TB / {day_tb * 365 / 1000:.1f} PB")
print(f"with 3x replication        : {day_tb * 365 * 3 / 1000:.1f} PB")
```

```output
clicked a week, average    : 2.3
clicked / received storage : 576 PB / 173 PB
total, and with 3x copies  : 749 PB, 2.2 EB
photos a year, ours / Google: 1.15T / 1.46T
voice notes a day / a year : 3 TB / 1.1 PB
with 3x replication        : 3.3 PB
```

### Try it locally: ping-pong balls in a 747

*(Beyond the notes: reproduced locally with the standard library. The ball's volume is computed, then rounded to 50 cm³ as the vault does.)*

```python title="lab_p18_pingpong.py"
# Ping-pong balls in a Boeing 747 (21.3 example 4), refined.
import math
ball = 4 / 3 * math.pi * 2 ** 3          # 4 cm across, in cm3
print(f"ball {ball:.0f} cm3; at 64% packing {ball / 0.64:.0f} cm3, use 50")
print(f"main cabin 60 x 6 x 2.5    : {60 * 6 * 2.5:.0f} m3, call it 1,000 with upper deck")
print(f"balls: cabin / with cargo  : {1e9 / 50 / 1e6:.0f}M / {1.5e9 / 50 / 1e6:.0f}M")
per = 1e9 / 50 / 450                     # 450 passengers
print(f"per passenger              : {per:,.0f} balls, {per * 50 / 1e6:.1f} m3")
```

```output
ball 34 cm3; at 64% packing 52 cm3, use 50
main cabin 60 x 6 x 2.5    : 900 m3, call it 1,000 with upper deck
balls: cabin / with cargo  : 20M / 30M
per passenger              : 44,444 balls, 2.2 m3
```

### Practice questions

1. Estimate the storage needed for a voice-note app used by 10 million people. Which user segments would you split by?
2. Estimate the market size for a food-delivery app in Mumbai. Show TAM, SAM and SOM.
3. How many ride-hailing drivers are needed to serve a city at 8 AM? Which assumption dominates?
4. Estimate annual revenue from ads on a news website with 5 million daily visitors.

**Outline for question 1:** Assume an average of 5 notes per user per day, 30 seconds each, at about 2 KB per second of compressed audio (about 16 kbps), so 60 KB per note. 10M x 5 x 60 KB = 3 TB a day, about 1.1 PB a year, or about 3.3 PB with 3x replication. Split heavy users (say 20 notes a day) from light users (1 a day), because heavy users dominate storage. Sanity-check: 300 KB per user per day is less than one photo.

**Outline for question 2:** Mumbai has about 2 crore (20M) people. About 25% (5M) order food online, at about 4 orders a month, giving 20M orders a month. At an average order of ₹400, that is ₹800 crore a month, or about ₹10,000 crore of GMV a year (TAM). SAM: the 60% in serviceable areas and price bands, about ₹6,000 crore. SOM: a 10% share in 3 years is about ₹600 crore of GMV, and a 20% take rate gives about ₹120 crore of revenue. Sanity-check: India's two large food-delivery platforms together process on the order of ₹60,000-70,000 crore a year, and a top-three metro at 10-15% of that is ₹6,000-10,000 crore, so the TAM is in range.

**Outline for question 3:** Use the Sigma casebook's Uber Bangalore case (Guesstimate 2). About 1 crore people, more than 50% of working age (about 50 lakh), 1 in 10 in corporate jobs (5 lakh), and 1 in 10 of those using cabs or autos at peak (50,000 rides). A 40% Uber share is 20,000 rides; at 2 rides per driver per hour, that is about 10,000 drivers. The peak-hour ride share dominates. Add about 15% for drivers offline. Sanity-check: about 1 driver per 1,000 residents.

**Outline for question 4:** 5M daily visitors x 3 page views x 4 ad slots = 60M impressions a day. At a $2 CPM, that is 60,000 x $2 = $120K a day, or about $44M a year. Sanity-check: about $9 per daily visitor per year, which is plausible for display ads. The CPM (which varies about 5-10x between India and the US) is the most sensitive input.

> [!WARNING] Beyond the notes: the rounding in the market examples
> The exact products differ from the outline's rounded words. The food-delivery run gives TAM 9,600, SAM 5,760 and SOM 576 (crore, a year), against the outline's about 10,000, 6,000 and 600. The YouTube bands give about 206M daily viewers exactly, and 209M with the vault's rounded 40M band, against "about 210M". All of these are the same order of magnitude; say which rounding you used.

*Related:* Chapter 21 (this page), 21.1 (structure), 21.2 (benchmarks), 21.4 (AI estimates); Chapter 19 (Market sizing and entry decisions)

## 21.4 AI estimates: tokens per user, inference compute, embedding storage

> For AI products, estimate three things: how many tokens each user consumes, what serving them costs in money and GPUs, and how much storage the embeddings need. Then state every conversion factor as an assumption.

### Concept

The vault sources cover classic guesstimates, not AI, so this note uses general knowledge. Every number marked **(assumption)** should be said aloud as one, and prices should be checked against a current price sheet before any real decision.

**Assumption sheet (say these before computing)**

| Factor | Working value | Note |
|---|---|---|
| Tokens per English word | ~1.3 (1 token is about 0.75 words) | Hindi and other Indic scripts can take 2-4x more tokens per word on many tokenizers (assumption) |
| Tokens per page of text | ~500-700 | at ~400-500 words a page |
| Input and output split | chat about 3:1 input to output; RAG 10:1 or more | retrieved context and chat history dominate input |
| Price per million tokens | e.g. **$1 input / $4 output (assumption)** for a mid-tier model | output usually costs 3-5x input; across model tiers prices differ by 10-100x |
| Compute per generated token | ~2 x parameters FLOPs | e.g. a 70B-parameter model is about 1.4 x 10^11 FLOPs per token |
| GPU serving throughput | **~1,000-2,000 output tokens/s per GPU (assumption)** for a ~70B model with batching | depends heavily on model, batch size and hardware |
| Embedding size | dimensions x bytes per dimension | float32 = 4 bytes, float16 = 2, int8 = 1, binary = 1/8 |
| Vector index overhead | ~1.5-2x raw vectors | graph indexes such as HNSW, plus metadata and replicas |

**1. Tokens per user**

- Tokens per day = active users x requests per user per day x (input + output tokens per request).
- In multi-turn chat, each turn usually resends the conversation history, so input tokens grow with conversation length. Prompt caching cuts the cost of the repeated part.

**2. Inference cost and compute**

- Daily cost = input tokens x input price + output tokens x output price. Keep input and output separate, because their prices differ.
- Gross-margin check: inference cost per user per month should be a small fraction of revenue per user (for example, under 20-30% for a subscription product).
- GPU count (self-hosted) = peak output tokens per second / output tokens per second per GPU, plus 30-50% headroom. Peak is usually 2-3x the daily average.
- Seconds per day is 86,400, about 10^5, so tokens per day / 10^5 gives the average tokens per second, slightly overstated, which is a safe direction for capacity.

**3. Embedding storage**

- Storage = items x chunks per item x dimensions x bytes per dimension x index overhead.
- Anchor: one 1,536-dimension float32 vector is 1,536 x 4 = 6,144 bytes, about 6 KB. One million chunks is about 6 GB raw, or about 9-12 GB with the index.
- Quantisation: int8 cuts raw size 4x and binary 32x, at some cost to recall (often recovered by re-ranking the top results at full precision).

**What interviewers look for**

- Naming the unit (per user, per request, per token) so the arithmetic stays clean.
- Separating input from output tokens, and API cost from self-hosted GPU cost.
- Naming the biggest uncertainty, usually how often users invoke the feature and how much context each call carries.

![From tokens to dollars: keep the input and output prices apart, then compare with revenue per user.](diagrams/l18-ai-cost-stack.svg)

### Real-world examples

**1. Chat assistant cost per user (illustrative).** 20 turns per active user per day x about 1,500 tokens per turn (with history and context) = 30,000 tokens a day, or about 900K (about 1M) tokens per user per month. At a blended **$2 per million tokens (assumption)**, that is about $2 per active user per month. Sanity-check: against a $20 subscription, inference is about 10% of revenue, which is healthy. A frontier model at 10x the price would take all of it.

**2. Semantic search over a help centre (illustrative).** 200,000 articles x 10 chunks = 2M chunks. At 1,024 dimensions x 4 bytes = 4 KB per vector, that is about 8 GB raw, or about 12-16 GB with the index. Sanity-check: that fits in the memory of a single large server, so a managed vector database is a convenience here, not a requirement.

**3. Capacity planning for a feature launch (illustrative).** A 5M-DAU app where 10% (500K users) use an AI feature twice a day, at 2,000 tokens per session (1,500 input + 500 output).

- Tokens: 500K x 2 x 2,000 = 2B tokens a day (1.5B input, 0.5B output).
- API cost: 1.5B x $1/M + 0.5B x $4/M = $1,500 + $2,000 = $3,500 a day, about $105K a month, or about $0.21 per feature user per month.
- Compute: 0.5B output tokens / 86,400 s is about 5,800 output tokens/s on average. At a 3x peak, that is about 17,000/s. At about 1,500 tokens/s per GPU, that is about 12 GPUs, or about 16 with headroom.
- Sanity-check: about $0.02 per DAU per day is small next to typical consumer ad revenue per user, but check provider rate limits at 17,000 tokens per second and plan a fallback model.

### Try it locally: chat cost, feature capacity and the meal planner

*(Beyond the notes: reproduced locally with the standard library. The prices are the assumptions the vault states, and the rounded words in the vault are printed next to the exact values.)*

```python title="lab_p18_ai_cost.py"
# AI chat cost (21.4 example 1), a feature launch (example 3) and the meal planner (question 1).
chat_month = 20 * 1500 * 30              # 20 turns a day, 1,500 tokens a turn
print(f"chat tokens a user a month : {chat_month:,} (vault: about 1M)")
print(f"cost at $2 a million       : ${chat_month / 1e6 * 2:.2f}; at 10x: ${chat_month / 1e6 * 20:.0f}")
users = 5e6 * 0.10                       # 10% of 5M DAU
ins, outs = users * 2 * 1500, users * 2 * 500     # two sessions a day each
day = ins / 1e6 * 1 + outs / 1e6 * 4     # $1 per million input, $4 per million output
print(f"launch tokens a day        : {(ins + outs) / 1e9:.0f}B ({ins / 1e9:.1f}B in, {outs / 1e9:.1f}B out)")
print(f"launch cost a day / month  : ${day:,.0f} / ${day * 30:,.0f}")
print(f"per feature user / per DAU : ${day * 30 / users:.2f} / ${day * 30 / 5e6:.3f} a month")
peak = outs / 86400 * 3                  # 3x peak on the average output rate
print(f"peak output tokens a second: {peak:,.0f}, about {peak / 1500:.0f} GPUs at 1,500 a second")
print(f"meal planner a month       : ${500e3 * 2 * 3000 / 1e6:,.0f} to ${500e3 * 2 * 3000 / 1e6 * 5:,.0f}")
```

```output
chat tokens a user a month : 900,000 (vault: about 1M)
cost at $2 a million       : $1.80; at 10x: $18
launch tokens a day        : 2B (1.5B in, 0.5B out)
launch cost a day / month  : $3,500 / $105,000
per feature user / per DAU : $0.21 / $0.021 a month
peak output tokens a second: 17,361, about 12 GPUs at 1,500 a second
meal planner a month       : $3,000 to $15,000
```

### Try it locally: embedding storage and the token bill

*(Beyond the notes: reproduced locally. The embedding sizes are the vault's, and the index overhead is a range.)*

```python title="lab_p18_embeddings.py"
# Embedding storage (21.4 example 2, practice question 2) and the copilot token bill (question 4).
def raw(items, chunks, dims, size):
    return items * chunks * dims * size
help_raw = raw(200_000, 10, 1024, 4)     # 200K articles x 10 chunks, float32
print(f"help centre raw            : {help_raw / 1e9:.1f} GB, with index {help_raw * 1.5 / 1e9:.0f}-{help_raw * 2 / 1e9:.0f} GB")
print(f"1M chunks at 1,536 dims    : {raw(1_000_000, 1, 1536, 4) / 1e9:.1f} GB raw")
f32 = raw(50_000_000, 3, 768, 4)         # 50M listings x 3 chunks
print(f"listings float32 / int8    : {f32 / 1e9:.0f} GB / {f32 / 4 / 1e9:.0f} GB")
print(f"float32 with index 1.5-2x  : {f32 * 1.5 / 1e9:.0f}-{f32 * 2 / 1e9:.0f} GB")
per = 5 * 600 + 500 + 300                # 5 articles, ticket and instructions, output
print(f"copilot tokens a ticket    : {per:,}, retrieved {5 * 600 / per * 100:.0f}%")
print(f"a month, input / total     : {(5 * 600 + 500) * 1e6 / 1e9:.1f}B / {per * 1e6 / 1e9:.1f}B")
```

```output
help centre raw            : 8.2 GB, with index 12-16 GB
1M chunks at 1,536 dims    : 6.1 GB raw
listings float32 / int8    : 461 GB / 115 GB
float32 with index 1.5-2x  : 691-922 GB
copilot tokens a ticket    : 3,800, retrieved 79%
a month, input / total     : 3.5B / 3.8B
```

> [!WARNING] Beyond the notes: the "per DAU per day" line in the capacity example
> The capacity example says about $0.02 per DAU per day. The arithmetic gives about $105,000 a month across 5M DAU, which is about $0.021 per DAU per **month**, or roughly $0.0007 a day. The vault's per-day figure is a unit slip. Say "per DAU per month" in an interview.

### Practice questions

1. Estimate the monthly inference cost of an AI meal planner with 500,000 monthly active users and 2 sessions per user per month. State your price assumption.
2. How much storage do embeddings need for 50 million product listings, each with 3 chunks, at 768 dimensions? What would int8 quantisation save?
3. What would make your cost estimate wrong by 10x? Name the two most sensitive inputs.
4. A support copilot answers 1 million tickets a month, retrieving 5 help articles of 600 tokens each per ticket. What dominates the token bill?

**Outline for question 1:** 500K x 2 = 1M sessions a month. Assume about 3,000 tokens per session (input plus output), so 3B tokens a month. At a blended **$1-5 per million tokens (assumption)**, the cost is about $3,000-15,000 a month, or about 0.6-3 cents per MAU. Sanity-check: even at the high end, that is far below a typical subscription price. Prompt caching, a smaller model for simple steps, or a cheaper tier would lower it.

**Outline for question 2:** 50M x 3 = 150M vectors. 768 x 4 bytes = 3,072 bytes, about 3 KB each, so 150M x 3 KB is about 460 GB raw, or about 700-900 GB with the index. int8 cuts raw vectors to about 115 GB, which saves about 345 GB (75%). Sanity-check: about 460 GB float32 needs a sharded or managed vector database, while about 115 GB int8 can fit on one high-memory server.

**Outline for question 3:** (a) Usage frequency: sessions per user can vary 10x between a daily habit and an occasional tool. (b) Tokens per call: chat history and retrieved context can push input from 500 to 10,000 tokens. Model choice is a close third, because prices across tiers differ by 10-100x.

**Outline for question 4:** Input is 5 x 600 = 3,000 tokens of retrieved context, plus about 500 for the ticket and instructions, against about 300 of output. Retrieved context is about 80% of tokens. 1M x 3,800 is about 3.8B tokens a month, about 3.5B of which is input. Reducing the articles retrieved from 5 to 3, or caching common articles, is the biggest cost lever.

*Related:* Chapter 21 (this page), 21.3 (common types), 21.5 (mental math); Chapter 4 (4.4 Latency, cost per query, and capacity planning); Chapter 5 (LLM basics - tokens, context windows, prompting, temperature); Chapter 5 (RAG, fine-tuning, and embeddings - when to use each); Chapter 6 (Unit economics - cost per task, inference cost, gross margin)

## 21.5 Mental math tactics

> Round early, keep the powers of ten in a separate column, and write each step down so the interviewer can follow, and check, the arithmetic.

### Concept

The goal is not accuracy to a few percent. It is clean, visible arithmetic with no order-of-magnitude slips. The sources put it bluntly: use 350 days, not 365, and "don't be anal" about precision.

**1. Round to friendly numbers**

- Round uncertain inputs to one significant figure, or to a number that divides cleanly. 1.45B becomes 1.4B or 1.5B; 365 days becomes 350 or 400; 52 weeks becomes 50.
- Round one factor up and the next one down so the errors cancel. Example: 365 x 48 is close to 400 x 45 = 18,000 (the true answer is 17,520, so 3% off).

**2. Scientific notation for big numbers**

- Split each number into a short mantissa and a power of ten, multiply the mantissas, and add the exponents.
- Example: 2.4B users x 120 photos x 2 MB = (2.4 x 1.2 x 2) x 10^(9+2+6) bytes, about 5.8 x 10^17 bytes, or 580 PB.
- Byte ladder: KB 10^3, MB 10^6, GB 10^9, TB 10^12, PB 10^15, EB 10^18.

**3. Fast division and percentages**

- Divide by 4: halve twice (300M / 4 = 75M). Divide by 5: double, then divide by 10 (340 / 5 = 68). Multiply by 25: multiply by 100, then divide by 4.
- Percentages are reversible: 8% of 50 = 50% of 8 = 4.
- 10% shifts the decimal one place, 1% shifts it two places, 5% is half of 10%.
- Near-squares: 48 x 52 = 50² - 2² = 2,496.

**4. Constants worth memorising**

- Seconds in a day: 86,400, about 10^5 (about 15% high, so a safe overestimate for capacity). Seconds in a year: about 3 x 10^7.
- Hours in a year: about 8,760, about 9,000. Working days in a year: about 250.
- Peak-to-average ratio for traffic: about 2-3x.
- Rule of 72: years to double = 72 / growth rate in percent (12% a year doubles in about 6 years).

**5. Indian units and currency**

- 1 lakh = 100,000 (10^5). 1 crore = 10 million (10^7). 1 lakh crore = 10^12.
- 1 billion = 100 crore, so 1.45 billion = 145 crore. 1 million = 10 lakh.
- Exchange rate: about ₹85-90 per US dollar (2025-26), so $1B is about ₹8,500-9,000 crore and ₹1 lakh crore is about $11-12B.

**6. Check as you go**

- Units check: write the unit next to every number (users x sessions/user/day = sessions/day).
- Reverse check: divide the answer back by one input and see whether you recover the other.
- Bracket it: compute a low and a high case. If they differ by more than 10x, an assumption needs more thought.

**Discipline**

- Do anything with more than two steps on paper or aloud, not in your head.
- Communicate the rounded result ("about $375 billion") but leave the working visible.

![Six tactics for clean mental arithmetic, with one example each.](diagrams/l18-mental-math.svg)

### Real-world examples

**1. Gas spending in one pass (Consulting Club casebook, inputs updated in 21.1).** 250M cars x 500 gallons = (2.5 x 5) x 10^(8+2) = 12.5 x 10^10 = 125B gallons. x $3 = $375B. Only one multiplication of mantissas and one addition of exponents.

**2. YouTube users with friendly divisors (Sigma ConceptBook).** 300M / 4 = 75M for each 20-year age band and 300M / 8 = about 40M for each 10-year band, so the age split is done in the head. The source deliberately uses 300M rather than the exact population so that the divisions are clean.

**3. Bangalore bike taxis in Indian units (Sigma casebook).** 1.3 crore = 13M. 0.5% of 13M = 65,000 (1% is 130,000, then halve). 65,000 / 13 = 5,000 bikes. Converting crores to millions first avoids losing a zero.

**4. Tokens to GPUs (see 21.4).** 0.5B output tokens a day / 10^5 seconds is about 5,000 tokens per second (the exact answer is 5,800), and x 3 for peak is about 15,000-17,000.

### Try it locally: the mental-math checks

*(Beyond the notes: reproduced locally. Each line puts the exact value next to the rounded one the vault uses.)*

```python title="lab_p18_mental_math.py"
# Mental-math checks from 21.5: each line prints the exact value beside the rounded one.
print(f"1.4B x 0.5 x 0.3 = {1.4e9 * 0.5 * 0.3:,.0f}")
print(f"2.3 crore = {2.3e7 / 1e6:.0f}M = {2.3e7 / 1e5:.0f} lakh; 2.3 / 145 = {2.3 / 145 * 100:.1f}%")
print(f"365 x 48 = {365 * 48:,} vs 400 x 45 = {400 * 45:,}, off {(18000 - 17520) / 17520 * 100:.1f}%")
print(f"4M x 3 a week: {4e6 * 3 * 52 / 1e6:.0f}M at 52 weeks, {4e6 * 3 * 50 / 1e6:.0f}M at 50")
print(f"1e8 requests a day: {1e8 / 1e5:,.0f} a second, exact {1e8 / 86400:,.0f}")
print(f"peak at 3x the exact figure: {3e8 / 86400:,.0f} a second")
print(f"0.5B output a day: {0.5e9 / 1e5:,.0f} a second, exact {0.5e9 / 86400:,.0f}")
print(f"2.4B x 120 x 2 MB = {2.4e9 * 120 * 2e6:.2e} bytes")
print(f"1 lakh crore at Rs 87 = ${1e12 / 87 / 1e9:.1f}B; rule of 72 at 12%: {72 / 12:.0f} years")
```

```output
1.4B x 0.5 x 0.3 = 210,000,000
2.3 crore = 23M = 230 lakh; 2.3 / 145 = 1.6%
365 x 48 = 17,520 vs 400 x 45 = 18,000, off 2.7%
4M x 3 a week: 624M at 52 weeks, 600M at 50
1e8 requests a day: 1,000 a second, exact 1,157
peak at 3x the exact figure: 3,472 a second
0.5B output a day: 5,000 a second, exact 5,787
2.4B x 120 x 2 MB = 5.76e+17 bytes
1 lakh crore at Rs 87 = $11.5B; rule of 72 at 12%: 6 years
```

### Practice questions

1. Compute 1.4 billion x 0.3 x 0.5 in your head, and say each step aloud.
2. Convert 2.3 crore into millions and into lakhs. What is 2.3 crore as a percentage of 145 crore?
3. Your product has 4 million users at 3 sessions per week. How many sessions per year? Round, then state the error.
4. A service handles 100 million requests a day. What are its average and peak requests per second?

**Outline for question 1:** Do the easy factor first: 1.4B x 0.5 = 0.7B (700M). Then 700M x 0.3 = 210M. The order matters: halving first keeps the numbers clean.

**Outline for question 2:** 2.3 crore = 2.3 x 10^7 = 23 million = 230 lakh. 2.3 / 145 is about 1.6% (since 1% of 145 is 1.45, and 2.3 / 1.45 is about 1.6).

**Outline for question 3:** 4M x 3 = 12M a week. x 50 weeks = 600M a year. The exact figure with 52 weeks is 624M, so the rounding is about 4% low, which is fine for a guesstimate.

**Outline for question 4:** 10^8 / 10^5 = 1,000 requests per second on average (the exact answer is about 1,160). At a 3x peak, that is about 3,000-3,500 requests per second.

*Related:* Chapter 21 (this page), 21.1 (structure), 21.2 (benchmarks), 21.3 (common types), 21.4 (AI estimates); Chapter 14 (RICE)

## Beyond the notes: checking the figures before you quote them

The vault's worked numbers are rounded at several steps. Quote the rounded figure, but know the product behind it.

| Vault figure | Straight product | What to say |
|---|---|---|
| 250M cars (130M homes x 2) | 260M cars, $390B a year | "about $375B, from 250-260M cars" |
| 10-year band about 40M (YouTube) | 37.5M, so 206M daily viewers | "about 200M daily users" |
| Food-delivery TAM about 10,000 crore | 9,600 crore | "about ₹10,000 crore" |
| Google Photos about 580 + 170 PB | 576 + 173 PB, 749 PB total | "about 750 PB" |
| Coffee drinkers 200M, 52B cups | 203M drinkers, 52.8B cups | "about 52B cups a year" |
| AI chat: 1M tokens a month, 10x takes all of $20 | 900K tokens: $1.80; at 10x, $18 (90%) | "about $2; at 10x, most of the $20" |
| Capacity: $0.02 per DAU per day | $0.021 per DAU per month | say "per month" |

A correction you can make on the spot: when the interviewer asks "where did 250M come from?", say "130M homes times two cars, rounded down" and the question is closed.

## Beyond the notes: interview corner

- **"How do you start a guesstimate you have never seen?"** Ask the clarifying questions out loud, then write the equation before any numbers. Let the interviewer correct the structure while it is still cheap to change.
- **"Your answer is 10x what you expected. What now?"** Check the units first (per day or per year, per user or per city). Most 10x errors are a unit slip or a missing division, not a wrong assumption.
- **"Which number would you check first?"** Name the most sensitive input with its reason, for example the drinker share in the coffee estimate or the per-user frequency in an AI feature.
- **"Why not a precise figure?"** A precise figure invites scrutiny of every digit. A rounded figure with a range and a named assumption shows the reasoning.

## Beyond the notes: pitfalls

- **The unit slip.** "Per DAU per day" and "per DAU per month" differ by a factor of 30. Write the unit next to every term.
- **Double-counting the frequency.** If the segment is already "users who order a month", do not multiply by orders a month again without checking.
- **Forgetting replication and retries.** Storage often needs 3x copies; API cost needs retries and evaluation traffic. Say which you included.
- **Using the cheapest or dearest tier by default.** Model prices differ by 10-100x across tiers; name the tier you assume.
- **Quoting a stale anchor without its year.** Dated benchmarks are fine if you say the year. Undated ones are the 1990s numbers the casebooks still carry.

## Revision cheat-sheet

![Chapter 21 on one page: five ideas, each with the question it answers.](diagrams/l18-big-picture.svg)

- **21.1** Clarify, segment, assume, compute, sanity-check. Write the equation before the numbers, validate the structure after step 2, and close with a rounded answer, a range, the key assumption and what you would verify.
- **21.2** Memorise the rounded India and US anchors and quote their year. Derive what you can: 1.45B / 4.4 households, 340M / 2.5 households, UPI at about 800M a day.
- **21.3** Four types, each with its equation: market sizing (units x penetration x frequency x price), user counts, storage (items x users x size x replication) and supply (peak demand / throughput x buffer). Size storage by data type, and size supply for the peak hour.
- **21.4** Count tokens per user, price input and output apart, convert to GPUs at peak with headroom, and convert embeddings with dimensions x bytes x index overhead. A 1,536-dimension float32 vector is about 6 KB.
- **21.5** Round to friendly numbers, multiply mantissas and add exponents, keep the units next to every number, and bracket the answer with a low and a high case.
- **Beyond the notes:** check the rounding behind each figure, quote "per month" or "per day" exactly, and say which tier or price you assumed.

## Self-test

<details class="quiz"><summary>What are the five steps of the guesstimate loop, in order?

Clarify, segment, assume, compute, sanity-check. Aim for 10-15 minutes in total, and validate the structure after step 2.

</details>

<details class="quiz"><summary>Why does the interviewer care more about structure than the final figure?

Because the grade rests on your reasoning: the equation, the stated assumptions, and your self-correction. A figure within a reasonable range with a clear structure scores better than a lucky number with a hidden assumption.

</details>

<details class="quiz"><summary>What are the three sanity checks you can pick from?

A per-unit check (divide the answer back to one person, household or day), a cross-check (estimate a second way, with agreement within 2-3x), and an anchor check (compare with a number you know, such as population or a physical limit).

</details>

<details class="quiz"><summary>What is the US gasoline estimate, and how do you check it?

About 250M cars x 500 gallons = 125B gallons, x $3 = about $375B a year (say $350-400B). Check it per car ($1,500 a year, about $30 a week) and against the EIA barrel figure (about 135-140B gallons a year).

</details>

<details class="quiz"><summary>Which four types cover most PM guesstimates, and what is each equation?

Market sizing (units x penetration x frequency x price), user counts (population x segment share x usage share), storage (items per user x users x size per item x replication), and supply and capacity (peak demand per hour / throughput per unit per hour x (1 + buffer)).

</details>

<details class="quiz"><summary>What does the chat assistant estimate show about cost per user?

About 1M tokens a user a month at a blended $2 per million (assumption) is about $2 per active user a month. Against a $20 subscription that is about 10% of revenue, which is healthy.

</details>

<details class="quiz"><summary>How do you size embedding storage for a vector index?

Items x chunks x dimensions x bytes per dimension x index overhead. A 1,536-dimension float32 vector is about 6 KB, so one million chunks is about 6 GB raw, or about 9-12 GB with the index.

</details>

<details class="quiz"><summary>What does int8 quantisation save, and what does it cost?

It cuts raw vector size by 4x compared with float32. It can cost some recall, which is often recovered by re-ranking the top results at full precision. In the listings example, 460 GB of float32 becomes about 115 GB.

</details>

<details class="quiz"><summary>What is a fast way to compute 365 x 48 in your head?

Round to 400 x 45 = 18,000. The true answer is 17,520, so the error is under 3%. Round one factor up and one down so the errors cancel.

</details>

<details class="quiz"><summary>(Beyond the notes) Why can "$0.02 per DAU per day" be a unit slip?

About $105,000 a month across 5M daily users is about $0.021 per user per month, which is roughly $0.0007 a day. Write the unit next to every number so a month cannot pass for a day.

</details>

<details class="quiz"><summary>(Beyond the notes) What should you say when asked where 250M cars came from?

"130M homes times two cars, rounded down." That names the rounding, and it is the honest answer. The straight product is 260M cars, about $390B a year.

</details>

<details class="quiz"><summary>(Beyond the notes) How do you answer when your estimate is 10x what you expected?

Check the units first: per day or per year, per user or per city. Most 10x errors are a unit slip or a missing division, not a wrong assumption.

</details>


# Chapter 22 · Case Types and How to Approach Each

<!-- lecture n="19" label="22" short="Case types" status="done" kind="case playbook" -->

## At a glance

| Question | Short answer |
|---|---|
| How many case types are there? | Eight: product design, improvement, root cause (RCA), metrics, pricing, strategy and market entry, go-to-market, and brainstorming. |
| How do you start any case? | Ask clarifying questions first. Then name the case type and pick its framework. |
| Which framework for design? | CIRCLES (Comprehend, Identify, Report, Cut, List, Evaluate, Summarize). |
| Which framework for RCA? | Define the metric, scope it, check external causes, walk the journey, then zoom in. |
| How do you price? | Find willingness to pay, estimate the cost floor, pick a strategy, then set a range. |
| How do you enter a market? | Size it, read the forces and competitors, check company fit, then recommend with conditions. |
| How do you end a case? | With one metric and one guardrail, and a clear recommendation with a trade-off. |
| What do you do with a lateral question? | Structure first, generate many ideas, then prioritise out loud. |
| Which case type is this? *(Beyond the notes)* | Read the verb in the prompt: design, improve, why did it drop, measure, price, enter, launch, brainstorm. |

> [!NOTE] Where this comes from
> The vault names four books and interview records for this chapter: the Sigma PM Casebook (2023-2024, Part B), the XLRI PM Casebook 2023, Lewis C Lin's *Decode and Conquer*, and the Primer *Frequently Asked Questions in Interviews*. The Sigma interview reports are cited in Chapter 23. No links are kept here.

## The big picture

This chapter is the playbook. Each case type tests a different skill, and each has a repeatable structure. The chapter covers product design, product improvement, root cause analysis, metrics, pricing, strategy and market entry, go-to-market, and brainstorming. Start with the clarifying questions in every case, then apply the matching framework.

The chapter has eight sections, one per case type:

- **22.1 Product design cases.** Design a product for a user group, using CIRCLES.
- **22.2 Product improvement cases.** Find pain points in an existing product and propose a prioritised fix.
- **22.3 Root cause analysis and diagnosis cases.** Explain why a metric moved, scoping before hypothesising.
- **22.4 Metrics cases.** Pick a north star, funnel metrics and guardrails.
- **22.5 Pricing cases.** Find willingness to pay, choose a strategy, and set a range.
- **22.6 Strategy and market entry cases.** Decide whether and how to enter a market.
- **22.7 Go-to-market and launch cases.** Plan a launch, rollout and success criteria.
- **22.8 Brainstorming and lateral questions.** Generate, structure and prioritise ideas out loud.

![Read the verb in the prompt to find the case type, then pick its framework.](diagrams/l19-which-case.svg)

## Key takeaways

- Identify the case type first, then pick the matching framework.
- Clarify scope and goal before you give any answer.
- Scope the problem before you hypothesise, especially in root cause questions.
- Always end with a metric and a guardrail.
- Give a clear recommendation with a trade-off, not a list of options.

> [!SIR] From the source notes
> Identify the case type first, then pick the matching framework.

## 22.1 Product design cases

> Design cases test whether you can turn a vague user need into a specific, prioritised product with a defended trade-off.

### Concept

**Typical prompts:** "Design a tablet for kids" (Sigma, Google PM), "How would you design a car for the deaf?" (Sigma, Flipkart), "How would you design an e-commerce platform for senior citizens?" (Sigma, Flipkart), "Design a bicycle renting app for tourists" (XLRI), "Design a product for Delhi Metro; analyse all stakeholders and choose one" (Sigma, Google PM).

**Step-by-step approach.** The CIRCLES flow in Chapter 12 (CIRCLES) is the default skeleton. Sigma's version is Context, Segment, Needs, Prioritise, Solution, KPIs.

1. **Comprehend.** Restate the prompt. Ask: new product or change to an existing one, physical or digital, which platform, which geography, and what the business goal is. Do not design yet.
2. **Identify the user.** List all stakeholders (user, buyer, operator), then 2-3 personas. Pick one primary persona and say why (size, pain, willingness to pay). Use Chapter 11 (Segmentation and personas).
3. **Report needs.** Walk the persona's current journey (the 5Es in Chapter 11, User journeys and the 5Es) and list the pains and jobs (Chapter 11, Jobs-to-be-done).
4. **Cut.** Prioritise 1-2 pains on frequency, severity and business impact, out loud. Use Chapter 11 (Identifying and prioritizing pain points).
5. **List solutions.** At least three distinct ideas per chosen pain, from a quick fix to a bold bet.
6. **Evaluate and pick.** Score on value vs effort (Chapter 14, Value vs effort) or Chapter 14 (RICE). Name the one you would build first, then walk its core flow, including edge cases (accessibility, safety, failure).
7. **Measure.** One success metric plus two guardrails. See Chapter 15 (North Star metric) and Chapter 15 (Guardrail and negative metrics).
8. **Summarise.** Persona, pain, solution, metric, top risk, and what you would cut for the MVP, in 30 seconds.

**Common mistakes:** jumping to features, designing for "everyone", skipping the metric, and ignoring who pays. See Chapter 12 (Common mistakes in design answers).

**If the product has AI:** add data needs, failure handling and eval criteria using Chapter 12 (Adapting CIRCLES for AI features).

![The design ladder: eight CIRCLES steps, each one an output you can say aloud.](diagrams/l19-ladder-design.svg)

### Real-world examples

- **Tablet for kids (Sigma, Google PM):** the interviewer fixes the age at 4-6. The candidate names kids, parents and teachers as stakeholders, drops educators, and splits pains by kids (display, sound, too many apps, can't type) and parents (privacy, screen time, content control). Priority features: a simplified UI on durable hardware for kids and parental controls for parents, then constraints (budget, child-privacy law) and prototype testing.
- **Car for the deaf (Sigma, Flipkart):** the candidate targets middle-aged professionals with buying power. The key pain is that drivers rely on audio cues (navigation, horns). The headline feature is horn detection: a sound above a decibel threshold triggers a steering-wheel vibration and shows where it came from on a dashboard screen.
- **Bicycle renting app for tourists (XLRI):** a by-the-book CIRCLES run. Clarifying questions pin it down to parks and tourist spots in India and foreign tourists, with online payment only. The personas are a solo traveller, a non-English-speaking group and a local tour guide. Native language, locating bikes, cost information and multi-currency payment come out as top priorities.

### Practice questions

1. Design a tablet for kids aged 4 to 6. Who is the user, and what is your first version?
2. Design an e-commerce experience for elderly shoppers. What trade-offs do you make against the core experience?
3. Design a smart speaker for a family with two working parents. How would you measure success?

> [!INTERVIEW] Design a tablet for kids aged 4 to 6. Who is the user, and what is your first version?
> **Answer outline (Q1):** Clarify the device goal (learning, entertainment, or both) and who pays. Users: the 4-6 year-old, with the parent as buyer and co-user. Pains: an overwhelming UI and fragile hardware for the child, plus safety and screen time for the parent. First version: durable hardware, a simplified voice-and-touch launcher with curated content, and a parent dashboard with time limits. Metric: weekly active learning minutes on parent-approved content. Guardrails: daily screen time stays under the parent's limit, and parental-control complaints.

> [!INTERVIEW] Design an e-commerce experience for elderly shoppers. What trade-offs do you make against the core experience?
> **Answer outline (Q2):** Pick elderly users who shop for essentials. Trade-off: larger targets and fewer choices against discovery. Start with reorder and voice or assisted checkout. Measure repeat-order rate and support calls per order.

> [!INTERVIEW] Design a smart speaker for a family with two working parents. How would you measure success?
> *(Beyond the notes: a starting point, not the vault's answer.)* Name the household's job first (dinner plans, reminders, kids' routines), then pick one north star such as weekly routines completed by voice. Add a guardrail on privacy complaints and on how often a family has to repeat a command.

*Related:* Chapter 12 (CIRCLES, Common mistakes, Adapting CIRCLES for AI features), Chapter 11 (Segmentation and personas), Chapter 14 (Value vs effort), Chapter 22 (this page).

## 22.2 Product improvement cases

> Improvement cases ask you to diagnose an existing product's pain points, then propose a prioritised fix you can defend.

### Concept

**Typical prompts:** "How would you improve LinkedIn?" (XLRI), "Critique and improve an application you like" (Sigma, Atlassian), "We would like you to take a lead on improving OLA" (Sigma, InfoEdge), "How would you improve Google Maps?" (Sigma, VMock), "What should be done to improve Yahoo Mail to match Gmail?" (Primer, Info Edge).

**Step-by-step approach.** The XLRI casebook uses a comprehend-first structure, and Chapter 13 (Five-step critique) adds a critique lens.

1. **Comprehend.** Define the product in one line. Ask what "improve" means: acquisition, engagement, monetisation, or a specific pain. Confirm scope with Chapter 16 (Scoping).
2. **Identify the user.** Pick the primary user and one secondary. Use Chapter 11 (Segmentation and personas).
3. **Map the journey.** Walk the core flow and mark friction points. Use Chapter 11 (User journeys and the 5Es) and Chapter 11 (Jobs-to-be-done) to see which job is under-served.
4. **Find pain points.** List candidate problems and rank them by frequency and severity with Chapter 11 (Identifying and prioritizing pain points).
5. **Brainstorm solutions.** Give at least three per chosen pain point, spanning a small fix, a medium feature and a bold bet.
6. **Prioritise.** Score with Chapter 14 (RICE) or Chapter 14 (Value vs effort). Defend the choice against the user and business impact.
7. **Define success.** Name a primary metric, a supporting metric and a guardrail. See Chapter 15 (North Star metric) and Chapter 15 (HEART).
8. **Risks and next steps.** Mention technical cost, dependency on other teams, and how you would test (A/B or a pilot).

**Critique lens (zoom levels):** Check the product at three zoom levels: the whole app, the feature, and the single screen. Mention familiarity (does it follow patterns users already know) and inclusivity (who is left out).

**Favourite-product answers:** prepare two or three products you know well so you can switch to a critique quickly. See Chapter 13 (Favorite product answers that show depth).


### Real-world examples

- **LinkedIn (XLRI, worked example):** the candidate asks whether "improve" means acquisition, engagement or revenue, confirms mobile app on both OSs, and picks engagement because the user base is already large and engagement feeds retention and revenue. Only then segments users (job seekers first) and brainstorms.
- **Google Maps (Sigma, VMock):** the interviewer picks revenue and Android (about 80% of users). The candidate compares urban millennials, middle-aged commuters and tourists, and picks tourists because they lean on Maps most. Pains: planning a short trip, and booking tickets across many sites. Solution: a free Travel Planner (interests plus length of stay, giving an itinerary) with one-click ticket booking that earns a commission. Metric: revenue per user per month, plus planner usage and booking conversion. Trade-off: fewer clicks on "More categories", which is acceptable.
- **Spotify (Sigma, Atlassian, "critique an app you like"):** the candidate builds personas, including an independent artist who struggles to get noticed. The proposals include collaborative playlists between independent artists and "Artist Features", where established artists recommend lesser-known ones. This is the favourite-product format: pick a secondary persona the product under-serves.
- **Watch the case type:** the Sigma "Uber Drivers", "Flipkart Notifications" and "Prime Video" cases are root cause cases (a metric dropped), not improvement cases. See Chapter 22 (22.3 Root cause analysis and diagnosis cases).

### Practice questions

1. How would you improve LinkedIn for job seekers in their first two years of work?
2. What should be done to improve Yahoo Mail to match Gmail?
3. Suggest improvements to a product you use daily. What is the one change you would ship first?

> [!INTERVIEW] How would you improve LinkedIn for job seekers in their first two years of work?
> **Answer outline (Q1):** Clarify the user (early-career, job search). Journey: profile setup, job search, application. Pain: weak signal on which roles fit. Solution set: skills-gap prompts, referral matching, application status. Pick skills-gap prompts, measure profile completion and application rate, guardrail on spam connection requests.

> [!INTERVIEW] What should be done to improve Yahoo Mail to match Gmail?
> **Answer outline (Q2):** Define the gap by feature, not vibes: spam filtering, search, mobile sync. Pick spam filtering because it hits daily trust. Measure spam reports per 1,000 users and inbox satisfaction; guardrail on false positives that hide real mail.

> [!INTERVIEW] Suggest improvements to a product you use daily. What is the one change you would ship first?
> *(Beyond the notes: a starting point.)* Walk the product's core flow once, mark the single step where you lose time, and rank three fixes by frequency and effort. Ship the fix that is cheap to test, and say how you would know it worked before you commit to the bigger ones.

*Related:* Chapter 13 (Five-step critique; Favorite product answers that show depth), Chapter 11 (Identifying and prioritizing pain points), Chapter 14 (RICE), Chapter 15 (HEART), Chapter 22 (this page).

## 22.3 Root cause analysis and diagnosis cases

> RCA cases give you a metric movement and ask why. Scope the problem first, then split causes into internal and external and walk the journey.

### Concept

**Typical prompts:** "Order cancellation on Amazon is up by 10%; identify the root cause" (XLRI), "Drivers on Uber have fallen by 2%. What would you do?" (Sigma), "Flipkart has seen a 20% drop in engagement on UGC" (Sigma), "Google Maps is showing a shorter ETA than the actual travel time" (Sigma, Just Dial), "Flipkart's hyperlocal business in Bangalore is observing breaches" (Sigma, Flipkart).

**Step-by-step approach.** Sigma and XLRI use the same skeleton. Full detail is in Chapter 16 (Root Cause Analysis).

1. **Define the metric.** Say what you think it means and get the interviewer to confirm (for example, "active drivers" = logged in and willing to accept rides for 2+ hours a day). Rule out a tracking bug or a definition change.
2. **Scope it.** How big, since when, sudden or gradual, and which geography, platform, OS, segment or product line. A sudden drop points to a release or an outage; a drop in one city points away from global releases. See Chapter 16 (Scoping).
3. **Check external causes quickly.** Competitors, seasonality or events, regulation, bad PR, partner changes. See Chapter 16 (Internal vs external causes).
4. **Walk the journey.** Lay out one linear journey with a metric per step, and ask which step moved. See Chapter 16 (Walking the user journey). If the metric is a product of inputs, decompose it with Chapter 15 (Metric trees and diagnosing metric movement).
5. **Zoom in on the step that moved.** Ask about recent changes there: a feature, UI, pricing or policy change, or a back-end change (errors, latency, crashes).
6. **Confirm the hypothesis with one data cut.** For example, "Is the drop much bigger between 10 PM and 6 AM?" One confirming cut beats five guesses.
7. **Decide whether it is actually bad.** A drop can be a side effect of a better experience (see Flipkart UGC below). Check the downstream metric (conversion, retention).
8. **Fix and prevent.** A short-term fix (rollback, hotfix, incentive), a long-term fix, and a prevention step (a test, an alert, a better metric).

**AI products:** add model changes, prompt regressions, data drift and cost spikes. See Chapter 16 (AI-specific RCA: model changes, prompt regressions, data drift, cost spikes).

![The RCA ladder: scope and check before you zoom in, then confirm with one cut.](diagrams/l19-ladder-rca.svg)

### Real-world examples

- **Uber Drivers (Sigma):** active drivers fell 2% gradually over 2 months, in Hyderabad only, on every device. The city-only scope rules out app releases. Walking the journey (sign-up, login, accept, pick-up, drop, payment), only income moves: requests and acceptance are flat, but earnings per trip fell. The cause is the removal of the late-night safety fee (10 PM-6 AM) after Hyderabad was declared a "safe city", and a late-night cut confirms it. Fixes: a graded city safety index instead of on/off, bundled incentives after n night rides, and experiments to price them.
- **Flipkart UGC (Sigma):** Q&A votes are down 20% over 2 months. Q&A impressions and CTR are stable, but Q&As viewed per session dropped after a release added text search inside Q&A. An A/B test showed conversion went up, so nothing needs fixing: change the metric to engagement per Q&A viewed.
- **Google Maps ETA (Sigma, Just Dial):** ETAs come out too short on all platforms, starting a few days ago and worst at peak hours. Data sources are unchanged, but a routing-algorithm update added real-time traffic and road-closure inputs. Fix: compare predictions with actuals before and after the update, retune the data-source weights, tell users, and add stronger pre-release validation plus a user feedback loop.
- **Flipkart Hyperlocal (Sigma):** average delivery time is up 10% in parts of Bangalore, about 9 minutes on a 90-minute promise. Every journey step is fine except pick-up to delivery. That splits into pick-up to landmark (fine) and landmark to door, where agents lose 5-10 minutes at apartment-gate security.
- **Amazon order cancellations up 10% (XLRI):** scope (duration, competitors too?, service, category, geography, channel), then external factors (regulation, substitutes, sentiment), then internal factors along the journey: search, cross-sell algorithm changes, listing and cart changes, removed payment modes, and delivery delays by pin code.

### Practice questions

1. Amazon order cancellations are up 10%. Walk me through your first 5 clarifying questions.
2. Cart drops rose 15% last month on mobile only. How do you diagnose it?
3. Daily active users fell 8% this week. What do you check first?

> [!INTERVIEW] Amazon order cancellations are up 10%. Walk me through your first 5 clarifying questions.
> *(Beyond the notes: a starting point.)* Ask what "cancellation" counts (before or after dispatch), the window (this week against last week), whether it is one category or all, one region or all, and whether it is one channel or every channel. Then ask whether anything changed in the product or in policy in the same window.

> [!INTERVIEW] Cart drops rose 15% last month on mobile only. How do you diagnose it?
> **Answer outline (Q2):** Scope: mobile only, which OS, which app version, which date. Journey: product, cart, address, payment. Hypotheses: a release that broke the cart button (internal, technical), a payment gateway outage on one network (technical), a competitor promotion (external, less likely since mobile only). Check version split and error logs first, then payment success rate by method.

> [!INTERVIEW] Daily active users fell 8% this week. What do you check first?
> *(Beyond the notes: a starting point.)* Check that the metric itself did not change (a tracking or definition change) before you check the product. Then split the drop by platform, version and region to see whether it is sudden or gradual.

*Related:* Chapter 16 (Scoping; Walking the user journey; Internal vs external causes; AI-specific RCA), Chapter 15 (Metric trees and diagnosing metric movement), Chapter 22 (this page).

## 22.4 Metrics cases

> Metrics cases ask how you would measure success. Pick a goal, map the funnel, choose a north star, and add guardrails.

### Concept

**Typical prompts:** "A new startup like Swiggy has low sales. Explain each stage of the customer journey, the possible reasons for low sales at each stage, and the success metrics" (Sigma, Samsung R&D), "Define success for Gmail" (Sigma), "LinkedIn is testing asking new users to upload a profile photo during sign-up instead of after it. What metrics will you look at?" (Lewis Lin), "You are rolling out emoji reactions on WhatsApp. How would you evaluate the change in user experience?" (XLRI), "Suggest a killer feature to improve LinkedIn, and what metrics would you track?" (Lewis Lin).

**Step-by-step approach:**

1. **Clarify the product and goal.** What it is for, who uses it (both sides, if it is a marketplace), and which business goal matters now: acquisition, engagement, retention or revenue. If the interviewer says "your choice", pick one and say why.
2. **Map the journey or funnel.** Lay out the stages (for example awareness, consideration, purchase, retention, referral) with one metric per stage. Use Chapter 15 (AARRR, pirate metrics) or Lewis Lin's AARM (acquisition, activation, retention, monetisation), and Chapter 15 (Funnel, marketplace, and retention metrics).
3. **Cross out what the change cannot move.** For a feature, drop stages it does not touch (Lewis Lin drops acquisition and monetisation for the profile-photo test). This shows focus.
4. **Choose one north star.** One metric that reflects delivered value, with a one-line justification. See Chapter 15 (North Star metric).
5. **Add 2-3 supporting metrics** that explain movement in the north star. For UX changes, Chapter 15 (HEART) gives goal, signal and metric per dimension.
6. **Add guardrails.** What must not get worse: sign-up completion, complaints, refunds, latency, cost. See Chapter 15 (Guardrail and negative metrics).
7. **Read the trade-off.** If an A/B test is in play, say which result would make you ship and which would make you stop, before seeing the numbers.
8. **Set a target and a time window.** For example, "+5% in 30-day retention over a 4-week test".

**Avoid:** listing 15 metrics with no hierarchy, or picking vanity metrics (total signups without retention).

![The metrics ladder: a goal, a funnel, one north star, then guardrails and a target.](diagrams/l19-ladder-metrics.svg)

### Real-world examples

- **Swiggy customer journey (Sigma, Samsung R&D):** five stages, each with reasons for low sales and metrics. Awareness: app visits, new customers, CAC. Consideration: visit-to-order conversion, time in app, bounce rate. Purchase: AOV, orders per period, % delivered successfully. Retention: retention rate, orders per repeat customer, LTV. Referral: CSAT, positive reviews, % of new customers from referrals.
- **LinkedIn profile photo during sign-up (Lewis Lin):** the candidate lists AARM metrics, then drops acquisition and monetisation as irrelevant. The two-week A/B test shows sign-up completion down 13.2% but posts up 4.9%, invites up 2.4% and profile completeness up 1.7%. The candidate argues the engagement gain justifies the sign-up loss. Lesson: name the guardrail (sign-up completion) up front and weigh it explicitly.
- **WhatsApp emoji reactions (XLRI):** uses HEART. Happiness: app-store ratings. Engagement: time per session and sessions per user per day. Adoption: install rate and downloads. Retention: DAU/WAU/MAU, and uninstalls staying below installs (users not switching to Signal or Telegram). Task success: feature usage over time, error rate and feature drop-off.

### Practice questions

1. How would you measure the success of a ride-hailing app's new scheduled-ride feature?
2. What metrics would you track for a new photo-upload step in a dating app?
3. Define a north star metric for a food delivery app.

> [!INTERVIEW] How would you measure the success of a ride-hailing app's new scheduled-ride feature?
> *(Beyond the notes: a starting point.)* Goal first: does the feature add rides or only move them? Funnel: schedule, confirm, the ride happens on time, the rider rides again. North star: scheduled rides completed per week. Guardrail: no-shows and cancellations on the driver side.

> [!INTERVIEW] What metrics would you track for a new photo-upload step in a dating app?
> **Answer outline (Q2):** Goal: more matches per user. Funnel: photo upload, profile complete, first like, first match, return visit. North star: weekly users who get at least one match. Supporting: profile-completion rate after the step. Guardrail: report or block rate, and photo-moderation load.

> [!INTERVIEW] Define a north star metric for a food delivery app.
> *(Beyond the notes: a starting point.)* Choose a metric that reflects a delivered order, not a visit: for example, weekly customers who get one order delivered within the promise. Explain why it beats orders alone (repeat customers, not one-off spikes), and name a guardrail such as delivery time.

*Related:* Chapter 15 (North Star; AARRR; HEART; Funnel, marketplace, and retention metrics; Guardrail and negative metrics; Metric trees), Chapter 21 (Guesstimate structure), Chapter 22 (this page).

## 22.5 Pricing cases

> Pricing cases ask what to charge. Anchor on willingness to pay, pick a strategy that fits the product, then test the price.

### Concept

**Typical prompts:** "How would you price the Kindle Fire HD?" (Lewis Lin), "How would you price Apple Home, the smart speaker from Apple?" and "How would you price the family subscription pack for JioSaavn?" (Sigma, Pricing section), "Price a new cloud-based project management software service" (XLRI, pricing case study).

**Step-by-step approach.** The XLRI casebook lists 11 strategies. See Chapter 17 (Cost-plus, value-based, and competitive pricing) for the core three.

1. **Clarify.** Who is the buyer (consumer, SMB, enterprise), what is the product, and is it a new category or a competitive one? Ask about the cost base and the goal (share, margin, speed of adoption).
2. **Find willingness to pay.** For a new category, use the value to the customer. For an existing one, start from competitor price plus any gap in features. See Chapter 17 (Cost-plus, value-based, and competitive pricing).
3. **Estimate cost floor.** Compute unit cost so you know the floor. Use cost-plus as a sanity check, not the main method.
4. **Pick the strategy.** Match it to the goal: penetration (win share), skimming (new premium product), premium, bundle, freemium, dynamic. See Chapter 17 (Monetization models: subscription, freemium, ads, take rate, razor-and-blade, bundling).
5. **Set the range.** Give a lower bound (cost or the cheapest substitute) and an upper bound (value or the premium competitor). Pick a point inside it and justify it.
6. **Segment if useful.** Tiers by user type or feature set, as in SaaS per-seat pricing.
7. **Test and iterate.** Run an A/B price test or survey. Note that surveys tend to be optimistic about price. See Chapter 17 (Running pricing experiments).
8. **Name the risks.** Churn, price anchoring, cannibalisation of a cheaper tier, and regulatory limits.

**Strategy quick map (XLRI's 11):** cost-plus, competitive, penetration, dynamic (surge), price discrimination, economy, premium, loss leader, value-based, skimming, bundle.

![The pricing ladder: find willingness to pay, check the cost floor, then pick a point in the range.](diagrams/l19-ladder-pricing.svg)

### Real-world examples

- **Kindle Fire HD (Lewis Lin):** willingness to pay is capped by the closest substitute, the Nexus 7 at $199. The cost floor is the teardown estimate of $174 per unit. Recommendation: price at the low end ($174) as a loss leader ("razor and blade"), because Amazon profits from digital content and needs tablet share.
- **Apple Home smart speaker (Sigma):** competitive pricing plus a brand premium. Start from Alexa and Google Home prices, estimate Apple's premium at about 15% (iPhone vs Pixel), and land at about Rs 5.75K for a Mini and Rs 11.5K for the full speaker.
- **JioSaavn family pack (Sigma):** the market is mature (Spotify, Gaana, YouTube Music) with 5 accounts per family pack. The candidate guessed 2x the individual price; the interviewer corrected it to the industry norm of about 1.5x, giving about Rs 150/month, or lower to win share from competitors.
- **Cloud project-management software (XLRI pricing case study):** tiered subscriptions (a basic tier with essential features and limited storage, a premium tier with more), set by customer segment and competitor research, plus a free trial or freemium version.

![Kindle: the substitute caps the price, and the cost floor sets the bottom.](diagrams/l19-pricing-range.svg)

### Try it locally: the 15% premium on competitor anchors

*(Beyond the notes: reproduced locally with the standard library, using the Sigma case's numbers. Google Home Rs 10K and Google Home Mini Rs 5K are the anchors; the 15% premium is the case's estimate.)*

```python title="lab_p19_pricing_anchor.py"
# Price a new smart speaker from competitor anchors (the Apple Home case, Sigma).
google_home, google_home_mini = 10_000, 5_000    # Rs, competitor list prices
alexa_low, alexa_high = 4_000, 9_000             # Rs, Alexa range
premium = 0.15                                   # brand premium estimate (iPhone vs Pixel)
print(f"full speaker vs Google Home : Rs {google_home * (1 + premium):,.0f}")
print(f"Mini vs Google Home Mini    : Rs {google_home_mini * (1 + premium):,.0f}")
print(f"Alexa range for comparison  : Rs {alexa_low:,} to Rs {alexa_high:,}")
```

```output
full speaker vs Google Home : Rs 11,500
Mini vs Google Home Mini    : Rs 5,750
Alexa range for comparison  : Rs 4,000 to Rs 9,000
```

The premium turns the two anchors into the Sigma candidate's numbers. Note that the premium is one estimate. Change it to 10% or 20% and the answer moves by Rs 1K or more on the full speaker, so the interviewer will ask how you would test it.

### Practice questions

1. How would you price a new smart speaker for India?
2. A music streaming app wants to launch a cheaper tier. What price and features would you propose?
3. How would you price the Kindle Fire HD?

> [!INTERVIEW] How would you price a new smart speaker for India?
> **Answer outline (Q1):** Clarify: mass-market or premium, and what it competes with (Alexa-class devices, cheap Bluetooth speakers). Willingness to pay: anchor on the nearest competitor. Cost floor from BOM. Strategy: penetration pricing for share, with a bundle of a free music trial. Range: the cost floor to the nearest premium device. Test two price points in two cities.

> [!INTERVIEW] A music streaming app wants to launch a cheaper tier. What price and features would you propose?
> *(Beyond the notes: a starting point.)* Name the cheaper tier's buyer (students, one listener at home) and the feature it gives up (offline downloads, a specific device, or ad breaks). Price it from the cost floor and the cheapest rival, and test the price against the premium tier so the cheaper plan does not pull people down from it.

> [!INTERVIEW] How would you price the Kindle Fire HD?
> *(Beyond the notes: a starting point.)* Name the closest substitute and its price first (the Nexus 7 at $199 in the vault's answer), then the cost floor ($174 per unit in the same answer). Decide whether the device earns its margin or whether it is a loss leader for content, and say which you chose and why.

*Related:* Chapter 17 (Cost-plus, value-based, and competitive pricing; Monetization models; Running pricing experiments), Chapter 19 (Porter's Five Forces), Chapter 15 (Funnel, marketplace, and retention metrics), Chapter 22 (this page).

## 22.6 Strategy and market entry cases

> Strategy cases ask whether, where and how a company should move. Check the market, the competitors, and whether the company is the right one to win.

### Concept

**Typical prompts:** "Assess the viability of Amazon's entry into food delivery" (Sigma, Product Entry), "An aspiring PM proposes that Amazon sell groceries from neighbourhood markets. What are the pros and cons?" (Lewis Lin), "You can sell a new oven or an oven mitt. Which do you choose?" (Lewis Lin), "Which of four airlines should a travel site use to make the most profit?" (Primer, Cleartrip), "Segment the camera market in India and estimate its size" (Primer, SAP), "How should MakeMyTrip use the inadequacies of IRCTC's site to its advantage?" (Primer, Info Edge).

**Step-by-step approach.** The Lewis Lin checklist is the base. See Chapter 19 (Market sizing and entry decisions).

1. **Clarify the objective.** Is it a new market, a new product, or a defensive move? What counts as success? Use Chapter 16 (Scoping) as a model for scoping.
2. **Size the market.** Market size, growth and margins. Use a guesstimate with Chapter 21 (Guesstimate structure) and Chapter 21 (Common guesstimate types).
3. **Assess the market forces.** Competition, buyer power, supplier power, entry barriers, substitutes. Use Chapter 19 (Porter's Five Forces).
4. **Assess competitors.** Number, resources, distribution, and what each does better. See Chapter 19 (Competitive analysis and moats).
5. **Check company fit.** Expertise, economies of scale, distribution access, supplier relations, and fit with the brand promise. Use Chapter 19 (SWOT and the Five Cs).
6. **Options and entry mode.** Build, partner, or acquire. See Chapter 19 (Partnerships, acquisitions, and build-vs-buy strategy).
7. **Recommend.** Yes or no, with conditions, a pilot, and the metric that would change your mind.
8. **Risks.** Regulation, customer trust, unit economics, and the time to reach profit.


### Real-world examples

- **Amazon into food delivery (Sigma):** the candidate scopes to restaurant delivery in the US (about $200B and growing). The "why" is that free food delivery could turn more customers into Prime members. Strengths: last-mile logistics and comfort with low margins. Weakness: no restaurant relationships, plus the discontinued Bangalore pilot, where cheap labour blunted Amazon's logistics edge. Three options are weighed: go independent with lower delivery costs, ally with or acquire a player, or don't enter. The candidate picks going independent, leaning on the delivery network and Prime.
- **Amazon groceries from neighbourhood markets (Lewis Lin):** order online and collect from a local store within 30 minutes. The candidate lists customer benefits (the Amazon experience, saved lists, speed) and Amazon benefits (customer experience, lower shipping cost, a transaction cut). The top issues are signing up stores, integration, quality, inventory accuracy, inventory availability, and customers bypassing Amazon later. The book criticises the "biggest risk" pick as arbitrary: always justify your pick.
- **Oven vs oven mitt (Lewis Lin):** a classic market-entry checklist question. Compare market size, competition, margins and company fit before choosing.
- **Note:** the Primer camera and gas-turbine questions are mostly market sizing. Run them with the guesstimate structure in Chapter 21 (Guesstimate structure).

### Practice questions

1. You can enter the market for selling ovens or oven mitts. Which do you choose and why?
2. Should a ride-hailing app enter food delivery in a Tier-2 Indian city?
3. Segment the camera market in India and estimate its size.

> [!INTERVIEW] You can enter the market for selling ovens or oven mitts. Which do you choose and why?
> *(Beyond the notes: a starting point.)* Compare market size, competition, margin and company fit for each, as the checklist says. Pick one, and name the single fact that would make you pick the other.

> [!INTERVIEW] Should a ride-hailing app enter food delivery in a Tier-2 Indian city?
> **Answer outline (Q2):** Market: food delivery size and growth in the city, margin per order. Competitors: incumbent share and their subsidies. Company fit: existing driver base and dispatch skills, low brand awareness in food. Options: pilot with partner restaurants, no full build. Recommend a 3-month pilot with a go or no-go on order frequency and driver utilisation.

> [!INTERVIEW] Segment the camera market in India and estimate its size.
> *(Beyond the notes: a starting point.)* Segment by buyer (consumers, professionals, businesses) and by price band, then size each segment as customers times the price per unit, with the assumptions written down.

*Related:* Chapter 19 (Porter's Five Forces; SWOT and the Five Cs; Competitive analysis and moats; Market sizing and entry decisions; Partnerships, acquisitions, and build-vs-buy), Chapter 21 (Common guesstimate types), Chapter 22 (this page).

## 22.7 Go-to-market and launch cases

> GTM cases ask how to launch a product: who to target first, through which channels, with what success criteria and how to roll out.

### Concept

**Typical prompts:** "How would you launch Google's driverless car service?" (XLRI), "Design a travel app. What would be your GTM strategy for it?" (Sigma laterals, Microsoft), "Design a marketing plan for a new product" (Primer, Infibeam), "How would you ensure good sales of a pharmaceutical product?" (Primer, SAP), "A case on AdWords publicity and launch in the SMB hotel industry" (Primer, Google).

**Step-by-step approach.** The XLRI GTM section and Chapter 18 (Pre-launch, launch, and post-launch activities) give the timeline.

1. **Clarify.** Product, target market, budget, timeline, and whether the launch is to new or existing users.
2. **Pick the target segment.** The first segment with the highest need and the easiest reach. See Chapter 11 (Segmentation and personas).
3. **Choose the rollout.** Pilot, MVP or phased rollout by region or cohort. See Chapter 18 (Pilots, MVPs, and phased rollouts).
4. **Choose channels.** Owned, paid, partner and organic. See Chapter 18 (Partnerships and distribution channels).
5. **Price and position.** Link to pricing thinking in Chapter 17 (Cost-plus, value-based, and competitive pricing).
6. **Plan pre-launch and post-launch.** Readiness, support, feedback loops and the first 30 days. See Chapter 18 (Pre-launch, launch, and post-launch activities).
7. **Define launch success.** Targets for adoption, activation and early retention. See Chapter 18 (Launch success criteria).
8. **Risks and kill criteria.** What would make you pause, and who decides.


### Real-world examples

- **Google's driverless car service (XLRI GTM example):** splits implementation into pre-launch, launch and post-launch. To match Uber's pilots, it proposes two: a family chauffeur service in a tech-aware city (San Francisco or Manhattan), with a safety driver on board and a week-long lottery pilot, and a package-delivery pilot, ideally with FedEx or UPS for visibility. Avoiding negative PR from a pilot accident is called out as the key risk. Only after the pilots come a short-video marketing campaign tying in Google Home and Maps, and media events.
- **Pharmaceutical product sales (Primer, SAP):** a prompt only, no model answer. A sound sketch is a channel plan through doctors and pharmacies, with a pilot in a few cities before a national push.
- **Online shopping trust (Primer, Infibeam):** a prompt only. Treat it as GTM for a sceptical segment: start with the objection (fraud, returns), answer with proof points (cash on delivery, easy returns, reviews), and pilot in one city.

### Practice questions

1. Launch a budget electric scooter in Bengaluru. What is your plan for the first 90 days?
2. How would you convince people to shop online for groceries?
3. Design a launch plan for a new B2B invoicing tool for small shops.

> [!INTERVIEW] Launch a budget electric scooter in Bengaluru. What is your plan for the first 90 days?
> **Answer outline (Q1):** Segment: college students and commuters on short routes. Rollout: one zone, then a second zone once utilisation hits a target. Channels: campus partnerships, app-store search, referral credits. Success: trips per scooter per day, repeat rate at day 30, and safety incidents as a guardrail. Kill criteria: utilisation below a set level for six weeks.

> [!INTERVIEW] How would you convince people to shop online for groceries?
> *(Beyond the notes: a starting point.)* Use the GTM answer from the Infibeam prompt above: name the objection first (freshness, substitutes, trust), answer it with proof points, and pilot in one area before you go wide.

> [!INTERVIEW] Design a launch plan for a new B2B invoicing tool for small shops.
> *(Beyond the notes: a starting point.)* Target the shops with the most invoices and a clear pain (late payments). Pilot with a handful of shops and a local accountant partner, measure invoices sent per shop per week, and set a kill rule if the second month shows no repeat use.

*Related:* Chapter 18 (Pre-launch, launch, and post-launch; Pilots, MVPs, and phased rollouts; Partnerships and distribution channels; Launch success criteria), Chapter 17 (Cost-plus, value-based, and competitive pricing), Chapter 22 (this page).

## 22.8 Brainstorming and lateral questions

> Lateral questions have no fixed frame. Structure the ideas, generate many, and then prioritise out loud.

### Concept

**Typical prompts:** "Brainstorm as many algorithms as possible for recommending Twitter followers" (Lewis Lin), "Suggest 5 new offerings that MakeMyTrip could come up with" (Primer, Info Edge), "What feature would you build to improve Google+?" (Lewis Lin), "Design some additional features to enhance WhatsApp" (Sigma laterals, Atlassian), "How would you stop fake profiles from being registered on jeevansathi.com?" (Primer, Info Edge), "Sell an accounting product to me" (Primer, SAP).

**Step-by-step approach:**

1. **Clarify the constraint.** Who is the user, what is the goal, and is there a limit (time, cost, tech)? See Chapter 16 (Scoping).
2. **Pick a structure.** Use a simple lens to generate ideas: by user type, by journey stage, by channel, or by technique (for example, the list of algorithms split into content-based, collaborative and hybrid).
3. **Brainstorm in batches.** Give at least three ideas, then go one level deeper on the best. Quantity first, then judgement.
4. **Prioritise out loud.** Score on user value and feasibility. Use Chapter 14 (Value vs effort) or Chapter 14 (RICE).
5. **Pick one and detail it.** Name the user, the core flow, and the success metric. See Chapter 12 (CIRCLES) for the depth.
6. **Trade-offs.** Say what the idea costs and what it risks.

**Sales pitch variant ("sell me X"):** name the buyer's pain first, then show the product as the answer. Do not open with features.

**Algorithm variant:** explain each approach in one or two lines, then compare them on data needs, cold-start and explainability. Background is in Chapter 5 (Computer vision, speech, and recommendation systems).


### Real-world examples

- **Twitter follower recommendations (Lewis Lin):** the candidate structures the space as behaviours (view, follow), relationships (A views B but not back, or both view each other) and follow states, then combines them into a grid of ways to suggest a third user C, giving 11 options. Asked to pick one, the candidate would A/B test on suggestion-to-follow ratio, and leads with "A and B are both acquaintances of C" because it mirrors real-life introductions. The lesson: a simple structure produces many ideas, then you prioritise with a reason.
- **Google+ feature (Lewis Lin):** the book's "think big" tip warns against "me too" ideas (a Facebook-style groups feature) and plain integration ideas. A good answer ties the idea to an under-served user job and names the metric it should move.
- **New offerings for MakeMyTrip (Primer, Info Edge):** a prompt only. A structured sketch splits ideas by trip stage (inspire, plan, book, travel, return) or by segment (families, students, corporate), then picks one to pilot.
- **Sigma "Laterals Questions" list:** mostly short design and improvement prompts (a search engine for kids, Facebook for people who cannot read or write, in-flight entertainment). Treat them as rapid-fire design cases: 2 minutes of structure, then 3 ideas and a pick.

### Practice questions

1. Brainstorm as many algorithms as you can for recommending accounts to follow.
2. Sell a pen to me.
3. Give five new features for a food delivery app that would bring back lapsed users.

> [!INTERVIEW] Brainstorm as many algorithms as you can for recommending accounts to follow.
> **Answer outline (Q1):** Structure: collaborative, content-based, graph, popularity, and hybrid. For each, say the data it needs and the cold-start problem. Pick a hybrid as the practical choice, with popularity as a fallback for new users. Measure follow-through rate and accounts followed per week.

> [!INTERVIEW] Sell a pen to me.
> *(Beyond the notes: a starting point.)* Ask who the buyer is and what they write, and what goes wrong with their current pen. Name the pain first (a pen that skips, runs out mid-exam), then show the product as the answer, and close with the price or the offer.

> [!INTERVIEW] Give five new features for a food delivery app that would bring back lapsed users.
> *(Beyond the notes: a starting point.)* Structure by reason for lapse (price, speed, a bad order, no reason to open the app). Give one feature per reason, plus one for habit (a reorder button). Pick one, and measure reactivation within 30 days.

*Related:* Chapter 12 (CIRCLES), Chapter 14 (RICE; Value vs effort), Chapter 11 (Jobs-to-be-done), Chapter 22 (Product design cases; this page).

## Beyond the notes: the case router in your head

*(Beyond the notes: a practical shortcut, not a rule from the vault.)* Most prompts show their type in one verb or one noun. Listen for it in the first sentence:

| What you hear | Case type | First framework |
|---|---|---|
| "design", "build", "a product for" | Product design | CIRCLES |
| "improve", "critique", "make better" | Improvement | Five-step critique |
| "dropped", "rose", "why did X go up or down" | Root cause | Scope, then the journey |
| "measure", "success", "north star", "metrics" | Metrics | Funnel and north star |
| "price", "charge", "what should it cost" | Pricing | Willingness to pay and range |
| "enter", "should we", "which market", "which option" | Strategy | Market, competitors, fit |
| "launch", "roll out", "first 90 days" | Go-to-market | Segment, pilot, channels |
| "brainstorm", "sell me", "as many as you can" | Brainstorming | Structure, then prioritise |

If two verbs fit, the first one in the prompt usually wins. Say the type out loud ("this is a root cause case") so the interviewer can correct you.

## Beyond the notes: pitfalls

- **Picking a framework before the type.** A CIRCLES run on an RCA prompt produces features for a problem that is a drop in a metric.
- **Treating a drop as a bug.** Check the metric's definition and tracking first, then the product.
- **Quoting the price without the range.** A single number has no defence. Show the floor and the ceiling.
- **Listing metrics with no north star.** Fifteen metrics and no hierarchy look busy and decide nothing.
- **Ending without a guardrail.** Every answer should close with a metric and the thing that must not get worse.

## Beyond the notes: interview corner

- **"Which case type is this?"** Name it out loud in the first minute, then say the framework you will use. Interviewers reward the structure, not the buzzword.
- **"Why not use CIRCLES for everything?"** It is a design skeleton. RCA needs a journey walk, pricing needs a range, and metrics need a funnel.
- **"Where do you start a pricing answer?"** With the buyer and the substitute, not the cost. The cost sets the floor; the value and the rival set the ceiling.
- **"How do you end a case?"** A one-line recommendation, the trade-off you accepted, one north star and one guardrail, and the test you would run first.

## Revision cheat-sheet

![Chapter 22 on one page: case type, framework and the chapter that teaches it.](diagrams/l19-big-picture.svg)

- **Start every case** with clarifying questions and the goal, then name the case type.
- **22.1 Design:** CIRCLES. Persona, pain, solution, metric, top risk, MVP cut.
- **22.2 Improvement:** comprehend "improve", find pains by frequency and severity, brainstorm three, prioritise, define success.
- **22.3 RCA:** define the metric, scope it, check external causes, walk the journey, zoom in, confirm with one cut, decide if it is bad, fix and prevent.
- **22.4 Metrics:** goal, funnel, one north star, 2-3 supporting metrics, guardrails, a trade-off read, a target and a window.
- **22.5 Pricing:** buyer and substitute, willingness to pay, cost floor, strategy, range, segment, test, risks.
- **22.6 Strategy:** objective, market size, forces, competitors, company fit, entry mode, a recommendation with conditions, risks.
- **22.7 GTM:** segment, rollout, channels, price and position, pre- and post-launch, success criteria, kill criteria.
- **22.8 Brainstorm:** clarify the constraint, pick a structure, go in batches, prioritise out loud, detail one, name the trade-off.
- **Beyond the notes:** the verb router, the pitfalls and the closing sentence that names the metric and the guardrail.

## Self-test

<details class="quiz"><summary>What is the first thing you do in any case?

Ask clarifying questions about the goal, the product and the scope. Do not give an answer or pick a framework yet.

</details>

<details class="quiz"><summary>Which framework is the default skeleton for product design cases?

CIRCLES: Comprehend, Identify, Report, Cut, List, Evaluate, Summarize. Sigma's version is Context, Segment, Needs, Prioritise, Solution, KPIs.

</details>

<details class="quiz"><summary>In an RCA case, why scope the problem before hypothesising?

Scope (how big, since when, sudden or gradual, which city, platform or segment) splits the search. A city-only drop points away from global releases, and a sudden drop points to a release or an outage.

</details>

<details class="quiz"><summary>In the Uber Drivers case, what showed that the cause was the late-night fee?

Only income moved. Requests and acceptance were flat, and earnings per trip fell. A late-night cut confirmed it: the drop was severe at night and small at peak hours.

</details>

<details class="quiz"><summary>What does a north star metric reflect?

One metric that reflects delivered value, with a one-line justification. Add 2-3 supporting metrics that explain its movement, then guardrails.

</details>

<details class="quiz"><summary>In a pricing case, what sets the lower and upper bound of the range?

The lower bound is the cost or the cheapest substitute. The upper bound is the value to the customer or the premium competitor. Pick a point inside the range and justify it.

</details>

<details class="quiz"><summary>Why is the Kindle Fire HD price set at $174 in the vault's answer?

Willingness to pay is capped by the closest substitute, the Nexus 7 at $199. The $174 cost floor sets the bottom, and Amazon profits from digital content, so a loss-leader price is defensible.

</details>

<details class="quiz"><summary>What should a market-entry answer end with?

A recommendation: yes or no, with conditions, a pilot, and the metric that would change your mind, plus the main risks (regulation, trust, unit economics, time to profit).

</details>

<details class="quiz"><summary>What is the default order in a go-to-market answer?

Clarify, pick the target segment, choose the rollout (pilot, MVP or phased), choose channels, price and position, plan pre- and post-launch, define launch success, then name the kill criteria.

</details>

<details class="quiz"><summary>(Beyond the notes) A prompt says "sell me a pen". What do you do first?

Name the buyer's pain before any features (for example, a pen that runs out mid-exam), then show the product as the answer, and close with the price or the offer.

</details>

<details class="quiz"><summary>(Beyond the notes) Why do you say the case type out loud?

It shows the interviewer your structure, and it gives them a chance to correct you before you spend time on the wrong framework.

</details>


# Chapter 23 · Worked Examples

<!-- lecture n="20" label="23" short="Worked examples" status="done" kind="worked cases" -->

## At a glance

| Question | Short answer |
|---|---|
| What is in this chapter? | Worked answers to real case questions: six Sigma cases, seven XLRI cases and ten annotated interview questions. |
| How should you use a worked case? | Read the prompt, answer it on your own, then compare with the structure and the conclusions. |
| What do the strong answers share? | They clarify the goal and scope first, then use the case type's framework, then quantify. |
| How do you do RCA with a worked case? | Walk the journey stage by stage, put one metric on each stage, then decompose the one that moved. |
| What closes a good answer? | A fix, a confirming data cut and a monitor or metric. Mitigate first, then fix the root cause. |
| What about borrowed products? | Interviewers borrow famous products (Google Maps, Amazon, Swiggy). Prepare the case types, not only your target company. |
| Which numbers were checked? | Each company and year in 23.3 is as the vault records it (for example, the Google Maps ETA question was asked at Just Dial). |
| Which pricing answer has the most numbers? *(Beyond the notes)* | Apple Home: Google Home Rs 10K, a 15% premium, and Rs 11.5K for the full speaker. |

> [!NOTE] Where this comes from
> The vault draws the cases from the Sigma PM Casebook (IIM Bangalore, 2023-24), the XLRI PM Casebook 2023, and candidate interview reports (Sigma's 2023-24 collection, and the Summer 2018 and Summer 2020 interview experiences). The vault marks its own additions as "Reviewer addition" or "Reviewer note". No links are kept here.

## The big picture

This chapter shows the case types from Chapter 22 applied to real prompts. Each answer is annotated to show the structure, the clarifying questions and the metrics that made it strong. Read a case, then answer it on your own before reading the solution.

The chapter has three sections:

- **23.1 Sigma casebook solutions.** Six cases from the Sigma casebook covering product design (Delhi Metro, Gen AI in Google apps), root cause analysis (Hyperlocal delivery, Uber drivers, Google Maps ETA) and pricing (a smart speaker).
- **23.2 XLRI casebook solutions.** Seven cases from the XLRI casebook covering improvement (LinkedIn), design (a lawyer marketplace, prioritised with RICE), diagnosis (Amazon searches, Amazon order cancellations), growth and pricing (Uber Premier gross bookings, SaaS tiers) and go-to-market (driverless car launch).
- **23.3 Annotated answers from interview experiences.** Ten real interview questions (Google, Just Dial, Samsung R&D, Flipkart, Gulf Talent, United Health Group, Amagi), many of them about borrowed products such as Google Maps, Amazon and Swiggy, each with what a strong answer does.

![Three sections, one habit: clarify, structure, quantify, then close with a fix and a metric.](diagrams/l20-three-habits.svg)

## Key takeaways

- Clarify the goal, the product and the scope before you pick a framework.
- Use the case type to choose the structure: CIRCLES for design, a metric tree for growth, a journey walk for RCA.
- In RCA, segment by region, category, platform and time before you hypothesise.
- Define each metric precisely (what counts as active, over what window) and quantify every guess.
- Mitigate first, then fix the root cause, and close with a monitor or metric.

> [!SIR] From the source notes
> Clarify the goal, the product and the scope before you pick a framework.

## 23.1 Sigma casebook solutions

> The Sigma casebook is best used as a template for structure, not as a script: the transcripts show how a strong candidate moves from clarifying questions to a framework, then to numbers and metrics.

### Cases

Each case below is condensed from the Sigma PM Casebook (IIM Bangalore, 2023-24). Source transcripts are rough PDF conversions, so the structures are reconstructed from the candidate's moves rather than quoted.

### Case 1: Product for Delhi Metro (design)

- **Prompt:** "Assume you are a PM at Google. Design a product for Delhi Metro. Analyse all stakeholders and choose one."
- **Case type:** Product design, goal is user adoption (not monetisation).
- **Answer structure:**
  - Clarify: digital or physical product, adoption or monetisation goal, which setting (platform or stations).
  - List stakeholders with pain points: commuters, station admin staff, safety staff.
  - Pick one persona and justify it (largest user base, adoption is the goal).
  - Propose 3 features: mobile ticketing (QR scanners, reduce queues), real-time crowd analysis, navigation support.
  - Prioritise on a value vs complexity matrix: navigation (medium value, low complexity) first, then mobile ticketing (high value, high complexity, needs DMRC onboarding), then crowd analysis (low value, medium complexity).
  - Finish with metrics: navigation requests, tickets booked.
  - **Interviewer pushback to prepare for:** "Why one commuter persona instead of splitting by age or tech literacy?" Have a one-line reason ready, or split the persona.

### Case 2: Gen AI features in Google apps (design, GenAI)

- **Prompt:** "You are a PM at Google. Introduce Gen AI based features in any Google app."
- **Case type:** Product improvement and design using generative AI.
- **Answer structure:**
  - Clarify the objective. The interviewer says user productivity first, then engagement, and any product. The candidate picks B2C for exposure.
  - Shortlist three apps (Photos, Meet, Gmail) and justify the pick. Meet is dropped (smaller audience, real-time video is hard). Photos beats Gmail because editing images takes more effort than text, so the productivity gain is bigger. The casebook notes that a scoring table (number of users, customer value, feature potential, fit with the objective) earns extra credit.
  - List pains before features: shaky panoramas, someone looking away in group photos, writing captions, extracting data from photos of notes and bills.
  - Features: Smart Panorama (merge 2-3 shots with generative fill, using gyroscope metadata), changing facial perspective (even adding a missing person), caption suggestions tuned to the platform (professional for LinkedIn), and OCR plus summarisation into a doc or sheet. Delivered through a "magic wand" prompt box calling Bard or Magic Editor.
  - Metrics: time saved per edit compared with external editors, edits per user per month, output accuracy (feedback, number of re-prompts, redrafts, corrections), and engagement (conversation length, session time).
  - Follow-up: Meet ideas (highlight reels from transcripts, generative video enhancement on weak networks, translated recordings, background filtering).
  - **Reviewer note (not in the transcript):** a stronger answer would also cover the AI failure modes: edited faces that look wrong, consent for altering people in photos, and labelling AI-edited images. See Chapter 12 (Adapting CIRCLES for AI features).

### Case 3: Flipkart Hyperlocal delivery breaches (diagnosis)

- **Prompt:** "Flipkart's hyperlocal business in Bangalore is observing breaches. Diagnose the issue."
- **Case type:** Root cause analysis. The Sigma TOC files this under RCA, not design.
- **Answer structure:**
  - Define the breach metric (average delivery time per order) and size the change: about 10% up, which on a 90-minute promise is about 9 minutes per order.
  - Check external factors first: weather (ruled out), government action on regional stores, store closures.
  - Segment by category and region: only some parts of Bangalore are affected, so server-side errors are unlikely.
  - Walk the delivery journey in four steps with a metric for each (acceptance, travel to store, pickup, pickup to delivery). Simplify to single-order delivery.
  - Only pickup-to-delivery time is up. Split it into pickup to landmark (traffic, construction, stops: all fine) and landmark to door.
  - **Root cause:** apartments in these areas have slow gate-security entry for delivery agents, costing 5-10 minutes per order. The interviewer nudged the candidate here ("think about a typical end-user location in Bangalore"). A natural fix is pre-registered agent entry or digital gate passes with apartment associations.

![The Hyperlocal journey: four steps, one of them split, and the gate at the landmark-to-door step.](diagrams/l20-flipkart-journey.svg)

### Try it locally: how big is the gap?

*(Beyond the notes: reproduced locally with the standard library, using the numbers in the case. It is an arithmetic check, not evidence.)*

```python title="lab_p20_hyperlocal_gap.py"
# Flipkart Hyperlocal: how big is the delay, and how much can the gate explain?
promise = 90                  # minutes, the delivery promise
rise = 0.10                   # average delivery time is up 10%
extra = promise * rise
print(f"extra time per order: {extra:.0f} minutes (10% of 90)")
for lost in (5, 10):
    print(f"gate loss of {lost:>2} min is {lost / extra:.0%} of the gap")
```

```output
extra time per order: 9 minutes (10% of 90)
gate loss of  5 min is 56% of the gap
gate loss of 10 min is 111% of the gap
```

The gap is about 9 minutes per order. A 5-minute gate loss would explain about half of it, and a 10-minute loss would be more than the whole gap. This is a plausibility check, not a proof: the gate loss is per order at one step, and the 10% is an average across parts of Bangalore. The confirming data cut is the one the case asks for: gate time by apartment, against the rest of the route.

### Case 4: Uber drivers' active count falls (RCA)

- **Prompt:** Active drivers on Uber are down about 2%, gradually over two months, and the drop is limited to Hyderabad.
- **Case type:** Root cause analysis with a supply-side metric.
- **Answer structure:**
  - Define the metric first: active driver = logged in and willing to accept rides for at least 2 hours a day.
  - Restate the facts and confirm the scope (gradual, 2 months, Hyderabad only, all devices and OSs).
  - Reason from the scope: releases are not region-specific, so a city-only drop points to a local cause. Vernacular support is ruled out because it would hit all Telugu-speaking regions.
  - Walk the driver journey with metrics: sign-up and login (fine), trip requests per day (flat, so not demand), acceptance rate and idle time (flat), pick-up and trip distance and duration (fine), payment (average monthly income down).
  - Decompose income: same trips, so earnings per trip fell. Tips are unchanged, so the fare paid to drivers fell.
  - **Root cause:** the "late night safety fee" (10 PM-6 AM) was removed after Hyderabad was declared a safe city. A time-of-day cut confirms it: the drop is severe at night and small at peak hours.
  - **Recommendations:** a graded city safety index that scales the night fare (instead of on/off), incentives bundled after n night rides to control cost, experiments to find the right incentive level, and passing some of the cost on to night riders.

![The Uber RCA tree: the scope rules out releases, and only income moves down the journey.](diagrams/l20-uber-drivers.svg)

### Case 5: Google Maps ETA is too short (RCA with metric lens)

- **Prompt:** Google Maps shows a shorter ETA than the real travel time. Users arrive late even when they follow the directions.
- **Case type:** Root cause analysis (the Sigma table of contents lists it in the RCA section, not under product design or the "Google Maps" app-improvement case).
- **Answer structure:**
  - Clarify: all platforms, many regions, started in the last few days, worse at peak hours. Traffic data sources are unchanged, but a routing update added more real-time traffic and road-closure data. Some users say the ETA barely changes with time of day.
  - Verify the change: compare predicted vs actual travel times before and after the update.
  - Hypothesise: the update may over-weight road closures or under-weight traffic at peak times.
  - Act in two steps: fix the algorithm weights, and tell users about the issue and the fix timeline.
  - Prevent recurrence: stronger testing of routing changes and a user feedback loop for reported discrepancies.

![Google Maps ETA: verify against actuals, hypothesise, act in two steps, then prevent.](diagrams/l20-google-maps-eta.svg)

### Case 6: Pricing a smart speaker (pricing)

- **Prompt:** "How would you price Apple Home, the smart speaker from Apple?"
- **Case type:** Pricing a new launch into a market with established competitors (Alexa, Google Home).
- **Answer structure:**
  - Clarify the product: a smart speaker with a voice assistant that also controls smart-home devices. It launches next quarter, with a goal of taking 20-30% market share.
  - Weigh the strategy: pricing below competitors would win share, but Apple's history is high differentiation at a premium price, and cutting price would dilute the brand. So: premium, benchmarked to competitors.
  - Ask for competitor prices: Google Home Rs 10K, Google Home Mini Rs 5K, Alexa range Rs 4K-9K.
  - Launch two variants to cover the low and high ends (useful in price-sensitive India).
  - Estimate Apple's premium at about 15% (iPhone 12 vs a comparable Google Pixel). That gives about Rs 5.75K for the Mini and Rs 11.5K for Apple Home.
  - Justify the premium: don't compete on rivals' strengths (Alexa's shopping, Google's search). Differentiate on Siri personalisation, with multi-user voice recognition giving each person tailored answers, and on design.
  - From the Sigma pricing approach (worth adding aloud): check whether there is a cost advantage before going low, and cover risks such as price elasticity and competitor or supplier reactions.

![Apple Home: the competitor anchors, and the 15% premium that lands the two variants.](diagrams/l20-apple-home-anchors.svg)

### Patterns across the Sigma cases

- Clarify first in every case, and state the goal (adoption, share, diagnosis) before the framework.
- Segment before you hypothesise. Region, category, platform and time window cut the search space fast.
- In RCA, walk the user journey stage by stage and attach one metric to each stage, then decompose the one that moved (income = trips x earnings per trip; delivery time = to landmark + landmark to door).
- RCA answers end with a confirming data cut (time of day in Uber) and a fix, not just a cause.
- Quantify guesses out loud. The interviewers push for numbers at every stage.
- Pricing answers need a goal, a market-maturity read and a risk list, not only a number.

### Practice questions

1. Redo the Delhi Metro case, but choose the safety staff as the persona. What changes in the features and metrics?
2. In the Uber Drivers case, the late-night fee removal saves Uber money. How would you decide whether to restore it, and what experiment would you run?
3. Apple Home is priced about 15% above Google Home. Build the case for and against holding that premium if share after six months is below the 20% goal.
4. Google Maps' ETA is too short for users on one route only. Do you roll back the update globally? Why or why not?

> [!INTERVIEW] Redo the Delhi Metro case, but choose the safety staff as the persona. What changes in the features and metrics?
> *(Beyond the notes: a starting point.)* The safety staff need alerts and crowd-density signals more than navigation. Features shift toward crowd analysis and incident reporting, and the metric becomes incidents handled per shift, with a guardrail on false alarms.

> [!INTERVIEW] In the Uber Drivers case, the late-night fee removal saves Uber money. How would you decide whether to restore it, and what experiment would you run?
> *(Beyond the notes: a starting point.)* Compare the cost of the fee with the drop in night drivers in Hyderabad. Run a graded fee in a few zones against a holdout, and decide on active night drivers and night completion rate, with a guardrail on rider wait times.

> [!INTERVIEW] Apple Home is priced about 15% above Google Home. Build the case for and against holding that premium if share after six months is below the 20% goal.
> *(Beyond the notes: a starting point.)* For: the premium matches the brand and the Siri differences, so the price buys margin. Against: a share miss means the premium is blocking adoption. Test a lower variant in two cities, and decide on share and retention before the next price move.

> [!INTERVIEW] Google Maps' ETA is too short for users on one route only. Do you roll back the update globally? Why or why not?
> **Short answer outline: Question 4**
> - Scope first: one route, so the update may not be the cause. Check whether the route has a road closure or a map error.
> - Mitigate narrowly: roll back the change for affected routes only, if the data supports it.
> - Verify with before-and-after ETA vs actual travel time on that route.
> - Global rollback only if the error shows up across regions.

*Related:* Chapter 22 (22.1 Product design cases; 22.3 Root cause analysis and diagnosis cases; 22.5 Pricing cases), Chapter 16 (Scoping; Walking the user journey), Chapter 12 (CIRCLES), Chapter 15 (Metric trees and diagnosing metric movement), Chapter 17 (Cost-plus, value-based, and competitive pricing).

## 23.2 XLRI casebook solutions

> The XLRI casebook pairs each case type with a worked answer, so use it to practise the type first and the company second: the same structure works for Amazon, LinkedIn or Uber.

### Cases

Condensed from the XLRI PM Casebook 2023 (Prometheus, the product, tech and UX committee). Most cases come from the "Product Design Frameworks" (CIRCLES, RICE) and "Product Cases" (improvement, RCA, pricing, GTM) chapters. The Amazon searches case comes from the Amazon app teardown, and the Uber Premier question from an Uber record in "Interview Experiences". Where the casebook answer stops short, additions are marked **Reviewer addition**.

### Case 1: How would you improve LinkedIn? (improvement)

- **Prompt:** "How would you improve LinkedIn?"
- **Case type:** Product improvement.
- **Answer structure:**
  - Define the product: a professional network for jobs, connections, clients and skills.
  - Clarify "improve": acquisition, engagement or revenue. Pick engagement (retention and revenue follow).
  - Fix scope: mobile app, both OS, region of your choice.
  - Segment users (job seekers, recruiters, salespeople, casual users) and pick job seekers, the most active base.
  - List 5 pains: unclear application status, unsure resume format, unaware of profile flaws, can't tell a startup from a big firm, can't find company reviews. Rate impact and pick the two "High" ones (resume format, profile flaws).
  - Solutions: an automated Resume Reviewer (impact high, effort medium), paid Mock Interviews with verified coaches (high, high), and Profile Strengthening Recommendations comparing you with shortlisted profiles (medium, medium).
  - Metrics per solution, for example resumes reviewed month on month and the change in shortlist rate after use (Resume Reviewer), interviews taken vs requested and subscription revenue (Mock Interviews), and applications per user and jobs-page DAU (Profile Recommendations).
  - Summarise: segment, the two pains, the three solutions.
  - **Reviewer note:** the answer gives no guardrail. Add one, for example spam applications or recruiter complaints, so higher application volume does not hurt match quality.

### Case 2: Design a marketplace for lawyers and clients (design)

- **Prompt:** Design and ideate a marketplace for lawyers and clients to access legal services.
- **Case type:** Two-sided marketplace design, using CIRCLES for needs and RICE for prioritisation (the casebook uses it as the RICE worked example).
- **Answer structure:**
  - Four personas, two per side. Inexperienced complainant (a first-time tenant in a metro dispute who can't tell which lawyer is good), experienced complainant (wants to know what lawyers charge), experienced lawyer (wants clients, struggles to manage case files), inexperienced lawyer (struggles to convince clients).
  - Write each as "As a / I am / I want to / I find" so the pain is explicit.
  - Features for both sides: lawyer profile and expertise, pricing quotation (indicative, since fees vary by case complexity), requirement posts by clients, "see interested clients" for lawyers, a contact point (call or chat), and a case-management portal for lawyers.
  - Score each on Reach, Impact, Confidence and Effort (High/Med/Low or 1-10).
  - Final order: lawyer profile, then requirement posts, then pricing quotation, then contact point. The lawyer-side portal is high effort and medium reach, so it waits.
  - **Reviewer addition:** the casebook gives no metrics. Add a north star (completed consultations per week), supply and demand health (requirement posts with a lawyer response within 24h), and a guardrail (complaints or disputes per consultation).

### Case 3: Searches dropped 10% on Monday (metrics and diagnosis)

- **Prompt:** "You are a PM at Amazon. You found out on Monday that searches decreased by 10%. What would you do?"
- **Case type:** Metric diagnosis.
- **Answer structure:**
  - Clarify the metric: searches per user or in total, and the comparison window (vs yesterday or the same day last week).
  - Check the shape: sudden or gradual, which region, which platform.
  - Test four domains: server issue (latency, load), technical bug (crash rates, funnel drop-off), cannibalisation (a new feature), competitors (time spent, competitor app updates).
  - The casebook stops at the investigation domains. **Reviewer addition:** rank the domains by what the data can rule out fastest (server dashboards first), then propose the fix once a cause is confirmed, plus an alert so it does not repeat.

### Case 4: Order cancellations up 10% at Amazon (RCA)

- **Prompt:** "Order cancellations on Amazon are up by 10%. Identify the root cause."
- **Case type:** Root cause analysis.
- **Answer structure:**
  - Clarify duration, trend, product category, geography and whether it is across channels.
  - Look at external causes: regulation or policy change, new substitutes, public sentiment.
  - Walk the buyer journey by channel (search ads, organic, email, app, shared links).
  - Inspect key actions: search results, cross-sell section, category tabs, checkout and payment.
  - Check recent changes to the recommendation algorithm and any cannibalisation from new listings.
  - Name the one or two changes most likely to explain the rise, then the data to confirm.

### Case 5: Double Uber Premier gross bookings (pricing and growth)

- **Prompt:** "Uber Premier bookings have gone down and you are looking to double the number of gross bookings (trips x fare). How will you go about this? How would you increase the fare without incurring losses or promotion expenses?"
- **Source:** an Uber interview record (round 2) in the casebook's "Interview Experiences" section, not a structured worked case. The candidate's answer is two lines; the rest below is a reviewer expansion.
- **Case type:** Growth with a metric tree, plus pricing.
- **Answer structure:**
  - Decompose the target: gross bookings = trips x average fare, so each lever is named.
  - Grow trips (from the record): promotions, a better app experience, more driver availability.
  - Grow fare (from the record): dynamic pricing at peak demand, a premium for optional services such as Wi-Fi.
  - The follow-up is the trap: promotions raise trips but cost money, so fare growth has to come from value-added services, not discounts.
  - Metrics (reviewer addition): trips per rider, fare per trip, promotion cost per trip, driver availability.
  - Same round, worth practising: "25% off up to Rs 50 vs 15% off up to Rs 100: which is better?" The break-even is a Rs 333 ride. Below it the 25% offer wins; above it the 15% offer wins.

![The Premier metric tree, and the break-even between the two promotions.](diagrams/l20-uber-premier.svg)

### Try it locally: which promotion wins?

*(Beyond the notes: reproduced locally with the standard library. The two offers and the Rs 333 break-even are the vault's; the table checks them at each fare.)*

```python title="lab_p20_uber_breakeven.py"
# Which promotion pays the rider more? 25% off up to Rs 50, or 15% off up to Rs 100?
def saving_a(fare):
    return min(0.25 * fare, 50)      # 25% off, capped at Rs 50
def saving_b(fare):
    return min(0.15 * fare, 100)     # 15% off, capped at Rs 100

for fare in (200, 300, 333, 334, 400, 700):
    a, b = saving_a(fare), saving_b(fare)
    better = "25% off" if a > b else "15% off" if b > a else "tie"
    print(f"fare Rs {fare:>3}: 25% offer saves Rs {a:>5.2f}, "
          f"15% offer saves Rs {b:>6.2f} -> {better}")
print(f"break-even fare: Rs {50 / 0.15:.2f}")
```

```output
fare Rs 200: 25% offer saves Rs 50.00, 15% offer saves Rs  30.00 -> 25% off
fare Rs 300: 25% offer saves Rs 50.00, 15% offer saves Rs  45.00 -> 25% off
fare Rs 333: 25% offer saves Rs 50.00, 15% offer saves Rs  49.95 -> 25% off
fare Rs 334: 25% offer saves Rs 50.00, 15% offer saves Rs  50.10 -> 15% off
fare Rs 400: 25% offer saves Rs 50.00, 15% offer saves Rs  60.00 -> 15% off
fare Rs 700: 25% offer saves Rs 50.00, 15% offer saves Rs 100.00 -> 15% off
break-even fare: Rs 333.33
```

The 25% offer is capped at Rs 50 from a fare of Rs 200 upward, while the 15% offer keeps growing with the fare until its Rs 100 cap. The two savings are equal at a fare of about Rs 333, so the vault's Rs 333 is the break-even. Below it the 25% offer saves more; above it the 15% offer does.

### Case 6: Price a SaaS project management tool (pricing)

- **Prompt:** Set a pricing strategy for a new cloud-based project management service.
- **Case type:** Pricing for software.
- **Answer structure:**
  - Segment customers by organisation size (small, mid-sized, large) and needs.
  - Benchmark competitors on features, ease of use and reviews to position the price.
  - Choose a subscription model, priced per user, from customer feedback and value-based pricing. Tiers differ on features, storage and collaboration.
  - Put numbers on it: basic at $15 per user per month (essential features, limited storage), premium at $30 per user per month (advanced features, unlimited storage, premium support).
  - Add a free trial or freemium version to drive conversion.
  - **Reviewer addition:** name the risks (a freemium tier that is too generous slows upgrades; per-seat pricing discourages adding casual users) and say how you would test the price points.

### Case 7: How would Google launch a driverless car service? (go-to-market)

- **Prompt:** "How would you launch Google's driverless car service?"
- **Case type:** Go-to-market and launch.
- **Answer structure:**
  - Define the goal: become the top player and catch the perceived leader, Uber.
  - Use Google's edge: the connected ecosystem (Google Home, Maps), and its AI.
  - Launch pilots in two markets: a family chauffeur service in a tech-aware city (with a safety driver, a week-long lottery pilot) and package delivery via Google Express or, for visibility, FedEx or UPS.
  - Use marketing that shows the ecosystem (a teenager tracked on Google Home and Maps).
  - Partner with developers to build apps on the driverless platform.
  - Name the constraint: legislation must change before a full service runs.

### Patterns across the XLRI cases

- Name the case type in the first minute, then choose the matching framework (CIRCLES for design, a driver tree for growth, a journey walk for RCA).
- For metric drops, clarify the metric and the comparison window before any hypothesis.
- Decompose a business target into its multiplicative parts (trips times fare) before proposing levers.
- Pilot before scale: pilots appear in the GTM answer, and free trials in the pricing answer.
- Prioritise visibly: impact ratings (LinkedIn), impact vs effort (LinkedIn solutions) and RICE (lawyer marketplace).
- Several casebook answers stop without metrics or guardrails (lawyer marketplace, Amazon searches). In an interview, always close with a metric and a guardrail.

### Practice questions

1. Redo the Amazon searches case for a food delivery app. Which domains change, and which stay the same?
2. Uber wants to double gross bookings but cannot offer deeper promotions. Which lever do you pull, and what do you watch?
3. Choose a tiered SaaS price for a 10-person team and a 500-person team. What feature separates the tiers?

> [!INTERVIEW] Redo the Amazon searches case for a food delivery app. Which domains change, and which stay the same?
> *(Beyond the notes: a starting point.)* The four domains stay: server, technical bug, cannibalisation and competitors. What changes is the competitor set (other delivery apps and restaurant direct orders) and the funnel (restaurant views and cart, not search results).

> [!INTERVIEW] Uber wants to double gross bookings but cannot offer deeper promotions. Which lever do you pull, and what do you watch?
> **Short answer outline: Question 2**
> - Decompose: gross bookings = trips times fare.
> - Without promotions, grow fare: dynamic pricing at peak times, optional paid add-ons.
> - Watch: fare per trip, trips per rider, churn after a price change, driver availability at peak.

> [!INTERVIEW] Choose a tiered SaaS price for a 10-person team and a 500-person team. What feature separates the tiers?
> *(Beyond the notes: a starting point.)* Price per user with a tier by need: for the 10-person team, the basic tier with limited storage; for the 500-person team, the premium tier with admin controls and premium support. The feature that separates the tiers is the one that the larger team needs and the smaller team does not, such as admin controls or unlimited storage.

*Related:* Chapter 22 (22.2 Product improvement cases; 22.3 Root cause analysis and diagnosis cases; 22.4 Metrics cases; 22.5 Pricing cases; 22.7 Go-to-market and launch cases), Chapter 15 (Metric trees and diagnosing metric movement), Chapter 17 (Cost-plus, value-based, and competitive pricing).

## 23.3 Annotated answers from interview experiences

> Real candidates were asked these questions. Each annotation says what the stronger answer did, and where a weaker answer usually goes wrong.

### Cases

Each entry gives the company, the question as the candidate reported it, what the answer did, and what a strong answer adds. Annotations are our reading of the reports, not the candidates' own assessments.

### 1. Google Pay: what problem does it solve, and which metrics?

- **Company:** Google (Google Pay), Sigma 2023-24 interview report.
- **Question:** "What is Google Pay solving? Summarise it in one statement. If you were the PM, what metrics would you track?"
- **What the answer did:** Gave a one-line positioning ("money made simple", an all-in-one payments app). Chose end users over merchants and used AARRR to order the metrics: acquisition (new and retained installs), activation (users who make a payment, including through apps like Swiggy), retention (returning payers), referral, and revenue (none for end users).
- **Annotation:** Strong because it scoped the users first, used a known framework in order, and defined activation as a payment event rather than an install. Weak answers list metrics without a framework or without defining each one.

### 2. Google Pay: design a tuition-fee payment feature, GTM and north star

- **Company:** Google (Google Pay), same report.
- **Question:** "Come up with a new feature for GPay for fee payments." After the candidate clarified that "fee" meant college tuition: "Design it, give the go-to-market, and name the north star metric."
- **What the answer did:** Noted that UPI limits make it unusable for large fees (IIMB's 4 lakh+ tuition), so added NEFT, IMPS and card payments. Added fee reminders, a pilot with user feedback, and later a financing option once adoption is high. GTM: start with IIMs and ISB, then other top schools, then IITs, NITs and private colleges. Onboard colleges with a free payment gateway, keep it free for students, and promote it with cashback, one-click reminder notifications and influencers. North star: number of payments successfully made.
- **Annotation:** Strong because it spotted a real constraint (the UPI limit) from the scale of the problem, sequenced pilot before scale, and treated GTM as a two-sided problem (colleges and students). Missing: a guardrail such as failed or reversed payments.

### 3. Google Photos: improve the product, then prioritise and set metrics

- **Company:** Google (Google Photos), Sigma 2023-24 interview reports (two different Google candidates).
- **Question:** One candidate got "Improve Google Photos", then prioritisation and metrics. Another got "Guess the space needed to store the photos in Google Photos" and "How can Google use the Photos app to its advantage?"
- **What the answer did:** The first candidate used CIRCLES, then prioritised and proposed metrics. The report's advice: interviewers ask you to quantify at every stage (for example, how often people use Google Photos), and define each metric precisely (bounce rate per day or per minute; an active user is one who used the platform at least twice; active users bounced per hour).
- **Annotation:** The strongest point in the report is the metric definition. "Active user" and "per hour" turn a vague metric into one you can measure. The storage question is a guesstimate (the report points to the Sigma casebook), and the interviewer expects a number with stated assumptions.

### 4. Google Maps ETA shorter than the real travel time (asked at Just Dial)

- **Company:** Just Dial, Sigma 2023-24 interview report, Round 1 (the only round), RCA. The prompt is about Google Maps, but the interviewer was Just Dial, not Google. The Sigma casebook's "Google Maps ETA" case is the same question with a longer model answer.
- **Question:** Google Maps shows a shorter ETA than the real travel time, and users arrive late even when they follow directions. What could the causes be?
- **What the answer did:** Confirmed scope with the interviewer: all platforms, a recent update, seen only in the last couple of days. Listed causes: outdated map, traffic not considered, speed limits ignored, ETA based on the air route rather than the road route. The cause was the air-route ETA, and the candidate proposed immediately pushing an update that reverts the last ETA change.
- **Annotation:** Strong because it scoped before hypothesising and gave a fast mitigation (revert) once a recent update was implicated. A stronger answer would add how to confirm the cause (compare predicted and actual times before and after the update) and how to prevent a repeat (pre-release validation). See Chapter 23 (23.1 Sigma casebook solutions), Case 5.

### 5. Google Maps: fewer clicks on the search bar

- **Company:** Google (Google Maps), Sigma 2023-24 interview report, Round 1.
- **Question:** "The search bar on Google Maps has a reduced number of clicks. What could be the possible reasons?"
- **What the answer did:** Confirmed what the search bar is, then asked whether the drop was recent or gradual, whether it hit both Android and iOS, and whether the POI shortcuts below the bar (hotels, restaurants, petrol) or other features had changed. The drop was gradual, over two months, with no recent deployment, which ruled out internal releases. The candidate then proposed a change in user behaviour: users going straight to directions from an external link or Google search, or better suggestions reducing the need to search.
- **Annotation:** Strong because it used the timing (gradual vs sudden, no deployment) to move from internal to behavioural and external causes, and could explain the deduction when asked. Like Flipkart UGC in Chapter 22 (22.3 Root cause analysis and diagnosis cases), fewer clicks may not be bad news; check whether navigation starts held steady.

### 6. "Amazon is seeing a decline in sales" (asked at United Health Group)

- **Company:** United Health Group, Analytics Manager role, Summer 2018 interview report, Round 2 (with two directors, stress-style). Not an Amazon interview.
- **Question:** "Amazon is seeing a decline in sales. How will you go about it? Last month there was an update in the process."
- **What the answer did:** The report records only the expected approach: find where in the value chain the update happened.
- **Annotation:** Use the clue in the prompt. Map the chain from acquisition to delivery, locate the update, and check the step it touched and every step after it, instead of listing every possible cause.

### 7. "Amazon has a calculator app and sales are dropping" (asked at Amagi)

- **Company:** Amagi, Product Management Intern, Summer 2020 interview report, Round 2 (interview by a Product Lead). Not an Amazon interview.
- **Question:** "Amazon has a calculator app and sales have been dropping. Do a root cause analysis."
- **What the answer did:** The report says only that the interviewer "majorly checked the thought process". No answer is recorded.
- **Annotation:** With an odd prompt like this, structure carries the answer. Clarify what "sales" means (downloads or paid upgrades), scope it (when, which platform or region), check external causes (free built-in calculators, competitors), then walk the store funnel (impressions, page views, installs, purchases) and say what data confirms each branch.

### 8. "A new startup like Swiggy has declining sales" (asked at Samsung R&D)

- **Company:** Samsung R&D, Sigma 2023-24 interview report, Round 1 (topics: guesstimates, RCA). The same prompt is solved in the Sigma casebook as "Success Metrics - Swiggy", credited to Samsung R&D.
- **Question:** "Let's consider a new startup like Swiggy. There is a decline in sales. Explain each stage of the customer journey, the possible reasons for fewer sales at each stage, and the relevant success metrics."
- **What the answer did:** The report points to the Sigma casebook solution, which uses five stages (awareness, consideration, purchase, retention, referral), each with reasons and 2-3 metrics. See Chapter 22 (22.4 Metrics cases).
- **Annotation:** Strong because it gives reasons and metrics per journey stage, so the interviewer can follow the diagnosis. To go further, say which stage you would check first and why (for a new startup, usually awareness and consideration).

### 9. Swiggy: sales are declining (asked at Gulf Talent)

- **Company:** Gulf Talent, Product Management, Summer 2018 interview report, Round 2 case.
- **Question:** "You are the PM at Swiggy. It is experiencing a decline in sales. What different things will you look at? You have to use a structured approach."
- **What the answer did:** The report records only the prompt and the instruction to be structured.
- **Annotation:** Run the RCA skeleton in Chapter 22 (22.3 Root cause analysis and diagnosis cases): define "sales" (orders or GMV), scope (city, time, platform, sudden or gradual), external causes (competitor discounts, season, regulation), then the funnel (app opens, restaurant views, cart, payment, delivery), with a metric at each step.

### 10. Swiggy: add a table-booking system (asked at Flipkart)

- **Company:** Flipkart, Product Management, Summer 2018 interview report, Round 2 case (about 90 minutes; elimination after every round).
- **Question:** "You are the Product Manager of Swiggy. If you want to add a table booking system, how would you do it?"
- **What the answer did:** The report records the prompt and the length of the round, not the candidate's answer.
- **Annotation:** A product design case. Use the same frame as Case 1 (Delhi Metro) in Chapter 23 (23.1 Sigma casebook solutions): clarify, stakeholders (diners and restaurants), personas, journey, features, prioritise, metrics. Add a strategy check: does table booking fit a delivery brand?

### Patterns across the interview experiences

- The strongest answers clarify before they structure, and state the goal before the framework.
- Interviewers push for numbers at every stage. Quantify guesses and define each metric.
- In RCA, use a clue in the prompt (an update, a timing pattern, a region) to split internal from external causes.
- Mitigate first, then fix the root cause, as in the Google Maps revert.
- Check who is asking: several "Amazon" or "Swiggy" prompts here were asked by other companies (United Health Group, Amagi, Samsung R&D, Gulf Talent, Flipkart). Interviewers borrow well-known products, so prepare the case types, not only your target company.
- A named framework helps only when each step gives a specific output (a metric, a hypothesis, a data check).

### Practice questions

1. For the Google Pay metrics question, define activation in one sentence and name the data you would use to measure it.
2. The Google Maps ETA shows a short time on one route only. Which two checks come before any rollback?
3. A Swiggy-style decline shows up only in the referral stage of the journey. What changes in your diagnosis?

> [!INTERVIEW] For the Google Pay metrics question, define activation in one sentence and name the data you would use to measure it.
> *(Beyond the notes: a starting point.)* Activation is the first completed payment in the app, not the install. Measure it from payment events, counting users with one successful payment within a set window of install (the window is yours to set, and should be stated).

> [!INTERVIEW] The Google Maps ETA shows a short time on one route only. Which two checks come before any rollback?
> **Short answer outline: Question 2**
> - Check the route itself: a closure or a map error may explain one route.
> - Compare predicted and actual travel time on that route before and after the update.
> - Only then decide between a narrow rollback and a global one.

> [!INTERVIEW] A Swiggy-style decline shows up only in the referral stage of the journey. What changes in your diagnosis?
> *(Beyond the notes: a starting point.)* The search narrows to referral: the referral link, the reward for the referrer and the new user's first order. Check CSAT and positive reviews from referred users, and the share of new customers from referrals, before you look at awareness or purchase.

*Related:* Chapter 22 (22.3 Root cause analysis and diagnosis cases; 22.4 Metrics cases), Chapter 16 (Scoping; Walking the user journey), Chapter 12 (CIRCLES), Chapter 23 (23.1 Sigma casebook solutions).

## Beyond the notes: reading a worked answer

*(Beyond the notes: a method for using this chapter, not content from the vault.)*

1. Cover the answer and write your own clarifying questions for two minutes.
2. Read the answer's structure only, and compare it with yours: which step did you skip?
3. Read the conclusion and the metric. Ask whether the metric would move if the answer were wrong.
4. Write down the one number you would have guessed differently, and why.

## Beyond the notes: a metric tree for growth

*(Beyond the notes: a general pattern, using the vault's own Uber Premier decomposition.)*

- **Business target:** gross bookings = trips x average fare.
- **Lever one:** trips, moved by promotions (costly), app experience and driver availability.
- **Lever two:** fare, moved by peak pricing and paid add-ons (no promotion cost).
- **Check:** every lever has a metric that would show it working, and a cost that would show it failing.

Use the same shape for any target made of a product of two numbers, such as income (trips x earnings per trip) or GMV (orders x order value).

## Beyond the notes: pitfalls

- **Copying a casebook answer as a script.** The structure transfers; the numbers do not.
- **Accepting the first cause.** Use one confirming data cut before you name a root cause.
- **Ignoring the cost of a fix.** A fee removal saves money in one place and costs it in another (the Uber Drivers case).
- **Forgetting that the company may not be the one that asked.** Check who is asking and what the prompt borrows.

## Beyond the notes: interview corner

- **"Which metric did you define first?"** The one that the case moved. Define it precisely (active, window, platform) before you hypothesise.
- **"What would make you roll back?"** A regional error with a clear before-and-after gap. A single route is a reason to check, not yet a reason to roll back everything.
- **"How do you close a pricing answer?"** A price inside a range, a test to confirm it, and the risk you are watching.

## Revision cheat-sheet

![Chapter 23 on one page: the three sections, the marquee case in each, and the habit that carries across them.](diagrams/l20-big-picture.svg)

- **23.1 Sigma:** Delhi Metro (persona and a value vs complexity matrix). Gen AI in Google apps (a scoring table to shortlist). Flipkart Hyperlocal (the landmark-to-door step). Uber Drivers (decompose income; a time-of-day cut). Google Maps ETA (verify, then act in two steps). Apple Home (competitor anchors plus a 15% premium).
- **23.2 XLRI:** LinkedIn (impact ratings). Lawyer marketplace (RICE). Amazon searches (four domains). Amazon cancellations (journey by channel). Uber Premier (trips x fare; the Rs 333 break-even). SaaS tiers (Rs per user per month, freemium). Driverless car launch (two pilots).
- **23.3 Interviews:** Google Pay (AARRR; the UPI constraint). Google Photos (define each metric). Google Maps ETA at Just Dial (scope, then revert). Google Maps search bar (gradual, no deployment). Amazon, Amagi, Swiggy and the others (structure, then the clue in the prompt).
- **Across all three:** clarify first; segment before you hypothesise; decompose the target; quantify out loud; mitigate, then fix; close with a metric and a guardrail.

## Self-test

<details class="quiz"><summary>Why does the Flipkart Hyperlocal case segment by category and region before hypothesising?

Only some parts of Bangalore are affected, so a server-side error is unlikely, and the cut narrows the search to the local causes such as the gate-security entry for agents.

</details>

<details class="quiz"><summary>In the Uber Drivers case, how was income decomposed?

Trips were flat, so the fall was in earnings per trip. Tips were unchanged, so the fare paid to drivers had fallen. The late-night safety fee was removed after Hyderabad was declared safe.

</details>

<details class="quiz"><summary>What confirming data cut ends the Uber Drivers RCA?

A time-of-day cut: the drop is severe at night (10 PM to 6 AM) and small at peak hours, which confirms the late-night fee as the cause.

</details>

<details class="quiz"><summary>Why does the Apple Home answer land at Rs 5.75K for the Mini and Rs 11.5K for the full speaker?

It takes the competitor anchors (Google Home Mini Rs 5K, Google Home Rs 10K) and adds the estimated 15% premium (iPhone 12 vs a comparable Pixel).

</details>

<details class="quiz"><summary>In the Uber Premier case, which offer wins at a fare of Rs 300, and where is the break-even?

The 25% offer wins at Rs 300 (it saves Rs 50, the cap, against Rs 45 for 15% off). The break-even is a Rs 333 ride, where the two offers save the same amount.

</details>

<details class="quiz"><summary>What did the Google Maps ETA answer at Just Dial do first, and why?

It confirmed the scope with the interviewer (all platforms, a recent update, seen only in the last couple of days) before any hypothesis, then gave a fast mitigation: revert the last ETA change.

</details>

<details class="quiz"><summary>What activation definition does the Google Pay answer use?

Activation is a payment event (users who make a payment, including through apps like Swiggy), not an install.

</details>

<details class="quiz"><summary>Why does the Google Photos answer insist on precise metric definitions?

"Active user" and "per hour" turn a vague metric into one you can measure, such as an active user being one who used the platform at least twice.

</details>

<details class="quiz"><summary>(Beyond the notes) A worked answer seems to list everything. What should you check?

Whether it names one metric and one guardrail, and whether it quantifies the guesses. Several casebook answers stop without them, so you should add both yourself.

</details>

<details class="quiz"><summary>(Beyond the notes) Why do interviewers borrow famous products such as Amazon or Swiggy?

Because the case type is the skill being tested. Prepare the case types, not just the answers for your target company.

</details>


# Chapter 24 · AI Case Bank

<!-- lecture n="21" label="24" short="AI case bank" status="done" kind="AI cases" -->

## At a glance

| Question | Short answer |
|---|---|
| What is in this chapter? | Eight full AI case solutions, each walked through from clarify to summary. |
| How should you use them? | Practise each case from its prompt first, then read the model answer and compare. |
| What is the answer skeleton? | Clarify, users, pain points, solutions, prioritisation, metrics with guardrails, risks, summary. |
| How do you scope an AI case? | One user and one job-to-be-done before any feature (24.1, 24.2, 24.3). |
| How do you handle facts? | Ground answers in trusted sources. Treat fabrication as a **zero-tolerance** guardrail (24.1, 24.3, 24.5). |
| Where does the North Star sit? | On the outcome the user wants, never on usage or clicks. |
| When does a human stay in the loop? | For every consequential action. Autonomy grows only as the data earns it (24.6). |
| When is cannibalisation a problem? | Only when it lowers combined margin or retention. Measure it with a holdout (24.8). |
| Which error should set the threshold? *(Beyond the notes)* | The error that costs more. Set the threshold from that cost, not from headline accuracy. |
| How do you launch safely? *(Beyond the notes)* | Start with low-risk, high-frequency features, then a staged rollout behind a kill switch. |

> [!NOTE] Where this comes from
> The vault lists no outside sources for these cases. Each model answer is built from general product knowledge, because the converted sources do not cover AI case solutions. The vault's further-reading list names *Blogs & Newsletters*, *AI Product Reading* and *Product Teardowns*. No links are kept here.

## The big picture

These are the **eight AI cases** of Part V. Each one is a full model answer: how to clarify the prompt, who the users are, where the pain is, what to build first, how to measure it, what can go wrong, and how to close in 30 seconds. Use them after you have the AI concepts from Chapters 4 to 10 and the frameworks from Chapters 11 to 20. Practise each case from its prompt before you read the model answer.

- **24.1** A study assistant for competitive exam aspirants: a grounded doubt solver and a mistake-driven quiz.
- **24.2** Generative AI in a navigation app: review summaries and conversational search first, in-drive help voice-only.
- **24.3** Success metrics for an AI resume reviewer: a North Star on interview callbacks, with fabrication and bias as guardrails.
- **24.4** Diagnosing a rise in chatbot hallucination complaints: verify, segment, correlate, reproduce, then fix.
- **24.5** An AI feature in a payments app: a dispute assistant with free alerts and a success fee on won disputes.
- **24.6** A support copilot for a logistics company: built for the agent first, with actions behind confirmation.
- **24.7** Should a food delivery app add an AI meal planner: a conditional yes, starting with dinner suggestions.
- **24.8** An AI feature is cannibalising the core product: decide if the shift lowers margin, then hand off to the paid core.

## Key takeaways

- Scope every AI case to one user and one job before proposing features.
- Ground answers in trusted sources, and treat fabrication as a zero-tolerance guardrail.
- Put the North Star on the outcome the user wants, not on usage or clicks.
- Keep a human in the loop for consequential actions, and expand autonomy with data.
- Start with low-risk, high-frequency features, and use kill switches and staged rollouts for launch.

> [!SIR] From the source notes
> Scope every AI case to one user and one job before proposing features.

## 24.1 Design an AI study assistant for competitive exam aspirants

> A strong answer scopes to one exam and one job-to-be-done, grounds every answer in trusted material, and measures learning outcomes rather than usage.

### Model answer

**Clarify.** Ask four questions out loud:

- *Which exam?* UPSC, JEE, NEET and CAT need different content and answer formats (MCQ vs essay). Assume one exam first: JEE or NEET, where answers are objective and easier to verify.
- *New product or a feature in an existing prep app?* Assume a feature inside an app that already has content and mock tests. That gives us a trusted corpus and an outcome signal.
- *What is the goal?* Better scores per hour of study, not more time in the app.
- *Business model and constraints?* Free, freemium or paid shapes the cost budget per question. Assume mobile-first, low bandwidth, English plus Hindi.

**Users and segments.** Tier-2/3 self-study students with no coaching or mentor; students in coaching classes who get stuck on homework after class; droppers (repeat takers) who know the syllabus but have plateaued. Pick self-study students as the primary segment: they feel the pain most (no one to ask), they are a large and price-sensitive group, and the product is their only feedback loop. (Using CIRCLES for an AI feature: Chapter 12, Adapting CIRCLES for AI features.)

**Pain points.** No feedback on answer writing; doubts stall progress for days; content overload with no sense of what to study next; the study plan does not adapt to weak areas. (See Chapter 11, Identifying and prioritizing pain points.)

**Solutions.**

1. Doubt solver that answers from the official syllabus and curated notes, with citations to the source passage (retrieval-grounded; see Chapter 5, RAG, fine-tuning, and embeddings).
2. Daily adaptive quiz built from the user's mistake log, using spaced repetition.
3. Answer-writing evaluator scored against an exam-specific rubric.
4. Study planner that re-plans weekly from mock-test results.

MVP: doubt solver plus mistake-driven quiz. The evaluator comes second because its rubric needs validation.

![The doubt solver: retrieve from the corpus, answer with a citation or say "not sure", then feed the mistake log into the quiz.](diagrams/l21-exam-doubt-loop.svg)

**Prioritization.** Score with RICE (Chapter 14, RICE): the doubt solver has the highest reach and frequency and the lowest risk. Answer evaluation has the highest value but needs human-graded calibration first.

**Metrics.** North star: mock-score improvement per active learner over four weeks. Supporting: weekly active questions solved, doubt resolution rate (answer accepted without a follow-up on the same doubt), D28 retention. Guardrails (Chapter 15, Guardrail and negative metrics): factual error rate on a weekly sample reviewed by subject experts (target under 1 percent), citation accuracy, p95 latency, cost per active user.

**Risks and mitigations.**

- *Hallucination in high-stakes content.* A confidently wrong physics derivation teaches the wrong thing. Mitigations: answer only from the retrieved corpus with citations, say "I'm not sure, here is the closest solved example" when retrieval is weak, add a "report wrong answer" button, and run a weekly expert-reviewed sample plus a golden set of past-paper questions before every model or prompt change (Chapter 8, Offline evals: golden datasets, rubrics, LLM-as-judge).
- *Learning harm.* Students outsource thinking instead of practising recall. Mitigation: "attempt first, then hint, then full solution" by default.
- *Cost.* Doubt solving is high frequency, and peak load comes the night before mocks. Keep cost per active user below ARPU: use a small model for routing and simple doubts, the large model only for multi-step problems, and cache answers to common questions (most doubts repeat across students). See Chapter 4, Latency, cost per query, and capacity planning.
- *Latency.* Aim for first tokens in under 2 seconds and stream the solution step by step. Image doubts (a photo of a question) take longer, so show progress.
- *Data and IP.* Under the India DPDP Act 2023, users under 18 need verifiable parental consent, which makes the age gate a launch blocker. Copyright on third-party coaching material limits the corpus to owned or licensed content.

**Summary.** "For self-study JEE/NEET aspirants, the biggest pain is doubts that stall progress. I'd ship a grounded, cited doubt solver with attempt-first hints, plus a mistake-driven daily quiz. Success is mock-score gain over four weeks. Guardrails: an expert-audited error rate under 1%, p95 latency, and cost per user. Launch on one exam, with parental consent for minors and a golden-set eval gate before any model change. The answer evaluator comes once its rubric agrees with human graders."

### Real-world examples

- **Khanmigo (Khan Academy):** AI tutor that guides students with questions rather than handing over answers, a direct example of the "attempt before reveal" design.
- **Duolingo Max:** premium tier with AI explanations of answers, showing how an AI explanation can be a paid upgrade.
- **PhysicsWallah Alakh AI (India):** launched in late December 2023 for JEE/NEET learners. Its AI Guru tutor takes doubts as text, image or voice. The company reports it is built on OpenAI's GPT-4-class models with retrieval (RAG) over its own content, which is the grounded-doubt-solver pattern in this answer.

### Practice questions

> [!INTERVIEW] Why would you pick self-study aspirants over coaching students as the first segment?
> *(Beyond the notes: a starting point.)* They feel the pain most, because nobody is there to answer their doubts, and the product is their only feedback loop. Coaching students already have a teacher to ask.

> [!INTERVIEW] How would you measure whether the doubt solver is actually teaching?
> **Outline:** compare mock scores of users who used the doubt solver against a matched group; track repeat questions on the same topic as a proxy for retained learning.

> [!INTERVIEW] What is your kill criterion if factual error rate rises after a model update?
> *(Beyond the notes: a starting point.)* Set a number before launch, for example an expert-audited error rate above the 1% guardrail, and roll back the model or prompt behind the kill switch while the golden set is re-run.

*Related:* Chapter 24 (AI Case Bank, this chapter), Chapter 8 (Offline evals), Chapter 7 (Handling hallucinations, errors, and recovery paths), Chapter 9 (Privacy, consent, and data retention, India DPDP Act 2023), Chapter 14 (RICE), Chapter 11 (Segmentation and personas).

## 24.2 Add generative AI to a navigation app

> Put generative AI where it reduces friction without putting a driver's attention at risk, and start with features that reuse data the app already has.

### Model answer

**Clarify.** Ask:

- *Which app and market?* Assume a Google Maps-style app in India with search, routing, place listings, reviews and transit.
- *What is the goal?* Engagement, monetisation (ads, bookings) or a better core experience? Assume the core experience: fewer steps from intent ("somewhere to eat") to a started trip.
- *Which surface?* Search and planning (phone in hand) or in-drive (eyes on the road). These carry very different risks.
- *Constraints?* Latency budget (search must feel instant), cost per query at hundreds of millions of users, and safety rules for use while driving.

**Users and segments.** Trip planners before a journey; tourists in unfamiliar cities; daily commuters who search the same places; drivers mid-trip. For the MVP, choose trip planners and tourists, because they have time to read and the stakes of a wrong result are lower than mid-drive.

**Pain points.** Long, natural-language searches ("quiet cafe with wifi near the metro, open late") do not map to categories; review skimming takes too long; multi-stop trips are tedious to build; ambiguous addresses waste time.

**Solutions.**

1. Conversational place search that turns a natural-language query into filters and ranked places.
2. Review summaries that show what reviewers agree on, such as "good coffee, slow service".
3. Multi-stop itinerary drafts the user edits before starting.
4. In-drive, a hands-free voice assistant ("find a cheap vegetarian place on my route", "report an accident ahead"). It answers briefly by voice, never needs the screen, and any route change needs a one-word confirmation.

**Prioritization.** Use value versus effort (Chapter 14, Value vs effort). Review summaries reuse existing review data, run at high frequency and carry low risk, so they go first. Conversational search comes second. Itineraries come third. The in-drive voice assistant is phase 2: highest frequency, but also the highest safety bar, so it ships only after search accuracy is proven and with a strict voice-only design.

![The phase plan: reuse data first, then search, itineraries, and the voice-only in-drive assistant last.](diagrams/l21-nav-phases.svg)

**Metrics.** North star: navigation starts or saves per active user from an AI-assisted session. Supporting: query success (user taps a result or starts navigation), time from search to navigation start, review summary expansion and trust signals, share of searches phrased in natural language. Guardrails (Chapter 15, Guardrail and negative metrics): wrong or closed-business rate, summary-versus-review mismatch rate on a sampled audit, screen interactions while the vehicle is moving (should not rise), p95 latency (for example under 1.5 s for search), and cost per query (summaries are precomputed and cached per place, not generated per view).

**Risks.** Hallucinated opening hours cause real harm, for example a user drives to a closed place. Summaries can amplify fake or biased reviews. Using the screen while driving is a safety issue. Location-history privacy becomes sharper once the assistant learns habits.

Cost at scale is the hidden risk: generating a summary on every place view would be very expensive, so summarise offline and refresh when new reviews arrive. Search needs a small, fast model for query-to-filter parsing, and the large model only for complex queries.

Mitigations: use only structured hours from the business listing as ground truth, cite the source reviews, filter suspected fake reviews before summarising, keep in-drive output voice-only and brief, run golden-set evals on query parsing before each model change, and let users opt out of personalisation.

**Summary.** "I'd start with planners and tourists, where errors are cheap and the user has time to read. First, precomputed review summaries (existing data, low cost, low risk), then conversational search that parses natural language into filters. Success is navigation starts or saves from AI sessions. Guardrails: wrong or closed-place rate, a summary-accuracy audit, latency, and cost per query. In-drive help comes last, as voice-only and hands-free, because a distracted driver is a safety failure, not a UX bug."

> [!QUESTION] The vault calls the in-drive assistant "phase 2" and also "last". Which is it?
> The chapter uses both. Read them together: it is the second wave of work, and it ships last, only after search accuracy is proven and with a voice-only design. *(Beyond the notes: the reading that fits both lines.)*

### Real-world examples

- **Google Maps with Gemini (place Q&A and review summaries, 2024):** Gemini summarises what reviewers say about a place and answers questions about it. This is the same "reuse existing review data" pattern as solution 2.
- **Google Maps Gemini navigation (announced November 2025):** a hands-free, conversational driving assistant (ask for a stop along the route, share ETA, report incidents by voice), plus landmark-based directions in the US. Google shipped in-drive generative AI as voice-only, which supports the phase-2 design above.
- **Waze Conversational Reporting:** announced in 2024 and rolled out more widely from October 2025. Drivers describe a hazard in plain speech, and Gemini turns it into a structured report, asking a follow-up if needed. Voice in, structured data out, with minimal screen use.

### Practice questions

> [!INTERVIEW] Why should in-drive AI be voice-only, with confirmation before any route change?
> *(Beyond the notes: a starting point.)* The driver's eyes and hands belong to the road. A spoken short answer keeps attention on driving, and a one-word confirmation stops a misheard request from changing the route.

> [!INTERVIEW] How would you measure whether review summaries are trustworthy?
> **Outline:** sample summaries each week, have raters check every claim against the underlying reviews, and track disputes raised by users.

> [!INTERVIEW] What would make you pause the conversational search launch?
> *(Beyond the notes: a starting point.)* A rise in the wrong or closed-place rate, a summary-accuracy audit that fails, or any rise in screen use while the vehicle moves.

*Related:* Chapter 24 (AI Case Bank, this chapter), Chapter 7 (User control, transparency, and confidence signals; Human-in-the-loop design), Chapter 5 (Agents and tool use), Chapter 8 (Guardrail metrics: harmful outputs, latency, cost), Chapter 11 (User journeys and the 5Es).

## 24.3 Define success metrics for an AI resume reviewer

> Anchor the North Star on the outcome the user actually wants (interviews), then use leading indicators and guardrails that catch fabrication and bias.

### Model answer

**Clarify.** Ask:

- *Who is the user?* Fresh graduates, career switchers or experienced hires, and is this B2C (job seeker) or B2B (a university or job board)?
- *What does it do today?* Score only, or also rewrite bullets? Rewrites raise the fabrication risk.
- *Business model?* Free, freemium or paid shapes the cost budget per review.
- *What is the business goal?* Acquisition for a job platform, or paid conversion?

Assume B2C, freemium, India-first, with the job seeker as the user and score plus rewrites. The outcome that matters is callbacks, not a satisfied click.

**Users and segments.** Fresh graduates need structure and keyword guidance; mid-career switchers need repositioning of transferable skills; experienced hires need sharper impact bullets. Recruiters are out of scope for this answer.

**Pain points.** Users do not know what applicant tracking systems and recruiters scan for; bullets are generic; they get no feedback loop on whether any of it worked.

**What we are measuring.** Rubric-based review of structure, clarity and impact; match against a pasted job description; bullet rewrites the user accepts or rejects; a 30-day follow-up asking about interviews. (The XLRI LinkedIn case in Chapter 23, XLRI casebook solutions, proposes the same feature and measures it with resumes reviewed and the change in shortlist rate.)

**Metrics.**

- **North Star:** interview callbacks per reviewed resume within 30 days, collected through the follow-up prompt. Compare cohorts, because callbacks are confounded by the job market (Chapter 15, North Star metric).
- **Leading indicators:** activation (upload plus view feedback), suggestion acceptance rate, edit-after-accept rate, re-review within seven days (a sign the user is iterating), and NPS.
- **Caution:** acceptance rate alone rewards flattering suggestions. Pair it with a human-rated quality score.
- **Guardrails** (Chapter 15, Guardrail and negative metrics): rate of invented experience or skills (tolerance is zero), PII leakage incidents, score gap across gender and college-tier groups (bias), p95 latency, cost per review, parse-failure rate on job descriptions.

![The metric tree: one North Star, leading indicators that move it, and guardrails that act as a veto.](diagrams/l21-resume-metric-tree.svg)

**Eval plan.** Build a golden set of about 200 resumes graded by recruiters against the rubric. Calibrate an LLM-as-judge against those grades before using it at scale (Chapter 8, Offline evals: golden datasets, rubrics, LLM-as-judge).

**How to read the metrics together.** If acceptance rises but callbacks stay flat, the suggestions are pleasing but not useful: revisit the rubric. If callbacks rise but the fabrication audit flags more invented claims, stop and fix, because short-term callbacks from inflated resumes turn into failed interviews and lost trust. The guardrails act as a veto, not a trade-off.

**Risks.** Fabrication of achievements, which can cost a candidate an offer: the model should only rephrase what the user wrote, flag any new number or skill for confirmation, and never invent metrics. Bias against non-prestigious colleges, career gaps or non-native English. Cost and latency: a full review is a long-context call, so cap free reviews per month, use a cheaper model for parsing and scoring, and save the large model for rewrites; users accept 10-20 seconds if progress is shown. Privacy: resumes hold sensitive personal data, so retention, consent and "don't train on my resume" controls must be explicit under the India DPDP Act 2023 (Chapter 9, Privacy, consent, and data retention).

**Summary.** "North Star: interview callbacks per reviewed resume within 30 days, compared by cohort. Leading indicators: activation, suggestion acceptance paired with a human-rated quality score, and re-reviews. Guardrails: zero fabricated claims, a bias gap below a set threshold, PII incidents, latency and cost per review. All of it is validated against a recruiter-graded golden set before any model change."

### Real-world examples

- **Jobscan:** resume-to-job-description matching and keyword scoring, a well-known example of the match-against-JD feature.
- **Teal:** resume builder and tracker that connects resume edits to job applications.
- **Kickresume:** a resume builder with an AI writer that drafts resume sections and cover letters. It is a direct example of the rewrite feature, and of why fabrication guardrails matter.

### Practice questions

> [!INTERVIEW] Why is "callbacks per resume" a better North Star than "reviews completed"?
> *(Beyond the notes: a starting point.)* Reviews completed measures use of the tool. Callbacks measure whether the reviewed resume helped the user get the outcome they came for.

> [!INTERVIEW] How would you detect bias in suggestions?
> **Outline:** create matched resume pairs that differ only in college tier or name, compare score and suggestion distributions, and set a threshold for the gap.

> [!INTERVIEW] What signal would tell you the rewrites are inflating claims?
> *(Beyond the notes: a starting point.)* A rise in the invented-claim rate on the fabrication audit, or rewrites that add numbers or skills the user did not confirm.

*Related:* Chapter 24 (AI Case Bank, this chapter), Chapter 15 (North Star metric; Funnel, marketplace, and retention metrics), Chapter 8 (Online metrics: task success, acceptance and edit rate, retention of AI users), Chapter 9 (Bias, fairness, and representation), Chapter 14 (Choosing and defending a framework).

## 24.4 Diagnose a rise in chatbot hallucination complaints

> Verify the metric first, segment by intent and version, then match the timeline to the most likely cause before proposing any fix.

### Model answer

**Clarify.** Which chatbot (assume customer support for a consumer fintech)? When did complaints rise, and by how much? Is the rise in absolute complaints or a rate? Which sources feed the complaints: support tickets, thumbs-down, app-store reviews? Did anything change in the model, prompts, knowledge base or product recently? (Chapter 16, Scoping: clarify, verify metrics, check platforms and segments.)

**Verify the metric.** Convert counts to complaints per 1,000 conversations. If volume doubled, a flat rate means no hallucination problem. Also classify complaints by type: invented policy, wrong fee or rate, invented product, wrong contact details.

### Try it locally: a rate, not a count

*(Beyond the notes: reproduced locally with the standard library. The counts are made up to show the arithmetic.)*

```python title="lab_p21_complaint_rate.py"
# Counts go up when volume goes up. The rate tells you whether the bot got worse.
weeks = {"week 1": (120, 40_000), "week 2": (240, 80_000)}   # (complaints, conversations)
for name, (complaints, conversations) in weeks.items():
    rate = complaints / conversations * 1000
    print(f"{name}: {complaints} complaints in {conversations:,} conversations = {rate:.1f} per 1,000")
```

```output
week 1: 120 complaints in 40,000 conversations = 3.0 per 1,000
week 2: 240 complaints in 80,000 conversations = 3.0 per 1,000
```

The complaints doubled, but so did the conversations. The rate did not move, so the first question is answered: there is no sign of a hallucination problem yet. Only a change in the rate would justify the next steps.

**Segment.** Break the rate down by intent, language, platform, app version and model version. A spike concentrated in one intent points to retrieval or content; a spike across everything points to a model or prompt change.

**Timeline correlation.** Line up complaint onset with deploys, prompt edits, knowledge-base updates, and silent vendor model updates. Note any external event: a new product, a regulatory change, a fee revision. (Chapter 16, Internal vs external causes.)

**Reproduce.** Replay a sample of conversations from the affected intent against the previous and current configuration. Run the golden eval set. Check whether the correct document was retrieved. A retrieval miss and a faithfulness failure with the right context need different fixes (Chapter 16, AI-specific RCA: model changes, prompt regressions, data drift, cost spikes).

**Likely causes and signatures.**

| Hypothesis | Signature | Check |
|---|---|---|
| Vendor model update | Spike across intents, same time as vendor change | Replay with pinned old version |
| Prompt regression | Spike after a prompt edit | Diff prompts, rerun eval set |
| Stale knowledge base | Spike in one policy intent | Compare doc dates with policy changes |
| Retrieval miss | Right answer absent from retrieved context | Log retrieval hit rate per intent |
| New intent with no content | Spike in a new feature area | Check coverage of intent list |
| Cost-driven change (smaller model, shorter context, fewer retrieved chunks) | Spike after a cost-cutting release; longer conversations hit worst | Compare cost per conversation and context length before and after |

![The RCA tree: the rate is verified first, the cuts and timeline narrow the cause, and the signature picks the fix.](diagrams/l21-hallucination-rca.svg)

**Fix and prevention.**

- *First 24-48 hours (mitigate):* roll back the config, or gate the affected intent with a kill switch (Chapter 10, Staged rollouts and kill switches). Route money-related intents (fees, refunds) to humans or to templated answers. Tell support and leadership what is affected and what customers were told.
- *Root-cause fix:* refresh the stale documents, fix retrieval, or revert the prompt. Add "I don't know, let me connect you to an agent" for uncovered intents.
- *Prevention:* pin model versions, add an eval gate on the golden set before any model, prompt or knowledge-base change (Chapter 8, Regression testing when models or prompts change), monitor faithfulness on a sampled live stream, and link knowledge-base updates to policy changes.

**Metrics.** Primary: hallucination rate on a sampled, human-reviewed set. Supporting: complaint rate per 1,000 conversations, retrieval hit rate for the affected intent, escalation rate, CSAT. Guardrails: refusal or "I don't know" rate (over-correction makes the bot useless), cost per resolved conversation (a bigger model or more retrieved context costs more), and p95 latency (extra verification steps slow replies).

**Risks.** A customer acts on a wrong fee or policy and loses money; Air Canada was held liable for its chatbot's wrong bereavement-fare advice, so the legal exposure is real. Over-tightening the bot can push all customers to human agents, raising cost.

**Summary.** Verify the rate, segment by intent and version, correlate the timeline, reproduce, then fix the cause. Protect customers with a kill switch and an escalation path while the root cause is confirmed.

### Real-world examples

- **Air Canada chatbot case (2024):** a tribunal held the airline responsible for incorrect refund advice from its chatbot. A well-known reference for hallucination liability.
- **Klarna AI assistant:** in February 2024 Klarna said its OpenAI-powered assistant handled about two-thirds of customer-service chats in its first month. In 2025 the CEO said it would make sure customers can always reach a human, after admitting that the focus on cost had hurt quality. It shows that automation rate is not a success metric without quality guardrails.
- **Intercom Fin:** AI agent grounded in a company's help content, the design pattern whose failures this case diagnoses.

### Practice questions

> [!INTERVIEW] Why convert counts to a rate before anything else?
> *(Beyond the notes: a starting point.)* Volume changes on its own. A count can double with no change in quality, so only a rate per conversation shows whether the bot itself got worse.

> [!INTERVIEW] How would you tell a retrieval failure from a generation failure?
> **Outline:** check whether the correct passage appears in the retrieved context; if it does and the answer still contradicts it, the failure is in generation.

> [!INTERVIEW] What would you tell leadership in the first 48 hours?
> *(Beyond the notes: a starting point.)* What is affected, what customers were told, what has been rolled back or gated, who owns the root-cause fix, and when the next update comes.

*Related:* Chapter 24 (AI Case Bank, this chapter), Chapter 7 (Handling hallucinations, errors, and recovery paths), Chapter 10 (Monitoring drift and vendor model updates), Chapter 8 (Regression testing when models or prompts change), Chapter 9 (Explainability and disclosure), Chapter 16 (Walking the user journey).

## 24.5 Launch an AI feature in a payments app: pricing and risks

> In payments, the right feature is one with clear ROI and a human approval step; price it on outcomes, and launch behind kill switches.

### Model answer

**Clarify.** Which feature? Assume an AI dispute and chargeback assistant for merchants. Who pays: merchants, consumers, or both? Is the goal revenue, retention, or lower support cost? Regulatory context: RBI rules for digital payments and the India DPDP Act 2023. Is there an existing merchant plan to bundle into?

**Users and segments.** High-volume merchants lose money to chargebacks and spend staff time on disputes; small merchants struggle with evidence and deadlines; consumers want spend insights. Pick high-volume and small merchants for the dispute assistant, because the ROI is measurable in recovered money.

**Pain points.** Dispute reason codes are confusing; deadlines are missed; evidence (invoices, delivery proof) is scattered across systems.

**Solutions.** The assistant reads transaction data, flags likely wins, drafts a response with the evidence list, and guides evidence upload. A human approves every submission. Consumer spend insights come later.

**Pricing options and recommendation.**

- Free for all merchants, as a retention play (no direct revenue, and cost scales with usage).
- Usage-based: a flat fee per dispute drafted, win or lose.
- Bundled into a premium merchant plan.
- Outcome-based: a share of the amount recovered, charged only on won disputes. This is the market norm for automated dispute tools: Stripe's Smart Disputes charges a share of the recovered amount only when the merchant wins, and Chargeflow charges 25% of recovered chargebacks.

Recommendation: a hybrid.

- *Free:* deadline alerts and an evidence checklist for every merchant. This is cheap (rules plus a small model) and builds trust.
- *Paid:* AI drafting and submission, priced as a success fee on won disputes, so the merchant pays only when they get money back. Add a per-dispute minimum, because many Indian disputes are small-ticket and a percentage of ₹500 does not cover the cost.
- *Large merchants:* a volume plan with a lower percentage.

Check unit economics first (Chapter 6, Unit economics: cost per task, inference cost, gross margin): (model cost + human QA cost) per contested dispute must sit well below fee × win rate × average disputed amount. If win rates are low in a reason code, don't auto-contest it. The platform's risks with outcome pricing are revenue that swings with win rates, and attribution disputes ("I would have won anyway"). See Chapter 6, Pricing models: per seat, usage-based, outcome-based, bundled, and Chapter 17, Cost-plus, value-based, and competitive pricing.

![The success-fee model: alerts are free, the fee is paid only on won disputes, and a minimum covers small tickets.](diagrams/l21-dispute-success-fee.svg)

### Try it locally: when does a success fee cover its cost?

*(Beyond the notes: reproduced locally. The 25% fee is Chargeflow's published share. The win rate and the cost per dispute are placeholders to show the arithmetic.)*

```python title="lab_p21_success_fee.py"
# Success fee on won disputes: does the fee cover the cost of contesting?
fee_share, win_rate = 0.25, 0.40        # 25% of recovered amount; win rate is a placeholder
cost_draft, cost_human = 4, 15          # rupees per contested dispute: model + human QA (placeholders)
cost = cost_draft + cost_human
for amount in (500, 100):
    expected_fee = fee_share * amount * win_rate
    print(f"dispute Rs {amount}: expected fee Rs {expected_fee:.0f}, cost Rs {cost}, "
          f"margin Rs {expected_fee - cost:+.0f}")
for amount in (500, 100):
    print(f"break-even win rate on Rs {amount}: {cost / (fee_share * amount):.0%}")
```

```output
dispute Rs 500: expected fee Rs 50, cost Rs 19, margin Rs +31
dispute Rs 100: expected fee Rs 10, cost Rs 19, margin Rs -9
break-even win rate on Rs 500: 15%
break-even win rate on Rs 100: 76%
```

On a Rs 500 dispute the expected fee covers the cost comfortably. On a Rs 100 dispute the same 25% fee loses money, and the win rate would need to be about 76% to break even. That is why the recommendation adds a per-dispute minimum for small tickets, and why low-win-rate reason codes should not be auto-contested.

**Metrics.** North Star: net recovered revenue per eligible merchant per month. Supporting: draft acceptance, time to submit, adoption among eligible merchants. Guardrails (Chapter 15, Guardrail and negative metrics): wrong-submission rate, PII exposure incidents (target zero), fraud-loss rate, p95 latency, cost per draft, merchant complaints.

**Risks.**

- *Hallucinated evidence.* An invented delivery date or a misquoted policy in a submission isn't just a wrong answer: it is a false statement to a card network or bank. The model may only cite documents that exist in the merchant's records (each claim links to an attached file), and the merchant approves before submission.
- *Misuse.* Merchants or fraudsters using the assistant to contest legitimate customer claims. Use fraud signals as a separate model, and don't contest disputes where the customer is likely right.
- *Data.* Cross-merchant leakage. Scope retrieval to one merchant's data, keep an audit log, and handle consumer PII under the DPDP Act and RBI data-storage rules (Chapter 9, Regulatory landscape: EU AI Act and sector-specific rules).
- *Cost and latency.* Latency is not critical (disputes take days), so use batch processing and cheaper models. Cost per draft is what matters, and it decides the pricing floor above.

**Launch plan.** Staged rollout to a pilot cohort, expanding by merchant size, with a kill switch (Chapter 10, Staged rollouts and kill switches; Chapter 18, Pilots, MVPs, and phased rollouts).

**Summary.** "I'd build an AI dispute assistant for merchants, because its value is measurable in money recovered. Alerts and checklists are free; drafting is a success fee with a minimum, in line with how Stripe and Chargeflow price, once cost per draft is confirmed to sit well under the expected fee. Every claim in a submission must cite a real document and gets merchant approval. North Star: net recovered revenue per eligible merchant. Guardrails: wrong-submission rate, PII incidents, and cost per draft. Pilot with one merchant segment behind a kill switch."

### Real-world examples

- **Stripe Smart Disputes:** Stripe's AI builds an evidence packet for eligible card disputes and can auto-submit it before the deadline. The fee is charged only on won disputes (a share of the recovered amount). This is outcome-based AI pricing in exactly this domain.
- **Chargeflow:** an automated chargeback-recovery tool priced at 25% of recovered chargebacks, with nothing charged on lost cases.
- **Intercom Fin:** AI support agent priced per resolution (publicly $0.99 per resolved conversation), another outcome-based AI price.
- **GitHub Copilot:** per-seat AI subscription, a contrast to usage-based pricing.

### Practice questions

> [!INTERVIEW] Outcome-based pricing is the norm for dispute tools. What are its risks for the platform, and when would a flat per-dispute fee be better?
> *(Beyond the notes: a starting point.)* Revenue swings with win rates, and attribution is hard ("I would have won anyway"). A flat fee is better when win rates are low or unpredictable, because the platform is paid for the work either way.

> [!INTERVIEW] What unit economics would you need to see before setting the per-dispute fee?
> **Outline:** cost per draft (tokens, infrastructure, review time) against expected recovered value per dispute and the share of disputes where the assistant contributes.

> [!INTERVIEW] How would you respond to a spike in wrong submissions?
> *(Beyond the notes: a starting point.)* Pause auto-drafting behind the kill switch, check which reason codes and merchants are affected, review the submissions already sent, and fix the evidence retrieval before resuming.

*Related:* Chapter 24 (AI Case Bank, this chapter), Chapter 6 (Build vs buy vs API access), Chapter 17 (Monetization models: subscription, freemium, ads, take rate, razor-and-blade, bundling; Running pricing experiments), Chapter 9 (Privacy, consent, and data retention; Regulatory landscape).

## 24.6 Build a support copilot for a logistics company

> Build for the agent first, keep a human in the loop for every consequential action, and expand autonomy only as acceptance and accuracy data justify it.

### Model answer

**Clarify.** Ask:

- *Who uses it?* Internal support agents, or customers directly? Assume internal agents at a B2B logistics firm handling tracking, delays, damage claims and rebooking.
- *What is the problem today?* Slow handling time, inconsistent answers, or agent attrition? Assume average handling time is high because agents hop between systems.
- *Scale and channels?* Tickets per day, chat vs email vs phone, and languages (English, Hindi and regional languages for Indian shippers).
- *Systems and data?* Transport management, warehouse, ticketing, a policy wiki. How fresh is tracking data, and is there an API?

Goal: faster resolution with customer satisfaction held steady.

**Users and segments.** Frontline agents (high volume, time pressure); team leads (quality and coaching); shippers, who are customers and out of scope for the MVP.

**Pain points.** Agents switch across four or five systems to answer one question; policy lookups are slow and inconsistent; damage-claim intake needs repeated information from emails and photos.

**Solutions.**

1. Single shipment summary pulling live status and history.
2. Suggested replies grounded in policy documents, with the policy clause cited.
3. Claim intake auto-filled from emails and photos, for agent review.
4. Suggested actions such as rebooking, which the agent confirms before execution.

**Prioritization.** Summary and suggested replies first, because the agent stays in control and the risk is low. Claim auto-fill second. Autonomous actions last, after acceptance and accuracy data justify them (Chapter 5, Agents and tool use; Chapter 7, Human-in-the-loop design).

**Architecture, briefly.** Retrieval over policy documents for answers (Chapter 5, RAG, fine-tuning, and embeddings); live API calls for shipment status, because stale tracking data is a common failure.

![The copilot flow: live facts and cited policy feed a draft, the agent confirms, and autonomy grows one action type at a time.](diagrams/l21-support-copilot-flow.svg)

**Metrics.** North Star: resolved tickets per agent hour, held at constant CSAT. Supporting: suggestion acceptance rate, edit distance on accepted suggestions, first-contact resolution, escalation rate. Guardrails (Chapter 15, Guardrail and negative metrics): wrong-action rate (for example, incorrect rebookings), CSAT, policy-citation accuracy, p95 latency in live chat, data-access violations, cost per conversation.

**Risks and mitigations.**

- *Hallucinated facts.* An invented ETA or a misquoted liability clause leads to a wrong refund. Status always comes from a live API call, never from the model's text. Policy answers cite the clause, and if retrieval confidence is low, the copilot says "no matching policy found" instead of guessing (Chapter 7, Handling hallucinations, errors, and recovery paths).
- *Wrong actions.* Rebooking or refunds need agent confirmation, with action logs and easy undo. Autonomy expands per action type only after the wrong-action rate stays low for weeks.
- *Latency.* In live chat, a suggestion that arrives after the agent has typed is useless. Aim for a draft in under 2-3 seconds, streamed, and precompute the shipment summary when the ticket opens.
- *Cost.* Price per ticket, not per seat: cost per conversation must stay below the agent time saved (a minute of agent time costs more than a typical LLM call, but long email threads and photos can get expensive). Use a small model for classification and summaries, a larger one only for complex claims.
- *People.* Agents over-trusting suggestions (watch accept-without-edit rates and audit quality), deskilling, and low adoption if it slows them down. Co-design with team leads.
- *Integration.* Legacy systems may lack APIs. Start with the 2-3 systems behind most tickets.

**Rollout.** Pilot with one team and one ticket type (tracking queries), compare handling time and CSAT against a control team, then add claims, then actions (Chapter 10, Staged rollouts and kill switches).

**Summary.** "I'd build for agents first, not customers. A live shipment summary plus policy-grounded reply drafts with citations, then claim auto-fill, then confirmed actions. North Star: resolved tickets per agent hour at constant CSAT. Guardrails: wrong-action rate, citation accuracy, p95 suggestion latency and cost per ticket. Facts come from live systems, never from the model's memory, and autonomy grows one action type at a time as the data earns it."

### Real-world examples

- **Intercom Fin:** AI agent grounded in company help content, a reference design for resolving support questions with citations.
- **Zendesk AI (agent copilot):** Zendesk's AI suite gives agents suggested replies, ticket summaries and next-step suggestions inside the agent workspace. It is the agent-first pattern this answer recommends.
- **Salesforce Service Cloud (Einstein, now Agentforce):** generates draft service replies grounded in knowledge articles and CRM data for the agent to review, with Agentforce extending to autonomous agents. This shows the copilot-to-agent autonomy ladder (Chapter 6, Copilot vs automation vs autonomous agent).

### Practice questions

> [!INTERVIEW] Why start with suggested replies rather than automated responses?
> *(Beyond the notes: a starting point.)* The agent stays in control and reads every reply before it leaves, so a wrong suggestion costs little and the team learns where the copilot fails.

> [!INTERVIEW] How would you detect that agents are over-trusting suggestions?
> **Outline:** watch acceptance without edits, check whether quality audits of accepted replies fall, and sample for mistakes that agents did not catch.

> [!INTERVIEW] What must be true before you let the copilot rebook shipments on its own?
> *(Beyond the notes: a starting point.)* The wrong-action rate for rebooking stays low for weeks, the action has an undo, every action is logged, and the team has a kill switch for that action type alone.

*Related:* Chapter 24 (AI Case Bank, this chapter), Chapter 7 (User control, transparency, and confidence signals), Chapter 6 (Copilot vs automation vs autonomous agent), Chapter 12 (Adapting CIRCLES for AI features), Chapter 8 (Online metrics: task success, acceptance and edit rate, retention of AI users), Chapter 11 (Jobs-to-be-done).

## 24.7 Should a food delivery app add an AI meal planner

> A "should we" question needs a decision framework and a clear recommendation. Here the answer is a scoped yes, because weekly planning is low-frequency and dinner decisions are high-frequency.

### Model answer

**Clarify.** Ask:

- *Which app and market?* Assume a Swiggy/Zomato-style app in Indian metros.
- *Why now? What is the goal?* Order frequency, AOV, retention, or a response to a competitor? Assume frequency and retention.
- *What does "meal planner" mean?* A weekly plan the user commits to, a nightly suggestion engine, or a health-goal coach? They have very different frequency and risk.
- *Constraints?* Restaurant menus rarely carry verified nutrition data, items go out of stock, and health claims carry regulatory and liability risk.

**Decision framework.** Evaluate user need, business fit, feasibility and risk. Each option gets a score.

**Users and segments.** Office workers who want a weekly healthy plan (low frequency); families with dietary constraints; fitness-focused users; and, most importantly, users stuck on the nightly "what do I order" decision (high frequency).

**Pain points.** Decision fatigue at dinner; repeated orders from the same few restaurants; dietary restrictions that search does not handle well.

**Options.**

| Option | Value | Effort | Risk |
|---|---|---|---|
| Full weekly meal planner | High for few users | High | High (nutrition claims, plan adherence) |
| Dinner suggestions in the home feed and cart | Medium-high, daily use | Low-medium | Low-medium |
| Diet-filtered search and recommendations | Medium | Low | Low |

**Recommendation.** Go with the dinner-suggestions option as a pilot, and add diet filters. Defer the full weekly planner until the pilot shows repeat planning behaviour. Score with value versus effort (Chapter 14, Value vs effort).

**Metrics.** North Star: orders per active user per month. Supporting: suggestion-to-order conversion, average order value, D28 retention for pilot users. Guardrails (Chapter 15, Guardrail and negative metrics): allergen or diet-label error rate (target zero), nutrition claim accuracy, restaurant availability errors (suggesting items that are out of stock), cost per suggestion, and cannibalisation of existing high-margin orders.

**Is it actually an AI problem?** Most of the value is ranking (what this user will order tonight), which the recommendation system already does (Chapter 5, Computer vision, speech, and recommendation systems). Generative AI adds value in two places: understanding free-text intent ("light, high-protein, under ₹300, no onion") and explaining why a dish fits. Keep the LLM to those jobs and the cost per session stays small. Precompute suggestions before peak hours so the home feed loads instantly, and generate only on explicit queries.

**Risks.**

- *Hallucinated nutrition or allergen info.* The model must never infer that a dish is "nut-free" or "high protein" from its name. Show only restaurant-supplied or lab-verified data, label estimates as estimates, and keep allergen claims out of scope at launch (Chapter 7, Handling hallucinations, errors, and recovery paths).
- *Supply mismatch.* Suggesting items that are out of stock or from closed restaurants. Filter on live availability.
- *Cannibalisation.* Suggestions shifting orders to lower-margin restaurants without raising frequency. Measure with a holdout.
- *Trust and privacy.* One bad suggestion erodes trust, and inferring health conditions from orders is sensitive data under the DPDP Act, so make health goals opt-in.

**Kill criteria.** Stop the pilot if suggestion-to-order conversion stays flat for six weeks, or if guardrail incidents occur.

**Summary.** "Conditional yes. Don't start with a weekly planner: it's low-frequency, high-commitment, and depends on nutrition data we don't have. Start with AI-assisted dinner suggestions and free-text diet search on top of the existing recommender, piloted with a holdout. Success is orders per active user versus holdout. Guardrails: zero unverified health or allergen claims, out-of-stock suggestion rate, and margin per order. If pilot users come back to plan repeatedly, build the planner, starting with users who opt in to health goals."

### Real-world examples

- **Zomato Healthy Mode (September 2025):** launched first in Gurugram. It gives dishes a "Healthy Score" (Low to Super) based on protein, complex carbs, fibre and micronutrients, using AI plus restaurant-supplied data. A follow-on, Healthy Subscriptions, lets users pre-schedule meals from high-scoring dishes. This is the planner idea arriving in stages, after the scoring layer exists.
- **Swiggy High Protein category:** a curated, filter-style answer to the same need, with no generative AI required. This is the "diet-filtered search" option in the table.
- **HelloFresh:** meal-kit subscription with weekly planning, a contrast on frequency and commitment.

### Practice questions

> [!INTERVIEW] Why is the weekly planner a weaker first bet than dinner suggestions?
> *(Beyond the notes: a starting point.)* The weekly planner is used once a week at most, needs a commitment, and depends on nutrition data the restaurants do not supply. Dinner suggestions are used nightly and reuse the recommender.

> [!INTERVIEW] How would you test cannibalisation?
> **Outline:** run a holdout on suggestions and compare total order value per user against the control, not just the suggested orders.

> [!INTERVIEW] What would make you reject the whole idea?
> *(Beyond the notes: a starting point.)* A pilot that cannot beat the holdout on orders per user, guardrail incidents that do not stop, or a margin per order that falls after the diet filters.

*Related:* Chapter 24 (AI Case Bank, this chapter), Chapter 14 (Choosing and defending a framework), Chapter 6 (Defensibility: proprietary data, distribution, workflow integration, switching costs), Chapter 18 (Pilots, MVPs, and phased rollouts), Chapter 11 (User journeys and the 5Es), Chapter 17 (Running pricing experiments).

## 24.8 An AI feature is cannibalising the core product

> First decide whether cannibalisation is bad. It is only a problem when the shift costs revenue or margin, and the fix depends on where the value moves.

### Model answer

**Clarify.** Ask:

- *Which product and which AI feature?* Assume a concrete one to keep the answer grounded: an ed-tech app whose AI tutor answers questions instantly, and paid live-doubt sessions with human experts are falling.
- *What exactly is being cannibalised?* A paid action, a high-margin action, or just engagement?
- *How is each monetised, and what does each cost to serve?* AI answers have inference cost; human sessions have expert cost.
- *How big and how fast is the shift?* And is it the same users moving, or different users?

**Define the problem.** Three cases:

1. Users move to a cheaper or free substitute: revenue loss. This is a problem.
2. Users move to a higher-value action inside the product: a win, even if the old action declines.
3. Engagement moves but revenue does not: a monetisation gap to fix.

**Measure.** Estimate the cannibalisation rate: the share of AI-feature users who would otherwise have done the core action. Use a holdout experiment where possible (Chapter 17, Running pricing experiments). Segment by user type and by task. Check whether the shift lands on paid or free actions.

**Options.**

1. Redesign the AI to hand off into the core flow, showing an answer plus a call to the paid or core feature.
2. Gate the AI behind the core subscription, or bundle it.
3. Price the AI as a premium or usage-based tier.
4. Differentiate: let the AI do what the core cannot.
5. Accept the shift and reposition the core around what the AI cannot do.

Use the moat lens: which options build defensibility rather than just protecting current revenue (Chapter 6, Defensibility; Chapter 19, Competitive analysis and moats). Compare copilot, automation and agent designs, since each changes how much the core is bypassed (Chapter 6, Copilot vs automation vs autonomous agent).

![The decision matrix: which cases are a problem, which are a win, and the margin maths that decides between them.](diagrams/l21-cannibalisation-matrix.svg)

**Do the margin maths, not just the revenue maths.** In the example, a human session might earn ₹200 and cost ₹120 in expert time, while an AI answer earns nothing directly but costs ₹1-3 in inference. If AI users retain better and convert to the annual plan more often, the shift can raise contribution margin even as session revenue falls. Model it per user over a full cycle (Chapter 6, Unit economics: cost per task, inference cost, gross margin).

### Try it locally: what one substituted session costs

*(Beyond the notes: reproduced locally with the example numbers from the chapter. The AI cost is the chapter's range of ₹1 to ₹3.)*

```python title="lab_p21_margin_shift.py"
# One human session replaced by one free AI answer: what happens to margin?
session_price, session_cost = 200, 120        # rupees, from the example
session_margin = session_price - session_cost
for ai_cost in (1, 2, 3):                     # rupees of inference per AI answer
    lost = session_margin + ai_cost           # the AI answer earns nothing directly
    print(f"AI answer costs Rs {ai_cost}: each substituted session loses Rs {lost} of margin")
print(f"so an AI user must bring back about Rs {session_margin + 1} to Rs {session_margin + 3}")
print("of margin per substitution, through retention or the annual plan, to break even")
```

```output
AI answer costs Rs 1: each substituted session loses Rs 81 of margin
AI answer costs Rs 2: each substituted session loses Rs 82 of margin
AI answer costs Rs 3: each substituted session loses Rs 83 of margin
so an AI user must bring back about Rs 81 to Rs 83
of margin per substitution, through retention or the annual plan, to break even
```

The session's margin of Rs 80 is lost the moment the user moves, and the AI answer adds its own cost on top. The shift only pays if those users come back with more margin than that, which is why the chapter asks for a full-cycle view and not a single-week revenue number.

**Recommendation for the example.** Option 1 plus option 3. The AI tutor handles quick doubts free up to a cap, then offers "talk to an expert" when the question is complex or the student is stuck after two AI attempts. Unlimited AI goes into the premium plan. This keeps the AI where it is cheap and good, and routes high-value moments to the paid core.

**Metrics.** North Star: contribution margin per user across core and AI together (not core revenue alone). Supporting: core action rate, AI-to-core handoff conversion, retention of the combined product, inference cost per active user. Guardrails: AI answer quality (expert-rated accuracy, since a cheap wrong answer that cannibalises a correct paid one is the worst outcome), overall engagement and NPS (so gating does not hide frustration), and p95 latency.

**Risks.** Over-correcting kills a feature that is building real strategic value. Internal politics can cause a team to protect the core metric. Not cannibalising yourself leaves the market to a competitor who will.

**Summary.** "Cannibalisation is only bad if it lowers combined margin or retention. I'd measure the true substitution rate with a holdout, model contribution margin per user including inference cost, and then redesign the AI to hand off to the paid core at high-value moments, with unlimited AI in the premium tier. Judge it on combined margin and retention, guarded by AI answer quality, because if we don't cannibalise ourselves, a competitor will."

### Real-world examples

- **Stack Overflow after ChatGPT (2023):** new-question volume fell sharply after ChatGPT launched, a widely cited case of substitution by an outside AI tool. Its responses included its own AI features (OverflowAI) and licensing its data to AI companies, which is option 5 (reposition around what AI can't replace: the human-verified corpus).
- **Chegg (2023 onward):** in May 2023 Chegg said ChatGPT was hurting new-subscriber growth, and its stock fell by about half in a day. It launched its own AI product (Cheggmate, with OpenAI), which is the "cannibalise yourself before someone else does" logic, though it struggled to win the shift back.
- **Google Search AI Overviews (2024 onward):** AI summaries answer some queries on the results page, reducing clicks to the links and ads that pay the bills. Google keeps links and ads inside the Overviews, which is option 1 (hand off to the core within the AI answer).

### Practice questions

> [!INTERVIEW] What would make cannibalisation good for the business?
> *(Beyond the notes: a starting point.)* The combined contribution margin per user goes up, or retention rises enough to pay back the margin lost per substituted session, as the run block above shows.

> [!INTERVIEW] How would you run the holdout?
> **Outline:** randomise users into exposed and holdout groups, track core action rate and total revenue over a full purchase cycle, not just a week.

> [!INTERVIEW] Which option would you pick first, and why?
> *(Beyond the notes: a starting point.)* Option 1, the handoff from the AI answer into the paid core. It keeps the cheap AI in place, sends the high-value moments to the paid action, and needs no new pricing decision before the data arrives.

*Related:* Chapter 24 (AI Case Bank, this chapter), Chapter 17 (Monetization models; Running pricing experiments), Chapter 19 (SWOT and the Five Cs; Porter's Five Forces; Competitive analysis and moats), Chapter 20 (Theme-based roadmaps and OKRs), Chapter 15 (Metric trees and diagnosing metric movement).

## Beyond the notes: the eval and kill-criteria checklist

Most AI cases end the same way: the candidate names an eval, a failure mode and a stop rule. A short checklist to say out loud:

- **Golden set first.** A labelled set of real or realistic inputs, graded against the rubric, run before every model, prompt or data change.
- **Calibrate any LLM-as-judge against human grades.** Check agreement on a sample before trusting the judge at scale.
- **Property checks that must never break.** Valid format, no PII, length limits, no unverified claims. These are pass or fail, not rates.
- **Shadow or holdout before full launch.** Run the feature, log its decisions, and compare with the current path.
- **A kill criterion with a number.** Name the metric and the level that stops the feature, and who can pull the switch.

## Beyond the notes: pitfalls in AI cases

- **Opening with features.** The chapter's model answers all scope first. A feature list with no user and no job-to-be-done loses the interviewer by minute three.
- **Quoting a single accuracy number.** Ask which slice, which cost of error and which baseline, as in Chapter 4.
- **A North Star on usage.** Sessions, queries and questions answered measure activity. Put the North Star on the outcome the user came for.
- **Forgetting the guardrail veto.** A guardrail that breaches stops the launch, even when the headline metric improved.
- **Treating escalation as failure.** A designed handoff to a person is part of the product, as the Klarna case shows.

## Beyond the notes: interview corner

- **"Which AI case should you practise first?"** The one closest to a product you use. The eight cases share one skeleton, so the second and third cases come faster.
- **"How do you explain the success fee?"** The platform earns only when the merchant wins money, so the incentives line up with the user. The risk is revenue that moves with win rates, so you price a minimum and check the unit economics first.
- **"Why not let the copilot act on its own?"** Consequential actions need a human confirmation until the wrong-action rate has stayed low for weeks. Autonomy then grows one action type at a time.
- **"How would you know a cannibalisation is a win?"** Compare combined contribution margin with a holdout over a full purchase cycle. Core revenue alone can fall while the business improves.

## Revision cheat-sheet

![Chapter 24 on one page: the eight-step answer skeleton, with guardrails as a veto on the metrics step.](diagrams/l21-big-picture.svg)

- **24.1 Doubt solver (exam prep).** Scope to one exam. Grounded, cited answers. Attempt first. North Star: mock-score gain over four weeks. Guardrail: expert-audited error rate under 1%.
- **24.2 Navigation app.** Phone-first planners before in-drive help. Reuse existing review data. In-drive is voice-only, with a one-word confirmation before any route change.
- **24.3 Resume reviewer.** North Star: callbacks per reviewed resume within 30 days, compared by cohort. Fabrication and bias are zero-tolerance guardrails. Calibrate the judge on recruiter grades.
- **24.4 Hallucination complaints.** Verify the rate per 1,000 conversations. Segment by intent and version. Reproduce, then fix the matching cause. Kill switch first.
- **24.5 Payments dispute assistant.** Free alerts, success fee on won disputes, a minimum for small tickets. Unit economics first. Every claim cites a real document.
- **24.6 Logistics copilot.** Agent first. Live facts, never memory. Confirmed actions, one type at a time. North Star: resolved tickets per agent hour at constant CSAT.
- **24.7 Meal planner.** A conditional yes: dinner suggestions as a holdout pilot, weekly planner later. North Star: orders per active user per month.
- **24.8 Cannibalisation.** Only a problem if combined margin or retention falls. Measure with a holdout. Hand off to the paid core at high-value moments.
- **Beyond the notes:** a per-case North Star and hard guardrail (table below); the threshold and the cost of each error; percentiles for latency.

| Case | North Star | The guardrail that vetoes |
|---|---|---|
| 24.1 Study assistant | Mock-score gain, four weeks | Factual error rate under 1% |
| 24.2 Navigation | Navigation starts per AI session | Screen use while the vehicle moves |
| 24.3 Resume reviewer | Interview callbacks within 30 days | Invented claims (zero tolerance) |
| 24.4 Hallucinations | Hallucination rate on a reviewed sample | Refusal rate (over-correction) |
| 24.5 Dispute assistant | Net recovered revenue per merchant | Wrong-submission rate |
| 24.6 Logistics copilot | Resolved tickets per agent hour | Wrong-action rate |
| 24.7 Meal planner | Orders per active user per month | Allergen or diet-label errors |
| 24.8 Cannibalisation | Contribution margin per user | AI answer quality |

## Self-test

<details class="quiz"><summary>Why does a PM scope every AI case to one user and one job before proposing features?

Because a feature list with no user or job cannot be prioritised or measured. One user and one job set the North Star, the guardrails and the first release.

</details>

<details class="quiz"><summary>Why should the North Star of an AI product sit on the outcome, not on usage?

Usage measures activity. The outcome, such as mock-score gain or interview callbacks, measures whether the product helped the user get what they came for.

</details>

<details class="quiz"><summary>Why are review summaries shipped before conversational search in the navigation case?

They reuse existing review data, run at high frequency, carry low risk, and can be precomputed and cached per place, so the cost stays low.

</details>

<details class="quiz"><summary>What must the in-drive assistant do before any route change?

Ask for a one-word confirmation. Its answers are brief and voice-only, so the driver's attention stays on the road.

</details>

<details class="quiz"><summary>Why convert hallucination complaints to a rate per 1,000 conversations before anything else?

Counts rise with volume. A doubling of complaints with a doubling of conversations is no change in quality, so only the rate shows whether the bot got worse.

</details>

<details class="quiz"><summary>What are the three cases of cannibalisation, and which one is a problem?

Users move to a cheaper or free substitute (a revenue loss, the problem); users move to a higher-value action (a win); engagement moves but revenue does not (a monetisation gap to fix).

</details>

<details class="quiz"><summary>Why does a success fee need a per-dispute minimum for small tickets?

A percentage of a small amount may not cover the cost of drafting and review. In the chapter's example, a percentage of Rs 500 does not cover the cost of a small-ticket dispute.

</details>

<details class="quiz"><summary>Why should the copilot's live shipment status come from an API, not the model's text?

Stale tracking data is a common failure, and an invented ETA leads to a wrong answer. Live facts come from the system of record, and the model only phrases them.

</details>

<details class="quiz"><summary>Why is the meal planner's first version a dinner suggestion, not a weekly plan?

Dinner decisions are high-frequency and reuse the recommender. A weekly planner is low-frequency, high-commitment, and depends on nutrition data the app does not have.

</details>

<details class="quiz"><summary>(Beyond the notes) What is the rule for judging a cannibalisation with a holdout?

Compare combined contribution margin and retention over a full purchase cycle. Core revenue alone can fall while the business improves.

</details>

<details class="quiz"><summary>(Beyond the notes) Why should the guardrails act as a veto rather than a trade-off?

A rise in a headline metric does not excuse a breach of a zero-tolerance guardrail, such as invented claims in a resume. Fixing the breach comes first.

</details>


# Chapter 25 · Practice Protocol

<!-- lecture n="22" label="25" short="Practice protocol" status="done" kind="practice" -->

## At a glance

| Question | Short answer |
|---|---|
| What is the solo drill? | A timed, 20-minute run through one case with a fixed clock. You cannot polish one section. |
| What does each phase need on paper? | A named output: a case type, three clarifying questions, a skeleton, a metric, two risks. |
| What if you have only 10 minutes? | A quick drill with six phases, for daily reps or a lateral prompt. |
| How is a peer mock run? | 35 minutes per candidate: 20 for the answer, 5 for follow-ups, 10 for feedback. |
| What is the rubric? | Eight criteria, each scored 1 to 5 with anchors at 1, 3 and 5. |
| What is the out-of-total for a case? | 35 for non-AI cases (seven criteria), 40 for AI cases (eight criteria). |
| What is the bar? | 60%: 21 out of 35, or 24 out of 40. Also: no criterion at 1. |
| What does "interview-ready" mean? | 4 or more on every criterion, across three consecutive mocks of different case types. |
| How often do you practise? | A weekly cadence: drill, review, peer mock, re-attempt. |
| Where does improvement show? | On a repeat of the same case a week later, not on a good first try. |

> [!NOTE] Where this comes from
> The protocol is built from the converted source notes the vault cites: a topic checklist, a guide to using the course folder, a list of past PM interview questions (FAQs for PM Roles), the Sigma PM Casebook (2023-2024) and the Sigma PM Interview Experiences (2023-24). The vault's further-reading list names *Blogs & Newsletters* and *Product Teardowns*. No links are kept here.

## The big picture

The case material only helps if you can perform it under time pressure. This chapter turns it into practice: a timed solo drill, peer mocks scored on one shared rubric, and a recording-and-review routine that tracks progress across weeks. The checklist and resource guide set what to cover and in what order.

- **25.1 Timed solo drill.** A minute-by-minute 20-minute drill, adapted per case type, plus a 10-minute variant and a follow-up drill.
- **25.2 Peer mock interviews and a feedback rubric.** The three-role mock format and an eight-criterion rubric scored 1 to 5.
- **25.3 Recording and reviewing your own answers.** Record, review within 24 hours, keep an error log, and re-attempt after a week.

## Key takeaways

- Use a fixed clock: a timed drill teaches you to cover every phase, not just the ones you like.
- Score every mock with the same rubric so you can see progress over weeks.
- Practise the lowest-scoring criterion on purpose, rather than the case you enjoy most.
- Record and review within 24 hours; memory of your reasoning fades fast.
- Re-attempt a case a week later; improvement on a repeat matters more than a good first try.

> [!SIR] From the source notes
> Use a fixed clock: a timed drill teaches you to cover every phase, not just the ones you like.

## 25.1 Timed solo drill (20 minutes)

> A fixed clock forces structure: you cannot polish one section, so you learn to cover the whole case in the time an interviewer gives you.

### Concept

Practise alone with a timer and one case prompt. Use cases from Chapter 24 (AI Case Bank) or the Part V case types. The checklist covers the topic spread to rotate through: guesstimates, product design, pricing, metrics, strategy, situational questions, and AI topics (Chapter 22, Product design cases; Metrics cases; Pricing cases; Strategy and market entry cases).

**Setup.** One phone timer, one sheet of paper, a pen. Read the prompt once, then start the clock. Do not pause it. Speak your answer out loud as you write.

**Minute-by-minute drill (20:00 total).**

| Clock | Phase | What you should have on paper |
|---|---|---|
| 0:00-1:00 | Read, identify the case type, restate | Case type (Chapter 22, Case Types and How to Approach Each) and one sentence restating the goal |
| 1:00-3:00 | Clarify | Three questions with the assumed answer next to each (alone, you answer them yourself) |
| 3:00-4:00 | Structure | The 5-6 step skeleton for this case type, written as a numbered list and said aloud |
| 4:00-10:00 | Core analysis | Design or improvement: segments, chosen persona, journey and pains. RCA: scope, external checks, journey with a metric per step. Pricing: buyer, WTP ceiling, cost floor, strategy. Metrics: journey or funnel with a metric per stage |
| 10:00-14:00 | Answer | Design or improvement: 3 ideas, prioritised (Chapter 14, Value vs effort or RICE), one detailed. RCA: ranked hypotheses, the one data cut that confirms the top one, the fix. Pricing: a number or range, with reasoning |
| 14:00-16:00 | Metrics | One North Star, two supporting metrics, one guardrail (RCA: the metric to watch after the fix) |
| 16:00-18:00 | Risks | Two risks with a mitigation each. AI cases: hallucination, cost per query, latency, and the eval you would run |
| 18:00-19:00 | Summary | Spoken aloud in 30-45 seconds: user, problem, answer, metric, top risk |
| 19:00-20:00 | Self-check | Score yourself on the Chapter 25.2 criteria and write down the weakest one |

![The 20-minute drill as one bar: nine phases back to back, with the core analysis taking the longest slot.](diagrams/l22-timer-bar.svg)

**Rules.**

- At 20:00 you stop, even if you are mid-sentence.
- If you are short on time at a checkpoint, skip detail, never skip the next phase.
- For AI cases, spend 30 seconds of the risks slot on evals and data needs (Chapter 20, AI PRD additions: eval criteria, failure modes, data requirements).

**Variants.**

- *10-minute quick drill* (for daily reps or lateral prompts): 0:00-1:00 restate, 1:00-2:00 clarify, 2:00-3:00 structure, 3:00-7:00 core analysis and answer, 7:00-9:00 metrics, 9:00-10:00 summary.
- *Follow-up drill:* real rounds keep going after your summary. Interviewers ask you to quantify ("how often do people use Google Photos?"), defend a trade-off, or "what would you do if the A/B test showed X?". After each drill, write three follow-ups you would ask yourself and answer one in 2 minutes.

![The two variants: a 10-minute quick drill, and the follow-up loop that runs after the summary.](diagrams/l22-variants.svg)

**Picking prompts.** Rotate case types so you never repeat a type two days in a row. Good sources: the prompts in each 22.x note, the cases in Chapter 23 (Sigma casebook solutions) and Chapter 23 (XLRI casebook solutions) (attempt first, then compare with the condensed solution), and the Chapter 24 (AI Case Bank).

### Try it locally: is the timetable right?

*(Beyond the notes: reproduced locally with the standard library. It checks that each drill's phases run back to back and end at the stated time, so no minute is lost or counted twice.)*

```python title="lab_p22_timetable.py"
# The drill timetables must run back to back and end at the stated time.
drill20 = [("read and restate", 0, 1), ("clarify", 1, 3), ("structure", 3, 4),
           ("core analysis", 4, 10), ("answer", 10, 14), ("metrics", 14, 16),
           ("risks", 16, 18), ("summary", 18, 19), ("self-check", 19, 20)]
quick10 = [("restate", 0, 1), ("clarify", 1, 2), ("structure", 2, 3),
           ("core analysis and answer", 3, 7), ("metrics", 7, 9), ("summary", 9, 10)]

def check(name, phases, total):
    gaps = [a[0] + " -> " + b[0] for a, b in zip(phases, phases[1:]) if a[2] != b[1]]
    minutes = sum(end - start for _, start, end in phases)
    ok = phases[0][1] == 0 and phases[-1][2] == total and not gaps and minutes == total
    print(f"{name}: {len(phases)} phases, {minutes} minutes, gaps: {gaps or 'none'}, ok: {ok}")

check("20-minute drill", drill20, 20)
check("10-minute drill", quick10, 10)
longest = max(drill20, key=lambda p: p[2] - p[1])
print(f"longest slot in the 20-minute drill: {longest[0]} ({longest[2] - longest[1]} min)")
```

```output
20-minute drill: 9 phases, 20 minutes, gaps: none, ok: True
10-minute drill: 6 phases, 10 minutes, gaps: none, ok: True
longest slot in the 20-minute drill: core analysis (6 min)
```

Both timetables are contiguous and add up to their totals. The core analysis gets the longest slot, which is where most of the case is built, so it is the slot to protect when the clock is short.

### Real-world examples

- **How long real rounds run:** the interview reports in Chapter 23 (Annotated answers from interview experiences) range from short single-question rounds (Just Dial's one-round RCA) to a 90-minute case round (Flipkart's Swiggy table-booking case). The 20-minute drill trains the core answer; the follow-up drill trains the rest.
- **Interviewers push for numbers:** a Google candidate in the Sigma 2023-24 reports notes being asked to quantify at every stage and to define each metric precisely. That is why the drill puts a number or a defined metric on paper in every phase.
- **The source folder's own advice:** solve casebook cases yourself, then mix in the interview-experience book "to know about the D day", which is the attempt-then-compare loop above.

### Practice questions

> [!INTERVIEW] Where do most candidates lose time in the first five minutes?
> **Outline:** asking too many clarifying questions, or starting a framework before the goal is agreed.

> [!INTERVIEW] What do you do when you finish the summary with two minutes left?
> **Outline:** use them to quantify one estimate or stress-test your top risk.

*Related:* Chapter 25 (Practice Protocol, this chapter), Chapter 25.2 (Peer mock interviews and a feedback rubric), Chapter 25.3 (Recording and reviewing your own answers), Chapter 22 (Brainstorming and lateral questions), Chapter 24 (AI Case Bank), Chapter 23 (Sigma casebook solutions).

## 25.2 Peer mock interviews and a feedback rubric

> A peer mock with a shared rubric gives you feedback you can act on, and the same rubric lets you measure progress week to week.

### Concept

**Format (35 minutes per candidate).** 20 minutes for the candidate's answer (the structure from Chapter 25.1), 5 minutes of interviewer follow-ups, and 10 minutes of feedback. Three roles rotate: interviewer (reads the prompt, answers clarifying questions from a prepared fact sheet, asks follow-ups, does not coach), candidate, and observer (scores with the rubric and notes the clock time at each phase). With only two people, the interviewer also scores, right after the case.

![The mock loop: three roles rotate through 35 minutes, and the observer scores with the rubric.](diagrams/l22-mock-loop.svg)

**Interviewer prep (5 minutes before).** Pick a casebook case from Chapter 23 (Sigma casebook solutions) or Chapter 23 (XLRI casebook solutions) and play the interviewer from the transcript. Facts are revealed only when asked (for example in Uber Drivers: "Hyderabad only", "gradual over 2 months"). This is the casebook's own advice: use the transcripts to set up a case between two people, then discuss and give feedback.

**Question bank.** Draw from the topic checklist: product design (add or cut a feature, customer journey, pain points), pricing, metrics (e-commerce, two-sided markets, mobile apps), strategy (market share, new market entry, monetisation, M&A), and situational questions (prioritisation, handling delays). The FAQs file has past interview questions from real company rounds, which work well as prompts (Chapter 23, Annotated answers from interview experiences).

**Behavioural and background questions.** Include one per session from the FAQs bank: "Why PM?", "Favourite product and what you would improve", "Walk me through past work". Score them with the same rubric, using the communication and structure criteria.

**Feedback rubric.** Score each criterion from 1 to 5 with the anchors below.

| Criterion | 1 (weak) | 3 (adequate) | 5 (strong) |
|---|---|---|---|
| Clarify and scope | Starts answering immediately | Asks some questions, misses the goal | Restates goal, asks 2-3 sharp questions, states assumptions |
| Structure | No framework, jumps around | Framework named, buckets overlap | Clear MECE-style buckets, signposted throughout |
| User and segmentation | One generic user | Two segments, weak pain points | Segments by need, pain points tied to a segment |
| Solution depth | Lists ideas with no link to users | Good ideas, little trade-off | Ideas linked to pain points, trade-offs named, MVP chosen |
| Prioritisation | None, or a framework applied without reasons | Framework applied, reasons thin | Framework justified, one trade-off defended |
| Metrics and guardrails | Vague ("engagement") | North Star plus metrics, no guardrail | North Star, supporting metrics, guardrails, and a measurement method |
| AI judgement (AI cases) | Ignores data, evals or failure modes | Mentions hallucination or privacy | Names evals, failure modes, human-in-loop, and kill criteria |
| Communication and time | Rambles, runs out of time | Mostly clear, time uneven | Concise, spoken summary, sections on time |

![The rubric at a glance: each criterion has an anchor at 1, 3 and 5.](diagrams/l22-rubric-anchors.svg)

**Scoring rules.**

- Score independently, then compare. Give each score with one piece of evidence ("2 on metrics: no guardrail named").
- AI judgement applies only to AI cases. Score non-AI cases out of 35 and AI cases out of 40.
- Below 60% (21/35 or 24/40), or any criterion at 1: the next two sessions focus on the weakest two criteria. Interview-ready means 4+ on every criterion across three consecutive mocks of different case types.
- Feedback order: one thing to keep, then the single most important fix, then everything else. A list of ten fixes changes nothing.
- Track scores in one table (date, case, case type, score per criterion, total) so trends are visible.

![The pass line: 60% of the total, and the two rules that override it.](diagrams/l22-pass-line.svg)

### Try it locally: a rubric scorer

*(Beyond the notes: a small scorer for the rubric above. It turns eight criterion scores into a percentage and a verdict, using the 60% bar, the "any criterion at 1" rule and the 4+ interview-ready check. The sample mocks are made up.)*

```python title="lab_p22_rubric.py"
# Rubric scorer: eight criteria scored 1 to 5. AI judgement counts only for AI cases.
CRITERIA = ["clarify and scope", "structure", "user and segmentation", "solution depth",
            "prioritisation", "metrics and guardrails", "AI judgement", "communication and time"]

def score(scores, ai_case):
    names = CRITERIA if ai_case else [c for c in CRITERIA if c != "AI judgement"]
    total = sum(scores[n] for n in names)
    maximum = 5 * len(names)                       # 40 for AI cases, 35 otherwise
    pct = total / maximum
    weakest = sorted(names, key=lambda n: scores[n])[:2]
    if pct < 0.60 or any(scores[n] == 1 for n in names):
        verdict = "below the bar: next two sessions on " + " and ".join(weakest)
    elif all(scores[n] >= 4 for n in names):
        verdict = "at the bar, 4+ on every criterion (count it toward three mocks)"
    else:
        verdict = "at the bar: practise the lowest criterion next"
    return total, maximum, pct, verdict

# (name, AI case?, scores). The AI score in non-AI mocks is ignored, so it is set to 0.
mocks = [
    ("mock A, product design", False, [4, 3, 3, 2, 3, 2, 0, 4]),
    ("mock B, AI case", True, [3, 4, 4, 4, 3, 3, 2, 4]),
    ("mock C, metrics", False, [5, 4, 4, 3, 4, 1, 0, 4]),
    ("mock D, AI case", True, [4, 4, 4, 4, 4, 4, 4, 4]),
]
ready = []
for name, ai_case, values in mocks:
    total, maximum, pct, verdict = score(dict(zip(CRITERIA, values)), ai_case)
    print(f"{name}: {total}/{maximum} = {pct:.1%}; {verdict}")
    if all(v >= 4 for v in values[:8 if ai_case else 7]):
        ready.append(name)
print("4+ on every criterion:", ", ".join(ready))
```

```output
mock A, product design: 21/35 = 60.0%; at the bar: practise the lowest criterion next
mock B, AI case: 27/40 = 67.5%; at the bar: practise the lowest criterion next
mock C, metrics: 25/35 = 71.4%; below the bar: next two sessions on metrics and guardrails and solution depth
mock D, AI case: 32/40 = 80.0%; at the bar, 4+ on every criterion (count it toward three mocks)
4+ on every criterion: mock D, AI case
```

Mock A sits exactly on the bar: 21 out of 35 is 60%, so it passes, but its two lowest criteria still need work. Mock C scores 71% overall and still counts as below the bar, because one criterion is at 1. That is the rule that stops a strong total hiding a missing guardrail. Only mock D is 4+ everywhere, and one such mock is not interview-ready on its own: the bar needs three consecutive mocks of different case types.

### Real-world examples

- **Sigma casebook, "How to make the most of it":** use the interview transcripts to set up a case between two people (or groups), discuss after solving, give each other feedback, and treat the transcripts as templates for the approach rather than as the solution.
- **Sigma 2023-24 interview reports:** a Disney Hotstar candidate's advice is to "form a case group early and practice". Several candidates name the Sigma casebook as their main preparation resource.
- **What interviewers probe:** the reports in Chapter 23 (Annotated answers from interview experiences) show follow-ups on quantification, metric definitions and "how did you reach that deduction?", which is why the format reserves 5 minutes for follow-ups.

### Practice questions

> [!INTERVIEW] Why should the interviewer not coach during the case?
> **Outline:** coaching hides what the candidate would do alone, so the feedback would not show real weaknesses.

> [!INTERVIEW] How would you use the rubric to set a goal for next week?
> **Outline:** pick the lowest-scoring criterion, practise only that for two sessions, and re-score.

*Related:* Chapter 25 (Practice Protocol, this chapter), Chapter 25.1 (Timed solo drill), Chapter 25.3 (Recording and reviewing your own answers), Chapter 23 (Sigma casebook solutions), Chapter 13 (Favorite product answers that show depth), Chapter 12 (Common mistakes in design answers).

## 25.3 Recording and reviewing your own answers

> You cannot see your own structure while you speak. A recording plus a fixed review routine shows the patterns that peers and timers miss.

### Concept

**Record every drill.** Use a phone voice memo (or video, if you want to check eye contact and pacing). Save the file with the date, case name and score from the rubric in Chapter 25.2.

**Review within 24 hours.** Listen at 1.25x speed. Do not stop to fix every word. Note the moments where you:

- Lost the thread or repeated yourself.
- Stated a number without a basis.
- Skipped metrics or guardrails.
- Ran past a time checkpoint from Chapter 25.1.

**Error log.** Keep one table with these columns: date, case, error type (structure, clarity, depth, metrics, time, AI judgement), what happened, fix. Patterns show up quickly; after five entries, the most common error type is your focus for the next week.

**Re-attempt.** Redo the same case one week later, using only the error log as a checklist. Compare the rubric scores. An improvement on the re-attempt matters more than a good first attempt on a new case.

**Weekly cadence.**

| Day | Activity |
|---|---|
| Mon | Timed drill on a new case from Chapter 24 (AI Case Bank) |
| Tue | Review recording, update error log |
| Thu | Peer mock with rubric scoring (Chapter 25.2) |
| Sat | Re-attempt last Monday's case using only the error log, then compare rubric scores |

![The weekly cycle: a new drill on Monday, review on Tuesday, a peer mock on Thursday, and a re-attempt on Saturday.](diagrams/l22-weekly-cycle.svg)

**Use the vault.** Read the model answer only after your own attempt, then compare what you missed. Keep notes short. The point is to change your next answer, not to build a bigger document.

### Real-world examples

- **Compare against a model answer:** after a recorded attempt at a casebook case, check your recording against the condensed solution in Chapter 23 (Sigma casebook solutions). For example, did you define "active driver" before diagnosing Uber Drivers, and did you find the time-of-day cut?
- **Check metric precision:** the Google Photos report in Chapter 23 (Annotated answers from interview experiences) says interviewers want "active users bounced per hour", not "bounce rate". Every vague metric in your recording is an error-log entry.

### Practice questions

> [!INTERVIEW] Why review within 24 hours rather than at the end of the week?
> **Outline:** memory of what you were thinking fades quickly, and the recording still has the reasoning fresh.

> [!INTERVIEW] What makes an error log more useful than a list of mistakes?
> **Outline:** the fix column turns each error into a rule you apply in the next drill.

*Related:* Chapter 25 (Practice Protocol, this chapter), Chapter 25.1 (Timed solo drill), Chapter 25.2 (Peer mock interviews and a feedback rubric), Chapter 23 (Annotated answers from interview experiences), Chapter 22 (Product improvement cases), Chapter 24 (Diagnose a rise in chatbot hallucination complaints).

## Beyond the notes: a tracker you can build in ten minutes

The vault asks for one table with the date, case, case type and the rubric scores. A spreadsheet with these columns does the job:

| Date | Case | Type | Clarify | Structure | Users | Solution | Priority | Metrics | AI | Comms | Total | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (date) | (case) | (type) | 1-5 | 1-5 | 1-5 | 1-5 | 1-5 | 1-5 | 1-5 or blank | 1-5 | sum | % and bar |

Leave the AI column blank for non-AI cases, so the total is out of 35, not 40. Add a column for the weakest criterion, and read the trend across the last three rows before you choose next week's focus.

## Beyond the notes: pitfalls in the protocol

- **Stopping the clock to think.** The drill is only useful if the clock keeps running. Pausing teaches the wrong habit for a live round.
- **Scoring without evidence.** A score with no reason ("3 on structure") cannot be acted on. Write the one piece of evidence beside each score.
- **Rotating case types too fast.** Every type needs practice. Rotating so you never repeat a type two days in a row keeps the spread even.
- **Reviewing without a fix.** An error log with no fix column is a diary. The fix turns each error into a rule for the next drill.
- **Chasing the total.** A high total can hide a criterion at 1. Read the lowest criterion first.

## Beyond the notes: interview corner

- **"How do you measure your own progress?"** Use one rubric, one table and one repeat case a week later. Compare the total and the weakest criterion, not only the feeling after the session.
- **"What does a strong mock look like?"** Concise, spoken, on time, with a measured guess on every number and a guardrail on every metric. The rubric's 5-anchors describe it.
- **"How do you prepare for a follow-up round?"** Write three follow-ups after each drill and answer one in two minutes. Quantification and defended trade-offs are the usual targets.

## Revision cheat-sheet

![Chapter 25 on one page: drill, record, log, mock, re-attempt, with the pass rule at the centre.](diagrams/l22-big-picture.svg)

- **25.1 Timed solo drill.** Fixed clock, nine phases for 20 minutes: restate, clarify, structure, core analysis, answer, metrics, risks, summary, self-check. The 10-minute quick drill has six phases. The follow-up drill runs after the summary: write three follow-ups, answer one in 2 minutes.
- **25.2 Peer mocks.** 20 minutes for the answer, 5 for follow-ups, 10 for feedback. Three rotating roles: the interviewer does not coach. Eight criteria, 1 to 5, with anchors at 1, 3 and 5. Non-AI cases out of 35, AI cases out of 40. Below 60%, or any criterion at 1: focus the weakest two. Interview-ready: 4+ on every criterion across three consecutive mocks of different types.
- **25.3 Recording and reviewing.** Record every drill, review within 24 hours at 1.25x, keep an error log with a fix for each entry, and re-attempt a week later. The weekly cadence: Mon drill, Tue review, Thu peer mock, Sat re-attempt.
- **Beyond the notes:** a one-row-per-mock tracker; the rubric scorer above; practise the lowest criterion on purpose.

## Self-test

<details class="quiz"><summary>Why does the 20-minute drill use a fixed clock that you do not pause?

Because a fixed clock forces you to cover every phase in the time an interviewer gives you. You cannot polish one section, so you learn the whole case.

</details>

<details class="quiz"><summary>What should be on paper by the end of the clarify phase?

Three questions, each with the assumed answer written next to it. Alone, you answer them yourself.

</details>

<details class="quiz"><summary>What happens at 20:00 in the solo drill?

You stop, even if you are mid-sentence. If you are short on time at a checkpoint, you skip detail, never the next phase.

</details>

<details class="quiz"><summary>What are the three roles in a peer mock, and what does the interviewer not do?

Interviewer, candidate and observer. The interviewer reads the prompt, answers clarifying questions from a fact sheet and asks follow-ups, but does not coach.

</details>

<details class="quiz"><summary>How many points is each case type out of, and why?

Non-AI cases are out of 35 (seven criteria at 5 each). AI cases are out of 40 (eight criteria, including AI judgement). AI judgement applies only to AI cases.

</details>

<details class="quiz"><summary>What is the bar for a passing mock, and what overrides it?

60%: 21 out of 35, or 24 out of 40. A criterion at 1 also triggers the focus on the weakest two criteria, even when the total is above 60%.

</details>

<details class="quiz"><summary>What does "interview-ready" mean in the protocol?

4 or more on every criterion across three consecutive mocks of different case types.

</details>

<details class="quiz"><summary>Why review a recording within 24 hours, and how?

Memory of your reasoning fades fast, while the recording still has it fresh. Listen at 1.25x, and note the moments you lost the thread, stated an unsupported number, skipped metrics or ran past a checkpoint.

</details>

<details class="quiz"><summary>What makes an error log more useful than a list of mistakes?

The fix column. It turns each error into a rule you apply in the next drill.

</details>

<details class="quiz"><summary>(Beyond the notes) What does the rubric scorer print for a total of 21 out of 35?

60.0%, which is exactly on the bar, so the mock passes and the lowest criterion is the next focus. The bar is a floor, not a target.

</details>
