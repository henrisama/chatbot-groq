import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

class Chatbot:
    def __init__(self):
        self.history = [SystemMessage(content="You are a helpful assistant.")]

        self.llm = ChatGroq(
            temperature=0,
            model="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("GROQ_API_KEY")
        )

    def respond(self, user_input):
        self.history.append(HumanMessage(content=user_input))
        
        prompt = ChatPromptTemplate.from_messages(self.history)

        chain = prompt | self.llm

        response = chain.invoke({'input': user_input})

        self.history.append(SystemMessage(content=response.content))
        
        return response.content
