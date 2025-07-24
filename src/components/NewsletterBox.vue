<script setup>
import "@shoelace-style/shoelace/dist/components/input/input.js"
import "@shoelace-style/shoelace/dist/components/select/select.js"
import "@shoelace-style/shoelace/dist/components/option/option.js"
import "@shoelace-style/shoelace/dist/components/button/button.js"
import "@shoelace-style/shoelace/dist/components/card/card.js"
</script>

<template>
  <sl-card class="newsletter-card">
    <div class="newsletter-title">📰 Subscribe to the PYQNow Newsletter</div>

    <form
      action="https://buttondown.com/api/emails/embed-subscribe/pyqnow"
      method="post"
      target="popupwindow"
      onsubmit="window.open('https://buttondown.com/pyqnow', 'popupwindow')"
      class="newsletter-form"
    >
      <sl-input
        type="email"
        name="email"
        label="Email"
        id="bd-email"
        help-text="Your email so that we could send you updates about PYQNow. No spam, promise!"
        required
        placeholder="you@youremail.com"
      ></sl-input>

      <sl-select
        label="Year"
        help-text="Select one to receive year specific updates"
        clearable
        id="year"
        name="metadata__year"
      >
        <sl-option value="1">1st</sl-option>
        <sl-option value="2">2nd</sl-option>
        <sl-option value="3">3rd</sl-option>
        <sl-option value="4">4th</sl-option>
      </sl-select>

      <sl-select
        label="Where did you get to know about PYQNow?"
        help-text="Completely optional"
        clearable
        id="source"
        name="metadata__source"
      >
        <sl-option value="a_friend">A Friend</sl-option>
        <sl-option value="college_group">College Group</sl-option>
        <sl-option value="github">GitHub</sl-option>
        <sl-option value="developer_himself">Developer himself</sl-option>
        <sl-option value="other">Other</sl-option>
        <sl-option value="wont_tell">Won't Tell</sl-option>
      </sl-select>

      <sl-button type="submit" value="Subscribe" variant="primary" class="newsletter-submit-button">
        Subscribe
      </sl-button>
    </form>
    <p>
      <a href="https://buttondown.com/refer/pyqnow" target="_blank" class="newsletter-footer">
        Powered by Buttondown.
      </a>
    </p>
  </sl-card>
</template>

<style scoped>
.newsletter-card {
  margin-inline: auto;
  margin-block: var(--sl-spacing-3x-large);
  text-align: start;

  form {
    display: flex;
    flex-direction: column;
    gap: var(--sl-spacing-small);
  }

  .newsletter-title {
    font-weight: var(--sl-font-weight-bold);
    font-size: var(--sl-font-size-large);
    margin-bottom: var(--sl-spacing-small);
  }

  .newsletter-submit-button {
    margin-top: var(--sl-spacing-medium);
    width: 100%;
  }

  .newsletter-footer {
    font-size: var(--sl-font-size-small);
  }
}
</style>
