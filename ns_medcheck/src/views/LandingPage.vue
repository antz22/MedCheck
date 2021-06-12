<template>
  <Page actionBarHidden="true">
    <GridLayout rows="auto,auto,auto">
      <GridLayout class="app-logo" row="0" rows="auto" cols="auto,auto">

        <Label class="logo" row="0" horizontalAlignment="center">
          <FormattedString>
            <Span text.decode="&#xf00e;" class="fas icon"></Span>
            <Span text="Med" class="med"></Span>
            <Span text="Check" class="check"></Span>
          </FormattedString>
        </Label>

      </GridLayout>

      <GridLayout rows="auto" cols="auto" row="1">
        <Image src="~/assets/images/landing.jpg" width="450" class="landing" horizontalAlignment="center" row="0" col="0" />
      </GridLayout>

      <GridLayout rows="auto,auto" cols="auto" row="2">
        <Button text="LOGIN" horizontalAlignment="center" row="0"
          class="btn-landing-top" @tap="goToLogin"/>
        <Button text="SIGNUP" horizontalAlignment="center" row="1"
          class="btn-landing-bottom" @tap="goToSignup"/>
      </GridLayout>

      <!-- <GridLayout class="cover" row="0" rows="*">
        <Label class="fas icon" text.decode="&#xf02d;" verticalAlignment="center"
          horizontalAlignment="center"/>
        <Label text="APP NAME" class="app-name" verticalAlignment="center" 
          horizontalAlignment="center"/>
        <Label text="" height="30" />
      </GridLayout>
      <GridLayout row="1" cols="2" class="btns-container">
        <Button text="LOGIN" horizontalAlignment="left"
          class="btn-landing-left" @tap="goToLogin"/>
        <Button text="REGISTER" horizontalAlignment="right"
          class="btn-landing-right" @tap="goToSignup" />
      </GridLayout> -->
    </GridLayout>
  </Page>
</template>

<script>
import Login from './Login.vue'

export default {
  name: 'LandingPage',
  components: {
    Login, 
  },
  methods: {
    goToLogin() {
      this.$navigateTo(Login)
    },
    goToSignup() {
      this.$navigateTo(Login)
    }

  }

};
</script>

<style scoped>
.app-logo {
  margin-top: 70;
  color: black;
}

.logo {
  font-size: 48px;
  font-weight: 500;
  margin-bottom: -30;
}

.med {
  font-weight: normal;
}

.check {
  font-weight: bold;
}

.btn-landing-top {
  margin-bottom: 28;
  width: 170;
  height: 50;
  background-color: #2D61EF;
  border-radius: 10;
  color: white;
  font-size: 24;
  font-weight: 300;
}

.btn-landing-bottom {
  width: 170;
  height: 50;
  background-color: #2D61EF;
  border-radius: 10;
  color: white;
  font-size: 24;
  font-weight: 500;
}
</style>
