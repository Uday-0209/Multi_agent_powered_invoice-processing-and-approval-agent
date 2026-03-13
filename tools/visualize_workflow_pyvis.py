from orchestration.workflow import build_workflow
from pyvis.network import Network


def visualize_workflow():

    workflow = build_workflow()
    graph = workflow.get_graph()

    net = Network(
        height="750px",
        width="100%",
        directed=True
    )

    # Add nodes
    for node in graph.nodes:
       
        color = "lightblue"

        if "save" in node:
            color = "green"

        if "decision" in node:
            color = "orange"

        if "notification" in node:
            color = "red"

        net.add_node(node, label=node, color=color)

    # Add edges
    for edge in graph.edges:
        source = edge[0]
        target = edge[1]
        net.add_edge(source, target)
    
    

    # Save interactive HTML
    net.write_html("workflow_graph.html")

    print("Workflow visualization saved as workflow_graph.html")


if __name__ == "__main__":
    visualize_workflow()