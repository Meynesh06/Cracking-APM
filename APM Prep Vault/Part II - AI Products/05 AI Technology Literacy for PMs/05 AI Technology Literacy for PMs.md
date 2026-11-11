---
tags: [apm, part-ii, ai-basics, machine-learning]
part: "Part II - AI Products"
---
# 05 AI Technology Literacy for PMs

This chapter covers the technical vocabulary an APM needs to scope AI work: learning types, the ML lifecycle, LLM basics, how to choose between RAG and fine-tuning, agents, and common AI product families. The goal is to ask the right questions, not to build models.

## Subsections
- [[5.1 AI, machine learning, deep learning, and generative AI]]: how the terms nest and when each fits.
- [[5.2 Supervised, unsupervised, and reinforcement learning]]: what feedback each learning type needs.
- [[5.3 The ML lifecycle - problem definition to deployment]]: the stages from problem framing to monitoring.
- [[5.4 LLM basics - tokens, context windows, prompting, temperature]]: tokens, context, prompts, and temperature.
- [[5.5 RAG, fine-tuning, and embeddings - when to use each]]: prompting vs RAG vs fine-tuning vs long context, with a comparison table.
- [[5.6 Agents and tool use]]: agent loops vs fixed workflows, tool calls, MCP, compounding error, and approval gates.
- [[5.7 Computer vision, speech, and recommendation systems]]: the three product families and their typical pitfalls.

## Key takeaways
- Start with the simplest approach (rules, then classic ML, then LLMs) and justify each step up.
- Labels and feedback decide what learning type is possible; LLM assistants use all three (self-supervised pre-training, supervised fine-tuning, RLHF).
- Tokens drive cost and latency, and a big context window is not memory; use prompting first, RAG for facts that change, fine-tuning for behaviour.
- Agents multiply error and cost across steps; add checks and approval for irreversible actions.
- CV, speech, and recommendation products depend on their data distribution, so test on the real segments (accents, devices, languages).

Back to [[00 Home]]
