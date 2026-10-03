<!-- ============================================================
     Archivo: src/views/auth/LoginExitoView.vue
     Descripción: Pantalla de login exitoso (redirige al dashboard).
     ============================================================ -->

<template>
  <div>
    <header class="navbar-status">
      <div class="nav-content">
        <span class="logo-circle"></span>
        <span class="nav-title">Validación de autenticación</span>
      </div>
    </header>

    <main class="status-container">
      <div class="top-status-box">
        <div class="placeholder-square"></div>
        <div class="mini-icons">
          <span class="icon-blue"></span>
          <span class="icon-green"></span>
        </div>
      </div>

      <section class="status-section">
        <div class="status-left">
          <h2>Estado</h2>
          <p class="status-sub">Autenticación aprobada</p>
        </div>

        <div class="status-right">
          <span class="status-lock-icon">🔓</span>
          <div class="status-message">
            <p class="msg-title">Credenciales correctas</p>
            <p class="msg-sub">Redirigiendo a tu espacio de trabajo...</p>
          </div>
        </div>
      </section>

      <div class="action-container">
        <button class="btn-submit" @click="irAlDashboard">continúa</button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const irAlDashboard = () => {
  router.push('/dashboard')
}
</script>