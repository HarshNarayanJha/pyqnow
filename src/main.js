import "./assets/main.css"

import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"

import { VueUmamiPlugin } from "@jaseeey/vue-umami-plugin"
import { setBasePath } from "@shoelace-style/shoelace/dist/utilities/base-path"

setBasePath("https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.16.0/cdn/")

const UMAMI_WEBSITE_ID = import.meta.env.VITE_UMAMI_WEBSITE_ID

const app = createApp(App)

if (UMAMI_WEBSITE_ID !== "") {
  app.use(
    VueUmamiPlugin({
      websiteID: UMAMI_WEBSITE_ID,
      scriptSrc: "https://cloud.umami.is/script.js",
      router,
      allowLocalhost: false,
      extraDataAttributes: {
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
