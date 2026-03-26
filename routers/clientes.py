from fastapi import APIRouter
from database import cursor, conexion

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def ver_clientes():
    cursor.execute("SELECT * FROM clientes")
    resultado = cursor.fetchall()

    clientes = []
    for cliente in resultado:
        clientes.append({
            "id": cliente[0],
            "nombre": cliente[1],
            "email": cliente[2],
            "ciudad": cliente[3]
        })

    return clientes


@router.post("/")
def crear_cliente(nombre: str, email: str, ciudad: str):
    cursor.execute(
        "INSERT INTO clientes (nombre, email, ciudad) VALUES (?, ?, ?)",
        (nombre, email, ciudad)
    )
    conexion.commit()

    return {"mensaje": "Cliente creado"}
