from fastapi import APIRouter, UploadFile, File
import os

from orchestration.workflow import build_workflow

router = APIRouter(prefix="/invoices")

workflow = build_workflow()


@router.post("/process")
async def process_invoice(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    os.makedirs("uploads", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = workflow.invoke({
        "file_path": file_path
    })

    return result         