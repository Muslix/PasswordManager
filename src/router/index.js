// src/router/index.js

import { createRouter, createWebHistory } from "vue-router";
import AddPassword from "../components/AddPassword.vue";
import PasswordList from "../components/PasswordList.vue";
import Dashboard from "../components/Dashboard.vue";
import CategoryView from "../components/CategoryView.vue"; 
import PasswordHistory from "../components/PasswordHistory.vue"; 

const routes = [
    { path: '/', component: Dashboard },
    { path: '/list', component: PasswordList },
    { path: '/add', component: AddPassword },
    { path: '/category/:category', name: 'CategoryView', component: CategoryView }, 
    { path: '/hist', component: PasswordHistory },
    // Fügen Sie hier weitere Routen hinzu
  ];
  

  const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  

export default router;
