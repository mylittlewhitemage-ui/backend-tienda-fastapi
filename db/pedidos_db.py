from database import cursor, conexion

def insertar_pedido(id_cliente, fecha):
    cursor.execute(
        "INSERT INTO pedidos (id_cliente, fecha) VALUES (?, ?)",
        (id_cliente, fecha)
    )
    conexion.commit()

def cliente_existe(id_cliente):
    cursor.execute("SELECT * FROM clientes WHERE id_cliente = ?", (id_cliente,))
    return cursor.fetchone()

def insertar_detalle(id_pedido, id_producto, cantidad):
    cursor.execute(
        "INSERT INTO detalle_pedidos (id_pedido, id_producto, cantidad) VALUES (?, ?, ?)",
        (id_pedido, id_producto, cantidad)
    )
    conexion.commit()

def obtener_pedidos():
    cursor.execute("SELECT * FROM pedidos")
    return cursor.fetchall()

def pedidos_con_clientes():
    cursor.execute("""
        SELECT clientes.nombre, pedidos.id_pedido, pedidos.fecha
        FROM clientes
        INNER JOIN pedidos
        ON pedidos.id_cliente = clientes.id_cliente
    """)
    return cursor.fetchall()

def productos_de_pedido(pedido_id):
    cursor.execute("""
        SELECT productos.nombre, detalle_pedidos.cantidad
        FROM productos
        INNER JOIN detalle_pedidos
        ON detalle_pedidos.id_producto = productos.id_producto
        WHERE detalle_pedidos.id_pedido = ?
    """, (pedido_id,))
    return cursor.fetchall()

def mejor_cliente_db():
    cursor.execute("""
        SELECT clientes.nombre,
               SUM(productos.precio * detalle_pedidos.cantidad) AS total
        FROM pedidos
        LEFT JOIN clientes ON clientes.id_cliente = pedidos.id_cliente
        LEFT JOIN detalle_pedidos ON detalle_pedidos.id_pedido = pedidos.id_pedido
        JOIN productos ON productos.id_producto = detalle_pedidos.id_producto
        GROUP BY clientes.nombre
        ORDER BY total DESC
    """)
    return cursor.fetchall()
