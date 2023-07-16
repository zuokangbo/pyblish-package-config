<template>

	<div class="pa-5">项目</div>
	<v-alert
      variant="outlined"
      type="warning"
      prominent
	  v-if="loading"
    >
	注意： 在项目初始化的过程中不要关闭程序，可能为造成意料之外的问题.
    </v-alert>
	<div v-if="loading" class="h-100 d-flex align-center justify-center text-center mt-16">
		<div>
			<div class="text-h5">项目环境初始化中。。。</div>
    		<v-progress-circular indeterminate color="primary" :size="100" :width="10"></v-progress-circular>
		</div>
  	</div>
	<v-skeleton-loader :loading="loading" type="paragraph">
		<projectListTab v-if="showPage === 1"></projectListTab>
	</v-skeleton-loader>

</template>

<script setup lang="ts">
import {ref} from "vue"
import projectListTab from "@/components/userComponent/projects/projectListTab.vue"


const showPage = ref(1);
const loading = ref(false);

// function ToProjectPage(index: number){
// 	showPage.value = index;
// }



</script>

<style>
</style>
