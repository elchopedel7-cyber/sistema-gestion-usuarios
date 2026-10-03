<!-- ============================================================
     Archivo: src/components/layout/Navbar.vue
     Descripción: Barra de navegación para las pantallas de
                  login y registro.
     ============================================================ -->

<template>
  <header class="navbar">
    <div class="nav-left">
      <span class="logo-circle"></span>
      <router-link to="/login" class="nav-link active">Inicio</router-link>
    </div>
    <div class="nav-right">
      <a href="#" class="nav-link">Ayuda</a>
      <a href="#" class="nav-link">Soporte</a>
      <router-link to="/registro" class="nav-link">Crear cuenta</router-link>
    </div>
  </header>
</template>

<script setup>
// No necesita lógica
</script>