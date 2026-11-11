---
tags: [apm, part-ii, ai-product-basics]
part: "Part II - AI Products"
---
# 04 What Makes an AI Product Different

AI products behave differently from classic software: outputs are probabilistic, data is a core input, quality is a distribution, and every call has a cost and latency. This chapter gives you the vocabulary to talk about those differences in an APM interview.

## Subsections
- [[4.1 Probabilistic outputs vs deterministic features]]: same input, different outputs; define acceptance bars instead of "works or doesn't."
- [[4.2 Data as a product input and data flywheels]]: data as a product input; how feedback loops compound and where they break.
- [[4.3 Quality as a distribution, not a bug count]]: measure quality by segment, tail, and severity.
- [[4.4 Latency, cost per query, and capacity planning]]: per-call cost and latency budgets, and the levers to control them.
- [[4.5 Trust, errors, and graceful failure]]: design for wrong answers, with clear fallbacks and recovery.

## Key takeaways
- AI outputs are probabilistic, so success is a rate with an agreed error budget.
- Data is a product input, and the feedback loop is the real moat if it is closed and clean.
- Quality is a distribution: check segments, the worst tail, and severity, not the average.
- Cost per query and latency are product constraints that shape the UX and pricing.
- Trust depends on calibration, transparency, control, and a graceful way out when the model fails.

Back to [[00 Home]]
