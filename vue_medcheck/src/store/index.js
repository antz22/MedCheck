import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
  },
  mutations: {
    initializeStore(state) {
      // login, authenticated or not
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token') as string
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setToken(state, token) {
      // login
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) { 
      // logout
      state.token = ''
      state.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})
