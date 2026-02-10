import sys
import os
import streamlit as st

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from ui.api_client import analyze_contract


st.set_page_config(page_title="SamvidAI", layout="wide")

st.title("🧠 SamvidAI – Contract Risk Analyzer")

contract_text = st.text_area(
    "Paste contract text",
    height=250,
    placeholder="Paste procurement / legal contract here..."
)

if st.button("Analyze Contract"):
    if not contract_text.strip():
        st.warning("Please paste a contract.")
    else:
        with st.spinner("Analyzing contract..."):
            try:
                result = analyze_contract(contract_text)

                st.metric("Risk Level", result["risk_level"])
                st.metric("Risk Score", result["risk_score"])

                st.subheader("⚠️ Risk Flags")
                for flag in result["flags"]:
                    st.write(f"- {flag}")

            except Exception as e:
                st.error("Backend unavailable. Showing demo result.")
