"""
============================================================
Archivo: models/rol.py
Descripción: Modelo SQLAlchemy para la tabla 'rol'.
             También define la tabla intermedia rol_permiso.
Autor: Juan Andrés Pérez
Fecha: 2026
============================================================
"""

from extensions import db


# Tabla intermedia N:M entre Rol y Permiso
rol_permiso = db.Table(
    "rol_permiso",
    db.Column("id_rol", db.Integer, db.ForeignKey("rol.id_rol"), primary_key=True),
    db.Column("id_permiso", db.Integer, db.ForeignKey("permiso.id_permiso"), primary_key=True)
)


class Rol(db.Model):
    """
    Representa un rol del sistema (Administrador, Editor, Lector).
    Cada rol agrupa un conjunto de permisos.
    """
    __tablename__ = "rol"

    id_rol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_rol = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))

    # Relación N:M con Permiso
    permisos = db.relationship(
        "Permiso",
        secondary=rol_permiso,
        backref=db.backref("roles", lazy="dynamic")
    )

    def to_dict(self):
        """Convierte el objeto a diccionario."""
        return {
            "id_rol": self.id_rol,
            "nombre_rol": self.nombre_rol,
            "descripcion": self.descripcion,
            "permisos": [p.nombre_permiso for p in self.permisos]
        }

    def __repr__(self):
        return f"<Rol {self.nombre_rol}>"