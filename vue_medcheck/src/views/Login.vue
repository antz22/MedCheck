<template>
  <div>
    <div class="text-container">
      <h1 class="header">APP NAME</h1>
      <div class="icon">
        <i class="fas fa-book"></i>
      </div>
    </div>
    <div class="w-full max-w-sm mx-auto">
      <form @submit.prevent="submitForm" class="bg-white shadow-md rounded px-12 pt-6 pb-8 mb-4">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
            Username
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Username" v-model="username">
        </div>
        <div class="mb-6">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            Password
          </label>
          <input class="shadow appearance-none rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="password" v-model="password">
        </div>
        <div class="flex items-center justify-between">
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Log In
          </button>
        </div>
      </form>
      <div v-if="errors.length">
        <div class="form-text">
          <p v-for="error in errors" :key="error">{{ error }}</p>
        </div>
      </div>
      <div class="form-text">
        <br>
        <p>Don't have an account yet? <router-link to="/sign-up">Sign up here!</router-link></p>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Log In | OneFocus'
  },
  methods: {
    async submitForm() {
      this.errors = []

      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")

      const formData = {
        username: this.username,
        password: this.password
      }

      await axios
        .post("/api/v1/token/login/", formData) 
        .then(response => {
          const token = response.data.auth_token

          this.$store.commit('setToken', token)

          axios.defaults.headers.common["Authorization"] = "Token " + token

          localStorage.setItem("token", token)

          const toPath = this.$route.query.to || '/home'

          this.$router.push(toPath)
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else {
            this.errors.push('Something went wrong. Please try again')

            console.log(JSON.stringify(error))
          }
        })
    }

  }
}


</script>

<style scoped>

#login {
  height: 100vh;
}

.text-container {
  margin-top: 2em;
  margin-bottom: 1em;
  font-weight: 600;
  font-size: 44px;
  text-align: center;
}

.header {
  display: inline-block;
}

.icon {
  display: inline-block;
  margin-left: 15px;
}

</style>
