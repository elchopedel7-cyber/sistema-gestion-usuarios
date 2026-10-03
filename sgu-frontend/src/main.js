// ============================================================
// Archivo: src/main.js
// Descripción: Punto de entrada de la aplicación Vue.
// ============================================================

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/styles/global.css'

// Activamos el efecto ripple
import { activarRipple } from './utils/ripple'
activarRipple()

const app = createApp(App)
app.use(router)
app.mount('#app')