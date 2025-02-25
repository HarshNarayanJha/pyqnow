<script setup>
import Chooser from '@/components/Chooser.vue'
import { pingServer } from '@/services/api'

pingServer()

const years = [
	{
		url: '/1',
		display: '1st Year',
		color: 'primary',
	},
	{
		url: '/2',
		display: '2nd Year',
		color: 'danger',
	},
	{
		url: '/3',
		display: '3rd Year',
		color: 'warning',
	},
	{
		url: '/4',
		display: '4th Year',
		color: 'success',
	},
]
</script>

<template>
  <div class="container">
    <img
      srcset="
        /pyqnow_small.png    512w,
        /pyqnow_half.png    1024w,
        /pyqnow_quarter.png 2048w,
        /pyqnow.png         4096w
      "
      sizes="(max-width: 640px) 100vw,
        (max-width: 960px) 80vw,
        90vw"
      priority="high"
      rel="preload"
      fetchpriority="high"
      as="image"
      alt="logo" />
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
    margin-bottom: 2em;
    background: linear-gradient(
      var(--color-border-hover) 0%,
      var(--color-background) 55%,
      var(--color-surface) 100%
    );
    box-shadow: 0px 5px 10px 0px var(--color-surface);
    border-radius: 30px;
  }

  p {
    color: var(--color-text-muted);
    font-size: 1.5rem;
    font-weight: 500;
  }

  @media (max-width: 500px) {
    h1 {
      font-size: var(--sl-font-size-3x-large);
    }

    img {
      margin: 1em 0;
    }

    p {
      color: var(--color-text-muted);
      font-size: 1.2rem;
    }
  }
}

sl-input {
  margin: var(--sl-spacing-large) 0;
}
</style>
