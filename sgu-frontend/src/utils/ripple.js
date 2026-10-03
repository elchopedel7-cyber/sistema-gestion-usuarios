// ============================================================
// Archivo: src/utils/ripple.js
// Descripción: Efecto ripple (onda) al hacer clic en botones.
// Se activa en cualquier elemento con clase .btn, .btn-submit,
// .btn-dark, .btn-outline o .btn-foto.
// ============================================================

export function activarRipple() {
  // Se ejecuta una sola vez al iniciar la app
  document.addEventListener('click', (event) => {
    const boton = event.target.closest('.btn, .btn-submit, .btn-dark, .btn-outline, .btn-foto')
    if (!boton) return

    // Crear el círculo del ripple
    const ripple = document.createElement('span')
    ripple.classList.add('ripple')

    // Calcular tamaño y posición
    const rect = boton.getBoundingClientRect()
    const size = Math.max(rect.width, rect.height)
    const x = event.clientX - rect.left - size / 2
    const y = event.clientY - rect.top - size / 2

    ripple.style.width = `${size}px`
    ripple.style.height = `${size}px`
    ripple.style.left = `${x}px`
    ripple.style.top = `${y}px`

    boton.appendChild(ripple)

    // Quitar el ripple después de la animación
    setTimeout(() => {
      ripple.remove()
    }, 600)
  })
}