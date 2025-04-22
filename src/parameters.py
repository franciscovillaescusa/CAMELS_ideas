from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage, AIMessage
from typing import Annotated, Literal
from langgraph.graph.message import add_messages

# Idea class
class IDEA(TypedDict):
    Title: str
    description: str

# Files class
class FILES(TypedDict):
    CAMELS: str
    
    
# Graph state class
class GraphState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    files: FILES
    idea: IDEA
    files: FILES
    CAMELS: str
