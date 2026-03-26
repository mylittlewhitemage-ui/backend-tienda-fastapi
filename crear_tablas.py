# ==============================
# crear_tablas.py
# ==============================
# Este archivo se encarga de crear la base de datos y sus tablas.

import sqlite3

# Conexión a la base de datos (se crea si no existe)
conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

# Tabla de clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes(
    id_cliente INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    ciudad TEXT
)
""")

# Tabla de productos
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id_producto INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio INTEGER NOT NULL,
    categoria TEXT
)
""")

# Tabla de pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INTEGER PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    fecha TEXT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
)
""")

# Tabla intermedia (detalle del pedido)
cursor.execute("""
CREATE TABLE IF NOT EXISTS detalle_pedidos(
    id_detalle INTEGER PRIMARY KEY,
    id_pedido INTEGER,
    id_producto INTEGER,
    cantidad INTEGER,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
)
""")

conexion.commit()
conexion.close()