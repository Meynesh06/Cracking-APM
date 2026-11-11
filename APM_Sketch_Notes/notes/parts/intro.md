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
