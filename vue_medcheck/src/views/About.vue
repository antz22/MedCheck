<template>
  <div class="autocomplete">
    <p>{{ diagnoses }}</p>
    <p>{{ gender }}</p>
    <p>{{ age }}</p>
    <p>{{ critical }}</p>

  </div>
</template>

<script>
import axios from 'axios'

  export default {
    name: 'SearchAutocomplete',
    data() {
      return {
        diagnoses: 0,
        critical: 0,
        gender: '',
        age: 0,
      };
    },
    mounted() {
			this.getUserData()
    },
    methods: {
      getUserData() {
        const django_base = 'http://0.0.0.0:5000/api/v1/get-data/'
        axios
          .get(django_base)
          .then(response => {
            this.diagnoses = response.data.diagnoses
            this.critical = response.data.critical
            this.gender = response.data.gender
            this.age = response.data.age
          })
          .catch(err => {
            console.log(err)
          })

      },
    },
  };
</script>

<style>
  .autocomplete {
    position: relative;
  }

  .autocomplete-results {
    padding: 0;
    margin: 0;
    border: 1px solid #eeeeee;
    height: 120px;
    overflow: auto;
  }

  .autocomplete-result {
    list-style: none;
    text-align: left;
    padding: 4px 2px;
    cursor: pointer;
  }

  .autocomplete-result.is-active,
  .autocomplete-result:hover {
    background-color: #4AAE9B;
    color: white;
  }
</style>