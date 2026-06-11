# 10 — AI Governance: Regulations, Frameworks, and Compliance

AI governance is moving from optional best practice to legal requirement. This chapter gives IT professionals the key frameworks they need to know.

---

## Why Governance Matters for IT Teams

Even if you're not a policy expert, you need to know:
- What regulations apply to AI you build or use
- What your organisation must document and report
- Where liability sits when AI systems cause harm
- How to advise clients on responsible AI deployment

---

## EU AI Act

**Status:** In force from August 2024; key requirements phased in through 2026-27

The EU AI Act is the world's first comprehensive AI regulation. It applies to any AI system used in the EU, regardless of where the developer is based.

### Risk Classification

The Act classifies AI systems by risk level:

| Risk Level | Examples | Requirements |
|------------|----------|--------------|
| Unacceptable | Social scoring, real-time biometric surveillance | **Banned** |
| High risk | Hiring, credit scoring, medical devices, critical infrastructure | Strict requirements |
| Limited risk | Chatbots, deepfakes | Transparency obligations |
| Minimal risk | Spam filters, AI-powered games | No specific requirements |

### High-Risk AI Requirements

If your AI system is classified as high-risk, you must:
- Maintain technical documentation
- Implement human oversight mechanisms
- Ensure data governance and data quality
- Conduct conformity assessments
- Register in the EU database
- Log decisions for auditability

### GPAI (General Purpose AI) Rules

Large foundation models (like GPT-4, Claude) have specific rules:
- Must provide technical documentation to downstream users
- Models capable of "systemic risk" (largest models) face additional obligations
- Transparency about training data usage

**Practical implication:** If you're building applications on top of foundation models for EU users, check whether your use case falls in the high-risk category.

---

## NIST AI Risk Management Framework (AI RMF)

**Origin:** US National Institute of Standards and Technology  
**Status:** Voluntary (but increasingly referenced in US federal procurement)

The NIST AI RMF organises AI governance around four functions:

1. **GOVERN:** Establish policies, culture, and accountability for AI risk
2. **MAP:** Identify and categorise AI risks in your context
3. **MEASURE:** Analyse and assess those risks
4. **MANAGE:** Prioritise and treat AI risks

This is a practical framework for organisations that want structured AI governance without waiting for legislation. Many US federal agencies and contractors are adopting it.

---

## ISO/IEC 42001 — AI Management System Standard

**Published:** 2023  
**Type:** Certifiable management system standard (like ISO 27001 for information security)

ISO 42001 helps organisations establish, implement, and improve an AI management system. It covers:
- AI policy and governance structure
- Risk assessment for AI systems
- Responsible AI objectives
- Supplier and third-party AI management
- Incident response for AI failures

**Why it matters:** ISO 42001 certification is becoming a differentiator for AI vendors and a requirement in some procurement processes, particularly in healthcare, finance, and government.

---

## GDPR and AI

The EU's General Data Protection Regulation (GDPR) predates the AI Act but applies to AI systems that process personal data.

**Key GDPR provisions for AI:**

| Article | Relevance to AI |
|---------|----------------|
| Art. 5 | Data minimisation — don't collect more than needed for training |
| Art. 13-14 | Transparency — tell people when automated decisions affect them |
| Art. 22 | Right not to be subject to purely automated decisions with legal effect |
| Art. 25 | Privacy by design — build data protection into AI systems from the start |
| Art. 35 | DPIA — Data Protection Impact Assessment required for high-risk processing |

**Practical implication:** If your AI system makes decisions about individuals (hiring, lending, healthcare triage), you likely need a DPIA and may need to offer a human review process.

---

## Australia: Privacy Act and AI

Australia's Privacy Act 1988 and its Australian Privacy Principles (APPs) apply to AI systems that handle personal information about Australians.

Key considerations:
- APP 3: Only collect personal information that's reasonably necessary
- APP 5: Tell people why you're collecting their information
- APP 11: Take reasonable steps to protect personal information
- The Privacy Act reforms (ongoing) are moving toward stronger AI-specific rules

The Australian government has also published a **Voluntary AI Safety Standard** (2024) with guidance for responsible AI deployment.

---

## Sector-Specific Regulations

AI in certain sectors faces additional rules:

| Sector | Key Regulations |
|--------|----------------|
| Healthcare | TGA oversight for software as medical devices (Australia); FDA (US) |
| Financial services | ASIC guidance (Australia); SEC/FINRA (US); FCA (UK) |
| Employment | Fair Work Act considerations; discrimination law |
| Education | Student data privacy regulations |
| Government | Public sector AI governance frameworks |

---

## Building a Responsible AI Policy for Your Organisation

A minimal responsible AI policy should cover:

1. **Approved use cases** — what AI is permitted for
2. **Prohibited use cases** — what AI must not do
3. **Data classification** — what data can be processed by which AI tools
4. **Approved tools** — vetted and approved AI tools list
5. **Human oversight requirements** — when human review is mandatory
6. **Incident response** — what to do when AI causes harm
7. **Training requirements** — who needs AI ethics training
8. **Review cadence** — how often the policy is updated

---

## Quick Compliance Checklist

Before deploying an AI system:

- [ ] Identify the risk level under EU AI Act (if applicable)
- [ ] Conduct a Data Protection Impact Assessment if handling personal data
- [ ] Document the AI system's purpose, data inputs, and decision outputs
- [ ] Establish human oversight for high-risk decisions
- [ ] Create an audit trail for AI decisions
- [ ] Brief staff on acceptable use
- [ ] Set a review date for the governance assessment

---

**Next:** [Staying Current with AI News](11-ai-news.md)
