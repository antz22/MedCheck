<template>
  <Page actionBarHidden="true">

    <!-- <ActionBar title="OneFocus" android:flat="true"/> -->

    <TabView android:tabBackgroundColor="#53ba82"
              android:tabTextColor="#c4ffdf"
              android:selectedTabTextColor="#ffffff"
              androidSelectedTabHighlightColor="#ffffff"
              androidTabsPosition="bottom"
              selectedIndex="0">

      <!-- <TabViewItem class="fas" title.decode="Home &#xf015;"> -->
      <!-- <TabViewItem class="fas" title.decode="&#xf469;"> -->
      <TabViewItem title="Component 1">
        <GridLayout columns="*" rows="*">
          <Home/>
        </GridLayout>
      </TabViewItem>

      <!-- <TabViewItem class="fas" title.decode="Tasks &#xf0ae;"> -->
      <TabViewItem title="Component 2">
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
  background-color: #53ba82;
  color: #ffffff;
}
</style>
