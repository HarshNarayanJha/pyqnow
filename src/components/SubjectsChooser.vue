<script setup>
import { Lit } from "litlyx-js"
import "@shoelace-style/shoelace/dist/components/details/details.js"
import "@shoelace-style/shoelace/dist/components/badge/badge.js"
import "@shoelace-style/shoelace/dist/components/button/button.js"
import "@shoelace-style/shoelace/dist/components/radio-button/radio-button.js"
import "@shoelace-style/shoelace/dist/components/radio-group/radio-group.js"
import "@shoelace-style/shoelace/dist/components/divider/divider.js"
import "@shoelace-style/shoelace/dist/components/copy-button/copy-button.js"
import { computed, onMounted, ref } from "vue"
import { RouterLink } from "vue-router"

import { useStorage } from "@vueuse/core"

const props = defineProps({
  year: {
    type: String,
    required: true,
  },
  sub: {
    type: String,
    required: false,
  },
  options: {
    type: Array,
    required: true,
  },
})

const branch = useStorage("branch", "cse")

onMounted(() => {
  const rg = document.querySelector("sl-radio-group")
  rg.addEventListener("sl-change", event => {
    branch.value = event.target.value
  })
  rg.value = branch.value
})

const branchOptions = computed(() => {
  return props.options.filter(p => p.branch?.includes(branch.value))
})

const branchChanged = p =>
  Lit.event("branch_changed", {
    metadata: {
      branch: p,
    },
  })

const syllabusClicked = p =>
  Lit.event("syllabus_clicked", {
    metadata: {
      subject: p,
    },
  })

const paperClicked = (p, y, t) =>
  Lit.event("paper_clicked", {
    metadata: {
      subject: p,
      year: y,
      paper: t,
    },
  })

onMounted(async () => {
  if (props.sub) {
    const sec = document.getElementById(props.sub)

    await new Promise(resolve => setTimeout(resolve, 200))
    sec.scrollIntoView({ behavior: "smooth" })
    await new Promise(resolve => setTimeout(resolve, 800))
    sec.show()

    Lit.event("subject_query", {
      metadata: {
        sub: props.sub,
      },
    })
  }
})
</script>

<template>
  <div class="options">
    <sl-radio-group>
      <sl-radio-button value="cse" pill :onclick="() => branchChanged('CSE')">CSE</sl-radio-button>
      <sl-radio-button value="ece" pill :onclick="() => branchChanged('ECE')">ECE</sl-radio-button>
      <sl-radio-button value="eee" pill :onclick="() => branchChanged('EEE')">EEE</sl-radio-button>
    </sl-radio-group>

    <sl-details
      v-for="sub in branchOptions"
      :summary="sub.code + ' - ' + sub.display"
      :id="sub.code"
    >
      <RouterLink :to="`/syllabus/${sub.code}`" :onclick="() => syllabusClicked(sub.code)">
        <sl-button pill>
          <sl-icon slot="prefix" name="file-earmark-text"></sl-icon>
          Syllabus
        </sl-button>
      </RouterLink>

      <sl-details v-if="sub.links">
        <div slot="summary">
          <sl-badge variant="primary" pill pulse>NEW</sl-badge> &nbsp; Some Useful websites for
          {{ sub.display }}
        </div>
        <ul>
          <li v-for="link in sub.links">
            {{ link.name }} - <a :href="link.url" target="_blank">{{ link.url }}</a>
          </li>
        </ul>
      </sl-details>

      <sl-details v-for="year in sub.papers" :summary="year.display">
        <div class="links">
          <sl-button
            v-for="(quiz1, i) in year.quiz1"
            :href="quiz1"
            target="_blank"
            variant="primary"
            :onclick="() => paperClicked(sub.code, year.display, `Quiz 1 - ${i}`)"
            v-if="year.quiz1"
          >
            <sl-icon slot="suffix" name="box-arrow-up-right"></sl-icon>
            {{ i + 1 }}. First Quiz
          </sl-button>

          <sl-button
            v-for="(mid, i) in year.mid"
            :href="mid"
            target="_blank"
            variant="warning"
            :onclick="() => paperClicked(sub.code, year.display, `Mid - ${i}`)"
            :disabled="!year.mid"
          >
            <sl-icon slot="suffix" name="box-arrow-up-right"></sl-icon>
            {{ i + 1 }}. Mid Semester
          </sl-button>

          <sl-button
            v-for="(quiz2, i) in year.quiz2"
            :href="quiz2"
            target="_blank"
            variant="success"
            :onclick="() => paperClicked(sub.code, year.display, `Quiz 2 - ${i}`)"
            v-if="year.quiz2"
          >
            <sl-icon slot="suffix" name="box-arrow-up-right"></sl-icon>
            {{ i + 1 }}. Second Quiz
          </sl-button>

          <sl-button
            v-for="(end, i) in year.end"
            :href="end"
            target="_blank"
            variant="danger"
            :onclick="() => paperClicked(sub.code, year.display, `End - ${i}`)"
            :disabled="!year.end"
          >
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
  padding: 1.2em;
  margin: 3em 2em;

  sl-radio-group {
    margin: 1em 0;
  }

  sl-details {
    margin: 1em 0;
    text-align: start;
    font-family: var(--font-body);
  }

  .links {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;

    sl-button {
      margin: 0.2em;
    }
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
    }
  }
}
</style>
