<script>
import router from '@/router';
import InfluencerNavbar from '../InfluencerNavbar.vue';

export default {
	components : {
		InfluencerNavbar
	}
}
</script>

<template>
	<div class = "container-fluid">
		<header>
			<InfluencerNavbar/>
		</header>
		<h3>Welcome Influencer!</h3>
		<div class = "row" id = "tiles">
			<div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
				<RouterLink class="card bg-info text-white text-center mb-4" to = "/influencer/ad_management">
					<div class="card-body">
						<h5 class = "card-title">Ad request management</h5>
						<p>Click here to manage pending ad requests or to create new ones.</p>
					</div>
				</RouterLink>
			</div>
		</div>
	</div>
</template>