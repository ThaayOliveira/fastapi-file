from fastapi import APIRouter, UploadFile, FastAPI, File
from domain.file_processor import FileProcessor

router = APIRouter()


@router.post("/file/create_file")
async def create_file():
    return FileProcessor().create_file()


@router.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    return await FileProcessor().upload_file(file)


@router.post("/file/add_data")
async def add_data(conta: str, agencia: str, texto: str, valor: float):
    data = {"conta": conta, "agencia": agencia, "texto": texto, "valor": valor}
    return await FileProcessor().add_data_to_file(data)


@router.post("/file/delete_data")
async def delete_data():
    return {"menssage": "Dado deletado com sucesso"}


@router.post("/file/list_files")
async def list_files():
    items = await FileProcessor().list_data_file()
    return {"menssage": items}