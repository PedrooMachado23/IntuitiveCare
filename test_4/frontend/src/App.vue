<template>
  <QueryData/>
</template>

<script>
import QueryData from './components/QueryData.vue';

export default {
  name: 'App',
  components: {
    QueryData
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body{
  margin: 0;
  background-color: rgb(228, 229, 230);
}
</style>
