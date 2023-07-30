<template>
	<div class="ma-2">
		<v-card class="mt-2">
		  <v-table class="elevation-1" fixed-header height="850px" density="compact">
			 <thead>
			   <tr>
				 <th class="font-weight-semibold">name</th>
				 <th class="font-weight-semibold">label</th>
				 <th class="font-weight-semibold">describe</th>
				 <th class="font-weight-semibold">to_path</th>
				 <th class="font-weight-semibold">tags</th>
				 <th class="font-weight-semibold">actions</th>
				 <th class="font-weight-semibold">active</th>
				 <th class="font-weight-semibold">families</th>
				 <th class="font-weight-semibold">hosts</th>
				 <th class="font-weight-semibold">optional</th>
				 <th class="font-weight-semibold">order</th>
				 <th class="font-weight-semibold">targets</th>
				 <th class="font-weight-semibold">action</th>
			   </tr>
			 </thead>
			 <tbody>
			   <tr v-for="item in filteredList" :key="item.name">
				 <td>{{ item.name }}</td>
				 <td>{{ item.label }}</td>
				 <td>{{ item.describe }}</td>
				 <td>{{ item.to_path }}</td>
				 <td>{{ item.tags }}</td>
				 <td>{{ item.actions }}</td>
				 <td>{{ item.active }}</td>
				 <td>{{ item.families }}</td>
				 <td>{{ item.hosts }}</td>
				 <td>{{ item.optional }}</td>
				 <td>{{ item.order }}</td>
				 <td>{{ item.targets }}</td>
				 <td>
				   <div class="d-flex align-center">
					 <v-tooltip text="Edit">
					   <template v-slot:activator="{ props }">
						 <v-btn color="blue" icon variant="text" @click="editItem(item)" v-bind="props">
						   <v-icon>mdi-pencil-outline</v-icon>
						 </v-btn>
					   </template>
					 </v-tooltip>
					 <v-tooltip text="Delete">
					   <template v-slot:activator="{ props }">
						 <v-btn icon variant="text" @click="deleteItem(item)" v-bind="props" color="error">
						   <v-icon>mdi-delete-outline</v-icon>
						 </v-btn>
					   </template>
					 </v-tooltip>
					<v-btn @click="edit_code(item.id)" color="blue">
					 		编辑Code
					</v-btn>
				   </div>
				 </td>
			   </tr>
			 </tbody>
		  </v-table>
		</v-card>
	</div>
</template>

<script setup lang="ts">
import {ref, computed} from "vue"

const dialog = ref(false);
const editedIndex = ref(-1);
const refForm = ref();

const editedItem = ref({
  id: 0,
  name: "",
  label: "",
  describe: "",
  to_path: "",
  tags: "",
  actions: "",
  active: "",
  families: "",
  hosts: "",
  optional: "",
  order: "",
  targets: ""
});

const nameRules = [
  (v) => !!v || "Name is required",
  (v) => (v && v.length >= 4) || "Name must be greater than 4 characters",
];

const formTitle = computed(() => {
  return editedIndex.value === -1 ? "添加新的配置" : "编辑新的配置";
});

const filteredList = [{
  id: 1,
  name: "fileInfo",
  label: "测试文件收集",
  describe: "描述测试长的文本测试，1111，2333",
  to_path: "",
  tags: "",
  actions: "",
  active: "",
  families: "",
  hosts: "",
  optional: "",
  order: "",
  targets: "",
}]

function close() {
	
}

function save() {
	
}

function edit_code(edit_id: number){
	
}

</script>

<style>
</style>

