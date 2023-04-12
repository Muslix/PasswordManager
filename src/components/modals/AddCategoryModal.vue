<!-- src/components/modals/AddCategoryModal.vue -->
<template>
    <div class="fixed z-10 inset-0 overflow-y-auto">
      <div
        class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
      >
        <div
          class="fixed inset-0 transition-opacity"
          @click="$emit('close')"
        >
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>
        <div
          class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:align-middle sm:max-w-lg sm:w-full sm:p-6"
          role="dialog"
          aria-modal="true"
          aria-labelledby="modal-headline"
        >
          <h3
            class="text-lg leading-6 font-medium text-gray-900 mb-4"
            id="modal-headline"
          >
            Add a new category
          </h3>
          <form @submit.prevent="addCategory">
            <input
              v-model="newCategoryName"
              type="text"
              class="border border-gray-300 rounded p-1 w-full"
              placeholder="Category name"
              required
            />
            <div class="mt-5 sm:mt-6">
              <button
                type="submit"
                class="inline-flex justify-center w-full rounded-md border border-transparent px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:border-blue-700 focus:ring-blue transition duration-150 ease-in-out sm:text-sm sm:leading-5"
              >
                Add
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        newCategoryName: "",
      };
    },
    methods: {
      async addCategory() {
        try {
          const response = await axios.post("http://localhost:5000/api/categories", {
            name: this.newCategoryName,
          });
  
          this.$emit("add-category", response.data);
          this.newCategoryName = "";
          this.$emit("close");
        } catch (error) {
          console.error("Error adding category:", error);
        }
      },
    },
  };
  </script>
  