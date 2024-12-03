<script>
import AdminNavbar from '../AdminNavbar.vue';
import router from '@/router';

export default {
	components: {
		AdminNavbar
	},
	data() {
		return {
			id : 0,
			thelist : [],
		}
	},
	async created() {
		const response = await fetch("http://localhost:8000/backend/admin/approve_sponsor", {
			method : 'GET',
			headers : {
				'Content-Type' : 'application/json',
				'Authentication-Token' : localStorage.getItem('Authentication-Token'),
			}
		});
		const result = await response.json();
		this.thelist = result;
	},
	computed : {
		nonePending() {
			return this.thelist.length > 0 ? false : true;
		}
	},
	methods : {
		approveSponsor : async function(theid) {
			const response = await fetch("http://localhost:8000/backend/admin/approve_sponsor", {
				method : 'POST',
				headers : {
					'Content-Type' : 'application/json',
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
				},
				body : JSON.stringify({"id" : theid})
			});
			const result = await response.json();
			console.log(result);
			if (result.message){
				console.log(result.message);
				alert(result.message);
			}
			else{
				alert("Sponsor has been approved.");
				router.go(0);
			}
		}
	}
}
</script>

<template>
<div class = "container-fluid">
	<header>
		<AdminNavbar/>
	</header>
	<h1 v-if="nonePending">There are no pending approvals.</h1>
	<div v-else>
		<div class = "row" v-for="sponsor in thelist">
			<div class = "col">
				<span>Sponsor ID : {{ sponsor[0] }}, Name : {{ sponsor[1] }}, Industry : {{ sponsor[2] }}</span>
			</div>
			<div class = "col">
				<button class = "btn btn-primary" @click = "approveSponsor(sponsor[0])">Approve sponsor</button>
			</div>
		</div>
	</div>
</div>
</template>