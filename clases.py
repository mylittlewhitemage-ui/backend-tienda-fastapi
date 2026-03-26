# ==============================
# clases.py
# ==============================
# Modelos de datos (validación con Pydantic)

from pydantic import BaseModel

class Pedido(BaseModel):
    id_cliente: int
    fecha: str

class DetallePedido(BaseModel):
    id_pedido: int
    id_producto: int
    cantidad: int
