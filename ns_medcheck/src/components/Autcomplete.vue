<template>

		<GridLayout class="autocomplete" rows="70,*,80">
			<TextField class="input" hint="Sore throat..."
				autocapitalizationType="none" v-model="search" :isEnabled="!processing"
				returnKeyType="next" row="0" @textChange="onChange" @blur="isOpen=!isOpen"></TextField>

			<StackLayout v-show="isOpen" id="autocomplete-results" class="autocomplete-results" row="1">
				<Label class="loading" v-if="isLoading" text="Loading results..."/>
				<ScrollView v-else>
					<StackLayout>
						<Label class="autocomplete-result" v-for="(result, i) in results" :key="i"
							@tap="setResult(result)" :class="{ 'is-active': i === arrowCounter }" :text="result.Name"/>
					</StackLayout>
				</ScrollView>
			</StackLayout>

			<Button text="Diagnose" @tap="getDiagnosis" class="btn-diagnosis" row="2" horizontalAlignment="center" verticalAlignment="center"/>

      <ActivityIndicator rowSpan="2" :busy="processing"></ActivityIndicator>

		</GridLayout>


</template>

<script>
import axios from 'axios'
import Home from '../views/Home.vue'

  export default {
    name: 'SearchAutocomplete',
    components: {
      Home
    },
    data() {
      return {
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

        processing: false,
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
    },
    methods: {
			getSymptoms() {
				const base = 'https://sandbox-healthservice.priaid.ch/symptoms'
				axios
					.get(base, {
						params: {
							token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFhZGl2MzAyM0BnbWFpbC5jb20iLCJyb2xlIjoiVXNlciIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjkyNTYiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ZlcnNpb24iOiIyMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xpbWl0IjoiOTk5OTk5OTk5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwIjoiUHJlbWl1bSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMjEtMDYtMTMiLCJpc3MiOiJodHRwczovL3NhbmRib3gtYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTYyMzU2MTIzMSwibmJmIjoxNjIzNTU0MDMxfQ.MOTLwmc35TNVkBHkRjfmrKKNcuF9WbcEtBKTWwlsZRs',
							language: 'en-gb',
							format: 'json'
						}
					})
					.then(response => {
						this.items = response.data
					})
			},
			getDiagnosis() {
        this.processing = true
				const base = 'https://sandbox-healthservice.priaid.ch/diagnosis'
				let symptomsArr = Object.values(this.symptoms).map((id) => {
					return id
				})
				console.log(`[${symptomsArr}]`)
				axios
					.get(base, {
						params: {
							token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFhZGl2MzAyM0BnbWFpbC5jb20iLCJyb2xlIjoiVXNlciIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjkyNTYiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ZlcnNpb24iOiIyMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xpbWl0IjoiOTk5OTk5OTk5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwIjoiUHJlbWl1bSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMjEtMDYtMTMiLCJpc3MiOiJodHRwczovL3NhbmRib3gtYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTYyMzU2MTIzMSwibmJmIjoxNjIzNTU0MDMxfQ.MOTLwmc35TNVkBHkRjfmrKKNcuF9WbcEtBKTWwlsZRs',
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
			},
			webScrape() {
				const django_base = '/api/v1/web-scrape/'
        console.log(this.diagnosis)
				axios
					.post(django_base, {
						condition: `${this.diagnosis.Name}`
					})
					.then(response => {
						this.summary = response.data.summary
						this.getLocation()
					})
					.catch(error => {
						console.log(error)
					})
			},
      getLocation() {
        const django_base = '/api/v1/get-location/'
        console.log(this.diagnosis)
        console.log(this.diagnosis.Rank)
        axios
          .post(django_base, {
            severity: `${this.diagnosis.Rank}`
          })
          .then(response => {
            this.location = response.data['items'][0]['address']['label']
            this.postDiagnosis()
          })
          .catch(error => {
            console.log(error)
          })
      },
			postDiagnosis() {
				const django_base = '/api/v1/create-diagnosis/'
				axios
					.post(django_base, {
						condition: `${this.diagnosis.Name}`,
						severity: `${this.diagnosis.Rank}`,
						summary: `${this.summary}`,
						location: `${this.location}`,
					})
          .then(response => {
            this.processing = false
            this.$navigateTo(Home)
            this.$navigateBack()
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
    border: 1px solid #b9b9b9;
    height: 120px;
    overflow: auto;
    font-size: 14;
  }
  .autocomplete-result {
    list-style: none;
    text-align: left;
    padding: 4px 2px;
    cursor: pointer;
  }
  .autocomplete-result.is-active,
  .autocomplete-result.focus {
    background-color: #4AAE9B;
    color: white;
  }

  .btn-diagnosis {
    width: 170;
    height: 50;
    border-radius: 11;
    color: white;
    background-color: #2D61EF;
    font-weight: 200;
    font-size: 20;
    margin-left: -20;
  }
</style>