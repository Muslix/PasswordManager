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
    generatePassword() {
    const length = 16;
    const charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]{}|;:,.<>?/';
    let password = '';

    for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * charset.length);
      password += charset.charAt(randomIndex);
    }

    this.newPassword.password = password;
  },
},
};
</script>