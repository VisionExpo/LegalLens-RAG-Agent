import json
import time
import statistics
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List

# ---- CONFIG ---- #

GOLDEN_DOCS_DIR = Path("evaluation/golden_docs")
RUNS_DIR = Path("evaluation/runs")
RUNS_DIR.mkdir(parents=True, exist_ok=True)

TOP_K = 5

# Fixed evaluation queries (DO NOT change once frozen)
EVAL_QUERIES = [
    "termination clause",
    "payment terms",
    "arbitration clause",
    "penalty and liquidated damages",
    "dispute resolution"
]

# ---- IMPORT PIPELINE COMPONENTS ---- #

from samvidai.ingestion.loader import load_pdf
from samvidai.layout.chunker import chunk_document
from samvidai.retrieval.embedding import EmbeddingModel
from samvidai.retrieval.vector_store import FAISSStore
from samvidai.risk_engine.classifier import RiskClassifier
from samvidai.risk_engine.scorer import RiskScorer


# ---- HELPERS ---- #

def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()[:12]


def percentile(values: List[float], p: int) -> float:
    if not values:
        return 0.0
    values = sorted(values)
    k = int(len(values) * p / 100)
    return values[min(k, len(values) - 1)]


# ---- EVALUATION ---- #

def evaluate_document(pdf_path: Path) -> Dict:
    timings = []
    retrieval_counts = []
    risk_scores = []

    # Ingest
    text_pages = load_pdf(pdf_path)

    # Chunk
    chunks = chunk_document(text_pages)

    # Embed + Index
    embedder = EmbeddingModel()
    vectors = embedder.encode([c.text for c in chunks])

    store = FAISSStore(embedder.dim)
    store.add(vectors, chunks)

    classifier = RiskClassifier()
    scorer = RiskScorer()

    for query in EVAL_QUERIES:
        start = time.time()

        q_vec = embedder.encode([query])[0]
        results = store.search(q_vec, top_k=TOP_K)

        latency = (time.time() - start) * 1000
        timings.append(latency)
        retrieval_counts.append(len(results))

        # Risk evaluation (deterministic)
        clause_risks = [classifier.classify(r.text) for r in results]
        score = scorer.score(clause_risks)
        risk_scores.append(score)

    return {
        "latency": {
            "p50_ms": round(percentile(timings, 50), 2),
            "p95_ms": round(percentile(timings, 95), 2)
        },
        "retrieval": {
            "avg_top_k": round(statistics.mean(retrieval_counts), 2),
            "empty_rate": retrieval_counts.count(0) / len(retrieval_counts)
        },
        "risk_engine": {
            "avg_score": round(statistics.mean(risk_scores), 2),
            "stddev": round(statistics.pstdev(risk_scores), 2)
        }
    }


# ---- MAIN ---- #

def main():
    run = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "documents": [],
    }

    for pdf in GOLDEN_DOCS_DIR.glob("*.pdf"):
        metrics = evaluate_document(pdf)
        run["documents"].append({
            "file": pdf.name,
            "hash": file_hash(pdf),
            **metrics
        })

    # Aggregate summary
    latencies = [d["latency"]["p50_ms"] for d in run["documents"]]
    run["summary"] = {
        "documents_tested": len(run["documents"]),
        "avg_p50_latency_ms": round(statistics.mean(latencies), 2),
    }

    # Save run
    ts = datetime.utcnow().strftime("%Y-%m-%d")
    out_file = RUNS_DIR / f"{ts}.json"
    with open(out_file, "w") as f:
        json.dump(run, f, indent=2)

    # Update latest.json
    with open(RUNS_DIR / "latest.json", "w") as f:
        json.dump(run, f, indent=2)

    print(f"✅ Evaluation completed: {out_file}")


if __name__ == "__main__":
    main()
