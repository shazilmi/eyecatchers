<script>
import router from '@/router';
import SponsorNavbar from '../SponsorNavbar.vue';

export default {
	components : {
		SponsorNavbar
	},
	data() {
		return {
			basics : {}
		}
	},
	computed : {
		noCampaigns() {
			return this.basics.campaigns.length > 0 ? false : true;
		}
	},
	async created() {
		const response = await fetch("http://127.0.0.1:8000/backend/sponsor/sponsor_basic_stats", {
			method : 'GET',
			headers: {
				'Content-Type' : 'application/json',
				'Authentication-Token' : localStorage.getItem('Authentication-Token'),
			},
		});
		const result = await response.json();
		console.log(result)
		this.basics = result;
	}
}
</script>
<template>
	<div class = "container-fluid">
		<header>
			<SponsorNavbar/>
		</header>
		<h3>Welcome, sponsor!</h3>
		<div class = "row" id = "tiles">
			<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
				<RouterLink class="card bg-info text-white text-center mb-4" to = "/sponsor/campaign">
					<div class="card-body">
						<h5 class = "card-title">Campaign management</h5>
						<p>Click here to view, modify or delete current campaigns and to add new ones.</p>
					</div>
				</RouterLink>
			</div>
		</div>
		<div id = "stats">
			<div class = "row">
				<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
					<div class="card bg-info text-white text-center mb-4">
						<div class="card-body">
							<h5 class = "card-title">Sponsor name</h5>
							<p>{{ this.basics.basic[0] }}</p>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
					<div class="card bg-info text-white text-center mb-4">
						<div class="card-body">
							<h5 class = "card-title">Sponsor industry</h5>
							<p>{{ this.basics.basic[1] }}</p>
						</div>
					</div>
				</div>
			</div>
			<h3>Campaign details</h3>
				<p class = "lead text-center" v-if = "noCampaigns">There are no current campaigns.</p>
			<div v-else>
				<div class = "row" v-for="campaign in basics.campaigns">
					<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
						<div class="card bg-info text-white text-center mb-4">
							<div class="card-body">
								<h5 class = "card-title">Campaign name</h5>
								<p>{{ campaign[2] }}</p>
							</div>
						</div>
					</div>
					<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
						<div class="card bg-info text-white text-center mb-4">
							<div class="card-body">
								<h5 class = "card-title">Campaign niche</h5>
								<p>{{ campaign[3] }}</p>
							</div>
						</div>
					</div>
					<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
						<div class="card bg-info text-white text-center mb-4">
							<div class="card-body">
								<h5 class = "card-title">Campaign budget</h5>
								<p>{{ campaign[4] }}</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>