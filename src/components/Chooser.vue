<script setup>
import "@shoelace-style/shoelace/dist/components/button/button.js"
import { Lit } from "litlyx-js"

const props = defineProps({
  options: {
    type: Array,
    required: true,
  },
})

const sendAnalytics = p =>
  Lit.event("year_button_click", {
    metadata: {
      year: p,
    },
  })
</script>

<template>
  <div class="options">
    <RouterLink v-for="opt in options" :to="opt.url" :onclick="() => sendAnalytics(opt.display)">
      <sl-button :variant="opt.color" size="large" class="option" outline>
        {{ opt.display }}
      </sl-button>
    </RouterLink>
  </div>
</template>

<style scoped>
.options {
  padding: 1.2em;
  margin: 3em 2em;
  margin-top: 0;
  padding-top: 0;

  a {
    margin: 0;
    padding: 0;
    text-decoration: none;
    color: unset;
  }

  .option {
    margin: 2em 2em;
    display: block;
  }

  @media (max-width: 768px) {
    .option {
      margin: 1em 0em;
    }
  }
}
</style>
