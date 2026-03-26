from fastapi import FastAPI
from routers import clientes, productos, pedidos

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}

app.include_router(clientes.router)
app.include_router(productos.router)
app.include_router(pedidos.router)

