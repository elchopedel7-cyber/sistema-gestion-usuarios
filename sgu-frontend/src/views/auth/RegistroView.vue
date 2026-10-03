<!-- ============================================================
     Archivo: src/views/auth/RegistroView.vue
     Descripción: Pantalla de registro conectada al backend.
     ============================================================ -->

<template>
  <div>
    <header class="navbar">
      <div class="nav-left">
        <span class="logo-circle"></span>
        <span class="nav-title">Acceso</span>
      </div>
      <div class="nav-right">
        <router-link to="/login" class="nav-link">Inicio</router-link>
        <a href="#" class="nav-link">Ayuda</a>
      </div>
    </header>

    <main class="container">
      <section class="info-side">
        <h1>Registro</h1>
        <p class="subtitle">Completa tus datos para continuar.</p>
      </section>

      <section class="form-side">
        <!-- Mensaje de error si falla el registro -->
        <div v-if="errorMensaje" class="alerta-error">
          ⚠️ {{ errorMensaje }}
        </div>

        <form @submit.prevent="crearCuenta">
          <div class="form-group">
            <label for="fullname">Nombre completo</label>
            <input
              type="text"
              id="fullname"
              v-model="nombre"
              placeholder="Ej. María González"
            >
            <small>Como aparece en tus documentos.</small>
          </div>

          <div class="form-group">
            <label for="email">Correo electrónico</label>
            <input
              type="email"
              id="email"
              v-model="email"
              placeholder="tucorreo@ejemplo.com"
            >
            <small>Usaremos este correo para confirmar tu cuenta.</small>
          </div>

          <div class="form-group">
            <label for="password">Contraseña</label>
            <input
              type="password"
              id="password"
              v-model="password"
              placeholder="Mínimo 8 caracteres"
            >
            <small>Incluye mayúscula, minúscula, número y carácter especial (ej: Juan123!)</small>
          </div>

          <div class="form-group">
            <label for="confirm-password">Confirmar contraseña</label>
            <input
              type="password"
              id="confirm-password"
              v-model="confirmPassword"
              placeholder="Repite tu contraseña"
            >
            <small>Debe coincidir exactamente.</small>
          </div>

          <div class="form-actions">
            <router-link to="/login" class="btn btn-outline">Ya tengo cuenta</router-link>
            <button type="submit" class="btn btn-dark">Crear cuenta</button>
          </div>
        </form>
      </section>
    </main>

    <footer class="footer">
      <p>© 2026 Plataforma &nbsp;&nbsp;&nbsp;&nbsp;
        <a href="#">Privacidad</a> &nbsp;&nbsp;&nbsp;&nbsp;
        <a href="#">Términos</a> &nbsp;&nbsp;&nbsp;&nbsp;
        <a href="#">Soporte</a>
      </p>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { authService } from '../../services/api'

const router = useRouter()

const nombre = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const errorMensaje = ref('')

const crearCuenta = async () => {
  errorMensaje.value = ''

  // 1. Validar campos vacíos
  if (!nombre.value || !email.value || !password.value || !confirmPassword.value) {
    alert('Por favor, completa todos los campos')
    return
  }

  // 2. Validar que las contraseñas coincidan
  if (password.value !== confirmPassword.value) {
    alert('Las contraseñas no coinciden')
    return
  }

  // 3. Guardar valores antes de navegar
  const nombreGuardado = nombre.value
  const correoGuardado = email.value
  const passGuardado = password.value

  // 4. Navegar inmediatamente a la pantalla de carga
  router.push({ path: '/cargando', query: { msg: 'Creando tu cuenta...' } })

  // 5. Esperar 1 segundo y llamar al backend
  setTimeout(async () => {
    try {
      // Llamar al backend real para crear el usuario
      const respuesta = await authService.registro(
        nombreGuardado,
        correoGuardado,
        passGuardado
      )

      console.log('✅ Usuario creado:', respuesta.data)

      // Ir a pantalla de éxito
      router.push('/registro-exito')

    } catch (error) {
      console.log('❌ Error al registrar:', error)

      // Si el backend dio error, ir a pantalla de error
      router.push('/registro-error')
    }
  }, 1000)
}
</script>

<style scoped>
.alerta-error {
  background-color: #fee2e2;
  border-left: 4px solid #e74c3c;
  color: #991b1b;
  padding: 14px 18px;
  border-radius: 8px;
  margin-bottom: 24px;
  font-size: 14px;
  font-weight: 500;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>