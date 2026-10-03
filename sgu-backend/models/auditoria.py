"""
============================================================
Archivo: models/auditoria.py
Descripción: Modelo SQLAlchemy para la tabla 'auditoria'.
             Registra las acciones realizadas por los usuarios.
Autor: Juan Andrés Pérez
Fecha: 2026
============================================================
"""

from datetime import datetime
from extensions import db


class Auditoria(db.Model):
    """
    Registra cada acción importante realizada en el sistema:
    inicios de sesión, ediciones, eliminaciones, etc.
    """
    __tablename__ = "auditoria"

    id_auditoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id_usuario"), nullable=True)
    accion = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    ip = db.Column(db.String(45))

    def to_dict(self):
        """Convierte el objeto a diccionario."""
        return {
            "id_auditoria": self.id_auditoria,
            "id_usuario": self.id_usuario,
            "accion": self.accion,
            "fecha": self.fecha.isoformat() if self.fecha else None,
            "ip": self.ip
        }

    def __repr__(self):
        return f"<Auditoria {self.accion}>"
