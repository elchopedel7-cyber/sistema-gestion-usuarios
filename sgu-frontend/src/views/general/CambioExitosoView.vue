<!-- ============================================================
     Archivo: src/views/general/CambioExitosoView.vue
     Descripción: Pantalla de éxito general (usada después de
                  guardar cambios en configuración o crear usuario).
     ============================================================ -->

<template>
  <div>
    <header class="navbar">
      <div class="nav-left">
        <span class="logo-circle"></span>
        <span class="nav-title">cambio exitoso</span>
      </div>
      <div class="nav-right">
        <router-link to="/dashboard" class="nav-link">Inicio</router-link>
        <a href="#" class="nav-link">Ayuda</a>
      </div>
    </header>

    <main class="container-cambio-exitoso">
      <section class="content-side-cambio">
        <h1>¡Cambio Exitoso!</h1>
        <p class="description">Bienvenido/a a la plataforma. Tu cuenta ha sido creada correctamente.</p>
        <p class="description">Ya puedes acceder a todas las funcionalidades.</p>

        <div class="action-container-cambio">
          <button type="button" class="btn-success" @click="irAlDashboard">
            ¡Cambio Exitoso!
          </button>
        </div>
      </section>

      <section class="visual-side-cambio">
        <div class="placeholder-box-cambio"></div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const irAlDashboard = () => router.push('/dashboard')
</script>