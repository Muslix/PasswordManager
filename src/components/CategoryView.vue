<template>
    <div>
      <PasswordList :category="category" />
    </div>
  </template>
  
  <script>
  import PasswordList from '@/components/PasswordList.vue';
  
  export default {
    components: {
      PasswordList
    },
    data() {
      return {
        category: null
      };
    },
    async created() {
      this.category = this.$route.params.category;
    },
  };
  </script>
  