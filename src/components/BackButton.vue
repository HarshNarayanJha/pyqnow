<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()

import '@shoelace-style/shoelace/dist/components/tooltip/tooltip.js'
import '@shoelace-style/shoelace/dist/components/icon-button/icon-button.js'

onMounted(() => {
  document.getElementById('back').addEventListener('click', e => {
    router.go(-1)
  })
})
</script>

<template>
  <div class="back">
    <sl-tooltip content="Back">
      <sl-icon-button name="arrow-left" label="Settings" id="back"></sl-icon-button>
    </sl-tooltip>
  </div>
</template>

<style scoped>
.back {
  margin-top: 1.5em;
  font-size: var(--sl-font-size-2x-large);
}

@media (max-width: 600px) {
  .back {
    margin-top: 0.2rem;
  }
}
</style>
