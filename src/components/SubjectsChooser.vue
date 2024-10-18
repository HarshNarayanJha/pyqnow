<script setup>
import "@shoelace-style/shoelace/dist/components/details/details.js";
import "@shoelace-style/shoelace/dist/components/badge/badge.js";
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
      <sl-details v-if="sub.links">
        <div slot="summary">
          <sl-badge variant="primary" pill pulse>NEW</sl-badge> &nbsp; Some Useful websites for {{ sub.display }}
        </div>
        <ul>
          <li v-for="link in sub.links">
            {{ link.name }} - <a :href="link.url" target="_blank">{{ link.url }}</a>
          </li>
        </ul>
      </sl-details>
      <sl-details v-for="year in sub.papers" :summary="year.display">
        <div class="links">
          <sl-button v-for="(quiz1, i) in year.quiz1" :href="quiz1" target="_blank" variant="primary" v-if="year.quiz1">
            <sl-icon slot="suffix" name="box-arrow-up-right"></sl-icon>
            {{ i + 1 }}. First Quiz
          </sl-button>

          <sl-button v-for="(mid, i) in year.mid" :href="mid" target="_blank" variant="warning" :disabled="!year.mid">
            <sl-icon slot="suffix" name="box-arrow-up-right"></sl-icon>
            {{ i + 1 }}. Mid Semester
          </sl-button>

          <sl-button v-for="(quiz2, i) in year.quiz2" :href="quiz2" target="_blank" variant="success" v-if="year.quiz2">
            <sl-icon slot="suffix" name="box-arrow-up-right"></sl-icon>
            {{ i + 1 }}. Second Quiz
          </sl-button>

          <sl-button v-for="(end, i) in year.end" :href="end" target="_blank" variant="danger" :disabled="!year.end">
            <sl-icon slot="suffix" name="box-arrow-up-right"></sl-icon>
            {{ i + 1 }}. End Semester
          </sl-button>
        </div>
      </sl-details>
    </sl-details>
    <p v-if="options.length == 0">
      No Papers Added Yet!
      <br />
      I will add more papers whenever I get the time
      <br />
      If it's urgent to get the papers please contact me
    </p>
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

@media (max-width: 900px) {
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
