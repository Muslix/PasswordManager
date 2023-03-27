<template>
  <div class="max-w-7xl mx-auto px-4 py-8">
    <h2 class="text-2xl font-bold mb-6">Password List</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="(password, index) in passwords" :key="index" class="bg-white shadow rounded-lg p-6">
        <h3 class="text-xl font-semibold mb-4">{{ password.title }}</h3>
        <div class="space-y-2">
          <div v-if="!password.editing" class="flex items-center">
            <span class="font-semibold">Category:</span>
            <span class="ml-2">{{ password.category.name }}</span>
          </div>
          <div v-else class="flex items-center">
            <span class="font-semibold">Category:</span>
            <select v-model="password.editedCategory" class="ml-2 border border-gray-300 rounded p-1">
              <option v-for="category in categories" :key="category.id" :value="category.id">
                {{ category.name }}
              </option>
            </select>
          </div>
          <div v-if="!password.editing" class="flex items-center">
            <span class="font-semibold">Username:</span>
            <span class="ml-2">{{ password.username }}</span>
          </div>
          <div v-else class="flex items-center">
            <span class="font-semibold">Username:</span>
            <input v-model="password.editedUsername" placeholder="Username" required class="ml-2 border border-gray-300 rounded p-1" />
          </div>
          <div class="flex items-center">
            <span class="font-semibold">Password:</span>
            <span v-if="password.showPassword && !password.editing" class="ml-2">
              {{ password.password }}
              <button @click="togglePasswordVisibility(password)" class="ml-2 px-3 py-1 rounded bg-indigo-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Hide</button>
            </span>
            <span v-else-if="!password.editing" class="ml-2">
              ********
              <button @click="togglePasswordVisibility(password)" class="ml-2 px-3 py-1 rounded bg-indigo-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Show</button>
              <button @click="copyPassword(password.password)" class="ml-2 px-3 py-1 rounded bg-green-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Copy</button>
            </span>
            <input v-if="password.editing" v-model="password.editedPassword" placeholder="Password" required class="ml-2 border border-gray-300 rounded p-1" />
          </div>
          <div class="w-full h-1 bg-gray-200 my-4">
            <div :class="{
              'h-full': true,
              'bg-red-600': passwordStrength(password.password) === 0,
              'bg-yellow-700': passwordStrength(password.password) === 1,
              'bg-yellow-500': passwordStrength(password.password) === 2,
              'bg-green-500': passwordStrength(password.password) === 3,
              'bg-green-700': passwordStrength(password.password) === 4
            }" :style="{ width: `${(passwordStrength(password.password) / 4) * 100}%` }"></div>
          </div>
          <div class="text-sm font-semibold">
            {{ passwordStrengthLabel(password.password) }}
          </div>
          <div class="mt-4">
            <button v-if="password.editing" @click="updatePassword(password)" class="px-3 py-1 mr-2 rounded bg-blue-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
              Save
            </button>
          <button v-if="!password.editing" @click="editPassword(password)" class="px-3 py-1 mr-2 rounded bg-blue-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
          Edit
          </button>
          <button @click="deletePassword(password)" class="px-3 py-1 rounded bg-red-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
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
  props: ['selectedCategory', 'filteredPasswords'], 
  data() {
    return {
      passwords: [],
      categories: [],
    };
  },
  async mounted() {
      await this.fetchPasswords();
      await this.fetchCategories();
  },
  methods: {
      async fetchPasswords() {
        const response = await axios.get('http://localhost:5000/api/passwords?include=category');
        let passwords = response.data.map((password) => {
          password.showPassword = false;
          password.editing = false;
          password.editedUsername = password.username;
          password.editedPassword = password.password;
          password.editedCategory = password.category;
          return password;
        });

        if (this.filteredPasswords && this.selectedCategory) {
          passwords = passwords.filter((password) => password.category.id === parseInt(this.selectedCategory));
        }
        this.passwords = passwords;
      },

      
      async fetchCategories() {
        const response = await axios.get("http://localhost:5000/api/categories");
        this.categories = response.data;
      },

      async updatePassword(password) {
        const updated_password = {
          title: password.title,
          username: password.editedUsername,
          password: password.editedPassword,
          category_id: password.editedCategory
        };

        await axios.put(`http://localhost:5000/api/passwords/${password.id}`, updated_password);
        password.username = password.editedUsername;
        password.password = password.editedPassword;
        password.category = this.categories.find(category => category.id === password.editedCategory);
        password.editing = false;
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
      editPassword(password) {
        password.editedCategory = password.category ? password.category.id : null;
        password.editing = true;
      },
    },

    watch: {
      category: {
        async handler() {
          await this.fetchPasswords();
        },
        immediate: true,
      },
    },
    
  };
  </script>

