from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

chat_template = ChatPromptTemplate.from_messages([
    ('system', "You are a helpful {domain} expert"),
    ('human', "Summarize the book '{book_name}' in a way that matches the following requirements:\n- Style: {style}\n- Length: {length}\n\nEnsure the summary is clear, engaging, and captures the core insights of the book.")
])

prompt = chat_template.invoke({
    
    "domain": "book summarization",
    "book_name": "Atomic Habits",
    "style": "Detailed",
    "length": "Medium (300 words)"  
    })

print(prompt)  # This will print the formatted messages