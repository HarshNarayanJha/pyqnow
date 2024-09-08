<script setup>
import { ref } from "vue";

import Chooser from "@/components/Chooser.vue";

const years = [
  {
    url: "/1",
    display: "1st Year",
    color: 'primary'
  },
  {
    url: "/2",
    display: "2nd Year",
    color: 'danger'
  },
  {
    url: "/3",
    display: "3rd Year",
    color: 'warning'
  },
  {
    url: "/4",
    display: "4th Year",
    color: 'success'
  },
];
</script>

<template>
  <div class="container">
    <!-- <h1>PYQNOW</h1> -->
    <img src="/pyqnow.png" alt="logo">
    <p>PYQs at your fingertips, success in sight</p>

    <Chooser :options="years"></Chooser>
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  text-align: center;
  max-width: 1000px;
  margin: 0 auto;

  h1 {
    font-weight: var(--sl-font-weight-bold);
    font-size: var(--sl-font-size-4x-large);
  }

  img {
    max-width: 100%;
    margin: 3em 0;
    margin-bottom: 0;
    background: linear-gradient(var(--background), var(--background-mute));
    border-radius: 30px;
  }

  p {
    color: var(--text-muted);
    font-size: 1.5rem;
  }

  @media (max-width: 500px) {
    h1 {
      font-size: var(--sl-font-size-3x-large);
    }
  }
}

sl-input {
  margin: var(--sl-spacing-large) 0;
}
</style>
