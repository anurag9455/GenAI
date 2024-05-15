
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# ##
# print("Hello")
# from langchain_community.llms import Ollama

# llm = Ollama(model="llama3")
# llm.invoke("Tell me a joke")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a coding assistant for python interview questions. Please respond by giving them code accordingly"),
        ("user","Question:{question}")
    ]
)
st.title("Langchain Demo with LLAMA3")
input_text=st.text_input("Kindly give the question to solve: ")

ollama_llm = Ollama(model="llama3")
parser = StrOutputParser()
chain = prompt|ollama_llm|parser

if input_text:
    st.write(chain.invoke({"question":input_text}))