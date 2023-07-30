<template>
<div class="ma-6">
	<v-card>
		 <v-card-text>
			<v-row>
				 <v-col cols="12" lg="4" md="6">
				 <div class="text-h5 mb-1">根路径配置</div>
				 </v-col>
				 <v-col cols="12" lg="8" md="6" class="text-right">
					 <v-dialog v-model="dialog" max-width="700">
					   <template v-slot:activator="{ props }">
						 <v-btn color="primary" v-bind="props" flat class="ml-auto">添加新的配置</v-btn>
					   </template>
					   <v-card>
						 <v-card-title class="pa-4 bg-secondary">
						   <span class="title text-white">{{ formTitle }}</span>
						 </v-card-title>

						 <v-card-text>
						   <v-form
							 class="mt-5"
							 ref="form"
							 v-model="refForm"
							 lazy-validation
						   >
							 <v-row>
							   <v-col cols="12" sm="6">
								 <v-text-field
								   variant="outlined"
								   color="primary"
								   density="compact"
								   v-model="editedItem.name"
								   :rules="nameRules"
								   label="name"
								 ></v-text-field>
							   </v-col>
							   <v-col cols="12" sm="6">
								 <v-text-field
								   variant="outlined"
								   color="primary"
								   density="compact"
								   :rules="nameRules"
								   required
								   v-model="editedItem.root_path"
								   label="root_path"
								 ></v-text-field>
							   </v-col>
							   <v-col cols="12" sm="6">
								 <v-text-field
								   variant="outlined"
								   color="primary"
								   density="compact"
								   v-model="editedItem.describe"
								   label="describe"
								 ></v-text-field>
							   </v-col>
							 </v-row>
						   </v-form>
						 </v-card-text>
						 <v-divider></v-divider>
						 <v-card-actions class="pa-4">
						   <v-spacer></v-spacer>
						   <v-btn color="error" @click="close">Cancel</v-btn>
						   <v-btn
							 color="secondary"
							 :disabled="
							   editedItem.name == '' || editedItem.root_path == ''
							 "
							 variant="flat"
							 @click="save"
							 >Save</v-btn
						   >
						 </v-card-actions>
					   </v-card>
					 </v-dialog>
				 </v-col>
			</v-row>
		 </v-card-text>
	</v-card>
	<v-card class="mt-2">
	  <v-table class="mt-5">
				 <thead>
				   <tr>
					 <th class="text-subtitle-1 font-weight-semibold">name</th>
					 <th class="text-subtitle-1 font-weight-semibold">root_path</th>
					 <th class="text-subtitle-1 font-weight-semibold">describe</th>
					 <th class="text-subtitle-1 font-weight-semibold">action</th>
				   </tr>
				 </thead>
				 <tbody class="text-body-1">
				   <tr v-for="item in filteredList" :key="item.name">
					 <td>{{ item.name }}</td>
					 <td>{{ item.root_path }}</td>
					 <td>{{ item.describe }}</td>
					 <td>
					   <div class="d-flex align-center">
						 <v-tooltip text="Edit">
						   <template v-slot:activator="{ props }">
							 <v-btn
							   color="blue"
							   icon
							   variant="text"
							   @click="editItem(item)"
							   v-bind="props"
							 >
							   <v-icon>mdi-pencil-outline</v-icon>
							 </v-btn>
						   </template>
						 </v-tooltip>
						 <v-tooltip text="Delete">
						   <template v-slot:activator="{ props }">
							 <v-btn
							   icon
							   variant="text"
							   @click="deleteItem(item)"
							   v-bind="props"
							   color="error"
							 >
							   <v-icon>mdi-delete-outline</v-icon>
							 </v-btn>
						   </template>
						 </v-tooltip>
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
  id: "",
  name: "1.jpg",
  root_path: "",
  describe: "",
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
	name: "dev",
	root_path: "project/dev/config",
	describe: "test"
}]

function close() {
	
}

function save() {
	
}


</script>

<style>

</style>
