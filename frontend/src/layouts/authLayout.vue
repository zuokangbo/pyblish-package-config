<template>
	<div class="d-flex text-center flex-grow-1">
		<v-sheet v-if="isShowSheet" class="layout-side d-none d-md-flex flex-column justify-space-between" >
		  <div class="mt-3 mt-md-10 pa-2">
			<div class="text-primary text-h4 font-weight-bold">
			  VFX Pipeline build 1.0
			</div>
			<div class="title my-2">
			  vfx 制作环境构建系统
			</div>
		  </div>
		</v-sheet>
		<v-card
		  variant="outlined"
		  class="flex-grow-1 d-flex align-center justify-center flex-column"
		>
		  <div class="layout-content ma-auto w-full">
			  <v-card color="grey-darken-3" class="pa-3 ma-3" elevation="3">
				<v-card-title class="my-4 text-h4">
				  <span class="flex-fill"> Welcome </span>
				</v-card-title>
				<v-card-subtitle>Sign in to your account</v-card-subtitle>
				<v-card-text>
					<v-form ref="refLoginForm" class="text-left" v-model="isFormValid" lazy-validation>
						<v-text-field v-model="account" required :error="error" density="default" color="primary" name="account" clearable  label="用户名" bg-color="#222" outlined></v-text-field>
						<v-text-field label="用户密码" ref="refPassword" v-model="password" :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" :type="showPassword ? 'text' : 'password'" :error="error" name="password" outlined bg-color="#222"></v-text-field>
						<v-btn :loading="isLoading" size="x-large" color="primary" class="mt-2" block>登录</v-btn>
						<div class="text-grey text-center text-caption font-weight-bold text-uppercase my-5">只能使用计算机登录的域用户和密码</div>
					</v-form>
				</v-card-text>
			  </v-card>
		  </div>
		  <div class="pa-5">Version 3.1.0 & Vite 4.2</div>
		</v-card>
	</div>
</template>

<script setup lang="ts">
import {ref} from "vue"


const refLoginForm = ref();
const account = ref("vuetify3-visitor@gmail.com");
const password = ref("sfm12345");
const isFormValid = ref(true);
const error = ref(false);
const showPassword = ref(false);
const isLoading = ref(false);
const isShowSheet = ref(true);



</script>

<style scoped>
.layout-side {
  width: 420px;
}

.layout-content {
  max-width: 480px;
  width: 100%;
}

</style>

