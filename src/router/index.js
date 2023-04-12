// src/router/index.js

import { createRouter, createWebHistory } from "vue-router";
import AddPassword from "../views/AddPasswordView.vue";
import PasswordList from "../views/PasswordListView.vue";
import Dashboard from "../views/DashboardView.vue";
import CategoryView from "../views/CategoryView.vue";
import PasswordHistory from "../views/HistoryView.vue"; 

const routes = [
  { path: '/', component: Dashboard },
  { path: '/list', component: PasswordList },
  { path: '/add', component: AddPassword },
  { path: "/categories", name: "Categories", component: CategoryView },
  { path: '/category/:categoryId', name: 'CategoryView', component: CategoryView }, 
  { path: '/category/:categoryId/passwords', name: 'CategoryPasswordList', component: PasswordList },
  { path: '/hist', component: PasswordHistory },
  // Add more routes here
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
