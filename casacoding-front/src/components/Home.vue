<template>
  <div id="root">
    <meta name="viewport" content="width=device-width, user-scalable=no">
    <pageheader></pageheader>
    <div id="content">
      <searchfilters
        @changeSelectedCat="onChangeSelectedCat"
        @submittedPurpose="onSubmittedPurpose"></searchfilters>
      <searchboard :cat_selected="cat_selected" :purpose="purpose"></searchboard>
    </div>
  </div>
</template>

<script>
import Pageheader from './Pageheader'
import Searchboard from './Searchboard'
import Searchfilters from './Searchfilters'

export default {
  name: 'Home',
  components: {Pageheader, Searchboard, Searchfilters},
  props: ['cat_selected', 'purpose'],
  methods: {
    onChangeSelectedCat (value) {
      this.cat_selected = value
    },
    onSubmittedPurpose (value) {
      this.purpose = value
    }
  }
}
</script>

<style scoped>
#content > div{
  float:left;
  margin-left:1%;
  margin-top:7%;
}
</style>
