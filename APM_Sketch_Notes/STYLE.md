# APM Prep Sketch Notes: writing guide for Part pages

Project root: `/Users/deep/Downloads/Product Management/APM_Sketch_Notes`. Toolkit: `/Users/deep/dkfile-toolkit`. Source: **the reviewed APM Prep Vault**, chapters 4-25 of *Crack the APM Role* (Parts II-V, 125 notes), split into **22 pages, one per vault chapter** (see `PLAN.md`). The reader: **a data/AI engineer (Azure Databricks, Microsoft Fabric) preparing for APM / product manager interviews at product companies and Indian campus placements**. They want to learn **without re-opening the vault**. Standing preferences: **every visual is an Excalidraw drawing**; **no video timestamps, no YouTube links and no external URLs** anywhere on the pages.

## 0. This project is built from notes, not a video (read first)

The toolkit was made for video transcripts. Here, wherever this guide says **transcript** or **speaker**, read **your page's vault notes** (`transcripts/raw/pNN.md`, which concatenates the chapter index note and every subsection note, each starting with `<!-- ===== vault note: NAME ===== -->`).

- **Page header:** `# Chapter V · Title` where V is the **vault chapter number** (e.g. `# Chapter 15 · Metrics`), and the comment carries both: `<!-- lecture n="12" label="15" short="..." status="done" kind="..." -->` (n = page number from PLAN.md, label = vault chapter).
- **Zero content loss** means: every concept, framework step, table, real-world example (with its company, year and numbers), practice question and answer outline, and every caveat from every vault note of your chapter appears on the page, in the vault's order (index overview first, then subsection 1, 2, ...). One or more H2s per vault subsection note. Keep the vault's facts exactly; do not invent new facts, figures or dates in the non-Beyond parts.
- **Practice questions from the vault** become quiz cards or `[!INTERVIEW]` callouts with their answer outlines; none are dropped. The Self-test still has 8-12 cards (you may use more if the vault has more questions).
- **Wikilinks** like `[[15.3 HEART]]` become plain text: "Chapter 15 (HEART)". The vault's "Further reading" and "Sources" sections are folded into one short `[!NOTE] Where this comes from` callout per page (source book names only, no URLs).
- `[!SIR]` callouts ("From the source notes") are optional; use them for a crisp one-line rule the vault states.
- **Coverage file** `notes/coverage/lN.md`: a table with one row per vault-note section (e.g. "15.3 HEART · Concept", "15.3 HEART · Real-world examples", "15.3 HEART · Practice questions") → the page heading(s) where it is covered. Every row must have a heading.
- **Beyond the notes** = anything you add: extra frameworks, internals, interview tips, pitfalls. Keep it clearly labelled and factually safe (well-known, stable facts only; no invented statistics).
- **Run blocks are rare.** Only where a calculation proves a point: guesstimate math, RICE/ICE scoring, unit economics, retention or funnel maths, a pricing or A/B test calculation. Plain Python stdlib only (`.venv/bin/python`), no `labhelpers` needed unless useful, short deterministic prints. Pages with nothing to compute have zero run blocks, and that is fine.
- **Depth targets for this project (override section 3):** 300-550 lines of markdown, **6-8 diagrams**, 0-4 run blocks per page. The AI Case Bank and Case Types pages may go to 650 lines.

Reference page to copy mechanics from (voice, callouts, quiz cards, diagram density): `notes/parts/l1.src.md` + `tools/diagrams_l1.py` once the lead has written them; until then the toolkit examples `/Users/deep/dkfile-toolkit/docs/examples/part_example.src.md` + `diagrams_example.py` (a finished Delta Lake page) and `dsa_part_example.src.md` + `dsa_diagrams_example.py` (an algorithms page with step-through tracers). Read one before you start.

## 1. Hard rules (never break)

