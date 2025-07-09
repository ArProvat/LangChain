from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("GEMINI_API_KEY not found in environment variables. Please check your .env file.")
else:
    print("GEMINI_API_KEY loaded successfully.")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash" ,google_api_key=api_key)
result = llm.invoke('tell me about langchain and it component')
print(result.content)
