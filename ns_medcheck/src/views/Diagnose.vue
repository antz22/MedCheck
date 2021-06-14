<template>
  <Page actionBarHidden="true">

    <GridLayout rows="100,150,*" cols="auto">

      <Label text="Check Up" class="page-title" row="0" horizontAlignment="center" verticalAlignment="center" />

      <GridLayout rows="auto, auto" row="1" marginLeft="20" marginRight="20">
        <StackLayout row="0" class="input-field">
          <TextField class="input" hint="Gender..." 
            autocorrect="false"
            autocapitalizationType="none" v-model="gender"
            returnKeyType="next"></TextField>
          <StackLayout class="hr-light"></StackLayout>
        </StackLayout>

        <StackLayout row="1" class="input-field">
          <TextField class="input" ref="password" 
            hint="Age..." v-model="age"></TextField>
          <StackLayout class="hr-light"></StackLayout>
        </StackLayout>

      </GridLayout>

      <GridLayout rows="50,*" row="2">
        <Label text="List Symptoms" class="page-subtitle" row="0"/>
        <Autocomplete row="1" marginLeft="20" marginRight="20"/>
      </GridLayout>

    </GridLayout>

  </Page>
</template>

<script>
import axios from 'axios'
import Autocomplete from '../components/Autcomplete.vue'

export default {
  name: 'Diagnose',
  components: {
    Autocomplete,
  },
  data() {
    return {
      gender: '',
      age: 0,
      symptoms: [],
      symptom1: {},

    }
  },
  methods: {

  }

}
</script>

<style scoped lang="scss">

.page-title {
  font-size: 35;
  margin-left: 20;
  color: black;
}

.page-subtitle {
  font-size: 30;
  margin-left: 20;
  color: black;
}

.form-input {
  border-color: lightgray;
  border-width: 0.5;
  padding: 5;
}

</style>