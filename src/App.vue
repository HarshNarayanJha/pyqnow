<script setup>
import { RouterLink, RouterView } from "vue-router";
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
</script>

<template>
  <header>
    <Header></Header>
  </header>

  <main>
    <RouterView />
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
  align-items: start;
  justify-content: center;

  flex: 1;
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
