from typing import Optional
from fastapi import FastAPI, Header, Response, Cookie
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    description: str
    value: float

app = FastAPI()

@app.get("/")
def read_root(user_agent: Optional[str] = Header(None)):
    return {"Hello": "World", "user_agent": user_agent}


@app.get("/cookie")
def cookie(response: Response):
    response.set_cookie(key="mycookie", value="123")
    return {"cookie": True}

@app.get("/get-cookie")
def get_cookie(mycookie: Optional[str] = Cookie(None)):
    return {"Cookie": mycookie}


@app.get("/items/{item_id}")
def read_item(item_id: int, p: bool, q: Optional[str] = None):
    return {"item_id": item_id, "q": q, "p": p}

@app.post("/item")
def add_item(new_item: Item):
    return new_item
