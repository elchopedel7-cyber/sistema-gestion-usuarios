<!-- ============================================================
     Archivo: src/views/logout/CerrandoSesionView.vue
     Descripción: Pantalla de transición cerrando sesión.
     ============================================================ -->

<template>
  <div>
    <header class="navbar">
      <div class="nav-content">
        <span class="logo-circle"></span>
        <span class="nav-title">Cerrando sesión...</span>
      </div>
    </header>

    <main class="cerrando-container">
      <section class="cerrando-status-hero">
        <h1>Cerrando sesión...</h1>
        <p class="cerrando-status-sub">Guardando preferencias y cerrando conexión segura.</p>
      </section>

      <section class="cerrando-loading-detail">
        <div class="cerrando-info-box">
          <div class="cerrando-spinner-container">
            <div class="cerrando-loading-spinner"></div>
          </div>
          <div class="cerrando-info-text">
            <p>Elemento central: Ícono de candado cerrándose (o logo de la plataforma).</p>
            <p>Debajo: Indicador de carga (spinner) moderno girando suavemente...</p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// Después de 3 segundos, va a la pantalla de sesión cerrada
onMounted(() => {
  setTimeout(() => {
    router.push('/sesion-cerrada')
  }, 3000)
})
</script>