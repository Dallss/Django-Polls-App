import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import sileo from 'sileo'

sileo.defaults.baseUrl = 'http://localhost:8000'
const app = createApp(App)

app.use(router)

app.mount('#app')
