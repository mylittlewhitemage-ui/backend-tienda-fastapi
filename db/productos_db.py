from database import cursor, conexion

def obtener_productos():
    cursor.execute("SELECT * FROM productos")
    return cursor.fetchall()

def insertar_producto(nombre, precio, categoria):
    cursor.execute(
        "INSERT INTO productos (nombre, precio, categoria) VALUES (?, ?, ?)",
        (nombre, precio, categoria)
    )
    conexion.commit()

def producto_mas_vendido_db():
    cursor.execute("""
        SELECT productos.nombre, SUM(detalle_pedidos.cantidad) as total
        FROM productos
        INNER JOIN detalle_pedidos
        ON productos.id_producto = detalle_pedidos.id_producto
        GROUP BY productos.nombre
        ORDER BY total DESC
        LIMIT 1
    """)
    return cursor.fetchall()
