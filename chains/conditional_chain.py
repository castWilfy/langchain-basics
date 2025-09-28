from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda

api_key = input("Enter your Google API key:")
project_id = input("Enter your GCP project ID:")

model = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0,
                google_api_key=api_key,
                project=project_id
)

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal["positive", "negative"] = Field(description='The sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    input_variables=["feedback"],
    template="Classify the sentiment of the following feedback text \n {feedback} \n {format_instructions}",
    partial_variables={'format_instructions': parser2.get_format_instructions()}
    )

prompt2 = PromptTemplate(
    input_variables=["feedback"],
    template="Generate a thank you message for the positive feedback: {feedback}"
    )

prompt3 = PromptTemplate(
    input_variables=["feedback"],
    template="Generate an apology message for the negative feedback: {feedback}"
    )

classifer_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
(lambda x: x.sentiment == 'positive', prompt2 | model | parser),
(lambda x: x.sentiment == 'negative', prompt3 | model | parser),
RunnableLambda(lambda x: "Invalid sentiment")
)

chain = classifer_chain | branch_chain

result = chain.invoke({'feedback': "The product quality is excellent and I am very satisfied with my purchase."})
print(result)  # result is a simple string