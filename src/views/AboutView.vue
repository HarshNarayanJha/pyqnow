<template>
  <div class="about">
    <h1>PYQNOW</h1>
    <p>PYQNow is a free website which provides one click access to all PYQs PDFs of BIT Exams.</p>
    <p>
      We were having a bad time finding all those PYQs on the
      <a href="https://bitmesra.ac.in">BIT website</a> and it wasted a lot of time, in which we are
      already much proficient that we don't need a bad website to help us in that.
    </p>
    <p>
      Many Subjects may also contain links to some useful websites that may aid in learning. I will
      keep updating the list
    </p>
    <p>
      So I made PYQNow, which (may) prevent us from following trails of question papers, and no more
      time wasting! (hopefully)
    </p>
    <p class="note">
      NOTE: Now we have papers for both CSE and ECE branches. Rest are in progress/depends on my
      mood.
    </p>
    <p class="note">
      PYQNow uses analytics powered by <a href="https://litlyx.com">litlyx.com</a> to improve user
      experience and continuously enhance the platform based on usage patterns. We do not and will
      never collect any user data whatsoever.
    </p>
  </div>
</template>

<style>
.about {
  width: 100%;
  text-align: center;
  max-width: 1000px;
  margin: 4em auto;

  h1 {
    font-weight: var(--sl-font-weight-bold);
    font-size: var(--sl-font-size-4x-large);
  }

  @media (max-width: 500px) {
    h1 {
      font-size: var(--sl-font-size-3x-large);
    }
  }

  p {
    font-size: var(--sl-font-size-large);
    margin: 1em 0;
  }

  p.note {
    color: var(--color-text-muted);
  }
}
</style>
