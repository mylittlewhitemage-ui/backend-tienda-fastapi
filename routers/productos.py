from fastapi import APIRouter
from database import cursor, conexion

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/")
def mostrar_productos():
    cursor.execute("SELECT * FROM productos")
    resultado = cursor.fetchall()

    productos = []
    for producto in resultado:
        productos.append({
            "id": producto[0],
            "nombre": producto[1],
            "precio": producto[2],
            "categoria": producto[3]
        })

    return productos


@router.post("/")
def crear_producto(nombre: str, precio: int, categoria: str):
    cursor.execute(
        "INSERT INTO productos (nombre, precio, categoria) VALUES (?, ?, ?)",
        (nombre, precio, categoria)
    )
    conexion.commit()

    return {"mensaje": "Producto creado"}
