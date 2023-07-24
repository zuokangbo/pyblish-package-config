<template>

<v-card class="ma-2">
	 <v-card-text>
		<v-row>
			 <v-col cols="12" lg="4" md="6">
			 <div class="text-h5 mb-1">根路径配置</div>
			 </v-col>
		</v-row>
	</v-card-text>
</v-card>

  <div class="app-container ma-2">
    <div class="d-none d-md-block sidebar">
      <pluginFileList></pluginFileList>
    </div>

    <div class="main">
		<fileAttrTable></fileAttrTable>
    </div>
  </div>
</template>

<script setup lang="ts">
import pluginFileList from "@/components/file/pluginFileList.vue";
import fileAttrTable from "@/components/file/fileAttrTable.vue";


</script>

<style scoped lang="scss">
.app-container {
  display: flex;
  height: 100%;
  width: 100%;
  font-size: 13px;

  .sidebar {
    display: flex;
    flex-direction: column;
    width: 300px;
    height: 100%;
    margin-right: 20px;
  }

  .main {
    flex: 1;
    width: 100%;
    height: 100%;
  }
}
</style>
