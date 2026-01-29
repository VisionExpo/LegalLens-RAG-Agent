import os

# Root-level structure
STRUCTURE = {
    "docs": [
        "HLD.md",
        "LLD.md",
        "ARCHITECTURE.md",
        "PIPELINE.md",
        "DATA_REPORTS.md",
        "EXPERIMENTS.md",
        "BENCHMARKS.md",
        "SECURITY.md",
        "ETHICS.md",
    ],
    "research": [
        "related_work.md",
        "papers.md",
        "findings.md",
    ],
    "product": [
        "roadmap.md",
        "monetization.md",
        "user_personas.md",
        "go_to_market.md",
    ],
    "src/samvidai/ingestion": [
        "__init__.py",
        "pdf_to_image.py",
        "preprocess.py",
    ],
    "src/samvidai/layout": [
        "__init__.py",
        "layoutlm.py",
    ],
    "src/samvidai/retrieval": [
        "__init__.py",
        "embeddings.py",
        "vector_store.py",
        "retriever.py",
    ],
    "src/samvidai/risk_engine": [
        "__init__.py",
        "classifier.py",
        "scorer.py",
    ],
    "src/samvidai/llm": [
        "__init__.py",
        "prompts.py",
        "inference.py",
    ],
    "src/samvidai/utils": [
        "__init__.py",
        "logger.py",
    ],
    "api": [
        "main.py",
    ],
    "ui": [
        "streamlit_app.py",
    ],
    "assets/images": [],
    "assets/videos": [],
    "assets/diagrams": [],
    "tests": [],
    "docker": [
        "Dockerfile",
    ],
}

ROOT_FILES = [
    "WEBSITE.md",
    "DEMO.md",
    "requirements.txt",
]

PLACEHOLDER_CONTENT = {
    ".md": "# TODO\n\nThis document will be updated.\n",
    ".py": "# TODO: Implement\n",
    "Dockerfile": "# TODO: Docker configuration\n",
    "requirements.txt": "# Add dependencies here\n",
}


def create_file(path, filename):
    full_path = os.path.join(path, filename)
    if os.path.exists(full_path):
        return

    ext = filename.split(".")[-1]
    content = PLACEHOLDER_CONTENT.get(
        f".{ext}", PLACEHOLDER_CONTENT.get(filename, "")
    )

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    print("🚀 Creating SamvidAI repository structure...\n")

    # Create folders and files
    for folder, files in STRUCTURE.items():
        os.makedirs(folder, exist_ok=True)
        for file in files:
            create_file(folder, file)

    # Create root-level files
    for file in ROOT_FILES:
        create_file(".", file)

    # Ensure __init__.py exists at package root
    os.makedirs("src/samvidai", exist_ok=True)
    create_file("src/samvidai", "__init__.py")

    print("✅ Repository structure created successfully!")
    print("📁 You are ready to start building SamvidAI.")


if __name__ == "__main__":
    main()
