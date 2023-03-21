<!-- src/components/Navbar.vue -->
<template>
    <nav class="bg-blue-500 p-4">
      <ul class="flex">
        <li class="mr-6">
          <router-link to="/" class="text-white text-lg hover:text-blue-200">Dashboard</router-link>
        </li>
        <li class="mr-6">
          <router-link to="/list" class="text-white text-lg hover:text-blue-200">Password List</router-link>
        </li>
        <li class="mr-6">
          <router-link to="/add" class="text-white text-lg hover:text-blue-200">Add Password</router-link>
        </li>
        <li class="mr-6">
          <router-link to="/hist" class="text-white text-lg hover:text-blue-200">History</router-link>
        </li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    /* eslint-disable */
    name: "Navbar",
  };
  </script>
  
  <style scoped>
  </style>
  