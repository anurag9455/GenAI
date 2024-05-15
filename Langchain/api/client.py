import requests
import streamlit as st

def get_llama(input_text):
    response=requests.post("http://localhost:1000/llama3/invoke",
                           json={
                               'input':{'topic':input_text}
                           }
                           )
    return response.json()['output']


st.title("Langchain Demo with LLAMA3")
input_text=st.text_input("Kindly give the question to solve: ")

if input_text:
    st.write(get_llama(input_text))