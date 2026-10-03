"""
============================================================
Archivo: services/auditoria_service.py
Descripción: Lógica de negocio para consultar la auditoría.
Autor: Juan Andrés Pérez
Fecha: 2026
============================================================
"""

from extensions import db
from models import Auditoria, Usuario


class AuditoriaService:
    """
    Servicio para consultar el registro de actividades.
    """

    @staticmethod
    def listar_auditoria(filtros: dict = None):
        """
        Lista los registros de auditoría con filtros opcionales.
        
        Filtros admitidos:
            - id_usuario: filtra por usuario específico
            - limite: número máximo de registros (por defecto 50)
        """
        consulta = Auditoria.query

        if filtros:
            if filtros.get("id_usuario"):
                consulta = consulta.filter_by(id_usuario=filtros["id_usuario"])

        # Ordenar por fecha descendente (más recientes primero)
        consulta = consulta.order_by(Auditoria.fecha.desc())

        # Aplicar límite
        limite = filtros.get("limite", 50) if filtros else 50
        registros = consulta.limit(limite).all()

        return registros

    @staticmethod
    def contar_auditoria():
        """Cuenta el total de registros de auditoría."""
        return Auditoria.query.count()

    @staticmethod
    def to_dict_con_usuario(registro: Auditoria):
        """
        Convierte un registro de auditoría a diccionario,
        incluyendo el nombre del usuario que realizó la acción.
        """
        usuario = Usuario.query.get(registro.id_usuario) if registro.id_usuario else None
        return {
            "id_auditoria": registro.id_auditoria,
            "id_usuario": registro.id_usuario,
            "nombre_usuario": usuario.nombre if usuario else "Usuario eliminado",
            "correo_usuario": usuario.correo if usuario else "N/A",
            "accion": registro.accion,
            "fecha": registro.fecha.isoformat() if registro.fecha else None,
            "ip": registro.ip
        }