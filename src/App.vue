<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->
    <nav>
      <RouterLink to="/">Paper Trail</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/about">BIT Questions Archive</RouterLink>
    </nav>
  </header>

  <main>
    <RouterView />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;

  nav {
    width: 100%;
    font-size: 16px;
    text-align: center;
    padding: 1em;
    margin-top: 0.5em;

    a {
      padding: 0.5em 1em;
      margin: 0.2em 0.5em;
      border-radius: 25px;
      background: var(--background-mute);
      color: var(--text);
    }

    a:first-of-type {
      font-weight: bolder;
      /* color: var(--text-inverse); */
      background: var(--c-accent);
    }
  }
}

main {
  margin-top: var(--sl-spacing-medium);
  display: flex;
  align-items: start;
  justify-content: center;

  flex: 1;
}

/* .logo {
  display: block;
  margin: 0 auto 2rem;
} */

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }

  /* .logo {
    margin: 0 2rem 0 0;
  } */
}
</style>
