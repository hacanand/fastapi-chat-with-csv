import os
from fastapi import FastAPI, Request
from langchain_experimental.agents.agent_toolkits import create_csv_agent
# from langchain_community.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()
 

 

app = FastAPI()
 
@app.get("/no/test")
async def test():
    return {"message": "Hello World"}

@app.get("/{query}")
async def chat(query: str):
        # llm=ChatGoogleGenerativeAI(temperature=0, model="gpt-3.5-turbo-0613", openai_api_key= os.environ["GOOGLE_API_KEY"])
        llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro",google_api_key=os.environ["GOOGLE_API_KEY"],temperature=0.5)
        agent_executer= create_csv_agent(llm, 'salaries.csv', verbose=True,return_intermediate_steps=True)
        response = agent_executer.invoke(query)
        return response

 