from fastapi import APIRouter
from clases import Pedido, DetallePedido
from services import pedidos_service

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get("/")
def ver_pedidos():
    return pedidos_service.listar_pedidos()

@router.post("/")
def crear_pedido(pedido: Pedido):
    return pedidos_service.crear_pedido(pedido)

@router.post("/detalle")
def agregar_producto(detalle: DetallePedido):
    return pedidos_service.agregar_detalle(detalle)

@router.get("/clientes")
def pedidos_clientes():
    return pedidos_service.pedidos_con_clientes()

@router.get("/{pedido_id}/productos")
def productos_pedido(pedido_id: int):
    return pedidos_service.productos_de_pedido(pedido_id)

@router.get("/mejores-clientes")
def mejor_cliente():
    return pedidos_service.mejor_cliente()
