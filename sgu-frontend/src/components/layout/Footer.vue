<!-- ============================================================
     Archivo: src/components/layout/Footer.vue
     Descripción: Pie de página reutilizable.
     ============================================================ -->

<template>
  <footer class="footer">
    <slot>
      <p>© 2026 Sistema de Acceso &nbsp;&nbsp;&nbsp;
         <a href="#">Privacidad</a> &nbsp;&nbsp;&nbsp;
         <a href="#">Términos</a> &nbsp;&nbsp;&nbsp;
         <a href="#">Contacto</a>
      </p>
    </slot>
  </footer>
</template>

<script setup>
// No necesita lógica
</script>