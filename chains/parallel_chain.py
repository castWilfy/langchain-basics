from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

api_key = input("Enter your Google API key:")
project_id = input("Enter your GCP project ID:")

model = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0,
                google_api_key=api_key,
                project=project_id
)

prompt1 = PromptTemplate(
    input_variables=["text"],
    template="Generate short ans simple notes from the following text \n {text}."
    )  

prompt2 = PromptTemplate(
    input_variables=["text"],
    template="Generate 5 short question answers from the following text \n {text}."
    )   

prompt3 = PromptTemplate(
    input_variables=["notes", "quiz"],
    template="Merge the provided notes and quiz into a single document notes -> {notes} and {quiz}."
    )   

 
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model | parser,
    "quiz": prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

text = """Artificial Intelligence (AI) is transforming the world in unprecedented ways."""
result = chain.invoke({'text': text})

print(result)  # result is a simple string