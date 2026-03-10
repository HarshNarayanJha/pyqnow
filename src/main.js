import "./assets/main.css"

import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"

import { VueUmamiPlugin } from "@jaseeey/vue-umami-plugin"
import { setBasePath } from "@shoelace-style/shoelace/dist/utilities/base-path"

setBasePath("https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.16.0/cdn/")

const UMAMI_WEBSITE_ID = import.meta.env.VITE_UMAMI_WEBSITE_ID
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

const app = createApp(App)

if (UMAMI_WEBSITE_ID !== "") {
  app.use(
    VueUmamiPlugin({
      websiteID: UMAMI_WEBSITE_ID,
      scriptSrc: `${API_BASE_URL}/stats/js`,
      router,
      allowLocalhost: false,
      extraDataAttributes: {
        "data-host-url": `${API_BASE_URL}/stats/events`,
        "data-do-not-track": true,
        "data-auto-track": true,
      },
    }),
  )
} else {
  console.log("UMAMI_WEBSITE_ID not set, skipping Umami plugin")
}

app.use(router)
app.mount("#app")
