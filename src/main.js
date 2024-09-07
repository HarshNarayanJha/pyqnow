import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { setBasePath } from '@shoelace-style/shoelace/dist/utilities/base-path';

setBasePath('https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.16.0/cdn/');

const app = createApp(App)

app.use(router)

app.mount('#app')
