from langgraph.graph import START, StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from src.parameters import GraphState
from src.reader import *
from src.idea import *


def build_graph(mermaid_diagram=False):
    """
    This function builds the graph
    """

    # Define the graph
    builder = StateGraph(GraphState)

    # Define nodes: these do the work
    builder.add_node("preprocess_node",   preprocess_node)
    builder.add_node("idea_agent",        idea_agent)
    
    
    # Define edges: these determine how the control flow moves
    builder.add_edge(START,               "preprocess_node")
    builder.add_edge("preprocess_node",   "idea_agent")
    builder.add_edge("idea_agent",        END)

    memory = MemorySaver()
    graph  = builder.compile(checkpointer=memory)

    # generate an scheme with the graph
    if mermaid_diagram:
        try:
            graph_image = graph.get_graph(xray=True).draw_mermaid_png()
            with open("graph_diagram.png", "wb") as f:
                f.write(graph_image)
            print("✅ Graph diagram saved to graph_diagram.png")
        except Exception as e:
            print(f"⚠️ Failed to generate or save graph diagram: {e}")
    
    return graph
