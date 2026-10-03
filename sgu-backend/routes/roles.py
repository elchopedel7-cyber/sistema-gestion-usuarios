"""
============================================================
Archivo: routes/roles.py
Descripción: Endpoints REST para roles y permisos.
Autor: Juan Andrés Pérez
Fecha: 2026
============================================================
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.rol_service import RolService

roles_bp = Blueprint("roles", __name__, url_prefix="/api")


def _get_ip():
    return request.remote_addr


def _get_admin_id():
    return int(get_jwt_identity())


# ============================================================
# GET /api/roles → Listar todos los roles
# ============================================================
@roles_bp.route("/roles", methods=["GET"])
@jwt_required()
def listar_roles():
    roles = RolService.listar_roles()
    return jsonify({
        "total": len(roles),
        "roles": [r.to_dict() for r in roles]
    }), 200


# ============================================================
# POST /api/roles → Crear un nuevo rol
# ============================================================
@roles_bp.route("/roles", methods=["POST"])
@jwt_required()
def crear_rol():
    datos = request.get_json() or {}
    nombre_rol = datos.get("nombre_rol", "").strip()
    descripcion = datos.get("descripcion", "")
    permisos_ids = datos.get("permisos_ids", [])

    exito, mensaje, rol = RolService.crear_rol(
        nombre_rol, descripcion, permisos_ids, _get_admin_id(), _get_ip()
    )

    if not exito:
        return jsonify({"error": mensaje}), 400

    return jsonify({
        "mensaje": mensaje,
        "rol": rol.to_dict()
    }), 201


# ============================================================
# POST /api/roles/asignar → Asignar rol a usuario
# ⚠️ ANTES de /roles/<id_rol>
# ============================================================
@roles_bp.route("/roles/asignar", methods=["POST"])
@jwt_required()
def asignar_rol():
    datos = request.get_json() or {}
    id_usuario = datos.get("id_usuario")
    id_rol = datos.get("id_rol")

    if not id_usuario or not id_rol:
        return jsonify({"error": "Debes enviar id_usuario e id_rol"}), 400

    exito, mensaje, usuario = RolService.asignar_rol_a_usuario(
        int(id_usuario), int(id_rol), _get_admin_id(), _get_ip()
    )

    if not exito:
        return jsonify({"error": mensaje}), 400

    return jsonify({
        "mensaje": mensaje,
        "usuario": usuario.to_dict()
    }), 200


# ============================================================
# GET /api/roles/<id> → Ver un rol
# ⚠️ AL FINAL
# ============================================================
@roles_bp.route("/roles/<int:id_rol>", methods=["GET"])
@jwt_required()
def obtener_rol(id_rol):
    rol = RolService.obtener_rol(id_rol)
    if not rol:
        return jsonify({"error": "Rol no encontrado"}), 404
    return jsonify(rol.to_dict()), 200


# ============================================================
# GET /api/permisos → Listar todos los permisos
# ============================================================
@roles_bp.route("/permisos", methods=["GET"])
@jwt_required()
def listar_permisos():
    permisos = RolService.listar_permisos()
    return jsonify({
        "total": len(permisos),
        "permisos": [p.to_dict() for p in permisos]
    }), 200