from typing import Optional
from fastapi import FastAPI, Header, Response, Cookie
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    quantidade: int
    descricao: str
    valor: float

app = FastAPI()

banco = []

@app.post("/item")
def add_item(item: Item):
    banco.append(item)
    return item

@app.get("/item")
def list_item():
    return banco

@app.get("/item/valor_total")
def get_valor_total():
    valor_total = sum([item.valor * item.quantidade for item in banco])

    # for item in banco:
    #     valor_total += item.valor * item.quantidade

    return {"total_value": round(valor_total, 3)}
