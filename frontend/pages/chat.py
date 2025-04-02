import streamlit as st
import requests, os, sys
from components.input_box import prompt_input
from components.output_box import response_output

st.header("🤖 질문하기")

prompt = prompt_input()

if st.button("질문하기"):
    response = requests.post("http://127.0.0.1:8000/generate", json={"prompt": prompt})
    if response.status_code == 200:
        answer = response.json()["response"]
        response_output(answer)
    else:
        st.error("백엔드에서 응답을 가져오지 못했습니다.")
