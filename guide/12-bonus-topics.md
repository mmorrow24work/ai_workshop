# 12 — Bonus Topics: Three Areas Every AI Practitioner Should Know

These three topics didn't fit neatly in earlier chapters but are essential for anyone who wants to move beyond basic AI usage into building real systems.

---

## Topic 1: Prompt Engineering

### What It Is

Prompt engineering is the practice of crafting inputs to LLMs that reliably produce the outputs you want. It sounds trivial — but a well-engineered prompt can be the difference between a model that's useful and one that's frustrating.

### Why It Matters

The same model with different prompts can produce wildly different quality outputs. Prompt engineering is a skill that pays dividends immediately, whether you're using AI for personal productivity or building AI-powered applications.

### Core Techniques

**1. Be Specific**
```
Bad:  "Write about climate change."
Good: "Write a 3-paragraph summary of the main causes of climate change, 
       suitable for a Year 10 student. Use plain language and no jargon."
```

**2. Assign a Role (System Prompt)**
```
System: "You are a senior software architect with 20 years of experience 
         in Python and cloud infrastructure. Be concise and precise."
User: "Review this code for performance issues."
```

**3. Few-Shot Examples**
Give the model 2-3 examples of the pattern you want before asking it to do the task:
```
Q: What is the capital of France? A: Paris
Q: What is the capital of Japan? A: Tokyo
Q: What is the capital of Brazil? A: [model fills in correctly]
```

**4. Chain-of-Thought (CoT)**
Ask the model to think step by step before giving an answer — dramatically improves reasoning:
```
"Before answering, think through this step by step. 
 Show your working. Then give your final answer."
```

**5. Structured Output**
Tell the model exactly what format you want:
```
"Return your answer as JSON with the following fields: 
 { 'summary': string, 'confidence': 0-100, 'sources': [string] }"
```

**6. Constraint Setting**
```
"Answer in under 150 words. Do not mention specific brand names. 
 If you don't know, say 'I don't know' rather than guessing."
```

### Prompt Engineering for Applications

When building AI applications, your system prompt is your most important piece of code. Structure it as:

1. **Role:** Who the AI is in this context
2. **Context:** What it needs to know about your system/data
3. **Instructions:** Specific rules and behaviours
4. **Output format:** Exactly what you want returned
5. **Constraints:** What it must never do

**Resource:** Anthropic Prompt Engineering Guide (docs.anthropic.com/prompt-engineering)

---

## Topic 2: RAG — Retrieval-Augmented Generation

### What It Is

RAG is a technique that gives LLMs access to information from a specific document collection at query time, rather than relying only on what was in the training data.

**The problem it solves:** LLMs are trained on data up to a cutoff date and don't know your internal documents. RAG lets you ask: "What does our policy say about X?" and get an accurate answer grounded in your actual documents.

### How RAG Works

```
1. INDEXING (done once):
   Your documents → Split into chunks → Generate embeddings → Store in vector database

2. QUERYING (done at runtime):
   User question → Generate embedding → Find similar chunks → 
   Include chunks in prompt → LLM answers using the retrieved context
```

### Key Components

**Embedding Model**
Converts text into a vector (list of numbers) that captures semantic meaning. Similar text produces similar vectors.

```python
# Example using Ollama's embedding model
import requests

response = requests.post("http://localhost:11434/api/embeddings", json={
    "model": "nomic-embed-text",
    "prompt": "How do I reset my password?"
})
embedding = response.json()["embedding"]  # List of 768 numbers
```

**Vector Database**
Stores embeddings and allows fast similarity search.

Popular options:
- **ChromaDB** — Simple, local, great for getting started
- **Pinecone** — Managed cloud service, production-ready
- **Weaviate** — Open-source, feature-rich
- **pgvector** — PostgreSQL extension (if you already use Postgres)
- **Qdrant** — High-performance, open-source

**Retrieval**
Given a user query, embed it and find the most semantically similar chunks from your document store.

### Simple RAG Example

```python
import chromadb
from anthropic import Anthropic

# Setup (do once)
chroma_client = chromadb.Client()
collection = chroma_client.create_collection("company_docs")

# Add documents (simplified)
collection.add(
    documents=["Our refund policy is 30 days...", "Password reset requires..."],
    ids=["doc1", "doc2"]
)

# At query time
anthropic = Anthropic()
user_question = "How do I get a refund?"

results = collection.query(query_texts=[user_question], n_results=2)
context = "\n".join(results["documents"][0])

message = anthropic.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": f"Context:\n{context}\n\nQuestion: {user_question}"
    }]
)
print(message.content[0].text)
```

### When to Use RAG

- Company knowledge bases and internal documentation
- Customer support with product manuals
- Legal or policy Q&A over specific documents
- Any application where the LLM needs facts from specific, updateable documents

---

## Topic 3: AI Agents and Agentic Systems

### What Is an AI Agent?

An AI agent is an LLM that can:
1. **Plan** a sequence of steps to achieve a goal
2. **Use tools** (search the web, read files, call APIs, run code)
3. **Observe results** of those tool calls
4. **Iterate** — adjust its plan based on what it learns

Traditional LLM: You ask → It answers. Single turn.  
AI Agent: You give a goal → It plans → It acts → It checks → It refines → It reports. Multiple turns.

### The Core Loop

```
Goal → Plan → Act → Observe → [Done? → Report] or [Not done? → Revise plan → Act again]
```

### Tool Use (Function Calling)

Agents use tools by calling functions. The LLM generates a structured request; your code executes it.

```python
import anthropic

tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"}
            },
            "required": ["city"]
        }
    }
]

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in Sydney?"}]
)

# If model wants to use a tool, it returns tool_use content
if response.stop_reason == "tool_use":
    tool_call = response.content[0]
    # Your code executes: get_weather(city=tool_call.input["city"])
    # Then feed result back to the model
```

### Real-World Agent Examples

**Claude Code:** An agent that:
- Plans what files to read/edit to accomplish a coding task
- Reads relevant files
- Writes code changes
- Runs tests to verify the changes
- Commits the result

**AutoGPT:** An early open-source agent that set the pattern for autonomous task execution.

**OpenDevin:** An open-source software engineering agent that can browse the web, write code, and run programs.

### Multi-Agent Systems

Complex tasks can be split across multiple specialised agents:

```
Orchestrator Agent
├── Research Agent (web browsing, information gathering)
├── Analysis Agent (processes gathered information)
├── Writing Agent (produces final document)
└── Review Agent (checks and improves the output)
```

Anthropic's model context protocol (MCP) and multi-agent frameworks make this increasingly practical.

### Key Considerations for Agents

**Safety:** Agents can take real-world actions. Add guardrails:
- Require human confirmation for destructive or irreversible actions
- Limit the scope of what tools agents can access
- Log all agent actions for auditability

**Reliability:** Agents can get stuck in loops, make wrong assumptions, or misinterpret goals. Design for failure:
- Set maximum iteration limits
- Build in checkpoints for human review
- Test extensively before deploying to production

**Cost:** Agentic workflows use many more tokens than single-turn queries. Monitor costs carefully.

---

## Further Reading

- Anthropic Cookbook (GitHub: anthropics/anthropic-cookbook) — Practical examples for all three topics
- LangChain documentation — Popular framework for building RAG and agent applications
- LlamaIndex documentation — Specialises in data ingestion and retrieval for LLMs
- "Building LLM Applications" course on DeepLearning.ai

---

*You've reached the end of the Zero to Hero guide. Check the [Resources](../resources/) folder for YouTube channels and inspiring AI projects.*
