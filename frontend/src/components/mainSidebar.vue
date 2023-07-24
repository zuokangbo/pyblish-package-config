<template>
	<v-navigation-drawer permanent border="none" elevation="1" v-model="drawer" :rail="rail" @click="rail = false" rail-width=65>
		<template v-slot:prepend>
		  <v-list-item class="pl-1"
		  lines="two"
          title="Pyblish Config"
		  subtitle="Pyblish Package Config v0.0.1"
		  >
		  <template v-slot:prepend>
			<v-avatar color="orange-darken-3" size="large">
			  <span class="text-h5">PB</span>
			</v-avatar>
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
	{"icon": "mdi-folder-table", "key": "project", "text": "项目列表", "link": "/project"},
	{"icon": "mdi-apple-keyboard-command", "key": "config", "text": "全局配置", "link": "/config"},
	{"icon": "mdi-upload", "key": "plugin", "text": "所有插件", "link": "/plugin"},
	{"icon": "mdi-help-circle-outline", "key": "help", "text": "帮助文档", "link": "/help"},
	{"icon": "mdi-update", "key": "update_log", "text": "更新日志", "link": "/update_log"},
]


</script>

<style>
</style>

