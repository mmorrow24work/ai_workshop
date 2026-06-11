# 07 — AI Harness Options: Beyond the Chat Interface

An "AI harness" is a tool or framework that wraps an LLM and gives you a structured way to work with it — automating tasks, managing context, running multi-step workflows, or integrating with your development environment.

---

## What Is a Harness?

Think of a raw LLM like an engine. A harness is the vehicle built around it:
- It provides the steering (workflow control)
- It connects the engine to useful tools (file access, web search, terminal)
- It manages the fuel efficiently (context and token management)
- It provides a dashboard (UI or CLI interface)

---

## Claude Code (Anthropic)

**Type:** CLI / Agentic coding assistant  
**Best for:** Developers; works across the entire codebase

Claude Code is Anthropic's official CLI tool. It runs in your terminal and has deep access to your local project — it can read files, write code, run tests, commit to git, and work autonomously on multi-step tasks.

```bash
# Install
npm install -g @anthropic-ai/claude-code

# Run in your project directory
claude

# One-shot task
claude "add unit tests for the auth module"
```

**Key features:**
- Full file system access (reads/writes your actual code)
- Git integration (stages, commits, creates PRs)
- MCP server support (connect to databases, APIs, etc.)
- Runs shell commands to test and validate its own work
- Memory system for persistent project context
- Hooks for automating pre/post action steps

**Pricing:** Requires Anthropic API key (pay-per-token) or Claude Max subscription

---

## Cursor

**Type:** IDE (fork of VS Code)  
**Best for:** Developers who want AI deeply embedded in their editor

Cursor is a VS Code fork with AI built in at the IDE level, not as a plugin.

**Key features:**
- Tab completion (accepts suggestions with Tab, like Copilot but smarter)
- Composer mode: describe a multi-file change; Cursor plans and executes it
- Chat panel: ask questions about your codebase; Cursor indexes all files
- Agent mode: autonomous multi-step coding tasks
- Works with Claude, GPT-4o, and other models

**Pricing:** Free tier available; Pro ~$20/month for unlimited AI usage

---

## GitHub Copilot

**Type:** IDE plugin (VS Code, JetBrains, Neovim, etc.)  
**Best for:** Developers who want AI suggestions without switching editors

The original AI coding assistant, now integrated deeply into VS Code.

**Key features:**
- Inline code completion
- Copilot Chat (ask questions, explain code, fix bugs)
- Copilot Workspace (plan and implement larger changes)
- GitHub integration (PR summaries, code review)

**Pricing:** $10/month individual; often free with GitHub Student/open source

---

## Continue.dev

**Type:** Open-source IDE extension (VS Code, JetBrains)  
**Best for:** Developers who want flexibility — use any model, including local ones

Continue is open-source and lets you connect to any LLM: Claude, GPT-4, local Ollama models, or any OpenAI-compatible API.

**Key features:**
- Chat with your codebase
- Inline editing
- Fully configurable model backend
- Works with local models (privacy-preserving option)

**Pricing:** Free and open-source; you bring your own API keys

---

## open-claw

**Type:** Community-built Claude interface  
**Best for:** Advanced Claude users wanting enhanced interface features beyond claude.ai

open-claw is a third-party interface that wraps the Claude API with a richer UI experience, including features like multi-conversation management, enhanced prompt tools, and workflow automation.

**Note:** As with any third-party tool, verify it's current and well-maintained before using with sensitive data. Your API key and prompts pass through the tool.

---

## hermes-agent

**Type:** Agent framework  
**Best for:** Developers building autonomous AI agents

hermes-agent is a framework for building multi-step AI agents. Rather than a single chat interface, it's a structured way to define tasks, tools, and reasoning loops for LLMs to execute.

**Key concepts:**
- Tool definitions: tell the agent what actions it can take
- Reasoning loops: the agent plans, acts, observes, and iterates
- Memory: persistent context across steps

---

## Comparison Table

| Tool | Type | Skill Level | Model Flexibility | Local Models | Price |
|------|------|-------------|------------------|--------------|-------|
| Claude Code | CLI/Agent | Intermediate | Claude only | No | API cost |
| Cursor | IDE | Beginner+ | Multi-model | No | Free/$20/mo |
| GitHub Copilot | IDE Plugin | Beginner | Multi-model | No | $10/mo |
| Continue.dev | IDE Plugin | Intermediate | Any (incl. local) | Yes | Free |
| open-claw | Web UI | Beginner | Claude only | No | API cost |
| hermes-agent | Framework | Advanced | Flexible | Depends | Open-source |

---

## Recommendation for Getting Started

1. **Complete beginner:** Start with claude.ai browser interface (no setup)
2. **Developer learning AI:** Cursor (easiest powerful IDE experience)
3. **Developer with privacy needs:** Continue.dev + Ollama (local model option)
4. **Developer wanting maximum power:** Claude Code (deepest agentic capability)
5. **Building your own agent:** hermes-agent or LangChain (see [Bonus Topics](12-bonus-topics.md))

---

**Next:** [Security Best Practices](08-security.md)
