<script>
import router from '@/router';
import AdminNavbar from '../AdminNavbar.vue';

export default {
	data() {
		return {
			result : {}
		}
	},
	components : {
		AdminNavbar
	},
	async created() {
		const response = await fetch("http://localhost:8000/backend/admin/stats", {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'Authentication-Token': localStorage.getItem('Authentication-Token'),
			},
		});
		const result = await response.json();
		console.log(result);
		this.result = result;
	}
}
</script>

<template>
	<div class="container-fluid" id="stats">
		<header>
			<AdminNavbar/>
		</header>
		<div class="row" id="row1">
			<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
				<div class="card bg-dark text-white text-center mb-4 someclass">
					<div class="card-body">
						<h5 class="card-title">Number of users : {{ this.result.users }}</h5>
						<p>Total number of users in the database. This includes admin, influencers and sponsors.</p>
					</div>
				</div>
			</div>
			<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
				<div class="card bg-dark text-white text-center mb-4 someclass">
					<div class="card-body">
						<h5 class="card-title">Number of sponsors : {{ this.result.sponsors }}</h5>
						<p>Total number of sponsors in the database. This includes both approved and yet-to-be approved
							sponsors.</p>
					</div>
				</div>
			</div>
			<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
				<div class="card bg-dark text-white text-center mb-4 someclass">
					<div class="card-body">
						<h5 class="card-title">Number of influencers : {{ this.result.influencers }}</h5>
						<p>Total number of influencers in the database.</p>
					</div>
				</div>
			</div>
		</div>
		<div class="row" id="row2">
			<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
				<div class="card bg-dark text-white text-center mb-4 someclass">
					<div class="card-body">
						<h5 class="card-title">Number of ad requests : {{ this.result.ads }}</h5>
						<p>Total number of ad requests made using the app.</p>
					</div>
				</div>
			</div>
			<div class="col-lg-4 col-md-12 mb-4 mb-lg-0 ">
				<div class="card bg-dark text-white text-center mb-4 someclass">
					<div class="card-body">
						<h5 class="card-title">Number of campaigns : {{ this.result.campaigns }}</h5>
						<p>Total number of campaigns made by sponsors. This includes private and public campaigns.</p>
					</div>
				</div>
			</div>
			<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
				<div class="card bg-dark text-white text-center mb-4 someclass">
					<div class="card-body">
						<h5 class="card-title">Number of public campaigns : {{ this.result.public_campaigns }}</h5>
						<p>Total number of public campaigns on the app.</p>
					</div>
				</div>
			</div>
		</div>
		<div class="row" id="row3">
			<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
				<div class="card bg-dark text-white text-center mb-4 someclass">
					<div class="card-body">
						<h5 class="card-title">Number of flagged users : {{ this.result.flagged }}</h5>
						<p>Total number of users who have been flagged on the app.</p>
					</div>
				</div>
			</div>
			<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
				<div class="card bg-dark text-white text-center mb-4 someclass">
					<div class="card-body">
						<h5 class="card-title">Number of unapproved sponsors : {{ this.result.unapproved }}</h5>
						<p>Total number of sponsors who are yet to be approved of.</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>