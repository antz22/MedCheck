import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'
import store from './store'

const DEV_URL = 'http://0.0.0.0:5000'
axios.defaults.baseURL = DEV_URL

import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'
import './assets/index.css'

createApp(App).use(store).use(router, axios).mount('#app')
