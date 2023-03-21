<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="max-w-6xl mx-auto px-4 py-8">
    <h2 class="text-3xl font-bold mb-6">Dashboard</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
      <div
        v-for="category in categories"
        :key="category.id"
        class="bg-white shadow-md rounded-lg p-6"
      >
        <router-link
          :to="{ name: 'CategoryView', params: { category: category.name } }"
          class="block w-full h-full text-center"
        >
          <h3 class="text-xl font-bold">{{ category.name }}</h3>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  data() {
    return {
      categories: [
        { id: 1, name: "Social" },
        { id: 2, name: "Work" },
        { id: 3, name: "Personal" },
        { id: 4, name: "Others" },
      ],
    };
  },
};
</script>
