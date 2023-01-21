from fastapi import APIRouter
from models.papel import Papel

router = APIRouter()

banco = []

@router.post("/")
def add_item(item: Papel):
    banco.append(item)
    return item

@router.get("/")
def list_item():
    return banco
