<script setup>
import { ref } from "vue";

import "@shoelace-style/shoelace/dist/components/input/input.js";

import SubjectsChooser from "@/components/SubjectsChooser.vue";
import BackButton from "@/components/BackButton.vue";
import { useRoute } from "vue-router";

const route = useRoute();

const year = route.params.year;

import subjects from "@/data/subjects.json";
import { computed } from "vue";
const mySubjects = subjects[year];

const filter = ref("");

const filteredSubjects = computed(() => {
  return mySubjects.filter(
    (e) =>
      e.code.toLowerCase().includes(filter.value.toLowerCase()) ||
      e.display.toLowerCase().includes(filter.value.toLowerCase()) ||
      Object.keys(e.papers).includes(filter.value)
  );
});
</script>

<template>
  <div class="container">
    <BackButton></BackButton>

    <h2>Select Subject</h2>

    <sl-input v-model.trim="filter" label="Search" help-text="Filter By Subject or Year" placeholder="Start Typing...">
      <sl-icon name="search" slot="prefix"></sl-icon>
    </sl-input>
    <SubjectsChooser :options="filteredSubjects"></SubjectsChooser>
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

    sl-icon {
      margin: var(--sl-spacing-small);
      margin-right: 0;
    }
  }
}
</style>
