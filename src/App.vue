<!-- src/App.vue -->
<template>
  <div id="app">
    <Navbar />
    <router-view @password-added="fetchPasswords" />
  </div>
</template>

<script>

import Navbar from './components/Navbar.vue';

export default {
  components: {
    Navbar
  },
  methods: {
    fetchPasswords() {
      this.$refs.passwordList.fetchPasswords();
    },
  },
};
</script>
