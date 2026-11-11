---
tags: [apm, readings]
---
# AI Product Reading

Verified reading on LLMs, agents, evals, AI UX and responsible AI for AI-focused APM interviews.

## LLM basics
- [Building LLM applications for production](https://huyenchip.com/2023/04/11/llm-engineering.html) by Chip Huyen: the real challenges of shipping LLM features.
- [Understanding the weird world of LLMs](https://simonwillison.net/2023/Aug/3/weird-world-of-llms/) by Simon Willison: a plain-language mental model of what LLMs are and aren't.
- [Open challenges in LLM research](https://huyenchip.com/2023/08/16/llm-research-open-challenges.html) by Chip Huyen: hallucination, context, multimodality and other limits PMs should know.
- [Patterns for building LLM-based systems](https://eugeneyan.com/writing/llm-patterns/) by Eugene Yan: evals, RAG, fine-tuning, caching and guardrails in one map.
- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) by Anthropic: vendor guidance on writing effective prompts.
- [Prompt engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering) by OpenAI: another vendor's view, useful to compare.
- [Prompting Guide](https://www.promptingguide.ai/): a broad catalogue of prompting techniques.

Pairs with [[5.4 LLM basics - tokens, context windows, prompting, temperature]] and [[4.1 Probabilistic outputs vs deterministic features]].

## RAG and agents
- [Agents](https://huyenchip.com/2025/01/07/agents.html) by Chip Huyen: how agents plan, use tools and fail.
- [Building a generative AI platform](https://huyenchip.com/2024/07/25/genai-platform.html) by Chip Huyen: walks through RAG, guardrails, routing and caching components.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) by Anthropic: when to use workflows versus agents, with clear patterns.
- [A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) by OpenAI: a product-oriented guide to use-case selection and design.
- [OpenAI Cookbook](https://cookbook.openai.com/) by OpenAI: worked examples that make RAG and tool use concrete.

Pairs with [[5.5 RAG, fine-tuning, and embeddings - when to use each]] and [[5.6 Agents and tool use]].

## Evals
- [Your AI product needs evals](https://hamel.dev/blog/posts/evals/) by Hamel Husain: the clearest argument for why evals are the core of AI quality.
- [A field guide to rapidly improving AI products](https://hamel.dev/blog/posts/field-guide/) by Hamel Husain: error analysis and iteration loops from real teams.
- [Using LLM-as-a-judge](https://hamel.dev/blog/posts/llm-judge/) by Hamel Husain: how to build a judge you can trust.
- [LLM evals notes](https://hamel.dev/notes/llm/evals/) by Hamel Husain: a compact reference on eval practice.
- [Product evals in three simple steps](https://eugeneyan.com/writing/product-evals/) by Eugene Yan: a lightweight eval workflow a PM can follow.
- [Create strong empirical evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) by Anthropic: how to design test cases and success criteria.
- [Evals guide](https://developers.openai.com/api/docs/guides/evals) by OpenAI: the vendor workflow for running evals.
- [Building eval systems that improve your AI product](https://www.lennysnewsletter.com/p/building-eval-systems-that-improve) by Lenny's Newsletter: an accessible PM-level take on eval systems.

Pairs with [[8.1 Offline evals - golden datasets, rubrics, LLM-as-judge]] and [[8.5 Regression testing when models or prompts change]].

## AI UX
- [People + AI Guidebook](https://pair.withgoogle.com/guidebook/) by Google PAIR: patterns and worksheets for designing human-centered AI.
- [Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/) by Microsoft HAX: 18 guidelines covering the full interaction lifecycle.

Pairs with [[7.2 User control, transparency, and confidence signals]] and [[7.3 Handling hallucinations, errors, and recovery paths]].

## Responsible AI and regulation
- [EU AI Act Explorer](https://artificialintelligenceact.eu/) : a navigable version of the Act with risk tiers and obligations.
- [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) by the European Union: the official legal text.
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) by NIST: a standard vocabulary for govern, map, measure, manage.
- [Responsible AI](https://ai.google.dev/responsible) by Google: a practical view of safety and fairness practices in product teams.

India DPDP Act 2023: search "Digital Personal Data Protection Act 2023" on meity.gov.in or indiacode.nic.in. No verified link yet.

Pairs with [[9.2 Privacy, consent, and data retention (India DPDP Act 2023)]] and [[9.5 Regulatory landscape - EU AI Act and sector-specific rules]].

[[00 Home]]
