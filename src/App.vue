<script setup>
import Footer from "@/components/Footer.vue"
import Header from "@/components/Header.vue"
import { RouterView } from "vue-router"

import "@shoelace-style/shoelace/dist/components/spinner/spinner.js"
import "@shoelace-style/shoelace/dist/components/skeleton/skeleton.js"
</script>

<template>
  <header>
    <Header></Header>
  </header>

  <main>
    <RouterView v-slot="{ Component }">
      <template v-if="Component">
        <Transition name="fade" mode="out-in">
          <KeepAlive>
            <Suspense timeout="1">
              <component :is="Component" :key="$route.path" />
              <template #fallback>
                <div class="loader">
                  <div class="spinner">
                    <sl-spinner style="font-size: 50px; --track-width: 8px"></sl-spinner>
                    <p v-if="$route.name === 'exam'">Loading PYQs Now...</p>
                    <p v-else-if="$route.name === 'syllabus'">Loading Syllabus Now...</p>
                    <p v-else>Loading Now...</p>
                  </div>
                  <div class="skeleton">
                    <sl-skeleton effect="sheen"></sl-skeleton>
                    <sl-skeleton effect="sheen"></sl-skeleton>
                    <sl-skeleton effect="sheen"></sl-skeleton>
                    <sl-skeleton effect="sheen"></sl-skeleton>
                  </div>
                </div>
              </template>
            </Suspense>
          </KeepAlive>
        </Transition>
      </template>
    </RouterView>
  </main>

  <Footer />
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

    .spinner {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      sl-spinner {
        margin-bottom: 0.5em;
      }

      p {
        font-size: 1.2em;
      }
    }

    .skeleton {
      display: flex;
      flex-direction: column;
      gap: 2em;
      margin-top: 8em;

      sl-skeleton {
        height: 1.4em;
      }
    }
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  filter: blur(0);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0.2;
  filter: blur(8px);
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }
}
</style>
