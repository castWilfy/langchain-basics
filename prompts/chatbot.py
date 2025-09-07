from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


api_key = input("Enter your Google API key:")
project_id = input("Enter your GCP project ID:")

model = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0,
                google_api_key=api_key,
                project=project_id
)

chat_history = [
    SystemMessage(content="You are a helpful assistant that summarizes books.")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break

    if not user_input or not api_key or not project_id:
        print("Please provide prompt, API key, and project ID.")
    else:
        try:
            # Get the result
            result = model.invoke(chat_history)
            chat_history.append(AIMessage(content=result.content))
            print("AI: ", result.content)

        except Exception as e:
            print(f"An error occurred: {e}")