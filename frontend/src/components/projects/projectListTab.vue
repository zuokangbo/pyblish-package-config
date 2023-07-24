<template>

<div>
	<h6 class="text-h6 font-weight-bold pa-5 d-flex align-center">
	    <span class="flex-fill">所有配置项</span>
	</h6>
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
