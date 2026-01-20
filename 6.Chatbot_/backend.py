from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from typing import TypedDict, Annotated
from dotenv import load_dotenv

load_dotenv()


llm = ChatGroq(model="llama-3.3-70b-versatile")


#STATE-
class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]


#NODE-
def chatnode(state: ChatState) ->ChatState:

    messages = state['messages']

    response = llm.invoke(messages).content

    return {'messages': [response]}


#BUILD GRAPH-
graph = StateGraph(ChatState)
checkpointer = InMemorySaver()

graph.add_node('chatnode', chatnode)

graph.add_edge(START, 'chatnode')
graph.add_edge('chatnode', END)


chatbot = graph.compile(checkpointer= checkpointer)





