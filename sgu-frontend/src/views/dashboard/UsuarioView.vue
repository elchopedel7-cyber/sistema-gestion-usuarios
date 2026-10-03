<!-- ============================================================
     Archivo: src/views/dashboard/UsuarioView.vue
     Descripción: Panel de usuario (solo lectura) con foto editable.
     ============================================================ -->

<template>
  <div>
    <header class="navbar-dash">
      <span class="logo-circle"></span>
      <span class="nav-title">Panel de usuario</span>
    </header>

    <div class="layout-container">
      <Sidebar pantallaActiva="usuario" />

      <main class="main-content">
        <section class="account-header">
          <!-- Avatar con opción de cambiar foto -->
          <div class="avatar-wrapper">
            <div class="avatar-large">
              <img
                v-if="fotoPerfil"
                :src="fotoPerfil"
                alt="Foto de perfil"
                class="avatar-image"
              >
              <span v-else class="avatar-placeholder">👤</span>
            </div>

            <!-- Input para subir foto (oculto) -->
            <input
              ref="inputFoto"
              type="file"
              accept="image/*"
              class="input-foto-oculto"
              @change="cargarFoto"
            >

            <!-- Botones -->
            <div class="avatar-buttons">
              <button class="btn-foto" @click="abrirSelector">
                📷 {{ fotoPerfil ? 'Cambiar foto' : 'Subir foto' }}
              </button>
              <button
                v-if="fotoPerfil"
                class="btn-foto btn-foto-quitar"
                @click="quitarFoto"
              >
                🗑️ Quitar
              </button>
            </div>
          </div>

          <div class="account-info">
            <h1>Cuenta</h1>
            <p class="account-tag">#bienvenido / Vista de resumen</p>
            <p class="account-desc">Este panel muestra el contexto del sistema y el significado de los roles. Solo lectura, sin controles ni acciones.</p>
          </div>
        </section>

        <section class="account-summary">
          <div class="summary-left">
            <h2>Resumen de tu cuenta</h2>
            <p class="section-sub">Información personal (solo lectura) y contexto de acceso por rol.</p>
          </div>

          <div class="summary-right-cards">
            <div class="info-card">
              <h3>Usuario</h3>
              <p class="card-tag">Identificación</p>
              <p class="card-data"><strong>Nombre y rol asignado:</strong> Alex Moreno – Administración.</p>
            </div>
            <div class="info-card">
              <h3>Contacto</h3>
              <p class="card-tag">Datos básicos</p>
              <p class="card-data"><strong>Email:</strong> alex.moreno@empresa.com · <strong>Dpto:</strong> Operaciones</p>
            </div>
          </div>
        </section>

        <section class="roles-section">
          <h2>Permisos por roles (solo lectura)</h2>
          <p class="section-sub">Cuatro tarjetas informativas para entender qué puede hacer cada rol.</p>

          <div class="roles-grid">
            <div class="role-card">
              <div class="role-icon">🛠️</div>
              <h3>Administrador</h3>
              <p class="role-tag">Gestión total</p>
              <p class="role-desc">Acceso a configuración global y usuarios.</p>
            </div>
            <div class="role-card">
              <div class="role-icon">🚨</div>
              <h3>Soporte</h3>
              <p class="role-tag">Atención</p>
              <p class="role-desc">Asiste incidentes y consulta logs.</p>
            </div>
            <div class="role-card">
              <div class="role-icon">📊</div>
              <h3>Analista</h3>
              <p class="role-tag">Consulta</p>
              <p class="role-desc">Accede a reportes y métricas.</p>
            </div>
            <div class="role-card">
              <div class="role-icon">👁️</div>
              <h3>Lectura</h3>
              <p class="role-tag">Visualización</p>
              <p class="role-desc">Solo lectura de información permitida.</p>
            </div>
          </div>
        </section>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Sidebar from '../../components/layout/Sidebar.vue'

// Referencia al input file (oculto)
const inputFoto = ref(null)

// Foto de perfil actual (URL de la imagen)
const fotoPerfil = ref('')

// Abrir el selector de archivos
const abrirSelector = () => {
  inputFoto.value.click()
}

// Cargar la imagen seleccionada
const cargarFoto = (event) => {
  const archivo = event.target.files[0]
  if (!archivo) return

  // Validar que sea imagen
  if (!archivo.type.startsWith('image/')) {
    alert('Por favor, selecciona una imagen válida (JPG, PNG, etc.)')
    return
  }

  // Validar tamaño máximo (2 MB)
  if (archivo.size > 2 * 1024 * 1024) {
    alert('La imagen no debe superar los 2 MB')
    return
  }

  // Convertir a base64 para mostrarla
  const reader = new FileReader()
  reader.onload = (e) => {
    fotoPerfil.value = e.target.result
  }
  reader.readAsDataURL(archivo)
}

// Quitar la foto
const quitarFoto = () => {
  fotoPerfil.value = ''
  if (inputFoto.value) {
    inputFoto.value.value = ''
  }
}
</script>