import { createRouter, createWebHistory } from "vue-router";

// 动态路由，基于用户权限动态去加载
export const dynamicRoutes = [];


export const routes = [
  {
    path: "/",
    component: () => import("@/layouts/adminLayout.vue"),
	children: [
		{
			path: "project",
			name: "project",
			component: () => import("@/views/projectPage.vue")
		},
		{
			path: "plugin",
			name: "plugin",
			component: () => import("@/views/PluginPage.vue")
		},
		{
			path: "config",
			name: "config",
			component: () => import("@/views/configPage.vue")
		},
		{
			path: "help",
			name: "help",
			component: () => import("@/views/helpDoc.vue")
		},
		{
			path: "update_log",
			name: "update_log",
			component: () => import("@/views/updateLogPage.vue")
		}
	]
  }
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

