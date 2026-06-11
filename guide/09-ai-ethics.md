# 09 — AI Ethics: Building and Using AI Responsibly

AI tools reflect the values of those who build and use them. Understanding the ethical dimensions isn't just about avoiding harm — it's about building trust with the people your work affects.

---

## Why AI Ethics Matters in Practice

Ethics in AI isn't abstract philosophy. It has real-world consequences:

- A hiring algorithm that discriminates based on gender
- A facial recognition system with much higher error rates for darker skin tones
- A medical AI that gives different quality advice based on a patient's postcode
- A chatbot that confidently fabricates legal advice

These failures damage individuals, create legal liability, and erode public trust in AI systems. IT professionals who build and deploy AI systems share responsibility for these outcomes.

---

## Bias and Fairness

**What it is:** AI models learn patterns from training data. If that data reflects historical biases, the model will too.

**Examples of bias in AI:**
- Image classifiers that associate "doctor" with men and "nurse" with women
- Loan models that penalise postcodes (which correlate with race) without explicitly considering race
- Resume screeners trained on historical hiring that perpetuate past discrimination

**What you can do:**
- Test your AI system across demographic groups before deployment
- Ask: "Who does this harm if it gets it wrong?"
- Use diverse, representative training data when fine-tuning
- Apply fairness metrics (demographic parity, equalized odds) to evaluate models

---

## Hallucinations and Truthfulness

LLMs generate plausible-sounding text — they don't actually "know" things the way humans do. They can and do generate false information with complete confidence.

**This matters when:**
- Using AI for legal research (it will cite cases that don't exist)
- Generating medical information
- Creating code for security-sensitive systems
- Building customer-facing responses that could be relied upon

**Mitigation:**
- Always verify AI-generated facts against authoritative sources
- Use RAG (Retrieval-Augmented Generation) to ground the model in real documents
- Be transparent with users when they're interacting with AI
- Build in human review for high-stakes outputs

---

## Consent and Transparency

**Do users know they're talking to AI?** In many countries and contexts, failing to disclose AI involvement is a legal and ethical problem.

- In customer service: users have a right to know
- In generated content: consider whether readers should know it's AI-written
- In research: participants should know if AI analysed their data

**The EU AI Act** (effective 2026) requires transparency when interacting with AI systems in many contexts. See [AI Governance](10-ai-governance.md) for more.

---

## Copyright and Intellectual Property

AI models are trained on massive datasets that include copyrighted content. This creates unresolved legal questions:

- Can AI-generated code reproduce copyrighted code?
- Who owns the copyright in AI-generated content?
- Does AI training on copyrighted data constitute infringement?

**Practical guidance:**
- Don't use AI-generated content in contexts where provenance is legally important without understanding the risk
- Review AI-generated code for licence conflicts (GitHub Copilot has a setting to filter suggestions matching public code)
- Keep humans in the loop for any content that will be published or legally relied upon

---

## Accessibility

AI tools can increase or reduce accessibility:

**Increasing:**
- Generating alt text for images
- Converting complex documents to plain language
- Real-time captioning and translation
- Helping people with reading difficulties understand text

**Reducing:**
- AI tools that assume high literacy
- Voice-only AI interfaces that exclude deaf users
- Tools that assume fast internet and modern hardware

**Design principle:** Consider how your AI system works for users with disabilities, older hardware, or limited connectivity.

---

## Environmental Impact

Training large AI models consumes significant energy and water. A single training run for a frontier model can emit as much CO₂ as several transatlantic flights — or more.

**Inference** (using the model) is less intensive but adds up at scale.

**Practical considerations:**
- Using efficient models (smaller, quantised local models) when frontier capability isn't needed reduces impact
- Some providers publish environmental commitments; Anthropic and Google have made carbon neutrality pledges
- For high-volume applications, the environmental cost of millions of API calls is worth considering in architecture decisions

---

## Autonomy and Human Oversight

As AI systems become more agentic (taking actions rather than just generating text), maintaining meaningful human oversight becomes critical.

**Questions to ask:**
- What decisions is the AI making autonomously?
- What are the consequences of a wrong decision?
- Is there a human who can review, override, or stop the AI?
- What's the audit trail?

For low-stakes tasks (formatting a document, summarising a meeting), autonomous AI is appropriate. For high-stakes tasks (financial transactions, medical advice, legal action), human oversight is essential.

---

## Core Ethical Principles Summary

| Principle | What It Means |
|-----------|--------------|
| Fairness | Don't discriminate; test across groups |
| Transparency | Be honest about AI involvement |
| Accountability | Have a human responsible for AI decisions |
| Privacy | Handle data with care; minimise collection |
| Safety | Test for harmful outputs before deployment |
| Reliability | Validate outputs; don't deploy if it hallucinates dangerously |

---

**Next:** [AI Governance](10-ai-governance.md)
