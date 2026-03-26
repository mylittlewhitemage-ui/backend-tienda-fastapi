from fastapi import APIRouter
from services import clientes_service

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def ver_clientes():
    return clientes_service.listar_clientes()

@router.post("/")
def crear_cliente(nombre: str, email: str, ciudad: str):
    return clientes_service.crear_cliente(nombre, email, ciudad)
