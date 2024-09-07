<script setup>
import "@shoelace-style/shoelace/dist/components/details/details.js";
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
    <sl-details v-for="sub in options" :summary="sub.code + ' - ' + sub.display">
      <sl-details v-for="year in sub.papers" :summary="year.display">
        <div class="links">
          <sl-button :href="year.mid" target="_blank" variant="warning">
            <sl-icon slot="suffix" name="box-arrow-up-right"></sl-icon>
            Mid Semester
          </sl-button>

          <sl-button :href="year.end" target="_blank" variant="danger">
            <sl-icon slot="suffix" name="box-arrow-up-right"></sl-icon>
            End Semester
          </sl-button>
        </div>
      </sl-details>
    </sl-details>
  </div>
</template>

<style scoped>
.options {
  /* background: var(--sl-color-blue-200); */
  /* border-radius: var(--sl-border-radius-medium); */
  padding: 1.2em;
  margin: 3em 2em;

  sl-details {
    margin: 1em 0;
    text-align: start;
  }

  .links {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
  }
}

@media (max-width: 500px) {
  .options {
    margin: 1em 0.2em;
    padding: 0.2em;

    .links {
      display: flex;
      flex-direction: column;
      align-items: center;

      sl-button {
        margin: 0.2em;
      }
    }

  }
}
</style>
