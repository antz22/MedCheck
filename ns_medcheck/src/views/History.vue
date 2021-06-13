<template>
  <ScrollView>

    <GridLayout class="logs" :rows="rows">

      <Label class="list-title" text="Logs" row="0" horizontalAlignment="center"/>

      <GridLayout v-for="(diagnosis, index) in diagnoses" :key="diagnosis.id" 
        class="diagnosis" rows="auto,auto,auto" cols="auto,auto" :row="index+1">

        <Label class="condition" :text="diagnosis.condition" horizontalAlignment="left" row="0"/>
        <Label class="severity" :class="getSeverity(diagnosis.severity)" :text="getSeverityText(diagnosis.severity)" horizontalAlignment="left" row="1"/>
        <Label class="date" :text="diagnosis.time" horizontalAlignment="left" row="2"/>
        <Label class="more" horizontalAlignment="right" row="2" @tap="goToMore(diagnosis)" >
          <FormattedString>
            <Span text="More "/>
            <Span class="fas" text.decode="&#xf054;"/>
          </FormattedString>
        </Label>

      </GridLayout>

    </GridLayout>

  </ScrollView>


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
    getSeverity(severity) {
      if (severity === "3") {
        return 's-high'
      } else if (severity === "2") {
        return 's-medium'
      } else if (severity === "1") {
        return 's-low'
      }
    },
    getSeverityText(severity) {
			if (severity == "3") {
				return "High Urgency - Seek Help"
			} else if (severity == "2") {
				return "Medium Urgency - Take Care"
			} else if (severity == "1") {
				return "Low Urgency - Self Care"
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
	margin-left: 35;
	margin-right: 35;
	background-color: #376BFC;
	color: white;
  margin-bottom: 20;
  border-radius: 5;
	padding: 10;
}

.condition {
  font-family: Montserrat, Montserrat SemiBold 600;
  font-size: 28px;
}

.severity {
  font-weight: normal;
  font-size: 18px;
  margin-right: 10;
  margin-top: 10;
}

.date {
  font-weight: 200;
  font-size: 16px;
  margin-top: 15;
  margin-right: 10;
  margin-bottom: 10;
}

.more {
  font-weight: 200;
  font-size: 16px;
  margin-top: 15;
  margin-right: 10;
  margin-bottom: 10;
}

.s-high {
  color: #FF3939;
}

.s-medium {
  color: #FFE81E;
}

.s-low {
  color: #56FF06;
}

</style>
