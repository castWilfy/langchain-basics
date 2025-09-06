from langchain_core.prompts import PromptTemplate

# Dynamic prompt template
prompt_template = PromptTemplate(
    input_variables=["book_name", "style", "length"],
    template = """
            You are a professional book summarizer. 
            
            Summarize the book "{book_name}" in a way that matches the following requirements:
            - Style: {style}
            - Length: {length}
            
            Ensure the summary is clear, engaging, and captures the core insights of the book.
            """,
    validate_template=True
)

prompt_template.save("prompts/template.json")