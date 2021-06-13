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
				this.items = [{'ID': 10, 'Name': 'Abdominal Pain'}]
				// const base = 'https://sandbox-healthservice.priaid.ch/symptoms'
				// axios
				// 	.get(base, {
				// 		params: {
				// 			token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNpZGR1LnBhYmJhQGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiOTI0NCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMS0wNi0xMCIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjIzNTIxNzUwLCJuYmYiOjE2MjM1MTQ1NTB9.V8T1ID5AFwSHaDWRMzZxO-zYeFXflFVaP--IW4Yh8IQ',
				// 			language: 'en-gb',
				// 			format: 'json'
				// 		}
				// 	})
				// 	.then(response => {
				// 		this.items = response.data
				// 		console.log(response.data)
				// 	})
			},
			getDiagnosis() {
				this.diagnosis = {'Name': 'Bloated belly'}
				// const base = 'https://sandbox-healthservice.priaid.ch/diagnosis'
				// let symptomsArr = Object.values(this.symptoms).map((id) => {
				// 	return id
				// })
				// console.log(`[${symptomsArr}]`)
				// axios
				// 	.get(base, {
				// 		params: {
				// 			token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNpZGR1LnBhYmJhQGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiOTI0NCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMS0wNi0xMCIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjIzNTIxNzUwLCJuYmYiOjE2MjM1MTQ1NTB9.V8T1ID5AFwSHaDWRMzZxO-zYeFXflFVaP--IW4Yh8IQ',
				// 			language: 'en-gb',
				// 			symptoms: `[${symptomsArr}]`,
				// 			gender: 'male',
				// 			year_of_birth: '1988',
				// 		}
				// 	})
				// 	.then(response => {
				// 		this.diagnosis = response.data
				// 		console.log(response.data[0])
				// 	})
				this.webScrape()
			},
			webScrape() {
				const django_base = 'http://0.0.0.0:5000/api/v1/web-scrape/'
				axios
					.post(django_base, {
						condition: `${this.diagnosis.Name}`
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
						severity: `${this.diagnosis.Rank}`
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
						// location: `${this.diagnosis.Name`,

    // condition = diagnosis_data['condition']
    // severity = diagnosis_data['severity']
    // summary = diagnosis_data['summary']
    // location = diagnosis_data['location']
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