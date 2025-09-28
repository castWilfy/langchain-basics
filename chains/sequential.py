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

prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="Generate a detailed report on {topic}."
    )   

prompt2 = PromptTemplate(
    input_variables=["text"],
    template="Generate a 5 pointer summary from the following text \n {text}."
    )   

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "The impact of AI on modern healthcare"})

print(result)  # result is a simple string