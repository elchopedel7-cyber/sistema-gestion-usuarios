<!-- ============================================================
     Archivo: src/views/dashboard/ConfiguracionView.vue
     Descripción: Pantalla de configuración del sistema.
     ============================================================ -->

<template>
  <div>
    <header class="navbar-dash">
      <span class="logo-circle"></span>
      <span class="nav-title">Configuración unificada</span>
    </header>

    <div class="layout-container">
      <Sidebar pantallaActiva="configuracion" />

      <main class="main-content">
        <section class="settings-header">
          <h1>Configuración</h1>
          <p class="header-sub">Ajustes de perfil, seguridad, preferencias y herramientas según tu rol.</p>
        </section>

        <section class="cards-grid">
          <div class="summary-card">
            <h3>Tarjeta 1 — Perfil y Seguridad</h3>
            <p class="card-tag">🔒 Gestión de credenciales</p>
            <p class="card-desc">Campos para actualizar contraseña y nombre de usuario. Incluye rol actual solo lectura.</p>
            <div class="card-icons">👤 ⚙️ 🔑</div>
          </div>
          <div class="summary-card">
            <h3>Tarjeta 2 — Preferencias Generales</h3>
            <p class="card-tag">🌐 Idioma, tema y controles</p>
            <p class="card-desc">Idioma/tema con dropdowns; notificaciones y privacidad con switches.</p>
            <div class="card-icons">👤 ⚙️ 🔑</div>
          </div>
          <div class="summary-card">
            <h3>Tarjeta 3 — Herramientas Específicas</h3>
            <p class="card-tag">📊 Soporte y analítica</p>
            <p class="card-desc">Preferencias de tickets y habilitación de gráficos/métricas según el rol.</p>
            <div class="card-icons">👤 ⚙️ 🔑</div>
          </div>
          <div class="summary-card">
            <h3>Tarjeta 4 — Administración Avanzada</h3>
            <p class="card-tag">⚠️ Requiere permiso de administrador</p>
            <p class="card-desc">Todos los controles deshabilitados con candado cerrado y apariencia atenuada.</p>
            <div class="card-icons">👤 ⚙️ 🔑</div>
          </div>
        </section>

        <section class="form-block">
          <h2>Perfil y Seguridad (Tarjeta 1)</h2>
          <p class="block-sub">Actualiza tu contraseña y configura tu nombre de usuario. El rol actual es solo lectura.</p>

          <form class="form-grid" @submit.prevent="guardar">
            <div class="form-group">
              <label>Contraseña actual</label>
              <input type="password" placeholder="Obligatorio">
            </div>
            <div class="form-group">
              <label>Nueva contraseña</label>
              <input type="password" placeholder="Mínimo 8 caracteres">
            </div>
            <div class="form-group">
              <label>Confirmar nueva contraseña</label>
              <input type="password" placeholder="Debe coincidir">
            </div>
            <div class="form-group">
              <label>Cambio de nombre de usuario</label>
              <input type="text" placeholder="Nuevo nombre de usuario">
            </div>
            <div class="form-group full-width">
              <label>Rol actual (Solo Vista)</label>
              <input type="text" value="Vista limitada" disabled class="disabled-view-input">
              <small>Ejemplo de dato bloqueado (Fondo gris)</small>
            </div>
            <div class="form-actions full-width">
              <button type="button" class="btn btn-outline">Cancelar</button>
              <button type="submit" class="btn btn-dark">Guardar cambios</button>
            </div>
          </form>
        </section>

        <section class="form-block">
          <h2>Preferencias Generales<br>(Tarjeta 2)</h2>
          <p class="block-sub">Controla idioma, tema, notificaciones y privacidad.</p>

          <form class="form-grid" @submit.prevent="guardar">
            <div class="form-group">
              <label>Idioma</label>
              <select>
                <option>Español / UX</option>
              </select>
              <small>Dropdown</small>
            </div>
            <div class="form-group">
              <label>Tema</label>
              <select>
                <option>Claro / Oscuro</option>
              </select>
              <small>Dropdown</small>
            </div>
            <div class="form-group">
              <label>Notificaciones</label>
              <input type="text" value="Email / Push / SMS" disabled class="disabled-view-input">
              <small>Toggle/switch</small>
            </div>
            <div class="form-group">
              <label>Privacidad</label>
              <input type="text" value="Todos, según rol" disabled class="disabled-view-input">
              <small>Toggle switch para nivel de acceso</small>
            </div>
            <div class="form-actions full-width">
              <button type="button" class="btn btn-outline">Cancelar</button>
              <button type="submit" class="btn btn-dark">Guardar cambios</button>
            </div>
          </form>
        </section>

        <section class="form-block">
          <h2>Herramientas Específicas<br>(Tarjeta 3)</h2>
          <p class="block-sub">Ajustes para soporte y analítica.</p>

          <form class="form-grid" @submit.prevent="guardar">
            <div class="form-group">
              <label>Preferencias de tickets (Soporte)</label>
              <input type="text" value="Activado / Desactivado" disabled class="disabled-view-input">
              <small>Toggle</small>
            </div>
            <div class="form-group">
              <label>Gráficos y métricas (Analítica)</label>
              <input type="text" value="Activado / Desactivado" disabled class="disabled-view-input">
              <small>Toggle</small>
            </div>
            <div class="form-actions full-width">
              <button type="button" class="btn btn-outline">Cancelar</button>
              <button type="submit" class="btn btn-dark">Guardar cambios</button>
            </div>
          </form>
        </section>

        <section class="form-block block-disabled">
          <h2>Administración Avanzada<br>(Tarjeta 4) — Deshabilitado</h2>
          <p class="block-sub">Accesos restringidos: requiere permisos de administrador.</p>

          <form class="form-grid" @submit.prevent>
            <div class="form-group">
              <label>Auditoría y seguridad avanzada (Administrador)</label>
              <input type="text" value="Solo admin" disabled>
              <small>Deshabilitado — Icono de candado cerrado (🔒)</small>
            </div>
            <div class="form-group">
              <label>Gestión de roles (Administrador)</label>
              <input type="text" value="Solo admin" disabled>
              <small>Deshabilitado — Icono de candado cerrado (🔒)</small>
            </div>
            <div class="form-actions full-width">
              <button type="button" class="btn btn-outline" disabled>Cancelar</button>
              <button type="submit" class="btn btn-dark" disabled>Guardar cambios</button>
            </div>
          </form>
        </section>

        <section class="toast-notification">
          <span class="toast-avatar">👤</span>
          <div class="toast-content">
            <h4>Usuario • Perfil</h4>
            <p class="toast-tag">Configuración</p>
            <p class="toast-desc">Notificación de guardado exitosa (Toast) en verde suave con check ✓.</p>
          </div>
        </section>
      </main>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import Sidebar from '../../components/layout/Sidebar.vue'

const router = useRouter()

const guardar = () => {
  router.push('/cambio-exitoso')
}
</script>