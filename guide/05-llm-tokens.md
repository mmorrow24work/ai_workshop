# 05 — LLM Tokens: What They Are and Why They Matter

Everything about how LLMs work, what they cost, and what they can do comes back to tokens. This chapter demystifies them.

---

## What Is a Token?

A token is the basic unit of text that an LLM processes. It's not exactly a word — it's more like a word fragment determined by the model's vocabulary.

**Rule of thumb:** 1 token ≈ 4 characters ≈ ¾ of a word (for English)

```
"Hello, how are you?"  →  5 tokens: ["Hello", ",", " how", " are", " you", "?"]
"tokenisation"         →  3 tokens: ["token", "isation"]   (roughly)
"AI"                   →  1 token
```

Different languages tokenise differently:
- English: ~1.3 tokens per word
- Chinese/Japanese: often more tokens per character
- Code: varies widely depending on syntax

**Try it yourself:** platform.openai.com/tokenizer — paste any text to see how it tokenises.

---

## Context Window

The context window is the maximum number of tokens a model can "see" at once — both your input AND its own output.

| Model | Context Window |
|-------|---------------|
| Claude Opus 4.8 | 200,000 tokens (~150,000 words — a long novel) |
| GPT-4o | 128,000 tokens |
| Gemini 2.0 Ultra | 1,000,000 tokens |
| Local Llama 3 (8B) | 8,000–128,000 tokens (depends on setup) |

**What this means in practice:**
- A 200K context window can hold roughly the entire Harry Potter series
- Conversations reset when they exceed the context window
- Large codebases can often fit within modern context windows

---

## Tokens and Cost

When using AI via API, you pay per token — both **input tokens** (what you send) and **output tokens** (what the model generates).

**Typical pricing (approximate, as of 2026):**

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|------------------------|
| Claude Sonnet 4.6 | ~$3 | ~$15 |
| Claude Haiku 4.5 | ~$0.25 | ~$1.25 |
| GPT-4o | ~$5 | ~$15 |
| GPT-4o-mini | ~$0.15 | ~$0.60 |

**Real-world example:**
- Summarising a 10-page document (~5,000 words ≈ 6,500 tokens input)
- Getting a 500-word summary (~375 tokens output)
- Total cost with Claude Sonnet: ~$0.02 — less than 2 cents

For high-volume applications, these costs add up — model selection and prompt efficiency matter.

---

## Prompt Caching

Anthropic and OpenAI both offer **prompt caching** — if you repeatedly send the same system prompt or context (e.g., a large document), the model caches it and charges reduced rates for subsequent calls.

This can reduce costs by 80-90% for applications that repeatedly query the same background context.

---

## Why Tokens Matter Beyond Cost

### 1. Context Window Limits
If your conversation or document exceeds the context window, the model loses track of earlier content. For long-running tasks, this is a real constraint.

**Mitigation strategies:**
- Summarise previous turns
- Use RAG (Retrieval-Augmented Generation) to pull in only relevant content
- Split large documents into chunks

### 2. Output Limits
Most API calls have a maximum output token limit (`max_tokens`). If you ask for a very long document and set `max_tokens=1024`, the response will be cut off.

### 3. Latency
More tokens = more time to generate. For real-time applications, prompt length significantly affects response speed.

---

## Chunking Strategies for Large Documents

When a document is too large for the context window:

1. **Fixed chunking:** Split into equal-sized chunks (e.g., 1,000 tokens each with 200-token overlap)
2. **Semantic chunking:** Split at natural boundaries (paragraphs, sections)
3. **Hierarchical summarisation:** Summarise each chunk, then summarise the summaries
4. **RAG:** Index the document and retrieve only relevant chunks at query time (see [Bonus Topics](12-bonus-topics.md))

---

## Quick Reference

| Concept | What It Is |
|---------|-----------|
| Token | ~4 chars / ¾ word — the unit LLMs process |
| Context window | Max tokens in + out the model can handle |
| Input tokens | Text you send to the model |
| Output tokens | Text the model generates |
| Prompt caching | Reduced cost for repeated identical context |
| Chunking | Splitting large docs to fit within context limits |

---

**Next:** [Subscription Packages](06-example-packages.md)
