# 🧠 SamvidAI – Low Level Design (LLD)

**Document Version:** 1.0  
**Status:** Draft  
**Owner:** Vishal Gorule  
**Last Updated:** 31/01/2026  

---

## Document Control

| Field | Value |
|------|------|
| Project Name | SamvidAI |
| Document Type | Low Level Design (LLD) |
| Version | 1.0 |
| Document Status | Draft |
| Confidentiality | Public |

---

## Revision History

| Version | Date | Description | Author |
|--------|------|-------------|--------|
| 1.0 | 30/01/2026 | Initial Low Level Design | Vishal Gorule |

---

## Table of Contents

1. Introduction  
2. Scope of Low Level Design  
3. System Context  
4. Detailed Component Design  
   - 4.1 Ingestion Module  
   - 4.2 Layout Analysis Module  
   - 4.3 Text Extraction Module  
   - 4.4 Embedding & Vector Store  
   - 4.5 Retrieval Engine  
   - 4.6 LLM Reasoning Engine  
   - 4.7 Risk Engine  
   - 4.8 Review & Feedback Module  
5. Data Models & Schemas  
6. API Design (FastAPI)  
7. Prompt Engineering Strategy  
8. Error Handling & Logging  
9. Performance & Optimization Details  
10. Security Implementation Notes  
11. Testing Strategy  
12. Deployment Implementation Details  
13. Limitations & Trade-offs  
14. Conclusion  

---

## 1. Introduction

This document presents the Low Level Design (LLD) for **SamvidAI**, an intelligent contract analysis system built using a vision-first, retrieval-augmented architecture (OpticalRAG).

While the High Level Design (HLD) defines *what* the system is and *why* it exists, this LLD focuses on *how* the system is implemented at a component, interface, and data-structure level.

---

## 2. Scope of Low Level Design

This LLD defines implementation-level details for all core SamvidAI components, including internal modules, APIs, data schemas, and operational behavior.

### In Scope
- Component responsibilities and interfaces  
- Data models and schemas  
- API definitions and contracts  
- Error handling, logging, and performance strategies  
- Deployment-level implementation considerations  

### Out of Scope
- Legal advice or legal correctness guarantees  
- UI/UX design specifications  
- Business policy decisions  
- Research benchmarking and experimentation  

---

## 3. System Context

SamvidAI operates as a modular backend system exposed via APIs and consumed by a UI.

External actors include:
- Legal professionals (users)
- External LLM providers
- Local or cloud infrastructure

Internal components communicate through explicit interfaces and never bypass validation or control layers.

---

## 4. Detailed Component Design

This section defines each major system component in execution order.  
All components follow these principles:
- Single responsibility  
- Explicit interfaces  
- Failure isolation  
- Traceability  
- Replaceability  

---

## 4.1 Ingestion Module

Responsible for accepting documents and converting them into normalized internal representations.

**Key Responsibilities**
- PDF validation
- Page image generation
- Metadata creation

**Output**
- Page images (300 DPI)
- Document metadata

---

## 4.2 Layout Analysis Module

Transforms page images into structured semantic regions using layout-aware vision models.

**Outputs**
- Region bounding boxes
- Region types
- Hierarchical relationships

This module preserves spatial and structural semantics.

---

## 4.3 Text Extraction Module

Performs region-level OCR to extract text aligned with layout structure.

**Key Characteristics**
- OCR per region (not full page)
- Conservative normalization
- Confidence scoring

---

## 4.4 Embedding & Vector Store

Converts region-level content into embeddings and indexes them for retrieval.

**Design Choices**
- Region-level embeddings
- Metadata-enriched vector entries
- Deterministic generation

---

## 4.5 Retrieval Engine

Selects the most relevant regions in response to user queries.

**Key Features**
- Query embedding
- Similarity search
- Hierarchical retrieval
- Strict context limits

---

## 4.6 LLM Reasoning Engine

Generates grounded explanations and summaries using retrieved regions only.

**Constraints**
- No full-document ingestion
- Structured outputs
- Explicit uncertainty signaling

LLMs are treated as probabilistic reasoning tools.

---

## 4.7 Risk Engine

Identifies and scores legal risks using hybrid rule-based and LLM-assisted logic.

**Risk Levels**
- High Risk
- Review Needed
- Standard

All outputs are advisory and require human validation.

---

## 4.8 Review & Feedback Module

Enforces mandatory human-in-the-loop validation.

**Reviewer Actions**
- Accept
- Reject
- Edit

Validated outputs are stored separately from raw AI outputs.

---

## 5. Data Models & Schemas

Core entities include:
- Document
- Page
- Region
- RegionText
- RegionEmbedding
- RetrievedRegion
- LLMOutput
- RiskFlag
- ReviewDecision
- ValidatedInsight

All models are versionable, traceable, and serializable.

---

## 6. API Design (FastAPI)

APIs expose ingestion, querying, risk analysis, and review workflows.

**Design Principles**
- Explicit schemas
- Versioned endpoints
- Stateless requests
- Predictable error handling

---

## 7. Prompt Engineering Strategy

Prompts are standardized, versioned, and safety-constrained.

**Key Rules**
- Retrieved context only
- Deterministic templates
- Structured outputs
- No speculation or legal advice

---

## 8. Error Handling & Logging

Errors are explicit, categorized, and isolated.

**Features**
- Standard error models
- Structured logging
- Request correlation IDs
- User-safe error messages

---

## 9. Performance & Optimization Details

Performance is optimized through:
- One-time preprocessing
- Region-level computation
- Aggressive caching
- Strict LLM input limits

Accuracy and explainability are prioritized over speed.

---

## 10. Security Implementation Notes

Security principles include:
- Least privilege
- Data minimization
- Controlled LLM boundaries
- Secure file handling
- Restricted logging

No sensitive content is logged or unnecessarily transmitted.

---

## 11. Testing Strategy

Testing is multi-layered:
- Unit tests
- Integration tests
- API tests
- Model behavior tests
- End-to-end workflows

Synthetic and public documents are used exclusively.

---

## 12. Deployment Implementation Details

Supported deployment models:
- Local
- Cloud
- Hybrid

Deployment uses containerization, environment-based configuration, and explicit startup validation.

---

## 13. Limitations & Trade-offs

Known limitations include:
- AI model uncertainty
- Layout dependency
- Hardware constraints
- Mandatory human review overhead

These trade-offs are intentional and transparent.

---

## 14. Conclusion

This Low Level Design provides a complete, implementation-ready blueprint for SamvidAI. By combining disciplined engineering, OpticalRAG principles, and human-in-the-loop validation, the system balances capability with trust, safety, and real-world legal applicability.

> This document serves as the authoritative reference for building, operating, and evolving SamvidAI.