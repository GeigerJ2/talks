<template>
  <!-- AiiDA and Renku marks on every slide but the title, which carries them full size. -->
  <div v-if="$nav.currentPage > 1" class="slide-logos">
    <img src="/logos/aiida/logo_AiiDA.png" alt="AiiDA" />
    <img src="/logos/renku/logo_renku.svg" alt="Renku" class="renku" />
  </div>
</template>

<style scoped>
/* Plain CSS rather than UnoCSS utilities: the utilities are generated from a
   source scan, and the export build drops them. */
.slide-logos {
  position: absolute;
  top: 2.9rem;
  right: 1.4rem;
  display: flex;
  align-items: center;
  gap: 0.9rem;
  opacity: 0.75;
  z-index: 10;
}

.slide-logos img {
  height: 20px;
}

/* The Renku mark is a wide wordmark, so it is sized by width to stay legible
   beside the AiiDA logo. */
.slide-logos img.renku {
  height: auto;
  width: 72px;
}
</style>
