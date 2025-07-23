<script setup>
import "@shoelace-style/shoelace/dist/components/icon-button/icon-button.js"
import "@shoelace-style/shoelace/dist/components/tooltip/tooltip.js"
</script>

<template>
  <nav>
    <RouterLink to="/">PYQNow</RouterLink>
    <RouterLink to="/about">About</RouterLink>
    <a href="https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/361" target="_blank">
      BIT Questions Archive
    </a>
  </nav>
</template>

<style scoped>
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
    color: var(--c-white-soft);
    background: var(--c-primary);
  }

  sl-icon-button {
    vertical-align: middle;
  }

  sl-icon-button::part(base) {
    color: var(--text);
  }
}

@media (max-width: 500px) {
  nav {
    padding: 0.6em;
    font-size: 14px;

    a {
      padding: 0.4em 0.6em;
      margin: 0.2em 0.4em;
    }
  }
}

@media (max-width: 450px) {
  nav {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
}
</style>
