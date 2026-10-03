"""
Archivo: models/__init__.py
Descripción: Exporta todos los modelos del sistema para 
             facilitar su importación desde otros módulos.
"""

from .usuario import Usuario
from .rol import Rol
from .permiso import Permiso
from .auditoria import Auditoria

__all__ = ["Usuario", "Rol", "Permiso", "Auditoria"]