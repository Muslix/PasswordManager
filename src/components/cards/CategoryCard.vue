<template>
    <div
      class="bg-white shadow-md rounded-lg p-0 relative"
    >
      <!-- Minus-Symbol -->
      <img
        src="@/assets/minus.png"
        alt="Delete icon"
        class="absolute top-2 right-2 w-4 h-4 cursor-pointer"
        @click.stop="deleteCategory"
      />
  
      <!-- Rest der Kategorie-Karte (in einem Container mit Innenabstand) -->
      <div class="p-6">
        <router-link
          :to="{
            name: 'CategoryPasswordList',
            params: { categoryId: category.id },
          }"
          class="block w-full h-full text-center"
        >
          <h3 class="text-xl font-bold">{{ category.name }}</h3>
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      category: {
        type: Object,
        required: true,
      },
    },
    methods: {
      deleteCategory() {
        this.$emit("delete-category", this.category.id);
      },
    },
  };
  </script>
  