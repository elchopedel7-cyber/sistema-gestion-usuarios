<!-- ============================================================
     Archivo: src/views/auth/RegistroExitoView.vue
     Descripción: Pantalla de transición de registro exitoso.
     ============================================================ -->

<template>
  <div>
    <header class="navbar">
      <div class="nav-content">
        <span class="logo-circle"></span>
        <span class="nav-title">Registro de Nuevo Usuario</span>
      </div>
    </header>

    <main class="container-transicion">
      <section class="welcome-block">
        <h1>Bienvenido</h1>
        <p class="welcome-sub">Estamos preparando tu registro.</p>
        <div class="action-buttons">
          <button type="button" class="btn btn-outline" @click="irAlLogin">Volver</button>
          <button type="button" class="btn btn-dark" @click="irAlDashboard">Continuar</button>
        </div>
      </section>

      <section class="info-section-transicion">
        <div class="info-left-transicion">
          <h2>Transición de Registro</h2>
          <p class="section-sub">Carga del formulario con configuración de seguridad.</p>
        </div>

        <div class="info-right-box-transicion">
          <div class="box-placeholder"></div>
          <div class="box-content">
            <h3>Nuevo Usuario</h3>
            <p class="highlight-text">Preparación en curso</p>
            <p class="box-desc">Icono central: silueta de persona con un símbolo de "+" junto al icono principal en color azul corporativo.</p>
            <div class="blue-icons">
              <span class="icon-user">👤</span>
              <span class="icon-plus">＋</span>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const irAlLogin = () => router.push('/login')
const irAlDashboard = () => router.push('/dashboard')
</script>