import sqlite3

conn = sqlite3.connect("prueba.db") #Crear conexión
cursor = conn.cursor() #Crear cursor para interactuar
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios ( 
               Id INTEGER PRIMARY KEY AUTOINCREMENT,         
               nombre TEXT NOT NULL,
               edad INTEGER)''')
conn.commit()
conn.close() #Cerrar conexión 

conn = sqlite3.connect("prueba.db") 
cursor = conn.cursor()
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Juan",21) )
conn.commit()
conn.close()




