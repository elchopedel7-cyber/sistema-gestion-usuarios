// ============================================================
// Archivo: src/router/index.js
// ============================================================

import { createRouter, createWebHistory } from 'vue-router'
import CambioExitosoView from '../views/general/CambioExitosoView.vue'

// Vistas AUTH
import LoginView from '../views/auth/LoginView.vue'
import LoginExitoView from '../views/auth/LoginExitoView.vue'
import LoginErrorView from '../views/auth/LoginErrorView.vue'
import RegistroView from '../views/auth/RegistroView.vue'
import RegistroExitoView from '../views/auth/RegistroExitoView.vue'
import RegistroErrorView from '../views/auth/RegistroErrorView.vue'


// Vistas generales
import LoadingView from '../views/general/LoadingView.vue'

// Vistas dashboard
import DashboardView from '../views/dashboard/DashboardView.vue'
import UsuarioView from '../views/dashboard/UsuarioView.vue'
import ConfiguracionView from '../views/dashboard/ConfiguracionView.vue'
import CrearUsuarioView from '../views/dashboard/CrearUsuarioView.vue'

// Vistas logout
import LogoutModalView from '../views/logout/LogoutModalView.vue'
import CerrandoSesionView from '../views/logout/CerrandoSesionView.vue'
import SesionCerradaView from '../views/logout/SesionCerradaView.vue'

const routes = [
  { path: '/', redirect: '/login' },

  // ---------- AUTH ----------
  { path: '/login', name: 'login', component: LoginView },
  { path: '/login-exito', name: 'login-exito', component: LoginExitoView },
  { path: '/login-error', name: 'login-error', component: LoginErrorView },
  { path: '/registro', name: 'registro', component: RegistroView },
  { path: '/registro-exito', name: 'registro-exito', component: RegistroExitoView },
  { path: '/registro-error', name: 'registro-error', component: RegistroErrorView },

  // ---------- GENERAL ----------
  { path: '/cargando', name: 'cargando', component: LoadingView },
  { path: '/cambio-exitoso', name: 'cambio-exitoso', component: CambioExitosoView },

  // ---------- DASHBOARD ----------
  { path: '/dashboard', name: 'dashboard', component: DashboardView },
  { path: '/usuario', name: 'usuario', component: UsuarioView },
  { path: '/configuracion', name: 'configuracion', component: ConfiguracionView },
  { path: '/crear-usuario', name: 'crear-usuario', component: CrearUsuarioView },

  // ---------- LOGOUT ----------
  { path: '/logout-modal', name: 'logout-modal', component: LogoutModalView },
  { path: '/cerrando-sesion', name: 'cerrando-sesion', component: CerrandoSesionView },
  { path: '/sesion-cerrada', name: 'sesion-cerrada', component: SesionCerradaView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router