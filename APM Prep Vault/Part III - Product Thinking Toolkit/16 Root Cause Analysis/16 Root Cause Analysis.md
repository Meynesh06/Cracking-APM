---
tags: [apm, part-iii, rca, diagnosis]
part: "Part III - Product Thinking Toolkit"
---
# 16 Root Cause Analysis

Root cause ("find the root cause", "a metric dropped X%, what would you do?") is one of the most common PM interview question types. It looks like a one-liner but tests structuring, prioritisation, and convergence. This chapter gives a repeatable sequence: scope the problem, walk the user journey, split internal from external causes, and add an AI-specific layer for AI products.

## Subsections
- [[16.1 Scoping - clarify, verify metrics, check platforms and segments]]: clarify the problem and rule out measurement errors before analysing.
- [[16.2 Walking the user journey]]: break the flow into stages and find where behaviour changed.
- [[16.3 Internal vs external causes]]: separate what your team controls from what the market or the world did.
- [[16.4 AI-specific RCA - model changes, prompt regressions, data drift, cost spikes]]: causes unique to AI products.

## Key takeaways
- Converge on a single most-probable root cause, with a logical path to it.
- Verify the metric first. Many "drops" are instrumentation errors.
- Use the user journey to localise the problem before you brainstorm causes.
- Sudden drops usually mean a release, outage, or bug. Gradual drops usually mean behaviour or market shifts.
- Close with solutions for the root cause, prioritised by impact and effort.

Back to [[00 Home]]
