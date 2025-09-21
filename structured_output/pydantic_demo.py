from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field, EmailStr

api_key = input("Enter your Google API key:")
project_id = input("Enter your GCP project ID:")

model = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0,
                google_api_key=api_key,
                project=project_id
)


# 1. Define structured schema
class Review(BaseModel):
    summary: str = Field(description="Concise summary of the review")
    sentiment: str = Field(description="Overall sentiment: positive, negative, or neutral")
    email: EmailStr = Field(default='abc@gmail.com', description="Email address of the reviewer")
# 2. Wrap with structured output
structured_model = model.with_structured_output(Review)

# 3. Invoke model
result = structured_model.invoke(
    "The hotel was fantastic! The staff were incredibly helpful"
)

# 4. Access fields
print(result.summary)     # dot notation
print(result.sentiment)