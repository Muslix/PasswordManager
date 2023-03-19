<!-- src/App.vue -->
<template>
  <div id="app">
    <h1>Password Manager</h1>
    <AddPassword @password-added="fetchPasswords" />
    <PasswordList ref="passwordList" />
  </div>
</template>

<script>
import AddPassword from './components/AddPassword.vue';
import PasswordList from './components/PasswordList.vue';

export default {
  components: {
    AddPassword,
    PasswordList
  },
  methods: {
    fetchPasswords() {
      this.$refs.passwordList.fetchPasswords();
    },
},
};
</script>