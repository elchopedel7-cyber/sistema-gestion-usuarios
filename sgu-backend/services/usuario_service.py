"""
============================================================
Archivo: services/usuario_service.py
Descripción: Lógica de negocio para gestión de usuarios.
             Listar, editar, eliminar lógicamente.
Autor: Juan Andrés Pérez
Fecha: 2026
============================================================
"""

from extensions import db
from models import Usuario, Rol, Auditoria


class UsuarioService:
    """
    Servicio que agrupa las operaciones CRUD de usuarios.
    """

    @staticmethod
    def listar_usuarios(filtros: dict = None):
        """
        Lista todos los usuarios con filtros opcionales.
        
        Filtros admitidos:
            - estado: True/False
            - rol: nombre del rol
            - busqueda: texto libre para nombre o correo
        """
        consulta = Usuario.query

        if filtros:
            # Filtro por estado
            if "estado" in filtros and filtros["estado"] is not None:
                consulta = consulta.filter_by(estado=filtros["estado"])

            # Filtro por búsqueda en nombre o correo
            if "busqueda" in filtros and filtros["busqueda"]:
                texto = f"%{filtros['busqueda']}%"
                consulta = consulta.filter(
                    db.or_(
                        Usuario.nombre.ilike(texto),
                        Usuario.correo.ilike(texto)
                    )
                )

        usuarios = consulta.order_by(Usuario.id_usuario).all()

        # Filtro por rol (se hace en Python por la relación N:M)
        if filtros and filtros.get("rol"):
            usuarios = [
                u for u in usuarios
                if any(r.nombre_rol == filtros["rol"] for r in u.roles)
            ]

        return usuarios

    @staticmethod
    def obtener_usuario(id_usuario: int):
        """Obtiene un usuario por su ID. Retorna None si no existe."""
        return Usuario.query.get(id_usuario)

    @staticmethod
    def editar_usuario(id_usuario: int, datos: dict, id_admin: int, ip: str = None):
        """
        Edita los datos de un usuario existente.
        Retorna (exito: bool, mensaje: str, usuario: Usuario|None)
        """
        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            return False, "Usuario no encontrado", None

        # Cambios permitidos
        if "nombre" in datos and datos["nombre"]:
            usuario.nombre = datos["nombre"].strip()

        if "correo" in datos and datos["correo"]:
            nuevo_correo = datos["correo"].lower().strip()
            # Validar que no exista otro usuario con ese correo
            existente = Usuario.query.filter_by(correo=nuevo_correo).first()
            if existente and existente.id_usuario != id_usuario:
                return False, "El correo ya está registrado por otro usuario", None
            usuario.correo = nuevo_correo

        if "estado" in datos:
            usuario.estado = bool(datos["estado"])

        # Cambio de rol
        if "rol" in datos and datos["rol"]:
            rol = Rol.query.filter_by(nombre_rol=datos["rol"]).first()
            if not rol:
                return False, f"El rol '{datos['rol']}' no existe", None
            usuario.roles = [rol]

        db.session.commit()

        UsuarioService._registrar_auditoria(
            id_admin, f"Editó al usuario ID {id_usuario}", ip
        )

        return True, "Usuario actualizado correctamente", usuario

    @staticmethod
    def eliminar_logicamente(id_usuario: int, id_admin: int, ip: str = None):
        """
        Elimina lógicamente un usuario (cambia estado a False).
        Retorna (exito: bool, mensaje: str)
        """
        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            return False, "Usuario no encontrado"

        if not usuario.estado:
            return False, "El usuario ya está inactivo"

        # Evitar que el admin se elimine a sí mismo
        if usuario.id_usuario == id_admin:
            return False, "No puedes eliminar tu propia cuenta"

        usuario.estado = False
        db.session.commit()

        UsuarioService._registrar_auditoria(
            id_admin, f"Eliminó lógicamente al usuario ID {id_usuario}", ip
        )

        return True, "Usuario desactivado correctamente"

    @staticmethod
    def reactivar_usuario(id_usuario: int, id_admin: int, ip: str = None):
        """Reactiva un usuario previamente desactivado."""
        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            return False, "Usuario no encontrado"

        if usuario.estado:
            return False, "El usuario ya está activo"

        usuario.estado = True
        db.session.commit()

        UsuarioService._registrar_auditoria(
            id_admin, f"Reactivó al usuario ID {id_usuario}", ip
        )

        return True, "Usuario reactivado correctamente"

    @staticmethod
    def _registrar_auditoria(id_usuario, accion, ip):
        """Registra una acción en la tabla auditoria."""
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