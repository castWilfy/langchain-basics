import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt

st.header("Book Summarizer")

# Input fields
book_name = st.selectbox("Select a book:", ["Atomic Habits", "To Kill a Mockingbird", "The Great Gatsby"])
style = st.selectbox("Choose explanation style:", ["Simple", "Detailed", "Storytelling", "Academic"])
length = st.selectbox("Choose explanation length:", ["Short (100 words)", "Medium (300 words)", "Long (500+ words)"])

api_key = st.text_input("Enter your Google API key:", type="password")
project_id = st.text_input("Enter your GCP project ID:")

template = load_prompt("prompts/template.json")

# Format user prompt
final_prompt = template.format(
    book_name=book_name,
    style=style,
    length=length
)

if st.button("Summarize"):
    if not api_key or not project_id:
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
            result = model.invoke(final_prompt)
            st.subheader("Summary")
            st.write(result.content)

        except Exception as e:
            st.error(f"An error occurred: {e}")
