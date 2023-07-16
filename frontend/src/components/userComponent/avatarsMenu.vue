<template>
	<v-container fluid style="height: 50px">
	    <v-row justify="center">
	      <v-menu min-width="200px" rounded>
	        <template v-slot:activator="{ props }">
	          <v-btn icon v-bind="props">
	            <v-avatar color="orange-darken-3" size="large">
	              <span class="text-h5">{{ user.initials }}</span>
	            </v-avatar>
	          </v-btn>
	        </template>
	        <v-card>
	          <v-card-text>
	            <div class="mx-auto text-center">
	              <v-avatar color="brown">
	                <span class="text-h5">{{ user.initials }}</span>
	              </v-avatar>
	              <h3>{{ user.department }}</h3>
	              <p class="text-caption mt-1">
	                {{ user.role }}
	              </p>
	              <v-divider class="my-3"></v-divider>
	              <v-btn rounded variant="text">个人账户</v-btn>
	              <div><v-btn rounded variant="text">查看帮助</v-btn></div>
	              <div><v-btn rounded variant="text">查看本地日志</v-btn></div>
	              <v-divider class="my-3"></v-divider>
	              <v-btn rounded variant="text">退出登录</v-btn>
	            </div>
	          </v-card-text>
	        </v-card>
	      </v-menu>
	    </v-row>
	  </v-container>
</template>

<script setup lang="ts">
interface IUserData {
	initials: string;
	department: string;
	role: string;
}

const props = withDefaults(defineProps<{user: IUserData}>(), {user: {initials: "左", department: "Ani", role: "Artist"},});

</script>

<style>
</style>
