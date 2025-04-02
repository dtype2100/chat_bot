import streamlit as st

def prompt_input():
    """사용자 프롬프트 입력 박스"""
    return st.text_area("프롬프트를 입력하세요", height=150)
