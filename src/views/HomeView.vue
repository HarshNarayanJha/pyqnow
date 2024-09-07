<script setup>
import { ref } from "vue";

import Chooser from "@/components/Chooser.vue";

const years = [
  {
    url: "/1",
    display: "1st Year",
  },
  {
    url: "/2",
    display: "2nd Year",
  },
  {
    url: "/3",
    display: "3rd Year",
  },
  {
    url: "/4",
    display: "4th Year",
  },
];
</script>

<template>
  <div class="container">
    <h1>Paper Trail</h1>

    <Chooser :options="years"></Chooser>
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  text-align: center;
  max-width: 1000px;
  margin: 0 auto;

  h1 {
    font-weight: var(--sl-font-weight-bold);
    font-size: var(--sl-font-size-4x-large);
  }
}

sl-input {
  margin: var(--sl-spacing-large) 0;
}
</style>
