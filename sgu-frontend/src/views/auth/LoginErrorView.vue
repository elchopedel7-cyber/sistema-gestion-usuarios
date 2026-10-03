<!-- ============================================================
     Archivo: src/views/auth/LoginErrorView.vue
     Descripción: Pantalla de login fallido.
     ============================================================ -->

<template>
  <div>
    <header class="navbar">
      <div class="nav-content">
        <span class="logo-circle"></span>
        <span class="nav-title">Acceso</span>
      </div>
    </header>

    <main class="error-container">
      <section class="hero-error">
        <h1>Autenticación fallida</h1>
        <p class="hero-sub">No pudimos verificar tus credenciales.</p>
        <div class="hero-actions">
          <button class="btn btn-outline">Contactar soporte</button>
          <button class="btn btn-dark" @click="irAlLogin">Volver al inicio de sesión</button>
        </div>
      </section>

      <section class="info-section">
        <div class="info-left">
          <h2>Estado de error</h2>
          <p class="info-sub">Validación denegada</p>
        </div>

        <div class="info-right-box">
          <div class="box-placeholder"></div>
          <div class="box-text">
            <h3>Datos erróneos o credenciales inválidas</h3>
            <p class="box-sub">Por favor, verifica tu información e intenta nuevamente.</p>
            <p class="box-desc">Revisa tu información e intenta nuevamente.</p>
          </div>
        </div>
      </section>

      <section class="details-section">
        <div class="details-left">
          <h2>Acciones</h2>
          <p class="details-sub">Selecciona una opción para continuar</p>
        </div>

        <div class="details-right-list">
          <div class="detail-item">
            <span class="detail-icon">🔒</span>
            <div class="detail-text">
              <h3>Acceso denegado</h3>
              <p>El candado permanece cerrado y en color rojo de alerta.</p>
            </div>
          </div>

          <div class="detail-item">
            <span class="detail-icon alert-icon">⚠️</span>
            <div class="detail-text">
              <h3>Sin spinner</h3>
              <p>El indicador de carga se oculta completamente.</p>
            </div>
          </div>
        </div>
      </section>
    </main>

    <footer class="footer">
      <p>© Seguridad del sistema &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Consejo: utiliza el mismo método de inicio de sesión registrado.</p>
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const irAlLogin = () => {
  router.push('/login')
}
</script>