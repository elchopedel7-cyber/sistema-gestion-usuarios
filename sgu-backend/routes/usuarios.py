"""
============================================================
Archivo: routes/usuarios.py
Descripción: Endpoints REST para gestión de usuarios (CRUD).
             GET    /api/usuarios           → Listar
             GET    /api/usuarios/<id>      → Ver uno
             PUT    /api/usuarios/<id>      → Editar
             DELETE /api/usuarios/<id>      → Eliminar lógico
             PUT    /api/usuarios/<id>/reactivar → Reactivar
Requiere JWT: sí
============================================================
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.usuario_service import UsuarioService

usuarios_bp = Blueprint("usuarios", __name__, url_prefix="/api/usuarios")


def _get_ip():
    return request.remote_addr


def _get_admin_id():
    """Obtiene el id del usuario autenticado desde el JWT."""
    return int(get_jwt_identity())


# ============================================================
# GET /api/usuarios → Listar todos los usuarios
# ============================================================
@usuarios_bp.route("", methods=["GET"])
@jwt_required()
def listar():
    """Lista todos los usuarios con filtros opcionales."""
    filtros = {
        "busqueda": request.args.get("busqueda"),
        "rol": request.args.get("rol"),
        "estado": None
    }

    # Manejar filtro de estado (viene como string en query params)
    estado_param = request.args.get("estado")
    if estado_param is not None:
        filtros["estado"] = estado_param.lower() == "true"

    usuarios = UsuarioService.listar_usuarios(filtros)

    return jsonify({
        "total": len(usuarios),
        "usuarios": [u.to_dict() for u in usuarios]
    }), 200


# ============================================================
# GET /api/usuarios/<id> → Ver un usuario específico
# ============================================================
@usuarios_bp.route("/<int:id_usuario>", methods=["GET"])
@jwt_required()
def obtener(id_usuario):
    """Obtiene los datos de un usuario por su ID."""
    usuario = UsuarioService.obtener_usuario(id_usuario)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify(usuario.to_dict()), 200


# ============================================================
# PUT /api/usuarios/<id> → Editar un usuario
# ============================================================
@usuarios_bp.route("/<int:id_usuario>", methods=["PUT"])
@jwt_required()
def editar(id_usuario):
    """Edita los datos de un usuario existente."""
    datos = request.get_json() or {}
    admin_id = _get_admin_id()

    exito, mensaje, usuario = UsuarioService.editar_usuario(
        id_usuario, datos, admin_id, _get_ip()
    )

    if not exito:
        return jsonify({"error": mensaje}), 400

    return jsonify({
        "mensaje": mensaje,
        "usuario": usuario.to_dict()
    }), 200


# ============================================================
# DELETE /api/usuarios/<id> → Eliminación lógica
# ============================================================
@usuarios_bp.route("/<int:id_usuario>", methods=["DELETE"])
@jwt_required()
def eliminar(id_usuario):
    """Desactiva un usuario (eliminación lógica)."""
    admin_id = _get_admin_id()

    exito, mensaje = UsuarioService.eliminar_logicamente(
        id_usuario, admin_id, _get_ip()
    )

    if not exito:
        return jsonify({"error": mensaje}), 400

    return jsonify({"mensaje": mensaje}), 200


# ============================================================
# PUT /api/usuarios/<id>/reactivar → Reactivar usuario
# ============================================================
@usuarios_bp.route("/<int:id_usuario>/reactivar", methods=["PUT"])
@jwt_required()
def reactivar(id_usuario):
    """Reactiva un usuario previamente desactivado."""
    admin_id = _get_admin_id()

    exito, mensaje = UsuarioService.reactivar_usuario(
        id_usuario, admin_id, _get_ip()
    )

    if not exito:
        return jsonify({"error": mensaje}), 400

    return jsonify({"mensaje": mensaje}), 200