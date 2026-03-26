from database import cursor, conexion

def obtener_clientes():
    cursor.execute("SELECT * FROM clientes")
    return cursor.fetchall()

def insertar_cliente(nombre, email, ciudad):
    cursor.execute(
        "INSERT INTO clientes (nombre, email, ciudad) VALUES (?, ?, ?)",
        (nombre, email, ciudad)
    )
    conexion.commit()
