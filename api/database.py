import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo : str
    autor: str
    paginas: int
    editorial: Optional[str]


@app.get("/") #Ruta vacia
async def index(): #Se define función asincrona
    return {"message" : "Hello World"}

@app.get("/libros/{id}") 
async def mostrar_libro(id:int): 
    return {"data" :id}

@app.get("/libros/{id}") 
async def mostrar_libro(id:int): 
    return {"data" :id}

@app.post("/libros/") 
async def insertar_libro(libro: Libro): 
    return {"message" : f"Libro: {libro.titulo} insertado correctamente"}
"""
@app.get("/items/{item_id}/{m}")
def read_item(item_id: int, m: str = None):
    return {"item_id" : item_id, "m" : m}
"""
