<template>
  <div class="bg-white shadow rounded-lg p-6 relative">
    <h3 class="text-xl font-semibold mb-4 inline-block">
      {{ password.title }}
    </h3>
    <button
      v-if="!password.editing"
      @click="editPassword"
      class="inline-block ml-2 text-gray-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
    >
      <span class="material-icons"> edit </span>
    </button>
    <button
      v-if="!password.editing"
      @click="deletePassword"
      class="absolute top-2 right-2 text-gray-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
    >
      <span class="material-icons"> delete </span>
    </button>
    <div class="space-y-2">
      <div class="flex items-center">
        <span class="font-semibold text-gray-900">Category:</span>
        <span class="ml-2 text-gray-900">{{ password.category.name }}</span>
      </div>
      <div v-if="!password.editing" class="flex items-center">
        <span class="font-semibold text-gray-900">Username:</span>
        <span class="ml-2 text-gray-900">{{ password.username }}</span>
      </div>
      <div v-else class="flex items-center">
        <span class="font-semibold text-gray-900">Username:</span>
        <input
          v-model="localPassword.editedUsername"
          placeholder="Username"
          required
          class="ml-2 border border-gray-300 rounded p-1"
        />
      </div>
      <div class="flex items-center">
        <span class="font-semibold text-gray-900">Password:</span>
        <span
          v-if="password.showPassword && !password.editing"
          class="ml-2 text-gray-900"
        >
          {{ password.password }}
          <button
            @click="togglePasswordVisibility"
            class="ml-2 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            <span class="material-icons text-gray-900"> visibility_off </span>
          </button>
        </span>
        <span v-else-if="!password.editing" class="ml-2 text-gray-900">
          ********
          <button
            @click="togglePasswordVisibility"
            class="ml-2 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            <span class="material-icons text-gray-900"> visibility </span>
          </button>
          <button
            @click="copyPassword(password.password)"
            class="ml-2 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
          >
            <span class="material-icons text-gray-900"> content_copy </span>
          </button>
        </span>
        <input
          v-if="password.editing"
          v-model="localPassword.editedPassword"
          placeholder="Password"
          required
          class="ml-2 border border-gray-300 rounded p-1"
        />
      </div>
      <div class="w-full h-1 bg-gray-200 my-4">
        <div
          :class="{
            'h-full': true,
            'bg-red-600': passwordStrength(password.password) === 0,
            'bg-yellow-700': passwordStrength(password.password) === 1,
            'bg-yellow-500': passwordStrength(password.password) === 2,
            'bg-green-500': passwordStrength(password.password) === 3,
            'bg-green-700': passwordStrength(password.password) === 4,
          }"
          :style="{
            width: `${(passwordStrength(password.password) / 4) * 100}%`,
          }"
        ></div>
      </div>
      <div class="text-sm font-semibold text-gray-900">
        {{ passwordStrengthLabel(password.password) }}
      </div>
      <div class="mt-4">
        <button
          v-if="password.editing"
          @click="updatePassword"
          class="px-3 py-1 mr-2 rounded bg-gray-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
        >
          Save
        </button>
        <button
          v-if="password.editing"
          @click="cancelEdit"
          class="px-3 py-1 rounded bg-gray-600 text-white text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
        >
          Cancel
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import zxcvbn from "zxcvbn";

export default {
  props: {
    password: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      localPassword: { ...this.password, editing: false },
    };
  },
  methods: {
    editPassword() {
      this.localPassword.editing = true;
    },
    deletePassword() {
      this.$emit("delete", this.password);
    },
    updatePassword() {
      this.$emit("update", this.password);
    },
    cancelEdit() {
      this.localPassword.editing = false;
      this.localPassword = { ...this.password };
    },
    togglePasswordVisibility() {
      this.$emit("toggle-visibility", this.password);
    },
    copyPassword(password) {
      this.$emit("copy-password", password);
    },
    passwordStrength(password) {
      const result = zxcvbn(password);
      return result.score;
    },
    passwordStrengthLabel(password) {
      const strength = this.passwordStrength(password);
      if (strength <= 1) {
        return "Weak";
      } else if (strength === 2) {
        return "Medium";
      } else {
        return "Strong";
      }
    },
  },
  watch: {
    password: {
      handler(newValue) {
        this.localPassword = { ...newValue };
      },
      deep: true,
    },
  },
};
</script>
