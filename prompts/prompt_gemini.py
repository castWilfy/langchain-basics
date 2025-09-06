import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.header("Research Tool")

# Input fields
user_input = st.text_input("Enter your prompt:")
api_key = st.text_input("Enter your Google API key:", type="password")
project_id = st.text_input("Enter your GCP project ID:")

if st.button("Summarize"):
    if not user_input or not api_key or not project_id:
        st.warning("Please provide prompt, API key, and project ID.")
    else:
        try:
            # Initialize the model
            model = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0,
                google_api_key=api_key,
                project=project_id
            )
            
            # Get the result
            result = model.invoke(user_input)
            st.subheader("Summary")
            st.write(result.content)

        except Exception as e:
            st.error(f"An error occurred: {e}")
