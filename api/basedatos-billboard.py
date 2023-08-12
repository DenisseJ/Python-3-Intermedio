import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

conn = sqlite3.connect("billboard100.db")
cursor  = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS datos ( 
               Id INTEGER PRIMARY KEY AUTOINCREMENT,         
               titulo TEXT NOT NULL,
               artista TEXT NOT NULL,
               posicion INTEGER)''')
conn.commit()
conn.close()

class Datos(BaseModel):
    id : int
    titulo : str
    artista : str
    posicion : int

app = FastAPI()

@app.post("/agregar/")
async def agregar_datos(datos :Datos):
    conn = sqlite3.connect("billboard100.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (titulo, artista, posicion) VALUES (?, ?,?)", (datos.titulo,datos.artista,datos.posicion) )
    conn.commit()
    conn.close()
    return{ "mensaje" : "Datos agregados exitosamente"}

@app.get("/datos/")
async def obtener_todos_datos():
    conn = sqlite3.connect("billboard100.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos" )
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return[{ "titulo" : resultados[1],"artista":resultados[2],"posicion":resultados[3]} for resultado in resultados]
    else:
        return{ "mensaje" : "No hay datos en la base de datos"}
    
@app.get("/consultar/{id}/")
async def consultar_datos():
    conn = sqlite3.connect("billboard100.db")
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, artista, posicion FROM datos WHERE id=?",(id,) ) #Coma necesario para mandar dupla
    resultados = cursor.fetchone()
    conn.close()
    if resultados:
        return[{ "titulo" : resultados[0],"artista":resultados[1],"posicion":resultados[2]} for resultado in resultados]
    else:
        return{ "mensaje" : "Datos no encontrados"}

@app.put("/actualizar/{id_value}")
async def actualizar_datos(id:int,datos :Datos):
    conn = sqlite3.connect("billboard100.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE datos SET titulo=?,artista=?,posicion=? WHERE id=?)", (datos.titulo,datos.artista,datos.posicion,id) )
    conn.commit()
    conn.close()
    return{ "mensaje" : "Datos actualizados exitosamente"}

@app.delete("/eliminar/{id_value}")
async def eliminar_datos(id :int):
    conn = sqlite3.connect("billboard100.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM datos WHERE id=?", (id) )
    conn.commit()
    conn.close()
    return{ "mensaje" : "Datos eliminados exitosamente"}

