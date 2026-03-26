# ==============================
# database.py
# ==============================
# Maneja la conexión global a la base de datos.

import sqlite3

conexion = sqlite3.connect("tienda.db", check_same_thread=False)
cursor = conexion.cursor()