import streamlit as st

def response_output(output_text):
    """LLM 응답 출력"""
    st.markdown("### 📢 응답")
    st.success(output_text)
