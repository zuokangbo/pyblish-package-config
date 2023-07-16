<template>
	<v-navigation-drawer permanent border="none" elevation="1" v-model="drawer" :rail="rail" @click="rail = false" rail-width=65>
		<template v-slot:prepend>
		  <v-list-item class="pl-1"
			lines="two"
			title="Zuokangbo"
			subtitle="20223@qq.com"
		  >
		  <template v-slot:prepend>
		    <avatars-menu></avatars-menu>
		  </template>
		  </v-list-item>
		  <v-divider></v-divider>
		</template>
		<v-list density="compact" nav>
		  <v-list-item v-for="subMenuItem in MenuDataList" :key="subMenuItem.key" :prepend-icon="subMenuItem.icon" :title="subMenuItem.text" :to="subMenuItem.link">
		  </v-list-item>
		</v-list>

		<template v-slot:append>
			<v-divider></v-divider>
			<v-btn block size="x-large" variant="text" prepend-icon="mdi-chevron-left" @click.stop="rail = !rail"></v-btn>
		</template>
	</v-navigation-drawer>
</template>

<script setup lang="ts">
import {ref} from "vue"
import avatarsMenu from "./userComponent/avatarsMenu.vue";

interface IMenuData {
	icon: string;
	key: string;
	text: string;
	link: string;
}
// icon: "mdi-format-list-checkbox",
// key: "menu.todo",
// text: "Todo",
// link: "/apps/todo",

const drawer = ref(true);
const rail = ref(false);

const MenuDataList: IMenuData[] = [
	{"icon": "mdi-home-account", "key": "client.home", "text": "主页", "link": "/client/home"},
	{"icon": "mdi-folder-table", "key": "client.projects", "text": "项目列表", "link": "/client/projects"},
	{"icon": "mdi-apple-keyboard-command", "key": "client.app", "text": "全局配置", "link": "/client/app"},
	{"icon": "mdi-upload", "key": "client.upload", "text": "插件管理", "link": "/client/upload"},
	{"icon": "mdi-squeegee", "key": "client.rendering", "text": "用户管理", "link": "/client/rendering"},
	{"icon": "mdi-expansion-card-variant", "key": "client.process", "text": "流程步骤进度", "link": "/client/process"},
	{"icon": "mdi-help-circle-outline", "key": "client.help", "text": "帮助文档", "link": "/client/help"},
	{"icon": "mdi-update", "key": "client.update", "text": "更新日志", "link": "/client/update"},
	{"icon": "mdi-cog", "key": "client.preference", "text": "偏好设置", "link": "/client/preference"}
]


</script>

<style>
</style>

