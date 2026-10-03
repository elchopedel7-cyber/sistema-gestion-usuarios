"""
============================================================
Archivo: models/usuario.py
Descripción: Modelo SQLAlchemy para la tabla 'usuario'.
Autor: Juan Andrés Pérez
Fecha: 2026
============================================================
"""

from datetime import datetime
from extensions import db  


# Tabla intermedia N:M entre Usuario y Rol
usuario_rol = db.Table(
    "usuario_rol",
    db.Column("id_usuario", db.Integer, db.ForeignKey("usuario.id_usuario"), primary_key=True),
    db.Column("id_rol", db.Integer, db.ForeignKey("rol.id_rol"), primary_key=True)
)


class Usuario(db.Model):
    """
    Representa un usuario del sistema.
    Incluye atributos personales, credenciales y estado.
    """
    __tablename__ = "usuario"

    # -------------------- Campos --------------------
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Boolean, default=True, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    ultimo_acceso = db.Column(db.DateTime, nullable=True)

    # -------------------- Relaciones --------------------
    roles = db.relationship(
        "Rol",
        secondary=usuario_rol,
        backref=db.backref("usuarios", lazy="dynamic")
    )

    # -------------------- Métodos --------------------
    def to_dict(self):
        """Convierte el objeto a diccionario (para respuestas JSON)."""
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "correo": self.correo,
            "estado": self.estado,
            "fecha_creacion": self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            "ultimo_acceso": self.ultimo_acceso.isoformat() if self.ultimo_acceso else None,
            "roles": [r.nombre_rol for r in self.roles]
        }

    def __repr__(self):
        return f"<Usuario {self.correo}>"