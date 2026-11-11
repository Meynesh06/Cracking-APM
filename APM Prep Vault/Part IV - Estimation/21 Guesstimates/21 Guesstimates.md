---
tags: [apm, part-iv, estimation, guesstimates]
part: "Part IV - Estimation"
---
# 21 Guesstimates
Guesstimates ask for a number you cannot look up, such as US gasoline spend, the bikes a bike-taxi startup needs, or the GPUs an AI feature needs at peak. Interviewers grade your structure, stated assumptions and self-checks more than the final figure. This chapter gives one repeatable loop, the anchor numbers to feed it, the standard equation for each question type, AI-specific conversions, and the arithmetic tricks that keep you fast and error-free.

## Notes in this chapter
- [[21.1 Guesstimate structure - clarify, segment, assume, compute, sanity-check]]: the five-step loop with a time budget, three sanity-check methods, and worked US gas (about $375B a year) and Bangalore bike-taxi (about 5,500 bikes) examples.
- [[21.2 Demographic and digital benchmarks for India and the US]]: a dated, source-labelled table of population, internet and smartphone users, households, urban share, vehicles, screen time, UPI volume, and metro populations.
- [[21.3 Common guesstimate types - market sizing, user counts, storage, supply]]: the equation and sanity check for each type, with corrected YouTube, Google Photos (about 750 PB a year) and ping-pong-ball worked examples.
- [[21.4 AI estimates - tokens per user, inference compute, embedding storage]]: an assumption sheet (tokens per word, price per million tokens, FLOPs per token, bytes per dimension) and worked cost, GPU and vector-storage estimates.
- [[21.5 Mental math tactics]]: rounding, scientific notation, fast division, time and byte constants, lakhs and crores, and checking as you go.

## Key takeaways
- Write the equation and confirm it with the interviewer before putting in any numbers.
- Every input gets a stated reason; never let an assumption stay implicit (for example, "one ride per user per day").
- Use round numbers and powers of ten, and write every intermediate result down.
- Finish with an independent sanity check (per unit, a second method, or a known anchor) and name the most sensitive assumption.
- Keep dated anchors: India about 1.45B people and about 950M internet users, the US about 340M people and about 133M households. Stale casebook inputs (250M Americans, $1.25 gas) can be off by 6x.

Back to [[00 Home]]
