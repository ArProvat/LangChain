from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()  
api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
os.environ['HUGGINGFACEHUB_API_TOKEN']=api_token
repo_id="mistralai/Mistral-7B-Instruct-v0.2"
#repo_id2='TinyLlama/TinyLlama-1.1B-Chat-v1.0'
llm=HuggingFaceEndpoint(repo_id=repo_id, temperature=0.1, task="conversational")

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Bangladesh and tell me about it?")
print(result.content)
