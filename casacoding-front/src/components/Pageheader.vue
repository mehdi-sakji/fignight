/* eslint-disable */

<template>
  <header>
    <b-navbar type="dark" toggleable="lg" variant="info">
      <b-navbar-brand href="#" class="mb-0">
        <span class="brd_ttl"> CasaSkills </span>
      </b-navbar-brand>
    </b-navbar>
  </header>
</template>

<script>
export default {

  name: 'Pageheader',
  methods: {
    toggleNav () {
      this.$parent.$emit('toggleNav')
    }
  }
}
</script>

<style scoped>

.b-navbar-brand img {
  max-height: 100%;
}
.brd_ttl {
  color: white;
  font-size: 1.3em;
  font-family:cursive;
  font-weight: bold;
}
header {
  position: fixed;
  z-index: 30;
  width:100%;
  left:0;
  top:0;
}
</style>
