# Top 10 AI Projects to Inspire and Teach

These projects are selected because they're either directly useful, exceptionally well-documented, or represent important ideas in AI. Each one is a learning opportunity — read the code, run it, contribute to it.

---

## 1. Ollama

**GitHub:** github.com/ollama/ollama  
**Skill level:** Beginner (to use) / Intermediate (to contribute)  
**Language:** Go  
**What it is:** The simplest way to run LLMs locally

Ollama lets you run open-weight LLMs with a single command. The project demonstrates how to package complex ML models into a clean CLI and REST API. Study the codebase to understand model serving, quantisation, and API design.

**Why it's inspiring:** Democratises AI by making local model inference accessible to anyone with a laptop.

**Start here:** `ollama run llama3` — running your first local LLM takes under 5 minutes.

---

## 2. Stable Diffusion (AUTOMATIC1111 WebUI)

**GitHub:** github.com/AUTOMATIC1111/stable-diffusion-webui  
**Skill level:** Beginner (to use) / Advanced (to contribute)  
**Language:** Python  
**What it is:** Web interface for AI image generation

Stable Diffusion generates images from text prompts locally on your GPU. The WebUI project wraps it in an accessible interface with hundreds of features. An astonishing demonstration of what open-source AI can achieve.

**Why it's inspiring:** One of the most-starred repos in GitHub history. Shows how community-driven open-source AI development works at scale.

**Start here:** Install the WebUI and generate your first image from a text description.

---

## 3. Hugging Face Transformers

**GitHub:** github.com/huggingface/transformers  
**Skill level:** Intermediate–Advanced  
**Language:** Python  
**What it is:** The standard library for working with AI models

The `transformers` library is the foundation of modern applied ML. It provides a unified API for thousands of pre-trained models — text, images, audio, video. If you're doing any serious ML work in Python, you'll use this.

**Why it's inspiring:** Hugging Face built an open ecosystem that made frontier model research accessible to everyone. The Hub hosts 500,000+ models, all freely downloadable.

**Start here:**
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
print(classifier("AI is amazing!"))
```

---

## 4. LangChain

**GitHub:** github.com/langchain-ai/langchain  
**Skill level:** Intermediate  
**Language:** Python / JavaScript  
**What it is:** Framework for building LLM-powered applications

LangChain provides building blocks for chaining LLM calls, connecting to data sources, and building agents. It's the most popular framework for AI application development and has a massive ecosystem.

**Why it's inspiring:** Turned the idea of "LLM applications" from research into something any developer can build.

**Start here:** Build a simple RAG application following LangChain's quickstart tutorial.

---

## 5. LlamaIndex

**GitHub:** github.com/run-llama/llama_index  
**Skill level:** Intermediate  
**Language:** Python  
**What it is:** Data framework for connecting LLMs to your data

LlamaIndex specialises in ingesting, structuring, and querying data with LLMs. Where LangChain is broad (chains, agents, tools), LlamaIndex goes deep on the data side — indexing, retrieval, and querying.

**Why it's inspiring:** Makes RAG accessible and production-ready. The documentation and tutorials are excellent learning resources.

**Start here:** Index a folder of documents and build a chatbot that answers questions about them.

---

## 6. PrivateGPT

**GitHub:** github.com/zylon-ai/private-gpt  
**Skill level:** Intermediate  
**Language:** Python  
**What it is:** 100% local, private AI document assistant

PrivateGPT lets you ask questions about your documents using a local LLM — nothing leaves your machine. Combines Ollama (or other local inference) with a vector database and a clean API.

**Why it's inspiring:** Solves the privacy vs. capability tension. Perfect demonstration of RAG + local models for enterprise use cases.

**Start here:** Install it and ask questions about your own documents.

---

## 7. OpenHands (formerly OpenDevin)

**GitHub:** github.com/All-Hands-AI/OpenHands  
**Skill level:** Intermediate  
**Language:** Python  
**What it is:** Open-source AI software engineer

OpenHands is an AI agent that can write code, run terminal commands, browse the web, and complete software engineering tasks. It's an open-source alternative to proprietary coding agents.

**Why it's inspiring:** Shows what agentic AI looks like in practice. The architecture is a great study in how to give LLMs tools and a reasoning loop.

**Start here:** Run it on a small, isolated coding task and watch the agent work.

---

## 8. AnythingLLM

**GitHub:** github.com/Mintplex-Labs/anything-llm  
**Skill level:** Beginner (to use)  
**Language:** JavaScript/Node.js  
**What it is:** All-in-one local AI stack with a polished UI

AnythingLLM provides a complete package: document management, chat interface, user management, and the ability to connect to any LLM (local or cloud). Think "self-hosted ChatGPT" with document upload.

**Why it's inspiring:** Shows how to build a production-quality AI product as an open-source project. Also immediately useful for teams wanting private document AI.

**Start here:** Run with Docker and upload some documents to test the RAG pipeline.

---

## 9. Perplexica

**GitHub:** github.com/ItzCrazyKns/Perplexica  
**Skill level:** Intermediate  
**Language:** TypeScript  
**What it is:** Open-source Perplexity AI alternative

Perplexica is an AI-powered search engine that answers questions by searching the web and synthesising results with citations. A faithful open-source recreation of Perplexity.ai.

**Why it's inspiring:** Demonstrates how to combine web search with LLMs. The codebase is clean and educational — great for understanding retrieval-augmented applications.

**Start here:** Set it up locally and compare its web-search-grounded answers to standard LLM responses.

---

## 10. Anthropic Cookbook

**GitHub:** github.com/anthropics/anthropic-cookbook  
**Skill level:** Beginner–Advanced  
**Language:** Python  
**What it is:** Official collection of code examples for building with Claude

A growing collection of Jupyter notebooks demonstrating real patterns: tool use, RAG, agents, prompt caching, vision, classification, and more. All examples use real Anthropic API calls.

**Why it's inspiring:** Curated by the team that built Claude. The cleanest examples of production-ready patterns for LLM applications.

**Start here:** Run any notebook that matches something you want to build. The notebooks are self-contained and well-commented.

---

## How to Use This List as a Learning Path

**If you're new to coding with AI:**
Start with Hugging Face Transformers → LangChain → Anthropic Cookbook

**If you want local AI:**
Start with Ollama → PrivateGPT → AnythingLLM

**If you want to build:**
Anthropic Cookbook (patterns) → LlamaIndex (data) → OpenHands (agents)

**If you want to understand AI deeply:**
Hugging Face Transformers source code → Andrej Karpathy's neural network tutorials → any model training codebase

---

## Contributing to These Projects

Open source AI projects welcome contributions. Good starting points:
- Fix documentation errors or unclear explanations
- Add examples or tutorials for features you've used
- Report bugs with minimal reproductions
- Translate documentation

Contributing to a well-used project is one of the best ways to learn, build your portfolio, and connect with the AI community.

---

*See also: [Top 10 YouTube Channels](youtube-channels.md)*
