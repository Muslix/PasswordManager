<!-- src/components/AddPassword.vue -->
<template>
    <div>
      <h2>Add Password</h2>
      <form @submit.prevent="addPassword">
        <input v-model="title" placeholder="Title" required />
        <input v-model="username" placeholder="Username" required />
        <input v-model="password" placeholder="Password" required />
        <button @click.prevent="generatePassword">Generate Password</button>
        <select v-model="category">
        <option disabled value="">Choose a category</option>
        <option>Personal</option>
        <option>Work</option>
        <option>Finance</option>
        <option>Social</option>
      </select>
        <button type="submit">Save</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        title: '',
        username: '',
        password: '',
        category: ''
      };
    },
    methods: {
      async addPassword() {
        const new_password = {
          title: this.title,
          username: this.username,
          password: this.password,
          category: this.category
        };
        await axios.post('http://localhost:5000/api/passwords', new_password);
        this.$emit('password-added');
      },
      generatePassword() {
        const length = 16;
        const charsetLower = 'abcdefghijklmnopqrstuvwxyz';
        const charsetUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        const charsetNumbers = '0123456789';
        const charsetSpecial = '!@#$%^&*()-=_+[]{}|;:,.<>?/';
        let password = '';

        // Zufällige Zeichen aus jeder Gruppe auswählen, um sicherzustellen, dass sie im Passwort enthalten sind
        const randomLower = charsetLower.charAt(Math.floor(Math.random() * charsetLower.length));
        const randomUpper = charsetUpper.charAt(Math.floor(Math.random() * charsetUpper.length));
        const randomNumber = charsetNumbers.charAt(Math.floor(Math.random() * charsetNumbers.length));
        const randomSpecial = charsetSpecial.charAt(Math.floor(Math.random() * charsetSpecial.length));

        // Die restlichen Zeichen aus dem gesamten Zeichensatz auswählen
        const charsetCombined = charsetLower + charsetUpper + charsetNumbers + charsetSpecial;
        for (let i = 0; i < length - 4; i++) {
        const randomIndex = Math.floor(Math.random() * charsetCombined.length);
        password += charsetCombined.charAt(randomIndex);
        }

        // Die ausgewählten Zeichen mischen, um das endgültige Passwort zu generieren
        password = password + randomLower + randomUpper + randomNumber + randomSpecial;
        password = password.split('').sort(() => Math.random() - 0.5).join('');

        this.password = password;
      },
    }
  };
  </script>
  