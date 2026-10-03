"""
============================================================
Archivo: extensions.py
Descripción: Instancias de extensiones Flask (SQLAlchemy, JWT).
             Se separan de app.py para evitar importaciones 
             circulares con los modelos.
Autor: Juan Andrés Pérez
Fecha: 2026
============================================================
"""

from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Instancias globales (se inicializan en app.py)
db = SQLAlchemy()
jwt = JWTManager()