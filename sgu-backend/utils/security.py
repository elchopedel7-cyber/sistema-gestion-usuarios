"""
Archivo: utils/security.py
Descripción: Funciones de seguridad para contraseñas.
"""

import bcrypt


def hash_password(password: str) -> str:
    """Convierte una contraseña a hash seguro con bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(password: str, hashed: str) -> bool:
    """Verifica si una contraseña coincide con el hash."""
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    except Exception:
        return False