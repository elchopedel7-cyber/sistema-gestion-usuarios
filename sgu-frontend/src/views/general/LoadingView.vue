<!-- ============================================================
     Archivo: src/views/general/LoadingView.vue
     Descripción: Pantalla de carga con spinner y mensaje.
     ============================================================ -->

<template>
  <main class="loading-container">
    <div class="loading-content">
      <div class="lock-icon">🔒</div>
      <p class="loading-text">{{ mensaje }}</p>
    </div>
  </main>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
const mensaje = route.query.msg || 'Cargando...'
</script>