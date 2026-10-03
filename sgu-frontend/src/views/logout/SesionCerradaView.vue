<!-- ============================================================
     Archivo: src/views/logout/SesionCerradaView.vue
     Descripción: Pantalla final de sesión cerrada.
     ============================================================ -->

<template>
  <div>
    <header class="navbar">
      <div class="nav-content">
        <span class="logo-circle"></span>
        <span class="nav-title">Validación de autenticación</span>
      </div>
    </header>

    <main class="cerrada-container">
      <div class="cerrada-top-status-box">
        <div class="cerrada-placeholder-square"></div>
        <div class="cerrada-mini-icons">
          <span class="cerrada-icon-blue"></span>
          <span class="cerrada-icon-green"></span>
        </div>
      </div>

      <section class="cerrada-status-section">
        <div class="cerrada-status-center">
          <span class="cerrada-lock-icon">🔒</span>
          <div class="cerrada-status-message">
            <h2 class="cerrada-msg-title">sesión cerrada</h2>
            <p class="cerrada-msg-sub">sesión cerrada</p>
          </div>
        </div>
      </section>

      <div class="cerrada-action-container">
        <button class="cerrada-btn-submit" @click="irAlLogin">continúa</button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const irAlLogin = () => router.push('/login')
</script>