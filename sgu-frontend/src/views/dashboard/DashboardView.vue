<!-- ============================================================
     Archivo: src/views/dashboard/DashboardView.vue
     Descripción: Panel principal con:
                  - Vista general (usuarios activos/inactivos/todos)
                  - Editar usuario (modal)
                  - Eliminar con confirmación
                  - Reactivar usuarios inactivos
                  - Actividad reciente (auditoría)
     ============================================================ -->

<template>
  <div>
    <header class="navbar-dash">
      <span class="logo-circle"></span>
      <span class="nav-title">Panel de Gestión de Usuarios</span>
    </header>

    <div class="layout-container">
      <Sidebar pantallaActiva="dashboard" />

      <main class="main-content">
        <section class="welcome-section">
          <h1>Bienvenido/a al panel</h1>
          <p class="welcome-sub">Administra usuarios, revisa su estado y ajusta la configuración del sistema desde un solo lugar.</p>
          <div class="toggle-buttons">
            <button
              class="btn-toggle"
              :class="{ active: vistaActiva === 'general' }"
              @click="cambiarVista('general')"
            >
              Vista general
            </button>
            <button
              class="btn-toggle"
              :class="{ active: vistaActiva === 'actividad' }"
              @click="cambiarVista('actividad')"
            >
              Actividad reciente
            </button>
          </div>
        </section>

        <!-- ============================================ -->
        <!-- VISTA 1: GENERAL (USUARIOS)                  -->
        <!-- ============================================ -->
        <template v-if="vistaActiva === 'general'">
          <section class="summary-section">
            <h2>Resumen rápido</h2>
            <p class="section-sub">Indicadores clave del sistema.</p>

            <div class="cards-grid">
              <div class="summary-card">
                <h3>Usuarios activos</h3>
                <p class="card-tag">Total: {{ totalActivos }}</p>
                <p class="card-desc">Usuarios con acceso al sistema.</p>
                <div class="card-footer-icons">✅</div>
              </div>

              <div class="summary-card">
                <h3>Usuarios inactivos</h3>
                <p class="card-tag">Total: {{ totalInactivos }}</p>
                <p class="card-desc">Usuarios desactivados (eliminación lógica).</p>
                <div class="card-footer-icons">⛔</div>
              </div>
            </div>
          </section>

          <section class="users-section">
            <div class="users-left">
              <h2>Usuarios registrados</h2>
              <p class="section-sub">Listado en vivo desde la base de datos.</p>
              <div class="users-actions">
                <input
                  type="text"
                  v-model="busqueda"
                  placeholder="Filtrar por nombre o email..."
                  class="search-input"
                >
                <button class="btn btn-dark" @click="irACrearUsuario">
                  Crear usuario
                </button>
              </div>

              <!-- Filtros por estado -->
              <div class="filtros-estado">
                <button
                  class="btn-filtro"
                  :class="{ active: filtroEstado === 'activos' }"
                  @click="filtroEstado = 'activos'"
                >
                  Activos ({{ totalActivos }})
                </button>
                <button
                  class="btn-filtro"
                  :class="{ active: filtroEstado === 'inactivos' }"
                  @click="filtroEstado = 'inactivos'"
                >
                  Inactivos ({{ totalInactivos }})
                </button>
                <button
                  class="btn-filtro"
                  :class="{ active: filtroEstado === 'todos' }"
                  @click="filtroEstado = 'todos'"
                >
                  Todos ({{ usuarios.length }})
                </button>
              </div>
            </div>

            <div class="users-list-container">
              <div v-if="cargandoUsuarios" class="estado-carga">
                ⏳ Cargando usuarios...
              </div>

              <div v-else-if="errorUsuarios" class="estado-error">
                ⚠️ {{ errorUsuarios }}
              </div>

              <div v-else-if="usuariosFiltrados.length === 0" class="estado-vacio">
                No hay usuarios que coincidan.
              </div>

              <div
                v-else
                class="user-row"
                v-for="usuario in usuariosFiltrados"
                :key="usuario.id_usuario"
              >
                <div class="user-info">
                  <span class="user-avatar">👤</span>
                  <div>
                    <h4 class="user-name">
                      {{ usuario.nombre }}
                      <span v-if="!usuario.estado" class="badge-inactivo">Inactivo</span>
                    </h4>
                    <p class="user-role">
                      {{ usuario.roles && usuario.roles.length ? usuario.roles[0] : 'Sin rol' }}
                    </p>
                  </div>
                </div>

                <div class="user-actions">
                  <span class="user-email">{{ usuario.correo }}</span>

                  <!-- Botón Editar -->
                  <button
                    class="btn-icono btn-editar"
                    @click="abrirEdicion(usuario)"
                    title="Editar usuario"
                  >
                    ✏️
                  </button>

                  <!-- Botón Eliminar (solo si está activo) -->
                  <button
                    v-if="usuario.estado"
                    class="btn-icono btn-eliminar"
                    @click="confirmarEliminar(usuario)"
                    title="Desactivar usuario"
                  >
                    🗑️
                  </button>

                  <!-- Botón Reactivar (solo si está inactivo) -->
                  <button
                    v-else
                    class="btn-icono btn-reactivar"
                    @click="confirmarReactivar(usuario)"
                    title="Reactivar usuario"
                  >
                    🔄
                  </button>
                </div>
              </div>
            </div>
          </section>
        </template>

        <!-- ============================================ -->
        <!-- VISTA 2: ACTIVIDAD RECIENTE (AUDITORÍA)      -->
        <!-- ============================================ -->
        <template v-else>
          <section class="summary-section">
            <h2>Actividad reciente</h2>
            <p class="section-sub">Historial de acciones registradas en el sistema.</p>

            <div class="cards-grid">
              <div class="summary-card">
                <h3>Total de acciones</h3>
                <p class="card-tag">{{ auditoria.length }} registros</p>
                <p class="card-desc">Todas las acciones importantes quedan registradas.</p>
                <div class="card-footer-icons">📋</div>
              </div>

              <div class="summary-card">
                <h3>Última actividad</h3>
                <p class="card-tag">
                  {{ auditoria[0] ? formatearFecha(auditoria[0].fecha) : 'Sin registros' }}
                </p>
                <p class="card-desc">El sistema registra cada inicio de sesión y cambio.</p>
                <div class="card-footer-icons">🕐</div>
              </div>
            </div>
          </section>

          <section class="users-section">
            <div class="users-left">
              <h2>Historial</h2>
              <p class="section-sub">Últimas acciones registradas.</p>
            </div>

            <div class="users-list-container">
              <div v-if="cargandoAuditoria" class="estado-carga">
                ⏳ Cargando historial...
              </div>

              <div v-else-if="errorAuditoria" class="estado-error">
                ⚠️ {{ errorAuditoria }}
              </div>

              <div v-else-if="auditoria.length === 0" class="estado-vacio">
                No hay registros de auditoría todavía.
              </div>

              <div
                v-else
                class="user-row"
                v-for="registro in auditoria"
                :key="registro.id_auditoria"
              >
                <div class="user-info">
                  <span class="user-avatar">📋</span>
                  <div>
                    <h4 class="user-name">{{ registro.accion }}</h4>
                    <p class="user-role">{{ registro.nombre_usuario }}</p>
                  </div>
                </div>
                <span class="user-email">{{ formatearFecha(registro.fecha) }}</span>
              </div>
            </div>
          </section>
        </template>
      </main>
    </div>

    <!-- ============================================ -->
    <!-- MODAL DE EDICIÓN                             -->
    <!-- ============================================ -->
    <div v-if="modalEdicion" class="modal-overlay" @click.self="cerrarEdicion">
      <div class="modal-edicion">
        <h3>Editar usuario</h3>
        <p class="modal-sub">{{ usuarioEditando.correo }}</p>

        <div class="modal-form">
          <label>Nombre completo</label>
          <input type="text" v-model="formEdicion.nombre">

          <label>Correo electrónico</label>
          <input type="email" v-model="formEdicion.correo">

          <label>Rol</label>
          <select v-model="formEdicion.rol">
            <option value="Administrador">Administrador</option>
            <option value="Editor">Editor</option>
            <option value="Lector">Lector</option>
          </select>

          <label>Estado</label>
          <select v-model="formEdicion.estado">
            <option :value="true">Activo</option>
            <option :value="false">Inactivo</option>
          </select>
        </div>

        <div v-if="errorEdicion" class="modal-error">⚠️ {{ errorEdicion }}</div>

        <div class="modal-actions">
          <button class="btn btn-outline" @click="cerrarEdicion">Cancelar</button>
          <button class="btn btn-dark" @click="guardarEdicion" :disabled="guardandoEdicion">
            {{ guardandoEdicion ? 'Guardando...' : 'Guardar cambios' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Sidebar from '../../components/layout/Sidebar.vue'
import { usuarioService, auditoriaService } from '../../services/api'

const router = useRouter()

const vistaActiva = ref('general')

// Usuarios
const cargandoUsuarios = ref(true)
const errorUsuarios = ref('')
const busqueda = ref('')
const usuarios = ref([])
const filtroEstado = ref('activos')  // activos | inactivos | todos

// Auditoría
const cargandoAuditoria = ref(false)
const errorAuditoria = ref('')
const auditoria = ref([])

// Modal de edición
const modalEdicion = ref(false)
const usuarioEditando = ref({})
const formEdicion = ref({ nombre: '', correo: '', rol: '', estado: true })
const guardandoEdicion = ref(false)
const errorEdicion = ref('')

// Contadores
const totalActivos = computed(() => usuarios.value.filter(u => u.estado).length)
const totalInactivos = computed(() => usuarios.value.filter(u => !u.estado).length)

// Filtro de usuarios
const usuariosFiltrados = computed(() => {
  let lista = usuarios.value

  // Filtrar por estado
  if (filtroEstado.value === 'activos') {
    lista = lista.filter(u => u.estado)
  } else if (filtroEstado.value === 'inactivos') {
    lista = lista.filter(u => !u.estado)
  }

  // Filtrar por búsqueda
  if (busqueda.value) {
    const texto = busqueda.value.toLowerCase()
    lista = lista.filter(u =>
      u.nombre.toLowerCase().includes(texto) ||
      u.correo.toLowerCase().includes(texto)
    )
  }

  return lista
})

// ============================================
// CARGAR DATOS
// ============================================
const cargarUsuarios = async () => {
  try {
    cargandoUsuarios.value = true
    errorUsuarios.value = ''
    const respuesta = await usuarioService.listar()
    usuarios.value = respuesta.data.usuarios || []
    console.log('✅ Usuarios cargados:', usuarios.value.length)
  } catch (err) {
    console.error('❌ Error al cargar usuarios:', err)
    errorUsuarios.value = err.response
      ? 'Error del servidor: ' + (err.response.data.error || err.response.status)
      : 'No se pudo conectar al servidor.'
  } finally {
    cargandoUsuarios.value = false
  }
}

const cargarAuditoria = async () => {
  try {
    cargandoAuditoria.value = true
    errorAuditoria.value = ''
    const respuesta = await auditoriaService.listar({ limite: 30 })
    auditoria.value = respuesta.data.registros || []
    console.log('✅ Auditoría cargada:', auditoria.value.length)
  } catch (err) {
    console.error('❌ Error al cargar auditoría:', err)
    errorAuditoria.value = err.response
      ? 'Error del servidor'
      : 'No se pudo conectar al servidor.'
  } finally {
    cargandoAuditoria.value = false
  }
}

const cambiarVista = (vista) => {
  vistaActiva.value = vista
  if (vista === 'actividad' && auditoria.value.length === 0) {
    cargarAuditoria()
  }
}

// ============================================
// EDITAR USUARIO
// ============================================
const abrirEdicion = (usuario) => {
  usuarioEditando.value = usuario
  formEdicion.value = {
    nombre: usuario.nombre,
    correo: usuario.correo,
    rol: usuario.roles && usuario.roles.length ? usuario.roles[0] : 'Lector',
    estado: usuario.estado
  }
  errorEdicion.value = ''
  modalEdicion.value = true
}

const cerrarEdicion = () => {
  modalEdicion.value = false
  usuarioEditando.value = {}
}

const guardarEdicion = async () => {
  errorEdicion.value = ''
  guardandoEdicion.value = true

  try {
    await usuarioService.editar(usuarioEditando.value.id_usuario, {
      nombre: formEdicion.value.nombre,
      correo: formEdicion.value.correo,
      estado: formEdicion.value.estado,
      rol: formEdicion.value.rol
    })

    console.log('✅ Usuario actualizado')
    modalEdicion.value = false
    await cargarUsuarios()

  } catch (err) {
    console.error('❌ Error al editar:', err)
    errorEdicion.value = err.response
      ? (err.response.data.error || 'Error al guardar')
      : 'No se pudo conectar al servidor.'
  } finally {
    guardandoEdicion.value = false
  }
}

// ============================================
// ELIMINAR (DESACTIVAR) USUARIO
// ============================================
const confirmarEliminar = async (usuario) => {
  const confirmar = window.confirm(
    `¿Estás seguro de desactivar a "${usuario.nombre}"?\n\n` +
    `El usuario quedará inactivo pero podrá reactivarse después.`
  )

  if (!confirmar) return

  try {
    await usuarioService.eliminar(usuario.id_usuario)
    console.log('✅ Usuario desactivado')
    await cargarUsuarios()
  } catch (err) {
    console.error('❌ Error al desactivar:', err)
    alert(err.response?.data?.error || 'No se pudo desactivar el usuario')
  }
}

// ============================================
// REACTIVAR USUARIO
// ============================================
const confirmarReactivar = async (usuario) => {
  const confirmar = window.confirm(
    `¿Reactivar a "${usuario.nombre}"?\n\n` +
    `El usuario recuperará el acceso al sistema.`
  )

  if (!confirmar) return

  try {
    await usuarioService.reactivar(usuario.id_usuario)
    console.log('✅ Usuario reactivado')
    await cargarUsuarios()
  } catch (err) {
    console.error('❌ Error al reactivar:', err)
    alert(err.response?.data?.error || 'No se pudo reactivar el usuario')
  }
}

// ============================================
// UTILIDADES
// ============================================
const formatearFecha = (fechaISO) => {
  if (!fechaISO) return 'Sin fecha'
  const fecha = new Date(fechaISO)
  return fecha.toLocaleString('es-CO', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const irACrearUsuario = () => {
  router.push('/crear-usuario')
}

onMounted(() => {
  cargarUsuarios()
})
</script>

<style scoped>
.estado-carga,
.estado-vacio,
.estado-error {
  padding: 30px;
  text-align: center;
  font-size: 14px;
  color: #555;
}

.estado-error {
  color: #991b1b;
  background-color: #fee2e2;
  border-left: 4px solid #e74c3c;
}

.badge-inactivo {
  background-color: #e74c3c;
  color: white;
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 12px;
  margin-left: 8px;
  font-weight: 500;
}

.filtros-estado {
  display: flex;
  gap: 8px;
  margin-top: 15px;
}

.btn-filtro {
  padding: 6px 14px;
  background-color: #ffffff;
  border: 1px solid #cccccc;
  border-radius: 6px;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-filtro:hover {
  border-color: #2c3e50;
}

.btn-filtro.active {
  background-color: #2c3e50;
  color: #ffffff;
  border-color: #2c3e50;
}

.user-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-icono {
  background: transparent;
  border: 1px solid transparent;
  padding: 6px 8px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 6px;
  transition: all 0.2s ease;
}

.btn-icono:hover {
  background-color: #e8eef7;
  transform: scale(1.1);
}

.btn-editar:hover {
  border-color: #3498db;
}

.btn-eliminar:hover {
  border-color: #e74c3c;
  background-color: #fee2e2;
}

.btn-reactivar:hover {
  border-color: #28a745;
  background-color: #e2f0d9;
}

/* ============================================ */
/* MODAL                                        */
/* ============================================ */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
  backdrop-filter: blur(4px);
}

.modal-edicion {
  background-color: #ffffff;
  border-radius: 12px;
  padding: 32px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  animation: modalIn 0.3s ease;
}

@keyframes modalIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}

.modal-edicion h3 {
  font-size: 22px;
  margin-bottom: 6px;
  color: #000000;
}

.modal-sub {
  font-size: 13px;
  color: #666;
  margin-bottom: 24px;
}

.modal-form {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 20px;
}

.modal-form label {
  font-size: 13px;
  font-weight: 600;
  color: #333;
  margin-top: 8px;
}

.modal-form input,
.modal-form select {
  padding: 10px 14px;
  border: 1px solid #cccccc;
  border-radius: 8px;
  font-size: 14px;
  transition: border-color 0.2s ease;
}

.modal-form input:focus,
.modal-form select:focus {
  border-color: #2c3e50;
  outline: none;
}

.modal-error {
  background-color: #fee2e2;
  border-left: 4px solid #e74c3c;
  color: #991b1b;
  padding: 12px 16px;
  border-radius: 6px;
  font-size: 13px;
  margin-bottom: 16px;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}
</style>