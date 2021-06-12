import Vue from 'nativescript-vue'
import App from './views/App'
import LandingPage from './views/LandingPage'
import Login from './views/Login'
import Diagnose from './views/Diagnose'
import DiagnosisView from './components/DiagnosisView'
import axios from 'axios'
import VueDevtools from 'nativescript-vue-devtools'

if(TNS_ENV !== 'production') {
  Vue.use(VueDevtools)
}
import store from './store'

// Prints Vue logs when --env.production is *NOT* set while building
Vue.config.silent = (TNS_ENV === 'production')


const DEV_URL = 'http://10.0.2.2:5000'
axios.defaults.baseURL = DEV_URL


new Vue({
  store,
  render: h => h('frame', [h(Login)])
}).$start()
