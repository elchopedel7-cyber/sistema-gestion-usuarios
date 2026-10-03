<!-- ============================================================
     Archivo: src/views/logout/LogoutModalView.vue
     Descripción: Modal de confirmación para cerrar sesión.
     ============================================================ -->

<template>
  <div>
    <!-- Fondo desenfocado -->
    <div class="logout-background-blur">
      <header class="navbar-dash" style="filter: blur(0px);">
        <span class="logo-circle"></span>
        <span class="nav-title">Panel de Gestión</span>
      </header>
      <div class="logout-container">
        <section class="logout-hero">
          <h1>Resumen rápido</h1>
          <p class="logout-hero-sub">Este contenido queda desenfocado por el modal de confirmación.</p>
        </section>
        <section class="logout-cards-grid">
          <div class="logout-summary-card">
            <h3>Estado del sistema</h3>
            <p class="card-tag">Operativo</p>
            <p class="card-desc">Monitoreo en tiempo real y reportes listos.</p>
          </div>
          <div class="logout-summary-card">
            <h3>Accesos recientes</h3>
            <p class="card-tag">Hoy</p>
            <p class="card-desc">Actividad de usuarios registrada correctamente.</p>
          </div>
        </section>
      </div>
    </div>

    <!-- Modal encima -->
    <div class="logout-modal-overlay">
      <div class="logout-modal-container">
        <div class="logout-modal-left">
          <h2>Modal: Cerrar sesión<br>(Confirmación)</h2>
          <p class="logout-modal-sub">Tarjeta centrada con fondo desenfocado/oscurecido del panel principal. Botones lado a lado.</p>
        </div>
        <div class="logout-modal-right">
          <p class="logout-meta-label">Icono + Pregunta</p>
          <div class="logout-alert-box">
            <span class="logout-alert-icon">🚪</span>
            <p class="logout-alert-text">¿Cerrar sesión? / ¿Estás seguro de que deseas salir del sistema de gestión?</p>
          </div>
          <div class="logout-modal-actions">
            <button type="button" class="btn btn-outline" @click="cancelar">Cancelar</button>
            <button type="button" class="btn btn-dark" @click="confirmar">Sí, salir</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const cancelar = () => {
  router.push('/dashboard')
}

const confirmar = () => {
  router.push('/cerrando-sesion')
}
</script>