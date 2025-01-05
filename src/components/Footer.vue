<script setup>
import '@shoelace-style/shoelace/dist/components/icon/icon.js'
</script>

<template>
  <nav>
    <p>Useful only for CSE branch students, for several reasons.</p>
    <p>
      &copy; 2025 <a href="https://github.com/HarshNarayanJha" target="_blank">Harsh Narayan Jha</a>
    </p>
    <p class="end">
      <a href="https://github.com/HarshNarayanJha/pyqnow" target="_blank" class="star">
        Star PYQNow on GitHub &nbsp;
        <img
          src="https://img.shields.io/github/stars/HarshNarayanJha/pyqnow?style=social"
          alt="GitHub Repo stars" />
      </a>
    </p>
    <br />
    <img
      src="https://visit-counter.vercel.app/counter.png?page=https%3A%2F%2Fpyqnow.netlify.app%2F&s=32&c=006fff&bg=00000000&no=2&ff=electrolize&tb=Visits%3A+&ta="
      alt="visits" />
  </nav>
</template>

<style scoped>
nav {
  width: 100%;
  font-size: 16px;
  text-align: center;
  padding: 2em;

  p {
    a {
      color: var(--c-primary-text);
    }

    a.star {
      color: unset;
      img {
        vertical-align: middle;
      }
    }

    a:hover {
      background: initial;
    }
  }

  p.end {
    margin-top: 1em;
  }
}

@media (max-width: 500px) {
  nav {
    padding: 0.6em;
    font-size: 15px;
  }
}
</style>
