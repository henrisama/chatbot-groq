import os
from typing import TypedDict
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

class ChatbotState(TypedDict):
    user_input: str
    response: str
    status: str

@tool
def synonym_tool(word: str) -> str:
    """
    Retorna sinônimos de uma palavra fornecida.
    """
    synonyms = {
        "feliz": ["alegre", "contente", "satisfeito"],
        "triste": ["abatido", "melancólico", "desanimado"],
        "rápido": ["veloz", "ligeiro", "ágil"]
    }
    return ", ".join(synonyms.get(word.lower(), ["Nenhum sinônimo encontrado"]))


@tool
def calculator_tool(expression: str) -> str:
    """
    Resolve uma expressão matemática simples e retorna o resultado.
    """
    try:
        result = eval(expression)
        return f"O resultado de {expression} é {result}"
    except Exception as e:
        return f"Erro ao calcular a expressão: {str(e)}"


class Chatbot:
    def __init__(self):
        self.history = [SystemMessage(content="You are a helpful assistant.")]

        self.llm = ChatGroq(
            temperature=0,
            model="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("GROQ_API_KEY")
        )

        self.tools = {
            "synonym_tool": synonym_tool,
            "calculator_tool": calculator_tool,
        }

        self.graph = StateGraph(ChatbotState)

        self.graph.add_node("start", self.start_node)
        self.graph.add_node("process_input", self.process_input_node)
        self.graph.add_node("end", self.end_node)

        self.graph.add_edge(START, "start")
        self.graph.add_edge("start", "process_input")
        self.graph.add_edge("process_input", END)

        self.compiled_graph = self.graph.compile()

    def start_node(self, state: ChatbotState) -> ChatbotState:
        state["status"] = "initialized"
        return state

    def process_input_node(self, state):
        user_input = state.get("user_input")
        self.history.append(HumanMessage(content=user_input))

        if user_input.startswith("sinônimo de "):
            word = user_input.replace("sinônimo de ", "").strip()
            response = self.tools["synonym_tool"](word)
        elif user_input.startswith("calcule "):
            expression = user_input.replace("calcule ", "").strip()
            response = self.tools["calculator_tool"](expression)
        else:
            response = self.llm(self.history).content

        self.history.append(SystemMessage(content=response))

        state["response"] = response
        return state

    def end_node(self, state):
        state["status"] = "completed"
        return state

    def respond(self, user_input):
        state = {"user_input": user_input}
        final_state = self.compiled_graph.invoke(state)
        return final_state.get("response")
