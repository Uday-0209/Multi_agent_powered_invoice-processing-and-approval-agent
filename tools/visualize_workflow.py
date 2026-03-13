from orchestration.workflow import build_workflow


def visualize_workflow():

    workflow = build_workflow()

    graph = workflow.get_graph()

    # print mermaid text
    print(graph.draw_mermaid())

    # get PNG bytes
    png_bytes = graph.draw_mermaid_png()

    # save manually
    with open("workflow_graph.png", "wb") as f:
        f.write(png_bytes)

    print("Workflow diagram saved to workflow_graph.png")


if __name__ == "__main__":
    visualize_workflow()