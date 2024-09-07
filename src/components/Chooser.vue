<script setup>
import "@shoelace-style/shoelace/dist/components/button/button.js";

const props = defineProps({
  options: {
    type: Array,
    required: true,
  },
});
</script>

<template>
  <div class="options">
    <RouterLink v-for="opt in options" :to="opt.url">
      <sl-button variant="primary" size="large" class="option" outline>
        <!-- <sl-icon slot="prefix" name="1-square"></sl-icon> -->
        {{ opt.display }}
      </sl-button>
    </RouterLink>
  </div>
</template>

<style scoped>
.options {
  /* background: var(--sl-color-blue-200); */
  /* border-radius: var(--sl-border-radius-medium); */
  padding: 1.2em;
  margin: 3em 2em;

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
}
</style>
