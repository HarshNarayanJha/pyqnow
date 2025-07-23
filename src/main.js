import "./assets/main.css"

import { setBasePath } from "@shoelace-style/shoelace/dist/utilities/base-path"
import { Lit } from "litlyx-js"
import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"

setBasePath("https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.16.0/cdn/")

const LIT_PROJECT_ID = import.meta.env.VITE_LIT_PROJECT_ID

if (LIT_PROJECT_ID !== "") {
  Lit.init(LIT_PROJECT_ID, { testMode: true })
}

const app = createApp(App)

app.use(router)

app.mount("#app")
