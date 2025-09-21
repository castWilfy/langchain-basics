from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated

api_key = input("Enter your Google API key:")
project_id = input("Enter your GCP project ID:")

model = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0,
                google_api_key=api_key,
                project=project_id
)

# Schema definition using TypedDict
class Review(TypedDict):
    summary: Annotated[str, "Concise summary of the review"]
    sentiment: Annotated[str, "Overall sentiment of the review, e.g., positive, negative, neutral"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hotel was fantastic! The staff were incredibly helpful""")

print(result['summary'])
print(result['sentiment'])