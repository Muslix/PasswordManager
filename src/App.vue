<!-- src/App.vue -->
<template>
  <div id="app" class="flex flex-col min-h-screen bg-gray-50">
    <Navbar />
    <div class="flex-grow">
      <router-view @password-added="fetchPasswords" />
    </div>
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
