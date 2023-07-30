<template>

<div>
	<v-card>
		 <v-card-text>
			<v-row>
				 <v-col cols="12" lg="4" md="6">
				 <div class="text-h5 mb-1">全部项目</div>
				 </v-col>
				 <v-col cols="12" lg="8" md="6" class="text-right">
					 <v-dialog v-model="dialog" max-width="700">
					   <template v-slot:activator="{ props }">
						 <v-btn color="primary" v-bind="props" flat class="ml-auto">添加新的项目</v-btn>
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
	<v-table class="pa-3">
	    <thead>
	    <tr>
	        <th class="text-left" v-for="header in headers" :key="header.text">
	        {{ header.text }}
	        </th>
	    </tr>
	    </thead>
	    <tbody>
	    <tr v-for="item in items" :key="item.project">
	        <td class="font-weight-bold">
	          {{item.project}}
	        </td>
	        <td>
	          {{item.build_dir}}
	        </td>
	        <td><v-chip size="small" color="primary" class="font-weight-bold">{{item.build_version}}</v-chip></td>
	        <td>{{ item.describe }}</td>
	        <td>{{ item.root_dir }}</td>
	        <td>
	        <v-btn elevation="4" variant="elevated" size="small" @click="open(item.project)" color="success">载入项目</v-btn>
	        </td>
	    </tr>
	    </tbody>
	</v-table>
</div>

</template>

<script setup lang="ts">
import {ref, computed} from "vue"

const dialog = ref(false);
const editedIndex = ref(-1);
const refForm = ref();

const formTitle = computed(() => {
  return editedIndex.value === -1 ? "添加新的配置" : "编辑新的配置";
});

const headers = [
  { text: "项目名称", value: "project" },
  { text: "构建目录", value: "build_dir" },
  { text: "构建版本", value: "build_version" },
  { text: "备注", value: "describe" },
  { text: "根目录", value: "root_dir" },
  { text: "操作", sortable: false, align: "right", value: "action" },
];

const items = [
  {
    project: "Pipeline1",
    build_dir: "pipeline2/script",
    build_version: "1.0.3",
    describe: "测试项目",
    root_dir: "dev,root_dir"
  },
  {
    project: "Pipeline2",
    build_dir: "pipeline3/script",
    build_version: "2.0.3",
    describe: "测试项目",
    root_dir: "dev,root_dir"
  }
];


const open = (project_name: string) => {
	console.log(project_name);
};

const load_project = (project_name: string) => {
	
};

</script>

<style lang="scss" scoped>
.v-table {
  background: none;
  table {
    padding: 4px;
    padding-bottom: 8px;

    th {
      text-transform: uppercase;
      white-space: nowrap;
    }

    td {
      border-bottom: 0 !important;
    }

    tbody {
      tr {
        transition: box-shadow 0.2s, transform 0.2s;

        &:not(.v-data-table__selected):hover {
          box-shadow: 0 3px 15px -2px rgba(220, 50, 50, 0.22);
          transform: translateY(-4px);
        }
      }
    }
  }
}
</style>
