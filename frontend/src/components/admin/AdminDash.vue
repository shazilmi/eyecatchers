<script>
import router from '@/router';
import AdminNavbar from '../AdminNavbar.vue';

export default {
	components : {
		AdminNavbar
	}
}
</script>

<template>
<div class = "container-fluid">
	<header>
		<AdminNavbar/>
	</header>
	<h3>Welcome, Admin</h3>
	<div class = "card">
		<div class = "card-body bg-dark-subtle">
			<h5 class = "card-title">Approve sponsor</h5>
			<p class = "card-text">Approve of any pending new sponsor signups.</p>
			<RouterLink to = "/admin/approve_sponsor" class=  "btn btn-primary">Approve sponsor</RouterLink>
		</div>
	</div>
</div>
</template>