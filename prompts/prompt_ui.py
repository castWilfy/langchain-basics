import getpass
import os
import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

st.header ("Research Tool")

user_input = st.text_input("Enter your prompt:")
key = st.text_input("Enter your Hugging Face API key:", type="password")

if st.button('Summerize'):
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = key
    
    llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  # let Hugging Face choose the best provider for you
)
    model = ChatHuggingFace(llm=llm)
    result = model.invoke(user_input)
    st.write(result.content)
    