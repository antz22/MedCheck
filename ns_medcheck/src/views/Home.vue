<template>
	<GridLayout rows="800,*" cols="auto">
		<GridLayout rows="200,300,300" cols="auto,auto" row="0" col="0">
			<Label text="Hello, Anthony" row="0" col="0" horizontalAlignment="left" class="greeting" />
			<Image src="~/assets/images/male-avatar.jpg" width="30" height="30" row="0" col="1" horizontAlignment="right" class="avatar" />

		</GridLayout>
		<!-- <Label class="fas" text.decode="&#xf481;"/>
		<Label class="fas" text.decode="&#xf071;"/> -->

		<GridLayout cols="30" rows="auto,auto" row="1" col="0" horizontalAlignment="center">
			<Label text="+" row="0" col="0"></Label>
			<Label text="Diagnose" row="1" col="0"></Label>
		</GridLayout>

	</GridLayout>
</template>

<script>
export default {

}
</script>

<style>

</style>