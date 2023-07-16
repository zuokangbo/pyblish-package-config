import { createRouter, createWebHistory } from "vue-router";

// 动态路由，基于用户权限动态去加载
export const dynamicRoutes = [];


export const routes = [
  {
    path: "/admin",
  	name: "admin",
    component: () => import("@/layouts/adminLayout.vue"),
  },
  // {
  //   path: "/:pathMatch(.*)*",
  //   name: "error",
  //   component: () =>
  //     import(/* webpackChunkName: "error" */ "@/views/errors/NotFoundPage.vue"),
  // }
];


const router = createRouter({
  history: createWebHistory(),
  // hash模式：createWebHashHistory，history模式：createWebHistory
  // process.env.NODE_ENV === "production"
  routes: routes
});

export default router;

