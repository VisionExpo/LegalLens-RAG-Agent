import streamlit as st
import requests
from pathlib import Path

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="SamvidAI", layout="wide")
st.title("🧠 SamvidAI — Contract Analysis")

st.markdown("Upload a contract and ask a legal question.")

# --- Upload ---
uploaded_file = st.file_uploader("Upload contract PDF", type=["pdf"])

question = st.text_input("Legal question", placeholder="e.g. What are the termination conditions?")

analyze = st.button("Analyze Contract")

if analyze:
    if not uploaded_file or not question:
        st.warning("Please upload a PDF and enter a question.")

    else:
        # Save uploaded file locally (Only for demo)
        data_dir = Path("data/ui_uploads")
        data_dir.mkdir(parents=True, exist_ok=True)
        pdf_path = data_dir / uploaded_file.name

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        payload = {
            "pdf_path": str(pdf_path),
            "question": question,
        }

        with st.spinner("Analyzing contract..."):
            resp = requests.post(
                f"{API_URL}/analyze-contract",
                json=payload,
                timeout=300,
            )

        if resp.status_code != 200:
            st.error(f"API error: {resp.text}")
        else:
            data = resp.json()

            st.subheader("✅ Answer")
            st.write(data["answer"])

            st.subheader("📌 Supporting Clauses")
            for c in data["retrieved_clauses"]:
                with st.expander(c["clause_id"]):
                    st.write(c["text"])