<!-- src/components/AddPassword.vue -->
<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Add Password
        </h2>
      </div>
      <form @submit.prevent="addPassword" class="mt-8 space-y-6">
        <input type="hidden" name="remember" value="true" />
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="title" class="sr-only">Title</label>
            <input
              v-model="title"
              id="title"
              name="title"
              type="text"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Title"
            />
          </div>
          <div>
            <label for="username" class="sr-only">Username</label>
            <input
              v-model="username"
              id="username"
              name="username"
              type="text"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Username"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              v-model="password"
              id="password"
              name="password"
              type="text"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Password"
            />
          </div>
        </div>
        <div class="flex items-center justify-between">
          <div>
            <button
              @click.prevent="generatePassword"
              type="button"
              class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-indigo-700 bg-indigo-100 hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Generate Password
            </button>
          </div>
          <div>
            <select
              v-model="category"
              class="block appearance-none w-full bg-white border border-gray-300 text-gray-700 py-2 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
            >
              <option disabled value="">Choose a category</option>
              <option>Personal</option>
              <option>Work</option>
              <option>Finance</option>
              <option>Social</option>
            </select>
          </div>
        </div>
        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Save
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
Das ist das aktual




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
  