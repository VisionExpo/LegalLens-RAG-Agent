from fastapi import APIRouter, UploadFile, File
from pathlib import Path

router = APIRouter()


@router.post("/upload")
def upload_contract(
    file: UploadFile = File(...),
    data_source: str = "govt_contracts",
):
    dest = Path("data") / data_source / file.filename
    dest.parent.mkdir(parents=True, exist_ok=True)

    with open(dest, "wb") as f:
        f.write(file.file.read())

    return {
        "status": "uploaded",
        "filename": file.filename,
        "data_source": data_source,
    }
