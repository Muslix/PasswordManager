<template>
    <div class="bg-white shadow rounded-lg p-6">
      <h3 class="text-xl font-semibold mb-4">Add New Password</h3>
      <form @submit.prevent="submitForm">
        <div class="mb-4">
          <label for="title" class="block text-gray-700 text-sm font-semibold mb-2">Title</label>
          <input id="title" v-model="newPassword.title" type="text" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Title">
        </div>
        <div class="mb-4">
          <label for="category" class="block text-gray-700 text-sm font-semibold mb-2">Category</label>
          <select id="category" v-model="newPassword.category_id" class="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            <option v-for="category in categories" :key="category.id" :value="category.id">
              {{ category.name }}
            </option>
          </select>
        </div>
        <div class="mb-4">
          <label for="username" class="block text-gray-700 text-sm font-semibold mb-2">Username</label>
          <input id="username" v-model="newPassword.username" type="text" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Username">
        </div>
        <div class="mb-4">
          <label for="password" class="block text-gray-700 text-sm font-semibold mb-2">Password</label>
          <input id="password" v-model="newPassword.password" type="password" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Password">
        </div>
        <button type="submit" class="w-full py-2 px-4 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2 focus:ring-offset-blue-100">
          Add Password
        </button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      categories: {
        type: Array,
        required: true,
      },
    },
    data() {
      return {
        newPassword: {
          title: "",
          category_id: "",
          username: "",
          password: "",
        },
      };
    },
    methods: {
      async submitForm() {
        this.$emit("password-added", this.newPassword);
        this.newPassword = {
          title: "",
          category_id: "",
          username: "",
          password: "",
        };
      },
    },
  };
  </script>
  