# 01 — AI Interfaces: How You Can Talk to an LLM

There's no single "right" way to use AI. Depending on your role, workflow, and technical comfort, you have several very different options. This chapter walks through each one.

---

## 1. Browser Interface

**Examples:** ChatGPT (chat.openai.com), Claude (claude.ai), Gemini (gemini.google.com)

The simplest way to start. Open a website, type a message, get a response.

**Best for:** Quick questions, brainstorming, one-off tasks  
**Limitations:** No automation, limited file handling, conversations don't persist across sessions (usually), not suitable for sensitive/client data on free tiers

---

## 2. Desktop Application

**Examples:** Claude Desktop, ChatGPT Desktop (macOS/Windows)

A native app installed on your computer. Feels more integrated than a browser tab.

**Best for:** People who want AI always available without browser distractions  
**Key feature:** Desktop apps often support **MCP (Model Context Protocol)** — letting the AI read your local files, run tools, and connect to local services  
**Limitations:** Same data privacy concerns as browser; check your organisation's policy

---

## 3. IDE Integration

**Examples:** GitHub Copilot (VS Code, JetBrains), Cursor, Continue.dev, Codeium

AI built directly into your code editor. Autocomplete, inline chat, code review — all without leaving your editor.

**Best for:** Developers writing code every day  
**Key feature:** Context-aware — the model sees your open files, project structure, and selected code  
**Limitations:** Copilot sends code to Microsoft/GitHub servers; verify this is acceptable for your client projects

---

## 4. WSL2 / Command Line Interface (CLI)

**Examples:** Claude Code (`claude`), Aider, Ollama CLI

Run AI tools directly in your terminal. This is where AI becomes a true automation tool.

```bash
# Example: Claude Code in your project directory
claude "explain what this function does"

# Example: Pull and run a model with Ollama
ollama run llama3
```

**Best for:** Developers, DevOps engineers, power users  
**Key feature:** Scriptable, automatable, works inside CI/CD pipelines  
**WSL2 note:** On Windows, WSL2 gives you a Linux environment where these CLI tools run natively — ideal for Windows users wanting the full Linux AI toolchain

---

## 5. API (Application Programming Interface)

**Examples:** Anthropic API, OpenAI API, Google Gemini API

Communicate with LLMs programmatically from your own code. This is how production applications are built.

```python
import anthropic

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Explain what an API is."}]
)
print(message.content[0].text)
```

**Best for:** Building AI-powered applications, automating workflows, integrating AI into existing systems  
**Key considerations:** Costs per token, rate limits, API key security, data handling agreements

---

## 6. MCP (Model Context Protocol)

MCP is a newer open standard that lets AI assistants connect to external tools and data sources in a structured, safe way. Think of it as a plugin system for AI.

**How it works:**
- An MCP server exposes "tools" (e.g., read a file, query a database, search the web)
- The AI client (e.g., Claude Desktop, Claude Code) discovers and calls these tools
- The AI can take actions and retrieve context beyond its training data

**Example MCP servers available:**
- File system access
- GitHub integration
- Postgres database queries
- Browser control (Playwright)
- Slack messages

**Best for:** Power users who want AI with deep integration into their local environment and business tools  
**Why it matters:** MCP is becoming the standard way to extend AI beyond its training data — expect to see it everywhere in 2026

---

## Quick Comparison

| Interface | Technical Skill Needed | Good For | Data Risk |
|-----------|----------------------|----------|-----------|
| Browser | None | Quick tasks | Medium |
| Desktop App | Low | Daily use + MCP | Medium |
| IDE Plugin | Low-Medium | Coding | Medium-High |
| CLI | Medium-High | Automation, dev work | Low (if local) |
| API | High | Building apps | Configurable |
| MCP | Medium | Rich integrations | Configurable |

---

**Next:** [LLM History](02-llm-history.md)
