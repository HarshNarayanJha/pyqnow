<script setup>
import { Lit } from "litlyx-js"
import "@shoelace-style/shoelace/dist/components/icon/icon.js"
import "@shoelace-style/shoelace/dist/components/badge/badge.js"
import "@shoelace-style/shoelace/dist/components/tooltip/tooltip.js"

const props = defineProps({
  bookmarks: {
    type: Array,
    required: true,
  },
})

const sendAnalytics = (c, y, t) =>
  Lit.event("bookmark_clicked", {
    metadata: {
      code: c,
      year: y,
      type: t,
    },
  })
</script>

<template>
  <div class="bookmarks">
    <div v-if="bookmarks && bookmarks.length > 0">
      <div class="section">
        <!-- <h3>PYQ Bookmarks</h3> -->
        <sl-badge variant="success" pill v-for="mark in bookmarks">
          <sl-icon name="file-earmark-pdf-fill"></sl-icon>
          <sl-tooltip :content="`Open PYQs for ${mark.code}`">
            <RouterLink
              :to="`/${mark.year}?sub=${mark.code}`"
              :onclick="() => sendAnalytics(mark.code, mark.year, 'pyq')"
            >
              {{ mark.display }}
            </RouterLink>
          </sl-tooltip>
        </sl-badge>
      </div>
      <div class="section">
        <!-- <h3>Syllabus Bookmarks</h3> -->
        <sl-badge variant="warning" pill v-for="mark in bookmarks">
          <sl-icon name="file-earmark-text-fill"></sl-icon>
          <sl-tooltip :content="`Open Syllabus for ${mark.code}`">
            <RouterLink
              :to="`/syllabus/${mark.code}`"
              :onclick="() => sendAnalytics(mark.code, mark.year, 'syllabus')"
            >
              {{ mark.display }}
            </RouterLink>
          </sl-tooltip>
        </sl-badge>
      </div>
    </div>
    <div v-else>
      <p class="no-bookmark-message">
        <sl-icon name="bookmark"></sl-icon>
        No Bookmarks yet! Go add some bookmarks for your subjects to access them quickly.
      </p>
    </div>
  </div>
</template>

<style scoped>
.bookmarks {
  margin-block: 2em;
  margin-inline: auto;
  width: 80%;
  text-align: center;

  div.section {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 0.4em;
    margin-block: 1.5em;

    sl-badge {
      font-size: var(--sl-font-size-x-large);
    }

    a {
      color: unset;
      font-size: var(--sl-font-size-medium);
    }
  }

  .no-bookmark-message {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5em;
  }
}

@media (max-width: 500px) {
  .bookmarks {
    width: 100%;
  }
}
</style>
