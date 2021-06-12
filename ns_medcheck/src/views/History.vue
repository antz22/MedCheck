<template>

  <GridLayout class="logs" :rows="rows">

    <Label class="list-title" text="Logs" row="0" horizontalAlignment="center"/>

    <GridLayout v-for="(diagnosis, index) in diagnoses" :key="diagnosis.id" 
      class="diagnosis" :class="getSeverity(diagnosis.severity)" rows="auto,auto,auto" cols="auto,auto" :row="index+1">

      <Label class="condition" :text="diagnosis.condition" horizontalAlignment="left" row="0"/>
      <Label class="severity" :text="diagnosis.severity" horizontalAlignment="left" row="1"/>
      <!-- <Label class="date" :text="diagnosis.date" horizontalAlignment="left" row="2"/> -->
      <Label class="fas more" text.decode="More &#xf054;" horizontalAlignment="right" row="2" @tap="goToMore(diagnosis)"/>

    </GridLayout>

  </GridLayout>

</template>

<script>
import axios from 'axios'
import DiagnosisView from '../components/DiagnosisView.vue'

export default {
  name: 'History',
	components: {
		DiagnosisView,
	},
  data() {
    return {
      diagnoses: [],
      errors: [],
      rowIndex: 0
    }
  },
  mounted() {
    this.getDiagnoses()
  },
  methods: {
    getDiagnoses() {
      axios
        .get('/api/v1/diagnoses/')
        .then(response => {
          this.diagnoses = response.data
					console.log(this.diagnoses)
        })
        .catch(error => {
          this.errors.push(error)
        })
    },
    getSeverity(priority) {
      if (priority === "3") {
        return 'b-high'
      } else if (priority === "2") {
        return 'b-medium'
      } else if (priority === "1") {
        return 'b-low'
      }
    },
		goToMore(diagnosis) {
			this.$navigateTo(DiagnosisView, {
        props: {
          diagnosis: diagnosis
        }
      })
		}
  },
  computed: {
    rows() {
      const rows = [];
      // additional one for label
      for (let i = 0; i <= this.diagnoses.length; i++) {
        rows.push("auto")
      }
      return rows.join(",")
    },
  },
}
</script>

<style scoped>
/* categories */
.list-title {
	color: black;
  margin-top: 60;
  margin-bottom: 60;
	text-align: center;
  font-size: 48px;
}

.diagnosis {
	margin-left: 50;
	margin-right: 50;
	background-color: #376BFC;
	color: white;
  margin-bottom: 20;
  border-radius: 5;
	padding: 10;
}

.condition {
  font-family: Montserrat, Montserrat SemiBold 600;
  font-size: 28px;
  /* margin-left: 10;
  margin-top: 10; */
}

.severity {
  font-weight: normal;
  font-size: 18px;
  margin-right: 10;
  margin-top: 10;
}

.more {
  font-weight: normal;
  font-size: 16px;
  margin-top: 5;
  margin-right: 10;
  margin-bottom: 10;
}

</style>
