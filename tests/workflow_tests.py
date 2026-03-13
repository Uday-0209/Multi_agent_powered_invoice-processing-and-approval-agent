from orchestration.workflow import build_workflow
from orchestration.state_factory import create_initial_state

workflow = build_workflow()

state = create_initial_state("sample_invoice.pdf")

result = workflow.invoke(state)

print("FINAL RESULT")
print(result)