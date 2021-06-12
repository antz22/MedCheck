<template>
	<Page actionBarHidden="true">
		<GridLayout class="diagnosis-card" rows="50,40,60,*,100">
			<Label row="0" :text="condition" class="condition" marginLeft="20" marginTop="20"/>
			<Label row="1" text="Low Urgency - self care" class="severity" marginLeft="20" marginTop="20"/>
			<Label row="2" text="June 09, 2021" class="date" marginLeft="20" marginTop="20"/>
			<StackLayout row="3" class="condition-info">
				<Label text="Condition" class="condition-title" />
				<Label textWrap="true" :text="summary" />
			</StackLayout>
			<StackLayout row="4" class="condition-info">
				<Label text="Nearest Location" class="condition-title" />
				<Label :text="location" />
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
}

.condition-info {
	color: white;
	margin: 15;
	padding: 15;

	.condition-title {
		font-weight: 400;
		

	}


}

</style>