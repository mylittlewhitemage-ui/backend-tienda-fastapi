from db import clientes_db

def listar_clientes():
    resultado = clientes_db.obtener_clientes()

    return [
        {
            "id": c[0],
            "nombre": c[1],
            "email": c[2],
            "ciudad": c[3]
        }
        for c in resultado
    ]

def crear_cliente(nombre, email, ciudad):
    clientes_db.insertar_cliente(nombre, email, ciudad)
    return {"mensaje": "Cliente creado"}
