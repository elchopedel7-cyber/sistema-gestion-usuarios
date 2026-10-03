"""
============================================================
Archivo: routes/auditoria.py
Descripción: Endpoint REST para consultar la auditoría.
             GET /api/auditoria           → Listar registros
             GET /api/auditoria/usuario/<id> → Registros de un usuario
             GET /api/auditoria/resumen   → Contar total
Requiere JWT: sí
============================================================
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from services.auditoria_service import AuditoriaService

auditoria_bp = Blueprint("auditoria", __name__, url_prefix="/api/auditoria")


# ============================================================
# GET /api/auditoria → Listar registros de auditoría
# ============================================================
@auditoria_bp.route("", methods=["GET"])
@jwt_required()
def listar():
    """Lista los registros de auditoría con filtros opcionales."""
    filtros = {
        "id_usuario": None,
        "limite": 50
    }

    # Filtro por usuario
    id_usuario = request.args.get("id_usuario")
    if id_usuario:
        try:
            filtros["id_usuario"] = int(id_usuario)
        except ValueError:
            return jsonify({"error": "id_usuario debe ser un número"}), 400

    # Filtro por límite
    limite = request.args.get("limite")
    if limite:
        try:
            filtros["limite"] = int(limite)
        except ValueError:
            return jsonify({"error": "limite debe ser un número"}), 400

    registros = AuditoriaService.listar_auditoria(filtros)

    return jsonify({
        "total": len(registros),
        "registros": [AuditoriaService.to_dict_con_usuario(r) for r in registros]
    }), 200


# ============================================================
# GET /api/auditoria/usuario/<id> → Registros de un usuario
# ============================================================
@auditoria_bp.route("/usuario/<int:id_usuario>", methods=["GET"])
@jwt_required()
def listar_por_usuario(id_usuario):
    """Lista los registros de auditoría de un usuario específico."""
    filtros = {"id_usuario": id_usuario, "limite": 50}
    registros = AuditoriaService.listar_auditoria(filtros)

    return jsonify({
        "total": len(registros),
        "id_usuario": id_usuario,
        "registros": [AuditoriaService.to_dict_con_usuario(r) for r in registros]
    }), 200


# ============================================================
# GET /api/auditoria/resumen → Contar total de registros
# ============================================================
@auditoria_bp.route("/resumen", methods=["GET"])
@jwt_required()
def resumen():
    """Devuelve un resumen de la auditoría."""
    total = AuditoriaService.contar_auditoria()
    return jsonify({
        "total_registros": total
    }), 200