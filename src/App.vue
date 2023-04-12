<!-- src/App.vue -->
<template>
  <div id="app" class="h-screen flex bg-gray-50">
    <Navbar />
    <div class="flex-grow overflow-y-auto">
      <router-view @password-added="fetchPasswords" />
    </div>
  </div>
</template>

<script>

import Navbar from './layouts/Navbar.vue';

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
