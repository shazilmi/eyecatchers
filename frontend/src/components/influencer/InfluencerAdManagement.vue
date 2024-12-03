<script>
import router from '@/router';
import InfluencerNavbar from '../InfluencerNavbar.vue';
import Shared from '../Shared.vue';

export default {
	components : {
		InfluencerNavbar
	},
	data() {
		return {
			ads_for_you : [],
			ads_by_you : [],
			accepted_ads : [],
			rejected_ads : [],
			influencer_id : localStorage.getItem('UID'),
			sponsor_name : '',
			requirements : '',
			payment_amount : '',
			id : 0,
		}
	},
	computed : {
		noAdsForYou() {
			return this.ads_for_you.length > 0 ? false : true;
		},
		noAdsByYou() {
			return this.ads_by_you.length > 0 ? false : true; 
		},
		noAccepted() {
			return this.accepted_ads.length > 0 ? false : true;
		},
		noRejected() {
			return this.rejected_ads.length > 0 ? false : true;
		},
	},
	async created() {
		this.acceptAd = Shared.acceptAd;
		this.rejectAd = Shared.rejectAd;
		const response = await fetch("http://localhost:8000/backend/influencer/get_pending_ads", {
			method : 'POST',
			headers : {
				'Content-Type' : 'application/json',
				'Authentication-Token' : localStorage.getItem('Authentication-Token'),
			},
			body : JSON.stringify({"influencer_id" : localStorage.getItem('UID')}),
		});
		const result = await response.json();
		if(result.message){
			alert(result.message);
		}
		else{
			this.ads_for_you = result.ads_for_you;
			this.ads_by_you = result.ads_by_you;
			this.accepted_ads = result.accepted_ads;
			this.rejected_ads = result.rejected_ads;
		}
	},
	methods : {
		setDetails : function(id, requirements, payment_amount, sponsor_name) {
			this.id = id;
			this.requirements = requirements;
			this.payment_amount = payment_amount;
			this.sponsor_name = sponsor_name;
		},
		modifyAd : async function() {
			const response = await fetch("http://localhost:8000/backend/influencer/modify_ad", {
				method : 'POST',
				headers : {
					'Content-Type' : 'application/json',
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
				},
				body : JSON.stringify({
					"ad_id" : this.id,
					"requirements" : this.requirements,
					"payment_amount" : this.payment_amount,
				})
			});
			const result = await response.json();
			if(result.message){
				alert(result.message);
			}
			else{
				alert("Ad request has been successfully negotiated.");
				router.go(0);
			}
		}
	}
}
</script>

<template>
	<div class = "container-fluid">
		<header>
			<InfluencerNavbar/>
		</header>
		<h3>Ad request management for influencer : {{ this.influencer_id }}</h3>
		<h5>Pending ad requests for you</h5>
		<div v-if = "noAdsForYou">
			<p>No ad requests for which action is to be taken.</p>
		</div>
		<div v-else>
			<div class = "row" v-for = "ad in ads_for_you">
				<div class="col">
					<p>Ad id : {{ ad[0] }}, Requirements : {{ ad[2] }},
						Payment amount : {{ ad[3] }}, Sponsor name : {{ ad[8] }}
					</p>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" @click = "setDetails(ad[0], ad[2], ad[3], ad[8])" data-bs-toggle = "modal" data-bs-target = "#modifyAd" width="32" height="32" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
					<path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
					<path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
					</svg>
				</div>
				<div class = "modal fade" id = "modifyAd">
					<div class = "modal-dialog">
						<div class = "modal-content bg-dark">
							<div class = "modal-header">
								<h1 class = "modal-title text-primary">
									Modify ad request
								</h1>
								<button class = "btn-close bg-danger" data-bs-dismiss = "modal"></button>
							</div>
							<div class = "modal-body text-bg-dark">
								<div class = "row">
									<p>Negotiating request from sponsor : {{ this.sponsor_name }}</p>
								</div>
								<form >
									<div class = "row">
										<input type = "text" id = "requirements" class = "form-control mt-5" :placeholder = "this.requirements" v-model = "requirements" />
										<label for = "requirements" class = "form-label">Requirements</label>
									</div>
									<div class = "row">
										<input type = "number" id = "payment" class = "form-control mt-5" :placeholder = "this.payment_amount" v-model = "payment_amount" />
										<label for = "payment" class = "form-label">Payment amount</label>
									</div>
								</form>
							</div>
							<div class = "modal-footer">
								<button class = "btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
								<button class = "btn btn-primary" @click="modifyAd">Make negotiation</button>
							</div>
						</div>
					</div>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" @click = "acceptAd(ad[0], ad[7], this.influencer_id)" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
					<path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
					<path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
					</svg>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" @click = "rejectAd(ad[0], ad[7], this.influencer_id)" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
					<path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
					<path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/>
					</svg>
				</div>
			</div>
		</div>
		<h5>Ad request modifications made by you</h5>
		<div v-if = "noAdsByYou">
			<p>No ad request modifications have been suggested by you.</p>
		</div>
		<div v-else>
			<div class = "row" v-for = "ad in ads_by_you">
				<div class = "col">
					<p>Ad id : {{ ad[0] }}, Requirements : {{ ad[2] }},
						Payment amount : {{ ad[3] }}, Sponsor name : {{ ad[8] }}
					</p>
				</div>
			</div>
		</div>

		<h5>Accepted ad requests</h5>
		<div v-if="noAccepted">
			<p>No accepted ad requests.</p>
		</div>
		<div v-else>
			<div class = "row" v-for="ad in accepted_ads">
				<div class="col bg-primary-subtle">
							<p>Ad id : {{ ad[0] }}, Requirements : {{ ad[2] }},
								Payment amount : {{ ad[3] }}, Influencer : {{ ad[5] }}
							</p>
				</div>
			</div>
		</div>

		<h5>Rejected ad requests</h5>
		<div v-if="noRejected">
			<p>No rejected ad requests.</p>
		</div>
		<div v-else>
			<div class = "row" v-for="ad in rejected_ads">
				<div class="col bg-primary-subtle">
							<p>Ad id : {{ ad[0] }}, Requirements : {{ ad[2] }},
								Payment amount : {{ ad[3] }}, Influencer : {{ ad[5] }}
							</p>
				</div>
			</div>
		</div>
	</div>
</template>