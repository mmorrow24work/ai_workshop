# 04 — Offline LLM Hosting: Running AI Locally

Running an LLM on your own hardware means your data never leaves your machine. This is essential when working with sensitive, confidential, or client data, and increasingly practical as hardware improves and models get more efficient.

---

## Why Run Locally?

- **Data privacy:** Nothing sent to external servers
- **Cost:** No per-token API fees after initial setup
- **Offline capability:** Works without internet
- **Customisation:** Fine-tune on your own data
- **Compliance:** Easier to satisfy data residency requirements

**Trade-off:** Requires capable hardware; local models are often slightly behind frontier proprietary models in raw capability.

---

## Hardware Requirements (Rough Guide)

| Model Size | Minimum RAM/VRAM | What You Get |
|------------|-----------------|--------------|
| 7B parameters | 8 GB RAM (CPU) / 6 GB VRAM | Fast, capable for most tasks |
| 13B parameters | 16 GB RAM / 10 GB VRAM | Better reasoning |
| 34B parameters | 32 GB RAM / 24 GB VRAM | Near-frontier quality |
| 70B+ parameters | 64 GB RAM / 40+ GB VRAM | Frontier-quality, needs serious hardware |

**Quantisation** (compressing models) lets you run larger models on less hardware — a 7B model quantised to 4-bit uses ~4GB of RAM.

---

## Ollama (Recommended Starting Point)

Ollama is the simplest way to download and run open LLMs locally. One command to install, one command to run a model.

### Install

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows
# Download installer from https://ollama.com/download
```

### Pull and Run a Model

```bash
# Pull a model (downloads ~4GB for llama3)
ollama pull llama3

# Run an interactive chat session
ollama run llama3

# Run a one-shot command
ollama run llama3 "Explain what a REST API is in simple terms"
```

### Key Ollama Models Available

| Model | Size | Best For |
|-------|------|----------|
| llama3 | 8B | General purpose, fast |
| llama3:70b | 70B | Near-frontier quality |
| mistral | 7B | Efficient, good reasoning |
| codellama | 7B-34B | Code-focused tasks |
| phi3 | 3.8B | Very fast, lightweight tasks |
| qwen2 | 7B-72B | Multilingual, coding |
| nomic-embed-text | — | Text embeddings for RAG |

### Ollama API (Use Programmatically)

Ollama runs a local REST API at `http://localhost:11434` — compatible with the OpenAI API format.

```python
import requests

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama3",
    "prompt": "What is machine learning?",
    "stream": False
})
print(response.json()["response"])
```

---

## Alternatives to Ollama

### LM Studio

A polished desktop GUI for downloading and running models. Great for non-technical users.

- Visual model browser
- Built-in chat interface
- Local API server (OpenAI-compatible)
- Platform: Mac, Windows, Linux
- Download: lmstudio.ai

### Jan.ai

Open-source desktop app, similar to LM Studio but fully open-source.

- Platform: Mac, Windows, Linux
- Supports multiple model formats
- MCP server support
- Download: jan.ai

### GPT4All

Focused on maximum privacy. Models run entirely on CPU (no GPU required).

- Great for older hardware
- Simple chat UI
- Supports many model formats
- Download: gpt4all.io

### LocalAI

More advanced: a drop-in OpenAI API replacement that runs locally. Supports text, images, audio, and embeddings.

- No GUI — pure API server
- Best for developers building applications
- GitHub: go-skynet/LocalAI

---

## Practical Tips

1. **Start with llama3 (8B)** — fast enough for most conversations and fits in 8GB RAM
2. **Use quantised models** (`ollama pull llama3:8b-instruct-q4_0`) if you're RAM-constrained
3. **Separate your tools** — use a local model for sensitive work, a cloud model for tasks requiring frontier capability
4. **Update regularly** — local model quality is improving rapidly; re-pulling models every few months is worthwhile

---

## When NOT to Use Local Models

- When you need frontier reasoning (complex legal analysis, cutting-edge code)
- When speed is critical (local inference is slower than cloud APIs on equivalent tasks)
- When you're on a basic laptop with less than 8GB RAM

---

**Next:** [LLM Tokens Explained](05-llm-tokens.md)
