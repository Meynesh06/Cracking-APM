---
tags: [apm, part-ii, evals, metrics]
part: "Part II - AI Products"
---
# 08 Evaluating and Measuring AI Products

Traditional products are measured by whether users complete a flow. AI products add a second question: is the output *good enough*, and how do you know before and after shipping? This chapter covers the layered approach: offline evals before launch, human review for ground truth, online metrics that show real behaviour, guardrail metrics that protect against harm, and regression tests so a model or prompt change does not quietly break what worked.

## Subsections
- [[8.1 Offline evals - golden datasets, rubrics, LLM-as-judge]] - pre-launch scoring against a fixed test set using rubrics, with an LLM as a scalable (but imperfect) grader.
- [[8.2 Human evaluation and labeling]] - human raters create ground truth, calibrate automated judges, and surface failure modes that metrics miss.
- [[8.3 Online metrics - task success, acceptance and edit rate, retention of AI users]] - what users actually do with AI output in production.
- [[8.4 Guardrail metrics - harmful outputs, latency, cost]] - the metrics that must not regress while you optimise for quality.
- [[8.5 Regression testing when models or prompts change]] - treating prompts and model versions like code, with a fixed eval suite as the release gate.

## Key takeaways
- Measure AI features in layers: offline evals, human review, online behaviour, and guardrails. No single number is enough.
- A golden dataset is only as good as its coverage of real user inputs, including the hard and adversarial ones.
- LLM-as-judge scales grading but must be calibrated against human labels before you trust it.
- Acceptance and edit rate are the most useful online signals for generative features, because they show whether users trusted the output.
- Every prompt or model change is a release. Run the same eval suite before shipping, and compare against the current baseline.

Back to [[00 Home]]
