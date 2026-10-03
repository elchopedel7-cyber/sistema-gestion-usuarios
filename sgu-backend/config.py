"""
============================================================
Archivo: config.py
Descripción: Configuración central del Sistema de Gestión 
             de Usuarios (SGU). Carga las variables de 
             entorno y define la conexión a MySQL.
Autor: Juan Andrés Pérez
Fecha: 2026
============================================================
"""

import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()


class Config:
    """
    Clase de configuración principal.
    Contiene las constantes usadas por Flask y SQLAlchemy.
    """

    # --------------------------------------------------------
    # Claves de seguridad
    # --------------------------------------------------------
    SECRET_KEY = os.getenv("SECRET_KEY", "sgu_secret_default")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "sgu_jwt_default")
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hora en segundos

    # --------------------------------------------------------
    # Configuración de la base de datos MySQL
    # --------------------------------------------------------
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "gestion_usuarios_db")

    # URI de conexión usando PyMySQL (driver puro de Python)
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Desactivar el seguimiento de modificaciones (mejora rendimiento)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --------------------------------------------------------
    # Configuración general
    # --------------------------------------------------------
    DEBUG = True
    JSON_SORT_KEYS = False