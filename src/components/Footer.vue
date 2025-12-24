<script setup>
import "@shoelace-style/shoelace/dist/components/icon/icon.js"
</script>

<template>
  <footer>
    <p>PYQNow is now useful for all branches (Currently CSE and ECE, WIP)</p>
    <p>
      &copy; 2025 <a href="https://github.com/HarshNarayanJha" target="_blank">Harsh Narayan Jha</a>
    </p>
    <p>
      <a href="https://github.com/dev-satyamjha" target="_blank">Satyam Jha</a> helped with subjects
      from other branches
    </p>
    <p class="end">
      <a href="https://github.com/HarshNarayanJha/pyqnow" target="_blank" class="star">
        Star PYQNow on GitHub &nbsp;
        <img
          src="https://img.shields.io/github/stars/HarshNarayanJha/pyqnow?style=social"
          alt="GitHub Repo stars"
        />
      </a>
    </p>
    <br />

    <div class="flex flex-row items-center gap-2">
      <!-- deployment went downhill for this one -->
      <!-- <img
      src="https://visit-counter.vercel.app/counter.png?page=https%3A%2F%2Fpyqnow.netlify.app%2F&s=32&c=006fff&bg=00000000&no=2&ff=electrolize&tb=Visits%3A+&ta="
      alt="visits"
    /> -->
      <a
        href="https://visitorbadge.io/status?path=https%3A%2F%2Fpyqnow.netlify.app"
        target="_blank"
      >
        <img
          src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fpyqnow.netlify.app&labelColor=%231a1a1a&countColor=%230066ff"
        />
      </a>
      <a
        href="https://visitorbadge.io/status?path=https%3A%2F%2Fpyqnow.netlify.app"
        target="_blank"
      >
        <img
          src="https://api.visitorbadge.io/api/daily?path=https%3A%2F%2Fpyqnow.netlify.app&label=VISITORS%20TODAY&labelColor=%231a1a1a&countColor=%230066ff"
        />
      </a>
    </div>
  </footer>
</template>

<style scoped>
footer {
  width: 100%;
  font-size: var(--sl-font-size-medium);
  text-align: center;
  margin-inline: auto;
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
  footer {
    padding: 0.6em;
    font-size: 15px;
  }
}
</style>
