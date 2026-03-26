from fastapi import APIRouter
from services import productos_service

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/")
def ver_productos():
    return productos_service.listar_productos()

@router.post("/")
def crear_producto(nombre: str, precio: int, categoria: str):
    return productos_service.crear_producto(nombre, precio, categoria)

@router.get("/mas-vendido")
def producto_mas_vendido():
    return productos_service.producto_mas_vendido()
