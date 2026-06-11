# 06 — Subscription Packages: Claude Pro, ChatGPT Plus, and More

Before building anything with an API, many people start with a subscription package. This chapter explains what you get, what the limits are, and when it's time to move to the API.

---

## Claude Pro (Anthropic)

**Price:** ~$20 USD/month (individual), ~$25/user/month (Teams)

### What You Get
- Access to all Claude models including Opus (the most powerful)
- Claude.ai web interface + Claude Desktop app
- Priority access during high demand
- Projects feature (persistent conversations with custom context)
- File uploads (PDFs, images, code files)
- MCP server support via Claude Desktop

### Usage Limits

Claude Pro uses an **active usage model** rather than a fixed message count. The key thing to understand:

- **Session active time** is measured — roughly 5 hours of heavy usage before you hit a temporary limit
- After hitting a limit, you're queued or asked to wait (typically a few hours)
- **Lighter usage** (reading, shorter prompts, fewer messages) makes your allowance go much further
- Limits reset regularly (not a strict monthly cap)

**Practical meaning for IT professionals:** For a normal working day of mixed AI use, Pro limits are rarely a problem. If you're stress-testing with hundreds of long messages, you may hit them.

### Teams Plan

For organisations: adds central billing, admin controls, and slightly higher usage limits. Data is not used for training (unlike the free tier). Essential if you're using Claude in a work context.

---

## ChatGPT Plus (OpenAI)

**Price:** ~$20 USD/month

### What You Get
- GPT-4o access (multimodal: text, vision, voice)
- o3-mini access (reasoning model)
- DALL-E 3 image generation
- Advanced Data Analysis (code interpreter)
- Custom GPTs (configure your own assistant)
- 100+ plugins/integrations
- Browsing capability (real-time web search)

### Usage Limits
- GPT-4o: ~80 messages per 3 hours on Plus (reverts to GPT-3.5 when exceeded)
- o3-mini: Limited messages per month (exact number changes; check openai.com)
- Image generation: ~40 images per day

**Practical meaning:** 80 messages per 3 hours is enough for normal use but can be hit quickly in intensive work sessions.

---

## Gemini Advanced (Google)

**Price:** Included with Google One AI Premium (~$20 USD/month, also includes 2TB Drive storage)

### What You Get
- Gemini 2.0 Ultra access
- Integration with Gmail, Docs, Drive, Meet
- 1M token context window (can analyse entire books)
- Image generation (Imagen 3)
- Deep Research mode (autonomous multi-step research)

### Usage Limits
- Less clearly documented than competitors; generally generous for typical use
- Google One plan also provides significant Google Drive storage, making it good value if you're in the Google ecosystem

**Best for:** People already using Google Workspace, or who need very long context windows.

---

## Comparing the Three

| Feature | Claude Pro | ChatGPT Plus | Gemini Advanced |
|---------|-----------|-------------|-----------------|
| Price/month | $20 | $20 | $20 |
| Best model | Opus 4.8 | GPT-4o / o3 | Gemini 2.0 Ultra |
| Context window | 200K tokens | 128K tokens | 1M tokens |
| Image generation | No | Yes (DALL-E 3) | Yes (Imagen 3) |
| Web browsing | Limited | Yes | Yes |
| Code interpreter | No | Yes | Yes |
| MCP support | Yes (Desktop) | Limited | No |
| Data training | No (Pro) | Opt-out available | Opt-out available |

---

## When to Move from Subscription to API

Subscriptions are great for individuals. Move to the API when:

1. **You're building an application** — subscriptions are for human users, not automated pipelines
2. **You need more control** — custom `max_tokens`, `temperature`, system prompts
3. **You need higher volume** — API rate limits are configurable vs. fixed subscription limits
4. **You need to integrate with your codebase** — API is the only option for programmatic use
5. **You need fine-grained cost tracking** — API usage is metered by token

**Getting started with the API:**
- Anthropic: console.anthropic.com (create API key, ~$5 minimum credit)
- OpenAI: platform.openai.com
- Google: aistudio.google.com

---

## A Note on Free Tiers

All three services offer free access with lower capabilities:
- **Claude.ai free:** Claude Sonnet with daily message limits
- **ChatGPT free:** GPT-4o with heavy rate limits; falls back to GPT-3.5
- **Gemini free:** Gemini 1.5 Flash

Free tiers are fine for learning and light personal use. **Do not use free tiers with any client or confidential data** — check the provider's data use policies carefully, as free tier data may be used for model training.

---

**Next:** [AI Harness Options](07-harness-options.md)
