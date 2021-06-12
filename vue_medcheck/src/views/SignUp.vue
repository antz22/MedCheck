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
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            Password
          </label>
          <input class="shadow appearance-none rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="Password" v-model="password">
        </div>
        <div class="mb-6">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            Repeat Password
          </label>
          <input class="shadow appearance-none rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="Repeat Password" v-model="password2">
        </div>
        <div class="flex items-center justify-between">
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Sign Up
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
        <p>Already have an account? <router-link to="/log-in">Log in here</router-link></p>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: 'SignUp',
  data() {
    return {
      username: '',
      password: '',
      password2: '',
      errors: []
    }
  },
  methods: {
    submitForm() {
      this.errors = []

      if (this.username === '') {
        this.errors.push('The username is missing.')
      }

      if (this.password === '') {
        this.errors.push('The password is too short.')
      }

      if (this.password !== this.password2) {
        this.errors.push('THe passwords don\'t match.') 
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password
        }

        axios
          .post("/api/v1/users/", formData)
          .then(response => {

            console.log(response)


            toast({
              message: 'Account created, please log in.',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              postition: 'bottom-right',
            })

            this.$router.push('/log-in')
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }

              console.log(JSON.stringify(error.response.data))

            } else if (error.message) {
              this.errors.push('Something went wrong. Please try again')

              console.log(JSON.stringify(error))
            }
          })
      }
    }
  }

}
</script>

<style>

/* for login page as well */

#signup {
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
