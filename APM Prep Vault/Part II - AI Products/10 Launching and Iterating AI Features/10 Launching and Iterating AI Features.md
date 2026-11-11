---
tags: [apm, part-ii, launch, iteration]
part: "Part II - AI Products"
---
# 10 Launching and Iterating AI Features
Shipping an AI feature is the start of learning, not the end of building. Models, data, and user behaviour all change after launch, so the launch plan needs staged exposure, a fast off-switch, and monitoring that catches silent drift. This chapter also covers how to close the loop with user feedback while respecting consent.

## Subsections
- [[10.1 Staged rollouts and kill switches]]: ramp exposure in gated steps, and keep a tested switch that turns the AI path off in minutes.
- [[10.2 Monitoring drift and vendor model updates]]: watch input, outcome, and vendor-model changes, and treat a provider's model update as a release.
- [[10.3 Feedback loops and consented data collection]]: design explicit and implicit feedback, and use data only for purposes users agreed to.

## Key takeaways
- Ramp AI features in gates (dogfood, allowlist, percentages) with quality, safety, and cost thresholds agreed in advance.
- Every AI feature needs a kill switch with a safe fallback, and the switch must be tested before launch.
- Pin model versions and run regression evals before any vendor model change reaches users.
- Monitor data drift, concept drift, and vendor drift separately, with alerts set against baselines.
- Collect feedback as a designed loop, and default to the narrowest consented use of user data.

Back to [[00 Home]]
