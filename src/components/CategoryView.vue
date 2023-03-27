<template>
  <div>
    <password-list :selectedCategory="selectedCategory" :filteredPasswords="true"></password-list>
  </div>
</template>

<script>
import PasswordList from '@/components/PasswordList.vue';

export default {
  components: {
    PasswordList,
  },
  data() {
    return {
      selectedCategory: null,
      passwords: [],
    };
  },
  async created() {
    this.selectedCategory = this.$route.params.category;
  },
  watch: {
    $route() {
      this.selectedCategory = this.$route.params.category;
    },
  }
  
};
</script>
