<script setup>
import BackButton from '@/components/BackButton.vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const [code, name] = route.params.code.split('-')

const { data, error, isFetching } = await fetchSubjects(year)

</script>

<template>
  <div class="container">
    <BackButton />

    <h2>Syllabus for {{ code }} {{ name }}</h2>


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
}

@media (max-width: 600px) {
  .container {
    h2 {
      margin-top: 0.2em;
    }
  }
}
</style>
