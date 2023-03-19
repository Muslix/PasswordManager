<!-- PasswordList.vue -->
<template>
  <div class="max-w-2xl mx-auto px-4 py-8">
    <h2 class="text-3xl font-bold mb-6">Password List</h2>
    <div class="space-y-6">
      <div
        v-for="(password, index) in passwords"
        :key="index"
        class="bg-white shadow rounded-lg p-6"
      >
        <h3 class="text-xl font-semibold mb-4">{{ password.title }}</h3>
        <div class="space-y-2">
          <div class="flex items-center">
            <span class="font-semibold">Username:</span>
            <span class="ml-2">{{ password.username }}</span>
          </div>
          <div class="flex items-center">
            <span class="font-semibold">Password:</span>
            <span v-if="password.showPassword" class="ml-2">
              {{ password.password }}
              <button
                @click="togglePasswordVisibility(password)"
                class="ml-2 px-3 py-1 rounded bg-indigo-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                Hide
              </button>
            </span>
            <span v-else class="ml-2">
              ********
              <button
                @click="togglePasswordVisibility(password)"
                class="ml-2 px-3 py-1 rounded bg-indigo-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                Show
              </button>
              <button
                @click="copyPassword(password.password)"
                class="ml-2 px-3 py-1 rounded bg-green-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
              >
                Copy
              </button>
            </span>
          </div>
          <div class="w-full h-1 bg-gray-200 my-4">
          <div
            :class="{
              'h-full': true,
              'bg-red-600': passwordStrength(password.password) === 0,
              'bg-yellow-700': passwordStrength(password.password) === 1,
              'bg-yellow-500': passwordStrength(password.password) === 2,
              'bg-green-500': passwordStrength(password.password) === 3,
              'bg-green-700': passwordStrength(password.password) === 4
            }"
            :style="{
              width: `${(passwordStrength(password.password) / 4) * 100}%`,
            }"
          ></div>
        </div>
          <div class="text-sm font-semibold">
            {{ passwordStrengthLabel(password.password) }}
          </div>
          <div class="mt-4">
            <button
              @click="updatePassword(password)"
              class="px-3 py-1 mr-2 rounded bg-blue-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              Edit
            </button>
            <button
              @click="deletePassword(password)"
              class="px-3 py-1 rounded bg-red-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
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
          password.editing = false;
          password.editedUsername = password.username;
          password.editedPassword = password.password;
          return password;
      });
      },
      
      async updatePassword(password) {
        const updated_password = {
          title: password.title,
          username: password.username,
          password: password.password,
          category: password.category
        };

        await axios.put(`http://localhost:5000/api/passwords/${password.id}`, updated_password);
        await this.fetchPasswords();
      },

      async deletePassword(password) {
        await axios.delete(`http://localhost:5000/api/passwords/${password.id}`);
        await this.fetchPasswords();
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

