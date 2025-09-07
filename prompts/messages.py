from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI


api_key = input("Enter your Google API key:")
project_id = input("Enter your GCP project ID:")

model = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0,
                google_api_key=api_key,
                project=project_id
)

messages = [
    SystemMessage(content="You are a helpful assistant that summarizes books."),
    HumanMessage(content="Summarize the book 'Atomic Habits' in a way that is clear, engaging, and captures the core insights of the book."),
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)