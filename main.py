import os
from fastapi import FastAPI, Request
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
# from pydantic import BaseModel

 

app = FastAPI()
 
@app.get("/no/test")
async def test():
    return {"message": "Hello World"}

@app.get("/{query}")
async def chat(query: str):
        llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", openai_api_key= os.environ["OPENAI_API_KEY"])
        agent_executer=create_csv_agent(llm, 'salaries.csv', verbose=True,return_intermediate_steps=True)
        response = agent_executer.invoke(query)

        return response
     