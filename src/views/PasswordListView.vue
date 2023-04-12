<template>
  <div>
    <div class="max-w-7xl mx-auto px-4 py-8 ">
    <h2 class="text-2xl font-bold mb-6">Password List</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <PasswordCard
        v-for="password in passwords"
        :key="password.id"
        :password="password"
      />
    </div>
  </div>
  </div>
</template>

<script>
import axios from "axios";
import PasswordCard from "../components/cards/PasswordCard.vue"
//import AddPasswordForm from "../components/forms/AddPasswordForm.vue";

export default {
  components: {
    PasswordCard,
  //  AddPasswordForm,
  },
  data() {
    return {
      passwords: [],
    };
  },
  async created() {
    await this.fetchPasswords();
  },
  methods: {
    async fetchPasswords() {
      const response = await axios.get("http://localhost:5000/api/passwords");
      this.passwords = response.data;
    },
  },
};
</script>
