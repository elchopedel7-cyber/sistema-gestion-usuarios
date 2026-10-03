// ============================================================
// Archivo: src/services/api.js
// Descripción: Configuración centralizada de Axios para
//              conectar el frontend con el backend Flask.
// Autor: Juan Andrés Pérez
// Fecha: 2026
// ============================================================

import axios from 'axios'

// ------------------------------------------------------------
// Configuración base
// ------------------------------------------------------------
const api = axios.create({
  baseURL: 'http://127.0.0.1:5000/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// ------------------------------------------------------------
// Interceptor de REQUEST: agrega el JWT automáticamente
// Cada petición lleva el token si existe en localStorage
// ------------------------------------------------------------
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('sgu_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// ------------------------------------------------------------
// Interceptor de RESPONSE: maneja errores globales
// Si el token expira (401), cierra sesión automáticamente
// ------------------------------------------------------------
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Si el backend dice 401 (no autorizado), el token expiró
    if (error.response && error.response.status === 401) {
      // Limpiamos el token
      localStorage.removeItem('sgu_token')
      localStorage.removeItem('sgu_usuario')

      // Si no estamos en login, redirigimos
      if (!window.location.pathname.includes('/login')) {
        window.location.href = '/login'
      }
    }
    return Promise.reject(error)
  }
)

// ============================================================
// SERVICIOS DE AUTENTICACIÓN
// ============================================================

export const authService = {
  /**
   * Inicia sesión con correo y contraseña.
   * @param {string} correo
   * @param {string} contrasena
   */
  login: (correo, contrasena) =>
    api.post('/auth/login', { correo, contrasena }),

  /**
   * Registra un nuevo usuario.
   * @param {string} nombre
   * @param {string} correo
   * @param {string} contrasena
   */
  registro: (nombre, correo, contrasena) =>
    api.post('/auth/registro', { nombre, correo, contrasena })
}

// ============================================================
// SERVICIOS DE USUARIOS
// ============================================================

export const usuarioService = {
  /** Lista todos los usuarios con filtros opcionales. */
  listar: (filtros = {}) => {
    const params = new URLSearchParams()
    if (filtros.busqueda) params.append('busqueda', filtros.busqueda)
    if (filtros.rol) params.append('rol', filtros.rol)
    if (filtros.estado !== undefined) params.append('estado', filtros.estado)
    return api.get(`/usuarios?${params.toString()}`)
  },

  /** Obtiene un usuario específico por ID. */
  obtener: (id) => api.get(`/usuarios/${id}`),

  /** Edita los datos de un usuario. */
  editar: (id, datos) => api.put(`/usuarios/${id}`, datos),

  /** Elimina lógicamente un usuario (estado = false). */
  eliminar: (id) => api.delete(`/usuarios/${id}`),

  /** Reactiva un usuario previamente desactivado. */
  reactivar: (id) => api.put(`/usuarios/${id}/reactivar`)
}

// ============================================================
// SERVICIOS DE ROLES Y PERMISOS
// ============================================================

export const rolService = {
  listar: () => api.get('/roles'),
  obtener: (id) => api.get(`/roles/${id}`),
  crear: (datos) => api.post('/roles', datos),
  asignar: (idUsuario, idRol) =>
    api.post('/roles/asignar', { id_usuario: idUsuario, id_rol: idRol }),
  listarPermisos: () => api.get('/permisos')
}

// ============================================================
// SERVICIOS DE AUDITORÍA
// ============================================================

export const auditoriaService = {
  listar: (filtros = {}) => {
    const params = new URLSearchParams()
    if (filtros.id_usuario) params.append('id_usuario', filtros.id_usuario)
    if (filtros.limite) params.append('limite', filtros.limite)
    return api.get(`/auditoria?${params.toString()}`)
  },
  porUsuario: (id) => api.get(`/auditoria/usuario/${id}`),
  resumen: () => api.get('/auditoria/resumen')
}

// ============================================================
// UTILIDADES
// ============================================================

/**
 * Guarda el token y los datos del usuario en localStorage.
 */
export const guardarSesion = (token, usuario) => {
  localStorage.setItem('sgu_token', token)
  localStorage.setItem('sgu_usuario', JSON.stringify(usuario))
}

/**
 * Elimina la sesión del localStorage.
 */
export const cerrarSesion = () => {
  localStorage.removeItem('sgu_token')
  localStorage.removeItem('sgu_usuario')
}

/**
 * Obtiene el usuario logueado desde localStorage.
 */
export const obtenerUsuario = () => {
  const usuario = localStorage.getItem('sgu_usuario')
  return usuario ? JSON.parse(usuario) : null
}

/**
 * Verifica si hay una sesión activa.
 */
export const estaAutenticado = () => {
  return !!localStorage.getItem('sgu_token')
}

export default api