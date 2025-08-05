<script async setup>
import "@shoelace-style/shoelace/dist/components/card/card.js"
import "@shoelace-style/shoelace/dist/components/tooltip/tooltip.js"

import BackButton from "@/components/BackButton.vue"
import { fetchSyllabus } from "@/services/api"
import { useRoute } from "vue-router"

const route = useRoute()
const code = route.params.code

const { data, error, isFetching } = await fetchSyllabus(code)

const getYoutubeSearchUrl = (topic, display) => {
  if (!topic || !display) return "#"
  return `https://www.youtube.com/results?search_query=${encodeURIComponent(`${topic} in ${display}`)}`
}
</script>

<template>
  <div class="container">
    <BackButton />

    <div v-if="isFetching">
      <sl-spinner style="font-size: 50px; --track-width: 10px"></sl-spinner>
    </div>

    <sl-alert variant="danger" open v-else-if="error">
      <sl-icon slot="icon" name="exclamation-octagon"></sl-icon>
      <strong>{{ error }}</strong>
    </sl-alert>

    <div v-else class="syllabus-text">
      <h2>Syllabus for {{ data.code }} - {{ data.display }}</h2>

      <div v-for="(module, key) in data.modules">
        <h3>Module {{ key }}</h3>
        <div v-for="(mod, name) in module">
          <h4>{{ name }}</h4>

          <!-- the actual topics -->
          <p>
            <template v-for="(t, index) in mod.topics" :key="index">
              <sl-tooltip
                :content="`Search ${t} on YouTube`"
                v-if="mod.important_topics?.includes(index)"
              >
                <a
                  :href="getYoutubeSearchUrl(t, data.display)"
                  target="_blank"
                  rel="noopener"
                  class="topic-important"
                >
                  {{ t }},
                </a>
              </sl-tooltip>
              <span v-else>{{ t }},&nbsp;</span>
            </template>
          </p>
        </div>
        <sl-divider></sl-divider>
      </div>
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
    margin-bottom: 1em;
    font-weight: var(--sl-font-weight-bold);
    font-size: var(--sl-font-size-x-large);
  }

  h3 {
    margin-top: 1em;
    margin-bottom: 0.2em;
    color: var(--color-text);
    font-family: var(--font-mono);
    font-size: var(--sl-font-size-large);
  }

  h4 {
    margin-top: 1.2em;
    margin-bottom: 0.4em;
    color: var(--color-text);
    font-weight: var(--sl-font-weight-bold);
  }

  p {
    margin-top: 0.2em;
    margin-bottom: 1.5em;
    font-family: var(--font-mono);
    font-size: var(--sl-font-size-medium);
  }

  a.topic-important {
    color: var(--sl-color-sky-700);
    font-weight: var(--sl-font-weight-bold);
    text-decoration: dotted underline;
    text-decoration-thickness: 5%;
    text-underline-offset: 4px;
    text-decoration-color: var(--sl-color-gray-400);
    text-decoration-skip-ink: none;
    text-decoration-skip: none;
  }

  .syllabus-text {
    text-align: start;
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
