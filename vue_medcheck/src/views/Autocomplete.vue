<template>
  <div class="autocomplete">
    <input
      type="text"
      @input="onChange"
      v-model="search"
      @keydown.down="onArrowDown"
      @keydown.up="onArrowUp"
      @keydown.enter="onEnter"
    />
    <ul
      id="autocomplete-results"
      v-show="isOpen"
      class="autocomplete-results"
    >
      <li
        class="loading"
        v-if="isLoading"
      >
        Loading results...
      </li>
      <li
        v-else
        v-for="(result, i) in results"
        :key="i"
        @click="setResult(result)"
        class="autocomplete-result"
        :class="{ 'is-active': i === arrowCounter }"
      >
        {{ result.Name }}
      </li>
    </ul>
    <button @click="getDiagnosis"/>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    name: 'SearchAutocomplete',
    data() {
      return {
        // array of objects...
        items: [],
        symptoms: [],
        isOpen: false,
        results: [],
        search: '',
        isLoading: false,
        arrowCounter: -1,

        diagnosis: [],
        summary: '',
        location: '',
      };
    },
    watch: {
      items: function (value, oldValue) {
        if (value.length !== oldValue.length) {
          this.results = value;
          this.isLoading = false;
        }
      },
    },
    mounted() {
      this.getSymptoms()
      document.addEventListener('click', this.handleClickOutside)
    },
    unmounted() {
      document.removeEventListener('click', this.handleClickOutside)
    },
    methods: {
      // commented out
      getSymptoms() {
        const base = 'https://sandbox-healthservice.priaid.ch/symptoms'
        axios
          .get(base, {
            params: {
              token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imxpc3Rlci5iYXJ1bmdAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiI5MjM0IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMjAwIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6Ijk5OTk5OTk5OSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IlByZW1pdW0iLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xhbmd1YWdlIjoiZW4tZ2IiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIyMDk5LTEyLTMxIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwc3RhcnQiOiIyMDIxLTA2LTA5IiwiaXNzIjoiaHR0cHM6Ly9zYW5kYm94LWF1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE2MjM2MTQzNjUsIm5iZiI6MTYyMzYwNzE2NX0.AtU7gDIRpAxdtmd9re6IsvOq8mytlykaRPds1o_PZvo',
              language: 'en-gb',
              format: 'json'
            }
          })
          .then(response => {
            this.items = response.data
            console.log(response.data)
          })
      },
      getDiagnosis() {
        const base = 'https://sandbox-healthservice.priaid.ch/diagnosis'
        let symptomsArr = Object.values(this.symptoms).map((id) => {
          return id
        })
        console.log(`[${symptomsArr}]`)
        axios
          .get(base, {
            params: {
              token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imxpc3Rlci5iYXJ1bmdAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiI5MjM0IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMjAwIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6Ijk5OTk5OTk5OSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IlByZW1pdW0iLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xhbmd1YWdlIjoiZW4tZ2IiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIyMDk5LTEyLTMxIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwc3RhcnQiOiIyMDIxLTA2LTA5IiwiaXNzIjoiaHR0cHM6Ly9zYW5kYm94LWF1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE2MjM2MTQzNjUsIm5iZiI6MTYyMzYwNzE2NX0.AtU7gDIRpAxdtmd9re6IsvOq8mytlykaRPds1o_PZvo',
              language: 'en-gb',
              symptoms: `[${symptomsArr}]`,
              gender: 'male',
              year_of_birth: '1988',
            }
          })
          .then(response => {
            this.diagnosis = response.data[0]['Issue']
            this.webScrape()
          })
          .catch(err => {
            console.log(err)
          })
      },
      webScrape() {
        const django_base = 'http://0.0.0.0:5000/api/v1/web-scrape/'
        console.log('Diagnosis', this.diagnosis)
        console.log('Diagnosis name', this.diagnosis['Name'])
        axios
          .post(django_base, {
            condition: `${this.diagnosis['Name']}`
          })
          .then(response => {
            console.log(response.data)
            this.summary = response.data.summary
            this.getLocation()
          })
          .catch(error => {
            console.log(error)
          })

      },
      getLocation() {
        const django_base = 'http://0.0.0.0:5000/api/v1/get-location/'
        axios
          .post(django_base, {
            severity: `${this.diagnosis.Ranking}`
          })
          .then(response => {
            console.log(response.data)
            this.location = response.data['items'][0]['address']['label']
            this.postDiagnosis()
          })
          .catch(error => {
            console.log(error)
          })
      },
      postDiagnosis() {
        const django_base = 'http://0.0.0.0:5000/api/v1/create-diagnosis/'
        axios
          .post(django_base, {
            condition: `${this.diagnosis.Name}`,
            severity: `${this.diagnosis.Rank}`,
            summary: `${this.summary}`,
            location: `${this.location}`,
          })

      },
      setResult(result) {
        this.search = result.Name;
        this.isOpen = false;
        this.symptoms.push(result.ID)
      },
      filterResults() {
        this.results = this.items.filter((item) => {
          return item.Name.toLowerCase().indexOf(this.search.toLowerCase()) > -1;
        });
      },
      onChange() {
        this.$emit('input', this.search);

        if (this.isAsync) {
          this.isLoading = true;
        } else {
          this.filterResults();
          this.isOpen = true;
        }
      },
      handleClickOutside(event) {
        if (!this.$el.contains(event.target)) {
          this.isOpen = false;
          this.arrowCounter = -1;
        }
      },
      onArrowDown() {
        if (this.arrowCounter < this.results.length) {
          this.arrowCounter = this.arrowCounter + 1;
        }
      },
      onArrowUp() {
        if (this.arrowCounter > 0) {
          this.arrowCounter = this.arrowCounter - 1;
        }
      },
      onEnter() {
        this.search = this.results[this.arrowCounter];
        this.isOpen = false;
        this.arrowCounter = -1;
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