1. **No video timestamps, no YouTube links, no `@[m:ss]` chips, no `video=` key** in the page comment.
2. **Be exhaustive.** Every point of your transcript must be on the page, in the speaker's order, with their examples, numbers, whiteboard walk-throughs and demo steps. Nothing is dropped because it "seems minor". The reader must never need the notes (section 1b).
3. **Everything not from the notes is labelled "Beyond the notes"**: section titles `## Beyond the notes: ...`, callout titles `Beyond the notes: ...`, `*(Beyond the notes)*` lead-ins, quiz prefix `(Beyond the notes)`, diagram text starting `beyond ·`. Source content is never labelled Beyond. Do a lot of Beyond: internals, configs and their defaults, version differences, pitfalls, how to spot a problem in practice, production tips, interview questions.
4. **Their code, as they wrote it.** Rebuild the code they type from the transcript (auto-transcripts garble names: fix them, list the fixes in `PLAN.md`). Code that cannot run here (a cloud platform, a cluster, a paid service) is shown as an **unrun** block with a title saying where it runs, e.g. ` ```sql title="on Databricks · name.sql" ` or ` ```python title="on Databricks · name.py" nocheck `, never with an output block. Numbers they read off their screen go in prose or a table, attributed to their run.
5. **Every block with an output block is really run** (`tools/check_code.py`) and its output is real. Never invent output, never hand-edit an output block. Fill outputs with `python3 tools/fixout.py notes/parts/lN.src.md --write`, then READ them and check they show what your prose says. Where the local engine differs from theirs, say so plainly in a `Beyond the notes:` callout. Never present a local result as theirs, never fake a feature locally.
6. **Every diagram is a real Excalidraw drawing** built with the Scene API (section 6). No ASCII art, no pasted images, no `text` blocks drawn as pictures.
7. **Do not edit shared tooling** (`tools/*.mjs`, `template.html`, `scene.py`, `dhelp.py`, `shelp.py`, `dlhelp.py`, `check_code.py`, `fixout.py`, `runner.py`, `make_traces.py`, `*.sh`, `package.py`, `lab/*.py` helpers and datasets) or other writers' `diagrams_lN.py` / `lN.src.md`. Need a helper? Define it at the top of your own `diagrams_lN.py` or inside your code block. Found a tooling bug? Report it in your final message; do not fix it.
8. **Do not run `tools/assemble.sh`** (it merges everyone's half-written pages). Use `sh tools/lchk.sh N`.
9. Files your code writes go under `lab/out/pN/...` (make the folder fresh in the block, so blocks are repeatable). Never write into `lab/data`.
10. Delete only explicit filenames (never glob `rm`). No real API keys or account names. **No `<a href="#...">` links** (the build throws); refer to other pages in plain text ("Part 3").
11. Tone: warm, clear, a little playful like a sketchbook; short paragraphs; **bold** for key terms, *italics* for quotes. Never use the words "genuinely", "honestly", "straightforward". No emojis.
12. `[!SIR]` callouts quote the speaker: short, clean sentences only (paraphrase garbled passages, never quote them).

## 1b. Zero content loss (the top priority)

1. Read your **whole** transcript file from start to end. Write down every point, example, number, analogy, warning, aside, doubt they anticipate ("you may have this question..."), UI element they click, config they name, mistake they make and correct, and every demo step with its result. Skip only sponsor breaks and "like and subscribe".
2. Every one of those items must appear on the page, in their order, with their numbers. Merge neighbours if you like, never drop.
3. Write `notes/coverage/lN.md` (internal, not built): a walk through the transcript in ~1-2 minute slices (the raw file's timestamps may be used in this internal file only; quote the first few words of each slice) → the page heading where that slice is covered. Any row without a heading is a bug: fix the page, not the table.
4. When in doubt whether something is "too minor", include it (a short sentence, a table row, or a `[!PEN]` scribble).
5. When they are loose or wrong, keep what they say and add a short `Beyond the notes:` correction. Also note where they correct themselves.

## 2. Files you read (per page N)

- `transcripts/raw/pNN.md` (or `tNN.md`): your part of the transcript. The full cleaned transcript is next to it if you need context.
- `PLAN.md` (which page covers what, the garbled-word fixes, the order of ideas across pages), `notes/parts/intro.md` (what the intro already says about the lab: do not repeat it at length).
- `lab/*.py` (the helper API and the datasets).

## 3. Page structure (`notes/parts/lN.src.md`)

```
# Part N · Title

<!-- lecture n="N" short="Short name" status="done" kind="one-two words" -->

## At a glance            (2-col table: Question | Short answer, 6-10 rows; last row(s) "... (Beyond the notes)")
## ... their content, in their order, one H2 per idea: whiteboard examples as diagrams, their code + their results,
##     local reproductions (run), [!SIR] quotes, [!QUESTION] doubts they anticipate
## Beyond the notes: ...  (several H2s: internals, configs table, version differences, pitfalls, production checklist, interview corner)
## Revision cheat-sheet   (one big-picture diagram lN-big-picture + bullet recap; Beyond items marked)
## Self-test              (8-12 quiz cards; 3-4 prefixed "(Beyond the notes)")
```

- Title line exactly `# Part N · Title` (the build strips the prefix). `short` = 2-4 words for tabs and cards. `kind` = a short tag (`foundations`, `transaction log`, `joins`...). Two sources on one page: `label="5–6"` in the comment.
- **Depth targets.** Long sources (30+ minutes): 450-800 lines of markdown, 10-16 diagrams, 6-12 run blocks. Medium: 350-600 lines, 8-12 diagrams, 4-8 run blocks. Short: 250-450 lines, 6-9 diagrams, 3-7 run blocks. "Detailed" means: draw the actual rows, keys, files, versions and numbers from their example, not boxes labelled "data".
- A run block is not decoration: each one proves a point of the page. Put it right after the section it reproduces, under a heading such as `### Try it locally: ...`, marked *(Beyond the notes: reproduced locally.)* when it is not their own code.

## 4. Markdown conventions

- Callouts: `> [!NOTE|TIP|WARNING|IMPORTANT|ANALOGY|SIR|INTERVIEW|PEN|QUESTION] Title` then lines starting `> `. `SIR` = the speaker's own clean words (short). `INTERVIEW` = interview corner. `QUESTION` = a doubt (the title) and its answer. `PEN` = a short margin scribble (title only). Beyond callout titles start `Beyond the notes:`.
- Quiz card (question on ONE line, blank line, answer, blank line):

```
<details class="quiz"><summary>Question text on ONE line?

Answer text, may use **bold** and `code`.

</details>
```

- Code fences: ` ```python title="lab_pN_x.py" ` + ` ```output ` (run, output filled by fixout); ` ```cpp title="x.cpp" ` + ` ```output ` (compiled with g++ and run); unrun code: ` ```LANG title="on PLATFORM · x" ` (add ` nocheck` for python); ` ```text ` for quoted text; ` ```json ` for a hand-cleaned excerpt (say it is an excerpt). An error that is meant to happen: an ` ```error ` block with the last line of the exception. A python block without an output block must still run cleanly.
- Two languages side by side (one tab choice switches every group on the page): wrap the fences in `<div class="codetabs">` ... `</div>` with blank lines around the fences.
- Diagram: `![Caption sentence.](diagrams/lN-name.svg)` on its own paragraph. Name = `lN-` + kebab-case. Captions say what to look at.
- Screenshot of a real UI you reproduced locally: `![Caption.](shots/lN-name.webp)` (framed with the `shot_url` from `dkfile.json`).
- Tables: pipe tables, short cells. Math in plain text (`1000 - 500 = 500`, `128 MB`, `O(log n)`).

## 5. Lab conventions

Every run block is **standalone** (its own process, its own imports, run from `lab/` with the project venv `.venv/bin/python` when it exists). Put shared helpers in `lab/labhelpers.py` (the lead owns it): stable names instead of random ids, no timestamps or durations, sorted output, short prints.

Determinism: output must be identical on every run. Do not print timestamps, durations, absolute paths, random ids or dict reprs whose order can vary. Seed every random generator. Keep outputs under ~40 lines. Blocks are cached: unchanged blocks are not re-run (`NOCACHE=1` forces it). Before delivery the lead runs `NOCACHE=1 python3 tools/check_code.py` on every page twice.

Optional **step-through tracers** for pure-Python blocks (no heavy imports): `<div class="tracer" data-trace="lN-name" data-code="file.py" data-call="setup; f(...)" data-viz="KIND"></div>` on its own line, `data-code` = the `title` of a python block on the same page. Viz kinds: `none`, `list:VAR`, `stack:VAR`, `window:ARR` (binary search window), `grid:M`, `range`, `hanoi:N`. Keep traces under 600 steps, give each a lead-in sentence saying what to watch. Use one or two per page where stepping through really helps.

## 6. Diagrams (Excalidraw via Python)

Write `tools/diagrams_lN.py`:

```python
# Excalidraw scenes for Part N. Run: python3 diagrams_lN.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw, arr
from shelp import legend, title, down, right

def d_main_idea():
    s = Scene()
    title(s, 'The main idea', 'one sentence that says what to look at')
    s.box(40, 120, 220, 90, 'step 1\nread the files', 'blue')
    s.box(340, 120, 220, 90, 'step 2\nshuffle by key', 'orange')
    s.arrow([(260, 165), (340, 165)], ORANGE)
    s.save('lN-main-idea')          # writes <outdir>/lN-main-idea.json (outdir = argv[1])

for f in [d_main_idea]:
    f()
```

Scene API (`scene.py`): `s.box(x, y, w, h, text, color, fs=20, style='solid|hachure', shape='rectangle|ellipse', dashed=False, sw=2, ff=5, ink=INK, opacity=100)`; `s.text(x, y, str, fs, color, ff)`; `s.arrow([(x,y),...], color, dashed, end='arrow', start=None, sw=2)`; `s.line(...)`; `s.zone(x, y, w, h, color)`. Box colours: blue green orange purple red yellow teal pink grey (+ zones zblue zpurple zgreen). Fonts: ff=5 handwriting (default), ff=3 monospace (file names, values, code). Text colours RED GREEN BLUE PURPLE ORANGE TEAL GREY INK.
Helpers: `scene.py` (`tree(s, root, x0, y0, ...)` with nodes `{'t','k','e','c','w','fs','dashed','ec'}`), `dhelp.py` (`arr` array cells, `stack`, `circle_people`, `bs_row` binary-search rows, `numline`, `_tw` text width), `shelp.py` (`title`, `legend`, `down`, `right`, `part` a partition with rows, `executor`, `opnode`, `plan_column`, `memory_stack`, `cores`), `dlhelp.py` (`pfile` a Parquet file with rows, `commit` a JSON commit, `ckpt`, `dv`, `folder`, `versions` a version timeline, `rowtable` a small table with highlighted/struck rows, `note`). Domain helpers for this project: write them at the top of your diagrams file, or ask the lead to add a `tools/xhelp.py`.

**Colour language (same on every page):** blue = users, customers, personas; purple = titles, frameworks and their structure (CIRCLES steps, Porter's forces); orange = process steps, flows, actions over time (journeys, rollouts, pipelines); green = good outcome, success metric, the chosen option, a pass; red = risk, failure, pain point, guardrail breach, a rejected option; yellow = the highlighted number, key insight or answer; grey = out of scope, deprioritized, inactive; teal = data, models and AI system parts (LLM, retriever, eval set, embeddings); pink = money: pricing, revenue, cost, margin.

Render and **look**: `sh tools/lchk.sh N` renders only `lN-*`; then

```
cd tools && python3 sheet.py lN- /tmp/dkfile-pv/sheetN.html && node shot.mjs file:///tmp/dkfile-pv/sheetN.html /tmp/dkfile-pv/sheetN.png 1280 800
```

and Read the PNG (several sheets if you have many diagrams). Fix overlaps, clipped text (single lines at most ~60 characters at fs 15-20; split longer ones), arrows that cross labels, colours that contradict the colour language. Each diagram tells one idea and is readable on its own. Draw every whiteboard drawing they make, plus more where useful.

## 7. Workflow for one page

1. Read your transcript fully and list every item (section 1b). Plan H2 sections in their order, one diagram per whiteboard drawing, one run block per point that can be proved locally.
2. Write and run the lab blocks first; check what really happens before writing prose about it.
3. Write `tools/diagrams_lN.py`; render; inspect the contact sheet; fix.
4. Write `notes/parts/lN.src.md`, fill outputs (`fixout.py --write`), read them.
5. `sh tools/lchk.sh N` must end with `0 problems` and print the preview path.
6. Look at the built page: `cd tools && node shots.mjs "file:///tmp/dkfile-pv/<project>/pN.html#lN" /tmp/dkfile-pv/shN 1300 900 0 "#lN .cover" "#lN figure.sketch"` and Read the PNGs (cover, a diagram, a tracer if any; also one 390 px wide mobile shot). No `PAGEERR` lines, nothing listed as overflowing.
7. Coverage pass: fill `notes/coverage/lN.md` from the transcript; add to the page whatever is missing.
8. Final message: files written, counts (diagrams / run blocks / quiz cards / lines), anything the local run did differently from theirs and how the page explains it, any tooling problem.
