from src.graph import build_graph
import time

# Start timer
start_time = time.time()

# Thread
config = {"configurable": {"thread_id": "1"}, "recursion_limit":100}

# build graph
graph = build_graph(mermaid_diagram=True)

# run the graph
result = graph.invoke({},config)

# End timer and report duration in minutes and seconds
end_time = time.time()
elapsed_time = end_time - start_time
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)
print(f"Ideas generated in {minutes} min {seconds} sec.")
