<script setup>
import BackButton from '@/components/BackButton.vue'
import { fetchSyllabus } from '@/services/api'
import { useRoute } from 'vue-router'

const route = useRoute()
const code = route.params.code

const { data, error, isFetching } = await fetchSyllabus(code)
</script>

<template>
  <div class="container">

    <div v-if="isFetching">
      <sl-spinner style="font-size: 50px; --track-width: 10px"></sl-spinner>
    </div>

    <sl-alert variant="danger" open v-else-if="error">
      <sl-icon slot="icon" name="exclamation-octagon"></sl-icon>
      <strong>{{ error }}</strong>
    </sl-alert>

    <div v-else>
      <h2>Syllabus for {{ data.code }} {{ data.display }}</h2>

      <div v-for="(module, key) in data.modules">
        <div v-for="(mod, name) in module">
          <h3>{{ key }}. {{ name }}</h3>
          <p>{{ mod.topics.join(', ') }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;

  h2 {
    margin-top: 1em;
    margin-bottom: 1em;
    font-weight: var(--sl-font-weight-bold);
    font-size: var(--sl-font-size-2x-large);
  }

  h3 {
    margin-top: 1em;
    margin-bottom: 0.2em;
    color: var(--color-text);
    font-family: var(--font-mono);
    font-size: var(--sl-font-size-large);
  }

  p {
    margin-top: 0.2em;
    margin-bottom: 1.5em;
    font-family: var(--font-mono);
    font-size: var(--sl-font-size-medium);
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
