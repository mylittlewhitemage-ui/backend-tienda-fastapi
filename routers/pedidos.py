from fastapi import APIRouter
from database import cursor, conexion
from clases import Pedido, DetallePedido

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.get("/")
def obtener_pedidos():
    cursor.execute("SELECT * FROM pedidos")
    return cursor.fetchall()


@router.post("/")
def crear_pedido(pedido: Pedido):
    cursor.execute(
        "INSERT INTO pedidos (id_cliente, fecha) VALUES (?, ?)",
        (pedido.id_cliente, pedido.fecha)
    )
    conexion.commit()

    return {"mensaje": "Pedido creado"}


@router.post("/detalle")
def agregar_producto_pedido(detalle: DetallePedido):
    cursor.execute(
        "INSERT INTO detalle_pedidos (id_pedido, id_producto, cantidad) VALUES (?, ?, ?)",
        (detalle.id_pedido, detalle.id_producto, detalle.cantidad)
    )
    conexion.commit()

    return {"mensaje": "Producto agregado al pedido"}


@router.get("/clientes")
def ver_pedidos_con_clientes():
    cursor.execute("""
        SELECT clientes.nombre, pedidos.id_pedido, pedidos.fecha
        FROM clientes
        INNER JOIN pedidos
        ON pedidos.id_cliente = clientes.id_cliente
    """)
    return cursor.fetchall()


@router.get("/{pedido_id}/productos")
def ver_productos_de_un_pedido(pedido_id: int):
    cursor.execute("""
        SELECT productos.nombre, detalle_pedidos.cantidad
        FROM productos
        INNER JOIN detalle_pedidos
        ON detalle_pedidos.id_producto = productos.id_producto
        WHERE detalle_pedidos.id_pedido = ?
    """, (pedido_id,))
    
    return cursor.fetchall()


@router.get("/mejores-clientes")
def mejor_cliente():
    cursor.execute("""
        SELECT clientes.nombre,
               SUM(productos.precio * detalle_pedidos.cantidad) AS total_gastado
        FROM pedidos
        LEFT JOIN clientes ON clientes.id_cliente = pedidos.id_cliente
        LEFT JOIN detalle_pedidos ON detalle_pedidos.id_pedido = pedidos.id_pedido
        JOIN productos ON productos.id_producto = detalle_pedidos.id_producto
        GROUP BY clientes.nombre
        ORDER BY total_gastado DESC
    """)
    
    return cursor.fetchall()


@router.get("/producto-mas-vendido")
def producto_mas_vendido():
    cursor.execute("""
        SELECT productos.nombre,
               SUM(detalle_pedidos.cantidad) AS total_vendido
        FROM productos
        INNER JOIN detalle_pedidos
        ON productos.id_producto = detalle_pedidos.id_producto
        GROUP BY productos.nombre
        ORDER BY total_vendido DESC
        LIMIT 1
    """)
    
    return cursor.fetchall()
