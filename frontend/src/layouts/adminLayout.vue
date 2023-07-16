<template>
	<!---Main Sidebar -->
	<mainAdminSidebar></mainAdminSidebar>
	<v-main>
		<div class="flex-fill">
		  <slot></slot>
		</div>
	</v-main>
</template>

<script setup lang="ts">
import mainAdminSidebar from "@/components/mainUserSidebar.vue";


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
