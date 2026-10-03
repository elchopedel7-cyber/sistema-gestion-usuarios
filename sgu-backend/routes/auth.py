"""
Archivo: routes/auth.py
Descripción: Endpoints REST para autenticación.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


def _get_ip():
    return request.remote_addr


@auth_bp.route("/registro", methods=["POST"])
def registro():
    datos = request.get_json() or {}
    nombre = datos.get("nombre", "").strip()
    correo = datos.get("correo", "").strip()
    password = datos.get("contrasena", "")

    exito, mensaje, usuario = AuthService.registrar_usuario(
        nombre, correo, password, _get_ip()
    )

    if not exito:
        return jsonify({"error": mensaje}), 400

    return jsonify({
        "mensaje": mensaje,
        "usuario": usuario.to_dict()
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    datos = request.get_json() or {}
    correo = datos.get("correo", "").strip()
    password = datos.get("contrasena", "")

    exito, mensaje, usuario = AuthService.login(correo, password, _get_ip())

    if not exito:
        return jsonify({"error": mensaje}), 401

    token = create_access_token(
        identity=str(usuario.id_usuario),
        additional_claims={
            "correo": usuario.correo,
            "nombre": usuario.nombre,
            "roles": [r.nombre_rol for r in usuario.roles]
        }
    )

    return jsonify({
        "mensaje": mensaje,
        "token": token,
        "usuario": usuario.to_dict()
    }), 200