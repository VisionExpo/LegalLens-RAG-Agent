# 🧪 Testing Strategy & Plan

This document outlines the **testing philosophy, scope, and roadmap** for SamvidAI.

SamvidAI is a **multimodal, retrieval-augmented AI system**, where correctness depends on both
deterministic pipelines and probabilistic model behavior.  
Testing is therefore **layered, pragmatic, and staged**, rather than exhaustive from day one.

---

## 🎯 Testing Philosophy

- Test **what can deterministically fail**
- Avoid over-testing probabilistic LLM outputs
- Prioritize **pipeline stability, performance, and regressions**
- Add tests **after behavior stabilizes**, not before

> The goal is confidence, not 100% coverage.

---

## 🧱 Testing Layers

SamvidAI follows a **layered testing approach**:

1. **Unit Tests** – Deterministic components
2. **Integration Tests** – Pipeline interactions
3. **Regression Tests** – Behavioral consistency
4. **Performance Tests** – Latency & memory
5. **Manual / Human Validation** – LLM quality

---

## 🧪 Phase-Wise Testing Plan

### Phase 1 — Core Pipeline (Initial)

**Focus:** Deterministic correctness

Planned tests:
- PDF → image conversion
- File I/O validation
- Page count consistency
- Image resolution verification

Examples:
- Invalid PDF handling
- Corrupted input files
- Large document ingestion

---

### Phase 2 — Retrieval & Embeddings

**Focus:** Retrieval sanity & stability

Planned tests:
- Embedding generation does not crash
- Vector store insert / query works
- Top-K retrieval returns expected regions
- Empty or malformed queries

Notes:
- Retrieval quality is validated manually initially
- Numerical correctness > semantic perfection

---

### Phase 3 — Risk Engine

**Focus:** Rule-based logic correctness

Planned tests:
- Clause classification mapping
- Risk label assignment (Red / Amber / Green)
- Confidence score boundaries
- Missing clause detection

LLM output content is **not strictly asserted**.

---

### Phase 4 — Human-in-the-Loop Flow

**Focus:** System stability

Planned tests:
- Accept / reject actions do not crash
- Feedback is persisted correctly
- Session-level state consistency
- UI → backend interaction sanity

---

## 🔁 Regression Testing

Regression tests are added **once acceptable behavior is reached**.

Goals:
- Prevent token explosion
- Detect major latency regressions
- Ensure retrieval does not silently degrade

Regression signals:
- Sudden latency increase (>30%)
- Token count deviation
- VRAM usage spikes

---

## ⚙️ Performance & Resource Testing

Performance testing is **first-class**, not optional.

Tracked metrics:
- End-to-end latency
- Token count per query
- VRAM usage
- CPU memory usage

Target thresholds:
- Latency < 15s (120-page contract)
- VRAM < 8 GB
- Token usage reduction ≥ 60% vs full-text RAG

---

## 🧠 What We Do NOT Test Early

- Exact LLM wording
- Natural language creativity
- UI pixel-perfect rendering
- Model “correctness” in subjective outputs

These are validated through:
- Human review
- Qualitative evaluation
- Data reports

---

## 🛠️ Tools & Frameworks (Planned)

- `pytest` for unit and integration tests
- Lightweight fixtures for sample PDFs
- Manual evaluation for LLM outputs
- Simple logging-based assertions for performance

CI integration will be added once:
- Core pipelines stabilize
- Test suite becomes deterministic

---

## 📂 Future Test Structure
```
tests/
├── ingestion/
│ └── test_pdf_to_image.py
├── retrieval/
│ └── test_retriever.py
├── risk_engine/
│ └── test_scoring.py
├── performance/
│ └── test_latency.py
└── test_smoke.py
```
---

## 🧭 Final Note

Testing in SamvidAI is **intentional, staged, and pragmatic**.

The system prioritizes:
- Stability over premature coverage
- Performance over cosmetic correctness
- Human-validated intelligence over brittle assertions

This strategy ensures high confidence **without slowing down innovation**.