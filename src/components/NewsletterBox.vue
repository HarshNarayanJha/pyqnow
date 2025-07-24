<script setup>
import "@shoelace-style/shoelace/dist/components/input/input.js"
import "@shoelace-style/shoelace/dist/components/select/select.js"
import "@shoelace-style/shoelace/dist/components/option/option.js"
import "@shoelace-style/shoelace/dist/components/button/button.js"
import "@shoelace-style/shoelace/dist/components/card/card.js"
import "@shoelace-style/shoelace/dist/components/icon/icon.js"
</script>

<template>
  <sl-card class="newsletter-card">
    <div class="newsletter-header">
      <div class="newsletter-title">
        <sl-icon name="newspaper" class="newsletter-icon"></sl-icon>
        Subscribe to the PYQNow Newsletter
      </div>
      <div class="newsletter-subtitle">Stay updated with the latest PYQ resources and updates</div>
    </div>

    <form
      action="https://buttondown.com/api/emails/embed-subscribe/pyqnow"
      method="post"
      target="popupwindow"
      onsubmit="window.open('https://buttondown.com/pyqnow', 'popupwindow')"
      class="newsletter-form"
    >
      <div class="form-group">
        <sl-input
          type="email"
          name="email"
          label="Email Address"
          id="bd-email"
          help-text="Your email so that we could send you updates about PYQNow. No spam, promise!"
          required
          placeholder="you@youremail.com"
        ></sl-input>
      </div>

      <div class="form-row">
        <div class="form-group">
          <sl-select
            label="Academic Year"
            help-text="Select your year for personalized updates"
            clearable
            id="year"
            name="metadata__year"
          >
            <sl-option value="1">1st Year</sl-option>
            <sl-option value="2">2nd Year</sl-option>
            <sl-option value="3">3rd Year</sl-option>
            <sl-option value="4">4th Year</sl-option>
          </sl-select>
        </div>

        <div class="form-group">
          <sl-select
            label="How did you find us?"
            help-text="Help us understand our reach (optional)"
            clearable
            id="source"
            name="metadata__source"
          >
            <sl-option value="a_friend">👥 A Friend</sl-option>
            <sl-option value="college_group">🏫 College Group</sl-option>
            <sl-option value="github">💻 GitHub</sl-option>
            <sl-option value="developer_himself">👨‍💻 Developer</sl-option>
            <sl-option value="other">🌐 Other</sl-option>
            <sl-option value="wont_tell">🤐 Prefer not to say</sl-option>
          </sl-select>
        </div>
      </div>

      <sl-button type="submit" variant="primary" size="large" class="newsletter-submit-button">
        <sl-icon slot="prefix" name="envelope"></sl-icon>
        Subscribe Now
      </sl-button>
    </form>

    <div class="newsletter-footer">
      <p class="footer-text">
        <a href="https://buttondown.com/refer/pyqnow" target="_blank" class="footer-link">
          Powered by Buttondown
        </a>
      </p>
    </div>
  </sl-card>
</template>

<style scoped>
.newsletter-card {
  max-width: 600px;
  margin-inline: auto;
  margin-block: var(--sl-spacing-3x-large);
  text-align: start;
  border-radius: var(--sl-border-radius-large);
  box-shadow: var(--sl-shadow-large);
  background: linear-gradient(
    135deg,
    var(--sl-color-primary-50) 0%,
    var(--sl-color-neutral-0) 100%
  );
  border: 1px solid var(--sl-color-primary-100);
}

.newsletter-header {
  margin-bottom: var(--sl-spacing-large);
  text-align: center;
}

.newsletter-title {
  font-weight: var(--sl-font-weight-bold);
  font-size: var(--sl-font-size-x-large);
  margin-bottom: var(--sl-spacing-x-small);
  color: var(--sl-color-primary-700);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--sl-spacing-small);
}

.newsletter-icon {
  font-size: var(--sl-font-size-x-large);
  color: var(--sl-color-primary-600);
}

.newsletter-subtitle {
  font-size: var(--sl-font-size-medium);
  color: var(--sl-color-neutral-600);
  font-weight: var(--sl-font-weight-normal);
}

.newsletter-form {
  display: flex;
  flex-direction: column;
  gap: var(--sl-spacing-medium);
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--sl-spacing-medium);
}

@media (max-width: 768px) {
  .form-row {
    grid-template-columns: 1fr;
  }
}

.form-group {
  display: flex;
  flex-direction: column;
}

.newsletter-submit-button {
  margin-top: var(--sl-spacing-medium);
  width: 100%;
  font-weight: var(--sl-font-weight-semibold);
  background: linear-gradient(135deg, var(--sl-color-primary-600), var(--sl-color-primary-700));
  border: none;
  transition: all 0.2s ease;
}

.newsletter-submit-button:hover {
  transform: translateY(-2px);
  box-shadow: var(--sl-shadow-medium);
}

.newsletter-footer {
  margin-top: var(--sl-spacing-large);
  text-align: center;
  padding-top: var(--sl-spacing-medium);
  border-top: 1px solid var(--sl-color-neutral-200);
}

.footer-text {
  margin: 0;
}

.footer-link {
  font-size: var(--sl-font-size-small);
  color: var(--sl-color-neutral-500);
  text-decoration: none;
  transition: color 0.2s ease;
}

.footer-link:hover {
  color: var(--sl-color-primary-600);
}
</style>
