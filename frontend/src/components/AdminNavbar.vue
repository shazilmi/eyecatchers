<script>
import Shared from './Shared.vue';

export default {
	created() {
		this.logoutUser = Shared.logoutUser;
	}
}
</script>

<template>
	<nav class = "navbar static-top bg-body-tertiary" id = "eyecatch" data-bs-theme = "dark">
		<span class = "navbar-brand mb-0 h1">Eyecatchers</span>
		<RouterLink class = "navbar-brand" id = "link" to = "/admin/dash">Dashboard</RouterLink>
		<RouterLink class = "navbar-brand" id = "link" to = "/admin/stats">Stats</RouterLink>
		<RouterLink class = "navbar-brand" id = "link" to = "/admin/find">Find</RouterLink>
		<span class = "navbar-brand" @click = "logoutUser">Logout</span>
	</nav>
</template>