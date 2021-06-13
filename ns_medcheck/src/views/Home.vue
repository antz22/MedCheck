<template>
	<GridLayout rows="600,*" cols="auto">
		<GridLayout class="hero" rows="100,120,100,50,80,80" cols="100,*" row="0" col="0">
			<Label text="Hello," row="0" col="0" horizontalAlignment="left" class="greeting" />
			<Label :text="name" row="1" col="0" class="greeting-name" />
			<GridLayout class="avatar-container" rows="*" row="1" col="1">
				<Image v-if="gender=='male'" src="~/assets/images/male-avatar.jpg" row="0" horizontalAlignment="right" class="avatar" />
				<Image v-else src="~/assets/images/female-avatar.jpg" row="0" horizontalAlignment="right" class="avatar" />
			</GridLayout>

			<FlexboxLayout justifyContent="space-around" alignItems="center" alignContent="center" backgroundColor="#7498FB" row="2">
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

			<GridLayout rows="52,50" cols="*" row="5">
				<Label text="Last Diagnosis" row="0" col="0" class="last-diagnosis" horizontalAlignment="center" verticalAlignment="center"/>
				<Label :text="lastdate" row="1" col="0" class="last-diagnosis-date" horizontalAlignment="center" verticalAlignment="top"/>
			</GridLayout>

		</GridLayout>

		<GridLayout class="diagnose" cols="80" rows="50,30" row="1" col="0" @tap="goToDiagnose" horizontalAlignment="center">
			<Label text="+" class="plus" row="0" col="0" horizontaAlignment="center"></Label>
			<Label text="Diagnose" class="plus-diagnose" row="1" col="0" verticalAlignment="center"></Label>
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
			lastdate: '',
			name: '',
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
					this.name = response.data.name
					this.lastdate = response.data.lastdate
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
	margin-bottom: 10;

	.greeting {
		font-weight: 300;
		margin-left: 40;
		margin-top: 45;
		font-size: 30;
	}

	.greeting-name {
		margin-top: -10;
		margin-left: 40;
		font-size: 48;
	}

	.avatar {
		width: 90;
		height: 90;
		border-radius: 50%;
		margin-right: 40;
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
	margin-left: -13;
}

.user-nums {
	margin-top: -8;
	font-size: 55;
	font-weight: 700;
	text-align: center;
}

.last-diagnosis {
	font-size: 21;
	margin-top: 20;
	margin-bottom: 5;
}

.last-diagnosis-date {
	font-size: 21;
	font-weight: 200;
	margin-bottom: 10;
}

.diagnose {
	background-color: #2D61EF;
	color: white;
	text-align: center;
	margin-top: 20;
	margin-bottom: 30;
	border-radius: 15;
	padding-top: 3;
	height: 90;
	width: 110;

	.plus {
		font-size: 36;
	}
}

.avatar-container {
	width: 100%;
	height: 100%;
	margin-top: -130;
}


</style>