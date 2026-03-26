from db import pedidos_db

def crear_pedido(pedido):
    if not pedidos_db.cliente_existe(pedido.id_cliente):
        return {"error": "Cliente no existe"}

    pedidos_db.insertar_pedido(pedido.id_cliente, pedido.fecha)
    return {"mensaje": "Pedido creado"}

def agregar_detalle(detalle):
    pedidos_db.insertar_detalle(
        detalle.id_pedido,
        detalle.id_producto,
        detalle.cantidad
    )
    return {"mensaje": "Producto agregado"}

def listar_pedidos():
    return pedidos_db.obtener_pedidos()

def pedidos_con_clientes():
    return pedidos_db.pedidos_con_clientes()

def productos_de_pedido(pedido_id):
    return pedidos_db.productos_de_pedido(pedido_id)

def mejor_cliente():
    return pedidos_db.mejor_cliente_db()
