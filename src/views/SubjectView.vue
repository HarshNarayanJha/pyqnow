<script setup>
import { ref, computed } from 'vue'

import '@shoelace-style/shoelace/dist/components/input/input.js'
import '@shoelace-style/shoelace/dist/components/alert/alert.js'
import '@shoelace-style/shoelace/dist/components/spinner/spinner.js'

import SubjectsChooser from '@/components/SubjectsChooser.vue'
import BackButton from '@/components/BackButton.vue'
import { useRoute } from 'vue-router'
import { fetchSubjects } from '@/services/api'

const route = useRoute()
const year = route.params.year
const filter = ref('')

const { data, error, isFetching } = await fetchSubjects(year)

const filteredSubjects = computed(() => {
  if (!data.value) return []

  return data.value.filter(
    e =>
      e.code.toLowerCase().includes(filter.value.toLowerCase()) ||
      e.display.toLowerCase().includes(filter.value.toLowerCase()) ||
      Object.keys(e.papers).includes(filter.value)
  )
})
</script>

<template>
  <div class="container">
    <BackButton></BackButton>

    <div v-if="isFetching">
      <sl-spinner style="font-size: 50px; --track-width: 10px"></sl-spinner>
    </div>

    <sl-alert variant="danger" open v-else-if="error">
      <sl-icon slot="icon" name="exclamation-octagon"></sl-icon>
      <strong>{{ error }}</strong>
    </sl-alert>

    <div v-else>
      <h2>Select Subject</h2>

      <sl-input
        v-model.trim="filter"
        label="Search"
        help-text="Filter By Subject or Year"
        placeholder="Start Typing...">
        <sl-icon name="search" slot="prefix"></sl-icon>
      </sl-input>
      <SubjectsChooser :options="filteredSubjects"></SubjectsChooser>
    </div>
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
    font-weight: var(--sl-font-weight-bold);
    font-size: var(--sl-font-size-3x-large);
  }
  sl-input {
    margin-top: 1.8em;
    text-align: start;
    font-family: var(--font-mono);

    sl-icon {
      margin: var(--sl-spacing-small);
      margin-right: 0;
    }
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
