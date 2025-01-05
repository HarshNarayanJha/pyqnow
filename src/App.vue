<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

import '@shoelace-style/shoelace/dist/components/spinner/spinner.js'
import '@shoelace-style/shoelace/dist/components/skeleton/skeleton.js'
</script>

<template>
  <header>
    <Header></Header>
  </header>

  <main>
    <Suspense>
      <template #default>
        <RouterView />
      </template>
      <template #fallback>
        <div class="loader">
          <sl-spinner style="font-size: 50px; --track-width: 10px"></sl-spinner>
          <div class="skeleton">
            <sl-skeleton effect="sheen"></sl-skeleton>
            <sl-skeleton effect="sheen"></sl-skeleton>
            <sl-skeleton effect="sheen"></sl-skeleton>
            <sl-skeleton effect="sheen"></sl-skeleton>
          </div>
        </div>
      </template>
    </Suspense>
  </main>

  <footer>
    <Footer></Footer>
  </footer>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

main {
  margin-top: var(--sl-spacing-medium);
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: center;

  flex: 1;

  .loader {
    width: 100%;
    max-width: 800px;
    margin: auto;

    .skeleton {
      display: flex;
      flex-direction: column;
      gap: 4em;
      margin-top: 8em;

      sl-skeleton {
        height: 2em;
      }
    }
  }
}

footer {
  height: 100px;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }
}
</style>
