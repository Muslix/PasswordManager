<!-- PasswordList.vue -->

<template>
    <div>
      <h2>Password List</h2>
      <ul>
        <li v-for="(password, index) in passwords" :key="index">
          <h3>{{ password.title }}</h3>
          <p>Username: {{ password.username }}</p>
          <p v-if="password.showPassword">Password: {{ password.password }} <button @click="togglePasswordVisibility(password)">Hide</button></p>
          <p v-else>Password: ******** <button @click="togglePasswordVisibility(password)">Show</button><button @click="copyPassword(password.password)">Copy</button></p>
          <div class="strength-container">
            <div class="strength-bar">
              <div :class="'strength-bar-segment strength-' + (index + 1)" v-for="index in 4" :key="index" :style="{width: (passwordStrength(password.password) >= index ? '25%' : '0')}"></div>
              <div class="strength-label">{{ passwordStrengthLabel(password.password) }}</div>
            </div>    
          </div>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import zxcvbn from "zxcvbn";

  export default {
    data() {
      return {
        passwords: []
      };
    },
    async mounted() {
      await this.fetchPasswords();
    },
    methods: {
        async fetchPasswords() {
        const response = await axios.get('http://localhost:5000/api/passwords');
        this.passwords = response.data.map((password) => {
            password.showPassword = false;
            return password;
        });
        },
      copyPassword(password) {
        navigator.clipboard.writeText(password).then(
        () => {
            alert("Password copied to clipboard!");
            },
        (err) => {
            alert("Failed to copy password to clipboard." + err);
            }
        );
      },
      passwordStrength(password) {
        const result = zxcvbn(password);
        return result.score;
      },
      togglePasswordVisibility(password) {
        password.showPassword = !password.showPassword;
      },
      passwordStrengthLabel(password) {
        const strength = this.passwordStrength(password);
        if (strength <= 1) {
        return "Weak";
        } else if (strength === 2) {
        return "Medium";
        } else {
        return "Strong";
        }
      },
    },
    watch: {
      async 'password-added'() {
        await this.fetchPasswords();
      },
    },
    
  };
  </script>

<style scoped>
.strength-bar {
  display: flex;
  height: 10px;
  width: 15%;
  margin-bottom: 10px;
}

.strength-bar-segment {

  transition: width 0.5s;
}

.strength-1 {
  background-color: #ff4b4b;
}

.strength-2 {
  background-color: #ffaa4b;
}

.strength-3 {
  background-color: #ffee4b;
}

.strength-4 {
  background-color: #4bff4b;
}
</style>
