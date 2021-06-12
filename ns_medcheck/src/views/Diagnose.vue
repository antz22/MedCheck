<template>
	<Page>

		<GridLayout rows="100,150,*" cols="auto">

			<Label text="Check Up" class="page-title" row="0" horizontAlignment="center" verticalAlignment="center" />

			<GridLayout rows="auto, auto" row="1">
				<StackLayout row="0" class="input-field">
					<TextField class="input" hint="Gender..." :isEnabled="!processing"
						autocorrect="false"
						autocapitalizationType="none" v-model="gender"
						returnKeyType="next"></TextField>
					<StackLayout class="hr-light"></StackLayout>
				</StackLayout>

				<StackLayout row="1" class="input-field">
					<TextField class="input" ref="password" :isEnabled="!processing"
						hint="Age..." v-model="age"></TextField>
					<StackLayout class="hr-light"></StackLayout>
				</StackLayout>

			</GridLayout>

			<GridLayout rows="50,*" row="2">
				<Label text="List Symptoms" class="page-subtitle" row="0"/>
				<!-- <Button text="Create Diagnosis" @tap="getDiagnosis" row="1"/> -->
				<!-- <Button @click="show2=!show2" text="add symptom" row="1" /> -->
				<Autocomplete row="1"/>
				<!-- <Autocomplete row="3" /> -->
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

			show2: false,
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