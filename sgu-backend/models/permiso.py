"""
============================================================
Archivo: models/permiso.py
Descripción: Modelo SQLAlchemy para la tabla 'permiso'.
Autor: Juan Andrés Pérez
Fecha: 2026
============================================================
"""

from extensions import db


class Permiso(db.Model):
    """
    Representa un permiso específico del sistema.
    Los permisos se asignan a roles y definen qué acciones 
    puede realizar un usuario.
    """
    __tablename__ = "permiso"

    id_permiso = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_permiso = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))

    def to_dict(self):
        """Convierte el objeto a diccionario."""
        return {
            "id_permiso": self.id_permiso,
            "nombre_permiso": self.nombre_permiso,
            "descripcion": self.descripcion
        }

    def __repr__(self):
        return f"<Permiso {self.nombre_permiso}>"