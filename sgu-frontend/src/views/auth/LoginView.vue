<!-- ============================================================
     Archivo: src/views/auth/LoginView.vue
     Descripción: Pantalla de inicio de sesión.
                  CONECTADO al backend Flask pero navegando 
                  inmediatamente a la pantalla de carga.
     ============================================================ -->

<template>
  <div>
    <Navbar />
    <div class="hero-banner"></div>

    <main class="container">
      <section class="login-section">
        <div class="login-form-container">
          <h2>Iniciar sesión</h2>
          <p class="subtitle">Usa tu correo y contraseña para acceder.</p>

          <!-- Mensaje de error si falla el login -->
          <div v-if="errorMensaje" class="alerta-error">
            ⚠️ {{ errorMensaje }}
          </div>

          <form @submit.prevent="iniciarSesion">
            <div class="form-group">
              <label for="email">Correo electrónico</label>
              <input
                type="email"
                id="email"
                v-model="email"
                placeholder="correo@ejemplo.com"
              >
              <small>Ejemplo: juan@test.com</small>
            </div>

            <div class="form-group">
              <label for="password">Contraseña</label>
              <input
                type="password"
                id="password"
                v-model="password"
                placeholder="••••••••"
              >
              <small>Ejemplo: Juan123!</small>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-outline" @click.prevent="recuperar">
                ¿Olvidaste tu contraseña?
              </button>
              <button type="submit" class="btn btn-dark">Ingresar</button>
            </div>
          </form>
        </div>
      </section>

      <section class="register-section">
        <div class="register-left">
          <h3>¿Primera vez aquí?</h3>
          <p>Crea tu cuenta en pocos pasos.</p>
          <div class="register-actions">
            <button class="btn btn-outline">Ver requisitos</button>
            <router-link to="/registro" class="btn btn-dark">Crear cuenta</router-link>
          </div>
        </div>

        <div class="register-right-box">
          <h4>Acceso rápido</h4>
          <p class="highlight-text">Registro en minutos</p>
          <p>Al registrarte podrás guardar información y acceder a tus servicios de forma más eficiente.</p>
        </div>
      </section>
    </main>

    <Footer />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from '../../components/layout/Navbar.vue'
import Footer from '../../components/layout/Footer.vue'
import { authService, guardarSesion } from '../../services/api'

const router = useRouter()

const email = ref('')
const password = ref('')
const errorMensaje = ref('')

// ------------------- LOGIN -------------------
const iniciarSesion = () => {
  // 1. Limpiar errores previos
  errorMensaje.value = ''

  // 2. Validar campos vacíos
  if (!email.value || !password.value) {
    alert('Por favor, completa todos los campos')
    return
  }

  // 3. GUARDAR los valores ANTES de navegar
  //    (porque el componente se destruye al cambiar de ruta)
  const correoGuardado = email.value
  const passGuardado = password.value

  // 4. Navegar INMEDIATAMENTE a la pantalla de carga
  router.push({ path: '/cargando', query: { msg: 'Validando credenciales...' } })

  // 5. Esperar 1 segundo (para que se vea el spinner) y llamar al backend
  setTimeout(async () => {
    try {
      // Llamar al backend real
      const respuesta = await authService.login(correoGuardado, passGuardado)

      // Guardar el JWT y datos del usuario
      guardarSesion(respuesta.data.token, respuesta.data.usuario)

      // Ir a la pantalla de éxito
      router.push('/login-exito')

    } catch (error) {
      // Si falla, ir a la pantalla de error
      console.log('Error de login:', error)
      router.push('/login-error')
    }
  }, 1000)
}

// ------------------- RECUPERAR -------------------
const recuperar = () => {
  alert('Función de recuperar contraseña próximamente disponible.')
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