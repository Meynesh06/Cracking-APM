# APM Prep Sketch Notes: plan

Source: the reviewed **APM Prep Vault** (`../APM Prep Vault/`), chapters 4-25 of *Crack the APM Role* (Parts II-V): 125 notes, about 7,000 lines. There is no video. Each page's source is that chapter's vault notes, concatenated in order into `transcripts/raw/pNN.md` (the chapter index note first, then each subsection note, each marked `<!-- ===== vault note: NAME ===== -->`).
Deliverable: one single-file HTML (`dist/APM_Prep_Notes.html`) + markdown + bundle zip. No timestamps, no YouTube links, no external URLs on the pages (the vault's Readings links stay in the vault). Excalidraw for every diagram. Local lab: plain Python 3.14 in `.venv` (stdlib only), used only where a calculation proves a point (guesstimates, RICE/ICE scoring, unit economics, retention, pricing tests).

Page numbers run 1-22 (`lN` files), but every page carries `label="<vault chapter number>"` so tabs and headers show the vault's chapter numbers (Ch4 ... Ch25).

| Page | label | Vault chapter (Part) | Source file | Writer |
|---|---|---|---|---|
| 1 | 4 | What Makes an AI Product Different (II) | p01.md | R (reference) |
| 2 | 5 | AI Technology Literacy for PMs (II) | p02.md | A |
| 3 | 6 | AI Product Strategy and Economics (II) | p03.md | A |
| 4 | 7 | Designing AI Experiences (II) | p04.md | B |
| 5 | 8 | Evaluating and Measuring AI Products (II) | p05.md | B |
| 6 | 9 | Responsible AI, Risk, and Regulation (II) | p06.md | C |
| 7 | 10 | Launching and Iterating AI Features (II) | p07.md | C |
| 8 | 11 | Understanding Users (III) | p08.md | D |
| 9 | 12 | Product Design with CIRCLES (III) | p09.md | D |
| 10 | 13 | Product Improvement and App Critique (III) | p10.md | D |
| 11 | 14 | Prioritization (III) | p11.md | E |
| 12 | 15 | Metrics (III) | p12.md | E |
| 13 | 16 | Root Cause Analysis (III) | p13.md | F |
| 14 | 17 | Pricing and Monetization (III) | p14.md | F |
| 15 | 18 | Go-to-Market and Launch (III) | p15.md | F |
| 16 | 19 | Strategy and Market Entry (III) | p16.md | G |
| 17 | 20 | Execution - Roadmaps, PRDs, and Agile (III) | p17.md | G |
| 18 | 21 | Guesstimates (IV) | p18.md | H |
| 19 | 22 | Case Types and How to Approach Each (V) | p19.md | I |
| 20 | 23 | Worked Examples (V) | p20.md | I |
| 21 | 24 | AI Case Bank (V) | p21.md | J |
| 22 | 25 | Practice Protocol (V) | p22.md | J |

Intro (`notes/parts/intro.md`, diagrams `l0-*` from `tools/diagrams_intro.py`) is written by writer R together with page 1.

## Cross-page references (plain text, never links)
Refer to other pages as "Chapter 15" (the vault number = the label), e.g. "see Chapter 15 for HEART". Vault wikilinks like `[[15.3 HEART]]` become "Chapter 15 (HEART)".

## Order of ideas
Part II (Ch4-10) builds AI literacy and AI product judgement. Part III (Ch11-20) is the general toolkit: users → design (CIRCLES) → critique → prioritization → metrics → RCA → pricing → GTM → strategy → execution. Part IV (Ch21) is estimation. Part V (Ch22-25) applies everything: case types, worked casebook examples, the AI case bank, and the practice protocol.

## Status
- scaffold, sources, STYLE.md, dkfile.json: done (lead)
