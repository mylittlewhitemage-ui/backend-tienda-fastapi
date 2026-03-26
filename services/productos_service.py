from db import productos_db

def listar_productos():
    resultado = productos_db.obtener_productos()

    return [
        {
            "id": p[0],
            "nombre": p[1],
            "precio": p[2],
            "categoria": p[3]
        }
        for p in resultado
    ]

def crear_producto(nombre, precio, categoria):
    productos_db.insertar_producto(nombre, precio, categoria)
    return {"mensaje": "Producto creado"}

def producto_mas_vendido():
    return productos_db.producto_mas_vendido_db()
