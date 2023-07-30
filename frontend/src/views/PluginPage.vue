<template>

<v-card class="ma-2">
	 <v-card-text>
		<v-row>
			 <v-col cols="12" lg="2">
				<v-combobox
				  label="选择类型"
				  density="compact"
				  :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
				  variant="underlined"
				></v-combobox>
			 </v-col>
			 <v-col cols="12" lg="2">
			 				<v-combobox
			 				  label="选择houst"
							  density="compact"
			 				  :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
			 				  variant="underlined"
			 				></v-combobox>
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
					   <v-form class="mt-5" ref="form" v-model="refForm" lazy-validation>
						 <v-row>
						   <v-col cols="12" sm="6">
							 <v-text-field
							   variant="outlined"
							   color="primary"
							   density="compact"
							   v-model="editedItem.name"
							   label="name"
							 ></v-text-field>
						   </v-col>
						   <v-col cols="12" sm="6">
							 <v-text-field
							   variant="outlined"
							   color="primary"
							   density="compact"
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

  <fileAttrTable></fileAttrTable>
</template>

<script setup lang="ts">
import {ref, computed} from "vue"

import fileAttrTable from "@/components/file/fileAttrTable.vue";

const dialog = ref(false);
const editedIndex = ref(-1);
const formTitle = computed(() => {
  return editedIndex.value === -1 ? "添加新的配置" : "编辑新的配置";
});

const refForm = ref();
const editedItem = ref({
  id: "",
  name: "1.jpg",
  root_path: "",
  describe: "",
});

function close() {
	
}

function save() {
	
}


</script>

<style scoped lang="scss">

</style>
