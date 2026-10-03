
# Sistema de Gestión de Usuarios (SGU)

**Evidencia:** GA7-220501096-AA3-EV01  
**Nombre de la Evidencia:** Codificación de módulos del software stand-alone, web y móvil  
**Aprendiz:** Juan Andrés Pérez Elguedo  
**Programa:** Análisis y Desarrollo de Software (ADSO)  
**Centro:** SENA - Cartagena, Bolívar  
**Año:** 2026

---

## 📋 Descripción

Sistema web completo para la gestión de usuarios que permite:

- ✅ Registro e inicio de sesión con JWT
- ✅ CRUD de usuarios (crear, listar, editar, eliminar)
- ✅ Eliminación lógica (desactivar/reactivar usuarios)
- ✅ Gestión de roles y permisos (Administrador, Editor, Lector)
- ✅ Auditoría de todas las acciones importantes
- ✅ Filtros por estado y búsqueda

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
|---|---|
| **Backend** | Python 3.14.8 + Flask |
| **Frontend** | Vue.js 3 + Vite + Vue Router |
| **Base de datos** | MySQL |
| **Autenticación** | JWT (JSON Web Tokens) + bcrypt |
| **API** | REST |
| **Control de versiones** | Git + GitHub |

---

## 📁 Estructura del Proyecto

```

sgu/
├── sgu-backend/              # Backend Python + Flask
│   ├── models/               # Modelos SQLAlchemy
│   ├── routes/               # Endpoints REST
│   ├── services/             # Lógica de negocio
│   ├── utils/                # Utilidades (bcrypt)
│   ├── app.py                # Punto de entrada
│   ├── config.py             # Configuración
│   ├── extensions.py         # SQLAlchemy + JWT
│   ├── database.sql          # Script de BD
│   └── requirements.txt      # Dependencias
│
├── sgu-frontend/             # Frontend Vue.js 3
│   ├── src/
│   │   ├── assets/styles/    # CSS global
│   │   ├── components/       # Componentes reutilizables
│   │   ├── views/            # 16 pantallas
│   │   ├── router/           # Vue Router
│   │   ├── services/api.js   # Axios + servicios
│   │   ├── App.vue
│   │   └── main.js
│   ├── index.html
│   └── package.json
│
├── docs/                     # Documentación
├── README.md                 # Este archivo
└── .gitignore

```

---

## 🚀 Instalación y Ejecución

### Requisitos previos

- Python 3.10+ → https://www.python.org/downloads/
- Node.js 18+ → https://nodejs.org/
- MySQL 8+ → https://dev.mysql.com/downloads/mysql/
- Git → https://git-scm.com/

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/sistema-gestion-usuarios.git
cd sistema-gestion-usuarios
```

Paso 2: Configurar la Base de Datos

1. Abrir MySQL Workbench
2. Ejecutar el script sgu-backend/database.sql
3. Se creará la BD gestion_usuarios_db con 6 tablas

Paso 3: Configurar el Backend

```bash
cd sgu-backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Backend corriendo en: http://127.0.0.1:5000

Paso 4: Configurar el Frontend

En otra terminal:

```bash
cd sgu-frontend
npm install
npm run dev
```

Frontend corriendo en: http://localhost:5173

---

🔐 Variables de Entorno

Crear el archivo sgu-backend/.env con:

```env
SECRET_KEY=sgu_secret_key_2026
JWT_SECRET_KEY=sgu_jwt_secret_2026

DB_USER=root
DB_PASSWORD=tu_contraseña_mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=gestion_usuarios_db
```

---

📡 Endpoints de la API

Método Endpoint Descripción Auth
GET /api/health Health check No
POST /api/auth/registro Registro No
POST /api/auth/login Login No
GET /api/usuarios Listar usuarios JWT
GET /api/usuarios/<id> Ver usuario JWT
PUT /api/usuarios/<id> Editar usuario JWT
DELETE /api/usuarios/<id> Eliminar (lógico) JWT
PUT /api/usuarios/<id>/reactivar Reactivar JWT
GET /api/roles Listar roles JWT
POST /api/roles/asignar Asignar rol JWT
GET /api/permisos Listar permisos JWT
GET /api/auditoria Ver auditoría JWT
GET /api/auditoria/resumen Resumen auditoría JWT

---

👥 Usuarios de Prueba

Correo Contraseña Rol
nuevo_admin@sgu.com Nuevo123! Administrador
juan@test.com Juan123! Editor

---

🎨 Pantallas del Frontend

Ruta Descripción
/login Inicio de sesión
/registro Registro de usuario
/dashboard Panel principal
/crear-usuario Crear usuario (admin)
/usuario Panel de usuario
/configuracion Configuración
/logout-modal Confirmar cerrar sesión

---

🧪 Cómo Probar

1. Verificar backend: Abrir http://127.0.0.1:5000/api/health → debe responder JSON
2. Verificar frontend: Abrir http://localhost:5173/login → debe cargar
3. Iniciar sesión con nuevo_admin@sgu.com / Nuevo123!
4. Crear usuario desde el dashboard
5. Editar / eliminar / reactivar usuarios
6. Ver auditoría en la pestaña "Actividad reciente"

---

🔧 Solución de Problemas

Error 401 Unauthorized

El token JWT expiró (dura 1 hora). Cerrar sesión e iniciar de nuevo.

Error de CORS

Verificar que app.py tenga CORS configurado con origins: ["http://localhost:5173"].

No conecta al backend

· Verificar que Flask esté corriendo
· Verificar que el puerto 5000 no esté ocupado

Error de MySQL

Verificar las credenciales en .env y que el servicio MySQL esté activo.

---

📝 Licencia

Proyecto académico SENA - 2026

---

👤 Autor

Juan Andrés Pérez Elguedo
Aprendiz ADSO - SENA Cartagena
2026

