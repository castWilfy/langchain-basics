from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

api_key = input("Enter your Google API key:")
project_id = input("Enter your GCP project ID:")

model = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0,
                google_api_key=api_key,
                project=project_id
)

prompt = PromptTemplate(
    input_variables=["product"],
    template="Give three reasons to buy {product}.")

# Use StrOutputParser to get a simple string output
output_parser = StrOutputParser()

chain = prompt | model | output_parser

result = chain.invoke({"product": "smartphone"})

print(result)  # result is a simple string

chain.get_graph().print_ascii()  # visualize the chain structure
