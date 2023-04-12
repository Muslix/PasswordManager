<template>
    <div class="max-w-6xl mx-auto px-4 py-8">
      <h2 class="text-3xl font-bold mb-6">Password History</h2>
      <table class="min-w-full divide-y divide-gray-200">
        <thead>
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">TITLE</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Username</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Password</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Category</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Timestamp</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="entry in history" :key="entry.id">
            <td class="px-6 py-4 whitespace-nowrap">{{ entry.title }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ entry.username }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ entry.password }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ entry.category }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ entry.timestamp }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        history: [],
      };
    },
    async mounted() {
      await this.fetchPasswords();
    },
    methods: {
      async fetchPasswords() {
        const response = await axios.get("http://localhost:5000/api/passwords/history");
        this.history = response.data.map((entry) => {
          entry.showPassword = false;
          entry.editing = false;
          return entry;
        });
      },
    },
  };
  </script>
  