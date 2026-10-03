<!-- ============================================================
     Archivo: src/views/dashboard/CrearUsuarioView.vue
     Descripción: Formulario para crear un nuevo usuario.
                  CONECTADO al backend Flask.
     ============================================================ -->

<template>
  <div>
    <header class="navbar">
      <div class="nav-content">
        <span class="logo-circle"></span>
        <span class="nav-title">Admin Dashboard</span>
      </div>
    </header>

    <main class="container-crear-usuario">
      <section class="form-header-crear">
        <h1>Crear información de usuario</h1>
        <h2>Creación de datos del usuario</h2>
        <p class="header-sub">Ingresar los datos del nuevo usuario</p>
      </section>

      <!-- Mensaje de error -->
      <div v-if="errorMensaje" class="alerta-error">
        ⚠️ {{ errorMensaje }}
      </div>

      <section class="form-section-crear">
        <form class="form-grid-crear" @submit.prevent="crearUsuario">
          <div class="form-group-crear">
            <label for="user-id">ID Usuario (deshabilitado)</label>
            <input
              type="text"
              id="user-id"
              value="Nuevo"
              disabled
              class="input-disabled"
            >
            <small>Se asignará automáticamente</small>
          </div>

          <div class="form-group-crear">
            <label for="fullname">Nombre Completo</label>
            <input
              type="text"
              id="fullname"
              v-model="nuevoUsuario.nombre"
              placeholder="Ej. Carlos Pérez"
              required
            >
          </div>

          <div class="form-group-crear full-width">
            <label for="email">Correo Electrónico</label>
            <input
              type="email"
              id="email"
              v-model="nuevoUsuario.correo"
              placeholder="correo@empresa.com"
              required
            >
          </div>

          <div class="form-group-crear full-width">
            <label for="password">Contraseña</label>
            <input
              type="password"
              id="password"
              v-model="nuevoUsuario.contrasena"
              placeholder="Mínimo 8 caracteres (ej: User123!)"
              required
            >
            <small>Debe tener mayúscula, minúscula, número y carácter especial</small>
          </div>

          <div class="form-group-crear full-width">
            <label>Rol Asignado</label>
            <div class="role-selector-crear">
              <button
                type="button"
                class="btn-role"
                :class="{ active: nuevoUsuario.rol === 'Administrador' }"
                @click="nuevoUsuario.rol = 'Administrador'"
              >
                Administrador
              </button>
              <button
                type="button"
                class="btn-role"
                :class="{ active: nuevoUsuario.rol === 'Editor' }"
                @click="nuevoUsuario.rol = 'Editor'"
              >
                Editor
              </button>
              <button
                type="button"
                class="btn-role"
                :class="{ active: nuevoUsuario.rol === 'Lector' }"
                @click="nuevoUsuario.rol = 'Lector'"
              >
                Lector
              </button>
            </div>
            <small>Define permisos del usuario</small>
          </div>

          <div class="form-actions-crear full-width">
            <button
              type="button"
              class="btn btn-outline"
              @click="cancelar"
            >
              Cancelar
            </button>
            <button
              type="submit"
              class="btn btn-dark"
              :disabled="cargando"
            >
              {{ cargando ? 'Creando...' : 'Guardar cambios' }}
            </button>
          </div>
        </form>
      </section>
    </main>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { authService, usuarioService } from '../../services/api'

const router = useRouter()

const cargando = ref(false)
const errorMensaje = ref('')

const nuevoUsuario = reactive({
  nombre: '',
  correo: '',
  contrasena: '',
  rol: 'Lector'
})

const crearUsuario = async () => {
  errorMensaje.value = ''

  // Validaciones básicas
  if (!nuevoUsuario.nombre || !nuevoUsuario.correo || !nuevoUsuario.contrasena) {
    errorMensaje.value = 'Completa todos los campos'
    return
  }

  cargando.value = true

  try {
    // 1. Crear el usuario con el backend
    const respuesta = await authService.registro(
      nuevoUsuario.nombre,
      nuevoUsuario.correo,
      nuevoUsuario.contrasena
    )

    const usuarioCreado = respuesta.data.usuario
    console.log('✅ Usuario creado:', usuarioCreado)

    // 2. Asignar el rol seleccionado
    //    Primero obtener los roles del backend
    const rolesResp = await usuarioService.obtener(usuarioCreado.id_usuario)
    console.log('Usuario obtenido:', rolesResp.data)

    // Asignar rol usando el endpoint de asignar
    // Necesitamos el id del rol según su nombre
    const rolesLista = await import('../../services/api').then(m => m.rolService.listar())
    const rolEncontrado = rolesLista.data.roles.find(
      r => r.nombre_rol === nuevoUsuario.rol
    )

    if (rolEncontrado) {
      const apiModule = await import('../../services/api')
      await apiModule.rolService.asignar(
        usuarioCreado.id_usuario,
        rolEncontrado.id_rol
      )
      console.log('✅ Rol asignado:', nuevoUsuario.rol)
    }

    // 3. Ir a la pantalla de éxito
    router.push('/cambio-exitoso')

  } catch (error) {
    console.error('❌ Error al crear usuario:', error)
    cargando.value = false

    if (error.response && error.response.data && error.response.data.error) {
      errorMensaje.value = error.response.data.error
    } else {
      errorMensaje.value = 'No se pudo crear el usuario. Verifica el backend.'
    }
  }
}

const cancelar = () => {
  router.push('/dashboard')
}
</script>

<style scoped>
.alerta-error {
  background-color: #fee2e2;
  border-left: 4px solid #e74c3c;
  color: #991b1b;
  padding: 14px 18px;
  border-radius: 8px;
  margin: 24px auto;
  max-width: 720px;
  font-size: 14px;
  font-weight: 500;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>