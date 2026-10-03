<!-- ============================================================
     Archivo: src/components/layout/Sidebar.vue
     Descripción: Menú lateral del dashboard.
                  Se reutiliza en Dashboard, Usuario y Configuración.
     Props:
       - pantallaActiva: 'dashboard' | 'usuario' | 'configuracion'
     ============================================================ -->

<template>
  <aside class="sidebar">
    <nav class="sidebar-nav">
      <router-link
        to="/dashboard"
        class="sidebar-link"
        :class="{ active: pantallaActiva === 'dashboard' }"
      >
        <span class="sidebar-icon">🏠</span> Inicio
      </router-link>

      <router-link
        to="/usuario"
        class="sidebar-link"
        :class="{ active: pantallaActiva === 'usuario' }"
      >
        <span class="sidebar-icon">👥</span> Usuarios
      </router-link>

      <router-link
        to="/configuracion"
        class="sidebar-link"
        :class="{ active: pantallaActiva === 'configuracion' }"
      >
        <span class="sidebar-icon">⚙️</span> Configuración
      </router-link>

      <button class="sidebar-link logout-link" @click="cerrarSesion">
        <span class="sidebar-icon">🚪</span> ¿Cerrar sesión?
      </button>
    </nav>
  </aside>
</template>

<script setup>
import { useRouter } from 'vue-router'

// Prop para saber qué enlace marcar como activo
defineProps({
  pantallaActiva: {
    type: String,
    default: 'dashboard'
  }
})

const router = useRouter()

const cerrarSesion = () => {
  router.push('/logout-modal')
}
</script>