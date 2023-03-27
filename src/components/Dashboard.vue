<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="max-w-6xl mx-auto px-4 py-8">
    <h2 class="text-3xl font-bold mb-6">Dashboard</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
      <div
        v-for="category in categories"
        :key="category.id"
        class="bg-white shadow-md rounded-lg p-0 relative"
      >
        <!-- Minus-Symbol -->
        <img
          src="@/assets/minus.png"
          alt="Delete icon"
          class="absolute top-2 right-2 w-4 h-4 cursor-pointer"
          @click.stop="deleteCategory(category.id)"
        />

        <!-- Rest der Kategorie-Karte (in einem Container mit Innenabstand) -->
        <div class="p-6">
          <router-link
            v-if="category.name"
            :to="{
              name: 'CategoryView',
              params: { category: category.id },
            }"
            class="block w-full h-full text-center"
          >
            <h3 class="text-xl font-bold">{{ category.name }}</h3>
          </router-link>
        </div>
      </div>
      <div class="bg-white shadow-md rounded-lg p-6 cursor-pointer flex justify-center items-center" @click="showAddCategoryModal = true">
        <div class="text-center text-4xl text-gray-400">
          <img style="width: 32px; height: 32px;" src="@/assets/plus.png" alt="Add icon" />
        </div>
      </div>
    </div>
    <div v-if="showAddCategoryModal" class="fixed z-10 inset-0 overflow-y-auto">
      <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity" @click="showAddCategoryModal = false">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>
        <div class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:align-middle sm:max-w-lg sm:w-full sm:p-6" role="dialog" aria-modal="true" aria-labelledby="modal-headline">
          <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4" id="modal-headline">
            Add a new category
          </h3>
          <form @submit.prevent="addCategory">
            <input v-model="newCategoryName" type="text" class="border border-gray-300 rounded p-1 w-full" placeholder="Category name" required>
            <div class="mt-5 sm:mt-6">
              <button type="submit" class="inline-flex justify-center w-full rounded-md border border-transparent px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:border-blue-700 focus:ring-blue transition duration-150 ease-in-out sm:text-sm sm:leading-5">
                Add
              </button>
            </div>
          </form>
        </div>
    </div>
</div>

  </div>
</template>

<script>
import axios from "axios";

/* eslint-disable */
export default {
  data() {
  return {
    categories: [],
    showAddCategoryModal: false,
    newCategoryName: ''
  };
},
methods: {
  async addCategory() {
    try {
      const response = await axios.post('http://localhost:5000/api/categories', {
        name: this.newCategoryName
      });

      this.categories.push(response.data);
      this.newCategoryName = '';
      this.showAddCategoryModal = false;
      this.fetchCategories();
    } catch (error) {
      console.error('Error adding category:', error);
    }
  },
  async deleteCategory(categoryId) {
    try {
      const response = await axios.delete(`http://localhost:5000/api/categories/${categoryId}`);

      if (response.data.success) {
        this.categories = this.categories.filter(category => category.id !== categoryId);
      } else {
        alert(response.data.message);
      }
    } catch (error) {
      console.error('Error deleting category:', error);
    }
  },
  async fetchCategories() {
    try {
      const response = await axios.get("http://localhost:5000/api/categories");
        this.categories = response.data;
    } catch (error) {
      console.error('Error fetching categories:', error);
    }
  },
},
created() {
  this.fetchCategories();
},

};
</script>
