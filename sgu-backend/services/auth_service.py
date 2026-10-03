"""
Archivo: services/auth_service.py
Descripción: Lógica de negocio para autenticación.
"""

import re
from datetime import datetime

from extensions import db
from models import Usuario, Rol, Auditoria
from utils.security import hash_password, verify_password


class AuthService:

    @staticmethod
    def validar_correo(correo: str) -> bool:
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(patron, correo))

    @staticmethod
    def validar_password(password: str):
        if len(password) < 8:
            return False, "La contraseña debe tener al menos 8 caracteres"
        if not re.search(r"[A-Z]", password):
            return False, "Debe contener al menos una mayúscula"
        if not re.search(r"[a-z]", password):
            return False, "Debe contener al menos una minúscula"
        if not re.search(r"\d", password):
            return False, "Debe contener al menos un número"
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False, "Debe contener al menos un carácter especial"
        return True, "OK"

    @staticmethod
    def registrar_usuario(nombre, correo, password, ip=None):
        if not nombre or len(nombre) < 2:
            return False, "El nombre debe tener al menos 2 caracteres", None
        if not AuthService.validar_correo(correo):
            return False, "El correo no tiene un formato válido", None
        if Usuario.query.filter_by(correo=correo).first():
            return False, "El correo ya está registrado", None
        es_valida, msg = AuthService.validar_password(password)
        if not es_valida:
            return False, msg, None

        nuevo = Usuario(
            nombre=nombre.strip(),
            correo=correo.lower().strip(),
            contrasena=hash_password(password),
            estado=True
        )
        rol_lector = Rol.query.filter_by(nombre_rol="Lector").first()
        if rol_lector:
            nuevo.roles.append(rol_lector)

        db.session.add(nuevo)
        db.session.commit()

        AuthService._registrar_auditoria(
            nuevo.id_usuario, f"Registro de usuario: {correo}", ip
        )
        return True, "Usuario registrado exitosamente", nuevo

    @staticmethod
    def login(correo, password, ip=None):
        if not correo or not password:
            return False, "Correo y contraseña son obligatorios", None

        usuario = Usuario.query.filter_by(correo=correo.lower().strip()).first()
        if not usuario:
            return False, "Credenciales incorrectas", None
        if not usuario.estado:
            return False, "La cuenta está inactiva. Contacte al administrador", None
        if not verify_password(password, usuario.contrasena):
            return False, "Credenciales incorrectas", None

        usuario.ultimo_acceso = datetime.utcnow()
        db.session.commit()

        AuthService._registrar_auditoria(
            usuario.id_usuario, f"Inicio de sesión: {correo}", ip
        )
        return True, "Login exitoso", usuario

    @staticmethod
    def _registrar_auditoria(id_usuario, accion, ip):
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