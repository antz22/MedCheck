<template>
  <Page actionBarHidden="true">

    <TabView android:tabBackgroundColor="#3351A6"
              android:tabTextColor="#AFAFAF"
              android:selectedTabTextColor="#ffffff"
              androidSelectedTabHighlightColor="#ffffff"
              androidTabsPosition="bottom"
              selectedIndex="0">

      <TabViewItem title="Home">
        <GridLayout columns="*" rows="*">
          <Home/>
        </GridLayout>
      </TabViewItem>

      <TabViewItem title="History">
        <GridLayout columns="*" rows="*">
          <History/>
        </GridLayout>
      </TabViewItem>



    </TabView>

  </Page>
</template>

<script>
import Home from "./Home.vue";
import History from "./History.vue";

export default {
  components: {
    Home,
    History,
  }
};

</script>

<style scoped>
ActionBar {
  background-color: #3351A6;
  color: #ffffff;
}
</style>
