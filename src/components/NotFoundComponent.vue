<script setup>
import BackButton from '@/components/BackButton.vue'
</script>

<template>
  <div class="container">
    <BackButton></BackButton>

    <h2>Page Not Found</h2>
    <p>Sorry, the page you are looking for does not exist.</p>
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  text-align: center;
  max-width: 1000px;
  margin: 0 auto;

  h2 {
    margin-top: 1em;
    line-height: 1.5em;
    font-weight: var(--sl-font-weight-bold);
    font-size: var(--sl-font-size-3x-large);
  }
}

@media (max-width: 600px) {
  .container {
    h2 {
      margin-top: 0.2em;
    }
  }
}
</style>
