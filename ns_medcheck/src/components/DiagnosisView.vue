<template>
  <Page actionBarHidden="true">
    <GridLayout class="diagnosis-card" rows="60,40,60,auto,auto">
      <Label row="0" :text="condition" class="condition" marginLeft="20" marginTop="20"/>
      <Label row="1" :text="severityText" :class="severityClass" marginLeft="20" marginTop="20"/>
      <Label row="2" :text="time" class="date" marginLeft="20" marginTop="20"/>
      <StackLayout row="3" class="condition-info">
        <Label text="Condition" class="condition-title" />
        <Label textWrap="true" :text="summary" class="condition-summary"/>
      </StackLayout>
      <StackLayout row="4" class="condition-info">
        <Label text="Nearest Location" class="condition-title" />
        <Label :text="location" textWrap="true" class="condition-summary" />
      </StackLayout>

    </GridLayout>

  </Page>
</template>

<script>

export default {
  name: 'DiagnosisView',
  props: {
    diagnosis: Object
  },
  data() {
    return {
      condition: this.diagnosis.condition,
      severity: this.diagnosis.severity,
      summary: this.diagnosis.summary,
      location: this.diagnosis.location,
      time: this.diagnosis.time,
    }
  },
  computed: {
    severityText() {
      if (this.severity == "3") {
        return "High Urgency - Seek Help"
      } else if (this.severity == "2") {
        return "Medium Urgency - Take Care"
      } else if (this.severity == "1") {
        return "Low Urgency - Self Care"
      }
    },
    severityClass() {
      if (this.severity == "3") {
        return "s-high"
      } else if (this.severity == "2") {
        return "s-medium"
      } else if (this.severity == "1") {
        return "s-low"
      }
    }
  }

}
</script>

<style scoped lang="scss">

.diagnosis-card {
  margin: 20;
  background-color: #376BFC;
  border-radius: 5;
}

.condition {
  color: white;
  font-size: 30;
  font-weight: 400;
}

.date {
  color: white;
  font-weight: 200;
}

.condition-info {
  color: white;
  margin: 15;
  padding: 15;
  background-color: #507FFE;
  border-radius: 5;

  .condition-title {
    font-weight: 400;
    font-size: 22;
    

  }

  .condition-summary {
    margin-top: 20;
    font-weight: 200;
  }


}

.location-ting {
  margin-top: 20;
  font-size: 18;
}

.severity {
  font-size: 18;
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