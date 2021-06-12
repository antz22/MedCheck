<template>
	<GridLayout rows="600,*" cols="auto">
		<GridLayout class="hero" rows="100,120,100,50,80,120" cols="100,*" row="0" col="0">
			<Label text="Hello," row="0" col="0" horizontalAlignment="left" class="greeting" />
			<Label text="Anthony" row="1" col="0" class="greeting-name" />
			<Image v-if="gender=='male'" src="~/assets/images/male-avatar.jpg" row="1" col="1" horizontalAlignment="right" class="avatar" />
			<Image v-else src="~/assets/images/female-avatar.jpg" row="1" col="1" horizontalAlignment="right" class="avatar" />

			<FlexboxLayout justifyContent="space-around" alignItems="center" alignContent="center" backgroundColor="#3c495e" row="2">
				<Label class="fas user-nums-icon" text.decode="&#xf481;"/>
				<Label class="fas user-nums-icon" text.decode="&#xf071;"/>
			</FlexboxLayout>
			<FlexboxLayout justifyContent="space-around" alignItems="center" alignContent="center" row="3">
				<Label text="Diagnoses" class="user-nums-type"/>
				<Label text="Critical" class="user-nums-type"/>
			</FlexboxLayout>
			<FlexboxLayout justifyContent="space-around" alignItems="center" alignContent="center" row="4">
				<Label :text="diagnoses" class="user-nums"/>
				<Label :text="critical" class="user-nums"/>
			</FlexboxLayout>

			<GridLayout rows="50,70" cols="*" row="5">
				<Label text="last diagnosis" row="0" col="0" class="last-diagnosis" horizontalAlignment="center" verticalAlignment="center"/>
				<Label text="foo" row="1" col="0" class="last-diagnosis-date" horizontalAlignment="center" verticalAlignment="center"/>
			</GridLayout>



		</GridLayout>
		<!-- <Label class="fas" text.decode="&#xf481;"/>
		<Label class="fas" text.decode="&#xf071;"/> -->

		<GridLayout class="diagnose" cols="80" rows="30,30" row="1" col="0" @click="goToDiagnose" horizontalAlignment="center">
			<Label text="+" class="plus" row="0" col="0" horizontaAlignment="center" verticalAlignment="center"></Label>
			<Label text="Diagnose" row="1" col="0" verticalAlignment="center"></Label>
		</GridLayout>

	</GridLayout>
</template>

<script>
import axios from 'axios'
import Diagnose from './Diagnose'

export default {
	name: 'Home',
	components: {
		Diagnose,
	},
	data() {
		return {
			diagnoses: 0,
			critical: 0,
			gender: '',
			age: 0,
		}
	},
	mounted() {
		this.getUserData()
	},
	methods: {
		getUserData() {
			axios
				.get('/api/v1/get-data/')
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
		goToDiagnose() {
			this.$navigateTo(Diagnose)
		}
	}

}
</script>

<style scoped lang="scss">
.hero {
	background-color: #2D61EF;
	color: white;

	.greeting {
		margin-left: 40;
		margin-top: 40;
		font-size: 36;
	}

	.greeting-name {
		margin-left: 40;
		font-size: 48;
	}

	.avatar {
		width: 93;
		// border-radius: 50%;
		border-radius: 50px;
		margin-right: 40;
		margin-top: -130;
		text-align: right;
	}

}

.user-nums-icon {
	font-size: 42;
}

.user-nums-type {
	font-size: 19;
	color: #D9D6D6;
	text-align: center;
}

.user-nums {
	font-size: 55;
	font-weight: 700;
	text-align: center;
}

.last-diagnosis {

}

.diagnose {
	background-color: #2D61EF;
	color: white;
	text-align: center;
	margin-top: 30;
	margin-bottom: 20;
	border-radius: 20;
	padding-top: 3;
	height: 70;
	width: 85;

	.plus {
		font-size: 42;
	}
}


</style>