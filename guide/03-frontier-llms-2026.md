# 03 — Frontier LLMs in 2026: The Current Landscape

The term "frontier model" refers to the most capable AI models available at any given time. In 2026, the landscape is competitive, with several strong players across proprietary and open-weight categories.

---

## Proprietary Models

### Anthropic — Claude Family

Anthropic was founded by former OpenAI researchers with a strong focus on AI safety. Their Constitutional AI approach trains models to be helpful, harmless, and honest.

| Model | Best For | Context Window |
|-------|----------|----------------|
| Claude Opus 4.8 | Complex reasoning, long documents, coding | 200K tokens |
| Claude Sonnet 4.6 | Balanced performance and speed | 200K tokens |
| Claude Haiku 4.5 | Fast, cost-effective tasks | 200K tokens |

**Strengths:** Nuanced writing, safety-conscious, excellent at following complex instructions, strong coding  
**API:** api.anthropic.com  
**Pricing:** Per-token; Sonnet is the sweet spot for most use cases

---

### OpenAI — GPT and o-Series

The company that sparked the current AI era. Two distinct model families:

| Model | Best For |
|-------|----------|
| GPT-4o | Multimodal (text, vision, voice), general purpose |
| o3 / o3-mini | Complex reasoning, maths, science — "thinks" before responding |

**Strengths:** Widest ecosystem, plugin/tool support, real-time voice (GPT-4o), best-in-class reasoning (o3)  
**API:** api.openai.com  
**Note:** o-series models trade speed for accuracy — they're slower but dramatically better at multi-step problems

---

### Google DeepMind — Gemini Family

| Model | Best For |
|-------|----------|
| Gemini 2.0 Ultra | Long-context tasks, multimodal, Google Workspace integration |
| Gemini 2.0 Flash | Speed-optimised, lower cost |

**Strengths:** Deepest integration with Google products (Docs, Gmail, Search), massive context window, strong at coding  
**API:** Google AI Studio / Vertex AI

---

### xAI — Grok

Elon Musk's AI company. Grok models are integrated into X (Twitter) and available via API.

**Strengths:** Real-time internet access, unfiltered tone compared to competitors  
**Note:** Less enterprise adoption than Anthropic/OpenAI/Google as of 2026

---

## Open-Weight Models

Open-weight models release their weights publicly, allowing anyone to download and run them locally. This is a game-changer for privacy, cost, and customisation.

### Meta — Llama 4

Meta has committed to open-weight releases. Llama 4 models compete with frontier proprietary models on many benchmarks.

**Best for:** Teams wanting full control, researchers, fine-tuning on proprietary data  
**Run it:** Via Ollama, Hugging Face, or cloud providers (AWS Bedrock, Groq)

---

### Mistral AI

French AI company producing lean, efficient models. Known for punching above their weight class.

| Model | Notes |
|-------|-------|
| Mistral Large | Frontier-quality proprietary |
| Mistral 7B / Mixtral | Open-weight, runs locally on consumer GPUs |

**Best for:** European data residency requirements, efficient local inference

---

### Other Notable Open-Weight Models (2026)

- **Qwen 2.5** (Alibaba): Strong multilingual, excellent coding
- **Phi-4** (Microsoft): Small model, surprisingly capable for reasoning tasks
- **DeepSeek V3** (DeepSeek): Strong coding and maths, open-weight

---

## How to Choose?

```
Are you building an app or automating a workflow?
├── Need max capability → Claude Opus or o3
├── Need speed + cost balance → Claude Sonnet or GPT-4o
├── Need cheapest/fastest → Claude Haiku or Gemini Flash
├── Need data to stay local → Ollama + Llama 4 or Mistral
└── Need Google Workspace integration → Gemini
```

---

## Benchmark Caution

Every company publishes benchmarks where their model wins. Real-world performance varies by task. Best practice: test the models that interest you on *your actual use cases* before committing.

**Useful benchmark resources:**
- LMSYS Chatbot Arena (human preference rankings)
- Hugging Face Open LLM Leaderboard (open models)
- LiveCodeBench (coding tasks)

---

**Next:** [Offline Hosting with Ollama](04-offline-hosting.md)
