<script setup>
import { ref } from "vue";

import "@shoelace-style/shoelace/dist/components/input/input.js";

import SubjectsChooser from "@/components/SubjectsChooser.vue";
import BackButton from "@/components/BackButton.vue";
import { useRoute } from "vue-router";

const route = useRoute();

const year = route.params.year;

import subjects from "@/data/subjects.json";
const mySubjects = subjects[year];

const filter = ref("");
</script>

<template>
  <div class="container">
    <BackButton></BackButton>

    <h2>Select Subject</h2>

    <sl-input v-model.trim="filter" label="Search" help-text="Filter By Subject or Year" clearable>
      <sl-icon name="search" slot="prefix"></sl-icon>
    </sl-input>
    <SubjectsChooser :options="mySubjects"></SubjectsChooser>
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
    font-size: var(--sl-font-size-x-large);
  }
  sl-input {
    text-align: start;

    sl-icon {
      margin: var(--sl-spacing-small);
    }
  }
}
</style>
