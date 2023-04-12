<!-- src/components/Navbar.vue -->
<template>
  <nav class="w-64 min-h-screen bg-gray-800 text-gray-100 p-4 flex flex-col fixed">
    <div class="text-white text-2xl font-bold mb-8">
      <router-link to="/">Passwordlix</router-link>
    </div>
    <ul class="flex flex-col space-y-2">
      <li>
        <router-link to="/" class="flex items-center py-2 px-4 bg-gray-700 hover:bg-gray-600 text-white text-lg rounded transition-colors duration-200">
          <i class="material-icons mr-2">dashboard</i> Dashboard
        </router-link>
      </li>
      <li>
        <router-link to="/list" class="flex items-center py-2 px-4 bg-gray-700 hover:bg-gray-600 text-white text-lg rounded transition-colors duration-200">
          <i class="material-icons mr-2">list_alt</i> Password List
        </router-link>
      </li>
      <li>
        <router-link to="/add" class="flex items-center py-2 px-4 bg-gray-700 hover:bg-gray-600 text-white text-lg rounded transition-colors duration-200">
          <i class="material-icons mr-2">add_circle</i> Add Password
        </router-link>
      </li>
      <li>
        <router-link to="/categories" class="flex items-center py-2 px-4 bg-gray-700 hover:bg-gray-600 text-white text-lg rounded transition-colors duration-200">
          <i class="material-icons mr-2">category</i> Categories
        </router-link>
      </li>
      <li>
        <router-link to="/hist" class="flex items-center py-2 px-4 bg-gray-700 hover:bg-gray-600 text-white text-lg rounded transition-colors duration-200">
          <i class="material-icons mr-2">history</i> History
        </router-link>
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
  