"""
============================================================
Archivo: services/rol_service.py
Descripción: Lógica de negocio para roles y permisos.
Autor: Juan Andrés Pérez
Fecha: 2026
============================================================
"""

from extensions import db
from models import Rol, Permiso, Usuario, Auditoria


class RolService:
    """
    Servicio que agrupa las operaciones de roles y permisos.
    """

    @staticmethod
    def listar_roles():
        """Lista todos los roles del sistema con sus permisos."""
        return Rol.query.order_by(Rol.id_rol).all()

    @staticmethod
    def obtener_rol(id_rol: int):
        """Obtiene un rol por ID. Retorna None si no existe."""
        return Rol.query.get(id_rol)

    @staticmethod
    def listar_permisos():
        """Lista todos los permisos del sistema."""
        return Permiso.query.order_by(Permiso.id_permiso).all()

    @staticmethod
    def crear_rol(nombre_rol: str, descripcion: str, permisos_ids: list, id_admin: int, ip: str = None):
        """
        Crea un nuevo rol con los permisos indicados.
        Retorna (exito, mensaje, rol)
        """
        if not nombre_rol or len(nombre_rol.strip()) < 3:
            return False, "El nombre del rol debe tener al menos 3 caracteres", None

        if Rol.query.filter_by(nombre_rol=nombre_rol.strip()).first():
            return False, "Ya existe un rol con ese nombre", None

        nuevo_rol = Rol(
            nombre_rol=nombre_rol.strip(),
            descripcion=descripcion
        )

        # Asignar permisos
        if permisos_ids:
            permisos = Permiso.query.filter(Permiso.id_permiso.in_(permisos_ids)).all()
            nuevo_rol.permisos = permisos

        db.session.add(nuevo_rol)
        db.session.commit()

        RolService._registrar_auditoria(
            id_admin, f"Creó el rol: {nombre_rol}", ip
        )

        return True, "Rol creado exitosamente", nuevo_rol

    @staticmethod
    def asignar_rol_a_usuario(id_usuario: int, id_rol: int, id_admin: int, ip: str = None):
        """
        Asigna un rol a un usuario (reemplaza los roles anteriores).
        Retorna (exito, mensaje, usuario)
        """
        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            return False, "Usuario no encontrado", None

        rol = Rol.query.get(id_rol)
        if not rol:
            return False, "Rol no encontrado", None

        # Reemplazar roles (un usuario tiene un rol a la vez en este proyecto)
        usuario.roles = [rol]
        db.session.commit()

        RolService._registrar_auditoria(
            id_admin, f"Asignó rol '{rol.nombre_rol}' al usuario ID {id_usuario}", ip
        )

        return True, "Rol asignado correctamente", usuario

    @staticmethod
    def _registrar_auditoria(id_usuario, accion, ip):
        """Registra la acción en la tabla auditoria."""
        try:
            auditoria = Auditoria(
                id_usuario=id_usuario,
                accion=accion,
                ip=ip or "desconocida"
            )
            db.session.add(auditoria)
            db.session.commit()
        except Exception as e:
            print(f"Error al registrar auditoría: {e}")