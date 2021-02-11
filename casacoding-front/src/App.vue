<template>
  <div id="app">
    <meta name="viewport" content="width=device-width, user-scalable=no">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  font-family: Trebuchet MS;
}
</style>
