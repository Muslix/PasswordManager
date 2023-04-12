<!-- src/views/CategoryView.vue -->
<template>
    <div class="max-w-full mx-auto px-4 py-8 ml-64">
      <h2 class="text-3xl font-bold mb-6">Categories</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <CategoryCard
          v-for="category in categories"
          :key="category.id"
          :category="category"
          @delete-category="onDeleteCategory"
        />
        <div
          class="bg-white shadow-md rounded-lg p-6 cursor-pointer flex justify-center items-center"
          @click="showAddCategoryModal = true"
        >
          <div class="text-center text-4xl text-gray-400">
            <img
              style="width: 32px; height: 32px;"
              src="@/assets/plus.png"
              alt="Add icon"
            />
          </div>
        </div>
      </div>
      <AddCategoryModal
        v-if="showAddCategoryModal"
        @close="showAddCategoryModal = false"
        @add-category="onAddCategory"
      />
    </div>

  </template>
  
  <script>
  import axios from "axios";
  import CategoryCard from "../components/cards/CategoryCard.vue";
  import AddCategoryModal from "../components/modals/AddCategoryModal.vue";
  
  export default {
    components: {
      CategoryCard,
      AddCategoryModal,
    },
    data() {
      return {
        categories: [],
        showAddCategoryModal: false,
      };
    },
    methods: {
      async fetchCategories() {
        try {
          const response = await axios.get("http://localhost:5000/api/categories");
          this.categories = response.data;
        } catch (error) {
          console.error("Error fetching categories:", error);
        }
      },
      onAddCategory(newCategory) {
      this.categories.push(newCategory);
    },
    onDeleteCategory(categoryId) {
      this.categories = this.categories.filter(
        (category) => category.id !== categoryId
      );
    },
  },
  created() {
    this.fetchCategories();
  },
};
</script>
