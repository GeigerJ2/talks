<template>
  <!-- Page number on every slide but the title. `$nav.total` counts only
       visible slides, so a slide carrying `hide: true` is excluded from
       both the number and the total. -->
  <footer v-if="$nav.currentPage > 1" class="page-number">
    {{ $nav.currentPage }} / {{ $nav.total }}
  </footer>
</template>

<style scoped>
/* Plain CSS rather than UnoCSS utilities: the utilities are generated from a
   source scan, and the export build drops them, leaving the footer in flow. */
.page-number {
  position: absolute;
  right: 1rem;
  bottom: 0.75rem;
  font-size: 0.75rem;
  line-height: 1rem;
  opacity: 0.4;
}
</style>
