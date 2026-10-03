"""
============================================================
Archivo: app.py
Descripción: Punto de entrada principal del backend del 
             Sistema de Gestión de Usuarios (SGU).
             Configurado con CORS para aceptar peticiones 
             del frontend Vue.js.
Autor: Juan Andrés Pérez
Fecha: 2026
============================================================
"""

from flask import Flask, jsonify
from flask_cors import CORS

from config import Config
from extensions import db, jwt


def create_app():
    """Fábrica que crea y configura la aplicación Flask."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # --------------------------------------------------------
    # Inicializar extensiones
    # --------------------------------------------------------
    db.init_app(app)
    jwt.init_app(app)

    # --------------------------------------------------------
    # CONFIGURACIÓN DE CORS
    # Permite que el frontend (localhost:5173) hable con el
    # backend (127.0.0.1:5000)
    # --------------------------------------------------------
    CORS(
        app,
        resources={r"/api/*": {
            "origins": [
                "http://localhost:5173",
                "http://127.0.0.1:5173",
                "http://localhost:3000"
            ]
        }},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        expose_headers=["Content-Type", "Authorization"]
    )

    # --------------------------------------------------------
    # Importar modelos
    # --------------------------------------------------------
    from models import Usuario, Rol, Permiso, Auditoria

    # --------------------------------------------------------
    # Registrar Blueprints (rutas)
    # --------------------------------------------------------
    from routes.auth import auth_bp
    from routes.usuarios import usuarios_bp
    from routes.roles import roles_bp
    from routes.auditoria import auditoria_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(roles_bp)
    app.register_blueprint(auditoria_bp)

    # --------------------------------------------------------
    # Ruta de prueba (health check)
    # --------------------------------------------------------
    @app.route("/api/health", methods=["GET"])
    def health_check():
        """Verifica que el backend esté funcionando."""
        return jsonify({
            "status": "ok",
            "mensaje": "Backend del Sistema de Gestión de Usuarios funcionando",
            "version": "1.0.0"
        }), 200

    return app


if __name__ == "__main__":
    app = create_app()
    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE USUARIOS - BACKEND")
    print("  Servidor: http://127.0.0.1:5000")
    print("  Health:   http://127.0.0.1:5000/api/health")
    print("  CORS:     Aceptando peticiones de localhost:5173")
    print("=" * 60)
    app.run(host="0.0.0.0", port=5000, debug=True)