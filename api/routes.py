from orchestration.workflow import build_workflow
from orchestration.state_factory import create_initial_state

workflow = build_workflow()


@app.post("/process-document")
async def process_document(file: UploadFile):

    file_path = save_file(file)

    state = create_initial_state(file_path)

    result = workflow.invoke(state)

    return result