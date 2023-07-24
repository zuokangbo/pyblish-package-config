<template>
	<!---Main Sidebar -->
	<mainSidebar></mainSidebar>
	<v-main>
		<div class="flex-fill">
		  <router-view> </router-view>
		</div>
	</v-main>
</template>

<script setup lang="ts">
import mainSidebar from "@/components/mainSidebar.vue";


</script>

<style scoped>
.scrollnav {
  height: calc(100vh - 326px);
}
.main-container {
  height: 100%;
  display: flex;
  flex-direction: column;
}
</style>
