# 02 — LLM History: From Transformers to the AI Era

Understanding where large language models came from helps you understand where they're going — and why everyone is suddenly talking about them.

---

## The Long Road Before Transformers

AI has been a research field since the 1950s, but practical language understanding was limited for decades. Early systems used rule-based approaches: hand-crafted grammars, keyword matching, decision trees. These worked in narrow domains but couldn't generalise.

**Key milestones before 2017:**
- **1966** — ELIZA: First chatbot (MIT). Pattern matching, no real understanding.
- **1980s-90s** — Expert systems: Rules written by humans. Brittle and expensive to maintain.
- **2013** — Word2Vec (Google): Words represented as vectors. Semantic relationships captured for the first time. "King - Man + Woman ≈ Queen."
- **2015** — Recurrent Neural Networks (RNNs) and LSTMs: Better at sequences, but struggled with long-range dependencies.

---

## 2017: The Transformer Changes Everything

**"Attention Is All You Need"** (Vaswani et al., Google, 2017) introduced the Transformer architecture. Instead of processing text word-by-word, Transformers use **attention mechanisms** to weigh every word against every other word simultaneously.

This unlocked:
- Parallel training on GPUs at massive scale
- Much better understanding of long-range context
- The foundation for every major LLM since

---

## 2018–2019: BERT and GPT-1/2

- **GPT-1** (OpenAI, 2018): 117M parameters. First large generative transformer. Showed promise.
- **BERT** (Google, 2018): Bidirectional — reads text left-to-right AND right-to-left. Became the standard for NLP benchmarks.
- **GPT-2** (OpenAI, 2019): 1.5B parameters. So good at generating coherent text that OpenAI initially refused to release it fully, citing misuse concerns. (This seems quaint now.)

---

## 2020: GPT-3 — The Moment Things Got Real

**GPT-3** (OpenAI, 2020): 175B parameters. The leap was staggering. Few-shot learning — give it a few examples in the prompt and it generalised to new tasks without any retraining. Developers started building real applications on top of it via the OpenAI API.

---

## 2022: ChatGPT — The Public Watershed

**November 30, 2022**: OpenAI launched ChatGPT, built on GPT-3.5 with **Reinforcement Learning from Human Feedback (RLHF)**. A technique that aligns the model to be helpful, honest, and less harmful by having human raters score outputs.

ChatGPT reached 1 million users in 5 days. 100 million in 2 months. No consumer app had ever grown that fast.

---

## 2023: The Race Accelerates

- **GPT-4** (OpenAI, March 2023): Multimodal (text + images). Passed the bar exam in the top 10%. Significant jump over GPT-3.5.
- **Claude** (Anthropic, 2023): Founded by ex-OpenAI researchers. Focus on safety and Constitutional AI — a technique for training AI to be helpful and harmless.
- **Gemini** (Google DeepMind, late 2023): Google's answer to GPT-4. Natively multimodal.
- **Llama 2** (Meta, 2023): Open-weights model released publicly. Sparked an explosion of open-source AI development.
- **Mistral 7B** (Mistral AI, 2023): Tiny but surprisingly capable. Showed that smaller models could compete with larger ones.

---

## 2024: Agents, Reasoning, and Local Models Mature

- **GPT-4o** (OpenAI): "Omni" — real-time voice, vision, and text in one model.
- **Claude 3 family** (Anthropic): Haiku, Sonnet, Opus tiers. Opus set new benchmarks.
- **Llama 3** (Meta): Open-weights models competitive with proprietary alternatives for many tasks.
- **Reasoning models emerge**: OpenAI o1 — models that "think before they speak" using chain-of-thought reasoning internally.

---

## 2025–2026: Where We Are Now

- Frontier models (Claude Opus 4, GPT-4o, Gemini 2) handle complex reasoning, long documents (1M+ token context), code, and multimodal inputs as standard.
- **AI agents** — models that can plan, use tools, and take actions over multiple steps — are moving from research to production.
- Open-source models (Llama 4, Mistral, Qwen) are near-frontier quality on many tasks.
- Local inference via Ollama, LM Studio, and others is practical for many use cases.

---

## Key Concepts Summary

| Term | What It Means |
|------|--------------|
| Parameters | The "knobs" in a model — more parameters generally means more capacity |
| Pre-training | Training on massive text corpora to learn language |
| Fine-tuning | Further training on specific tasks or behaviours |
| RLHF | Human raters teach the model to prefer helpful, harmless outputs |
| Context window | How much text a model can "see" at once |

---

**Next:** [Frontier LLMs in 2026](03-frontier-llms-2026.md)
