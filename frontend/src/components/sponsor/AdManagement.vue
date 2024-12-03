<script>
import router from '@/router';
import SponsorNavbar from '../SponsorNavbar.vue';
import Shared from '../Shared.vue';

export default {
	components : {
		SponsorNavbar
	}, 
	data() {
		return {
			campaign : this.$route.params.id,
			ads : [],
			influencers : [],
			ads_by_influencers : [],
			influencer_id : 0,
			sponsor_id : 0,
			requirements : "",
			payment_amount : 0,
			id : 0,
			interested : [],
			accepted_ads : [],
			rejected_ads : [],
		}
	},
	computed : {
		noAds() {
			return this.ads.length > 0 ? false : true;
		},
		noInterest() {
			return this.interested.length > 0 ? false : true;
		},
		noMods() {
			return this.ads_by_influencers.length > 0 ? false : true;
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
		this.sponsor_id = localStorage.getItem('UID');
		const response = await fetch("http://localhost:8000/backend/sponsor/ad_details", {
			method : 'POST',
			headers : {
				'Content-Type' : 'application/json',
				'Authentication-Token' : localStorage.getItem('Authentication-Token'),
			},
			body : JSON.stringify({"campaign" : this.campaign}),
		});
		const result = await response.json();
		if(result.message){
			alert(result.message);
		}
		else{
			this.ads = result.ads;
			this.influencers = result.influencers;
			this.ads_by_influencers = result.ads_by_influencers;
			this.interested = result.interested;
			this.accepted_ads = result.accepted_ads;
			this.rejected_ads = result.rejected_ads;
		}
	},
	methods : {
		createAd : async function() {
			const response = await fetch("http://localhost:8000/backend/sponsor/create_ad_request", {
				method : "POST",
				headers : {
					'Content-Type' : 'application/json',
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
				},
				body : JSON.stringify({
					"campaign" : this.campaign,
					"sponsor" : localStorage.getItem('UID'),
					"influencer_id" : this.influencer_id,
					"requirements" : this.requirements,
					"payment_amount" : this.payment_amount,
				}),
			});
			const result = await response.json();
			if (result.message){
				alert(result.message);
			}
			else{
				alert("Ad created successfully.");
				router.go(0);
			}
		},
		editAd : async function() {
			const response = await fetch("http://localhost:8000/backend/sponsor/update_ad_request", {
				method : "POST",
				headers : {
					'Content-Type' : 'application/json',
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
				},
				body : JSON.stringify({
					"ad_id" : this.id,
					"sponsor" : localStorage.getItem('UID'),
					"influencer_id" : this.influencer_id,
					"requirements" : this.requirements,
					"payment_amount" : this.payment_amount,
				}),
			});
			const result = await response.json();
			if (result.message){
				alert(result.message);
			}
			else{
				alert("Ad modified successfully.");
				router.go(0);
			}
		},
		deleteAd: async function(id) {
			const response = await fetch("http://localhost:8000/backend/sponsor/delete_ad_request", {
				method: "POST",
				headers : {
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
					'Content-Type' : 'application/json',
				},
				body : JSON.stringify({
					"ad_id" : id,
					"sponsor" : localStorage.getItem('UID'),
				}),
			});
			const result = await response.json();
			if(result.message){
				alert(result.message);
			}
			else{
				alert("Ad request deleted successfully");
				router.go(0);
			}
		},
		setDetails: function(id) {
			this.id = id;
			for (let ad of this.ads){
				if(ad[0] == id){
					this.influencer_id = ad[5];
					this.requirements = ad[2];
					this.payment_amount = ad[3];
				}
			}
		},
		setDetailsMods: function(id) {
			this.id = id;
			for (let ad of this.ads_by_influencers){
				if(ad[0] == id){
					this.influencer_id = ad[5];
					this.requirements = ad[2];
					this.payment_amount = ad[3];
				}
			}
		},
		setDetailsRejected: function(id) {
			this.id = id;
			for (let ad of this.rejected_ads){
				if(ad[0] == id){
					this.influencer_id = ad[5];
					this.requirements = ad[2];
					this.payment_amount = ad[3];
				}
			}
		}
	}
}
</script>

<template>
	<div class = "container-fluid">
		<header>
			<SponsorNavbar/>
		</header>
		<h3>Ad request management for campaign id : {{ this.campaign }}</h3>
		<h5>Ad requests pending approval from influencers</h5>
		<div v-if="noAds">
			<p>No current pending ad requests.</p>
		</div>
		<div v-else>
			<div class = "row" v-for="ad in ads">
				<div class="col bg-primary-subtle">
							<p>Ad id : {{ ad[0] }}, Requirements : {{ ad[2] }},
								Payment amount : {{ ad[3] }}, Influencer : {{ ad[5] }}
							</p>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" @click = "setDetails(ad[0])" data-bs-toggle = "modal" data-bs-target = "#editAd" width="32" height="32" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
					<path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
					<path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
					</svg>
				</div>
				<div class = "modal fade" id = "editAd">
					<div class = "modal-dialog">
						<div class = "modal-content bg-dark">
							<div class = "modal-header">
								<h1 class = "modal-title text-primary">
									Edit ad request
								</h1>
								<button class = "btn-close bg-danger" data-bs-dismiss = "modal"></button>
							</div>
							<div class = "modal-body text-bg-dark">
								<form >
									<div class = "row">
										<input type = "text" id = "requirements" class = "form-control" :placeholder = "this.requirements" v-model = "requirements" />
										<label for = "requirements" class = "form-label">Requirements</label>
									</div>
									<div class = "row">
										<input type = "number" id = "payment_amount" class = "form-control" :placeholder = "this.payment_amount" v-model = "payment_amount" />
										<label for = "payment_amount" class = "form-label">Payment Amount</label>
									</div>
									<div class = "row">
										<label for = "influencer">Choose the influencer:</label>
										<select name = "influencer_id" v-model = "influencer_id" id = "influencer">
											<option v-for = "influencer in influencers" :value = "influencer[0]">{{ influencer[0] }}, {{ influencer[1] }}</option>
										</select>
									</div>
								</form>
							</div>
							<div class = "modal-footer">
								<button class = "btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
								<button class = "btn btn-primary" @click="editAd">Edit ad request</button>
							</div>
						</div>
					</div>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" @click = "deleteAd(ad[0])" width="32" height="32" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16">
					<path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5"/>
					</svg>
				</div>
			</div>
		</div>

		<h5>Ad request pending negotiations</h5>
		<div v-if="noMods">
			<p>No current pending ad requests.</p>
		</div>
		<div v-else>
			<div class = "row" v-for="ad in ads_by_influencers">
				<div class="col bg-primary-subtle">
							<p>Ad id : {{ ad[0] }}, Requirements : {{ ad[2] }},
								Payment amount : {{ ad[3] }}, Influencer : {{ ad[5] }}
							</p>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" @click = "setDetailsMods(ad[0])" data-bs-toggle = "modal" data-bs-target = "#editAd" width="32" height="32" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
					<path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
					<path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
					</svg>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" @click = "acceptAd(ad[0], this.sponsor_id, ad[5])" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
					<path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
					<path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
					</svg>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" @click = "rejectAd(ad[0], this.sponsor_id, ad[5])" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
					<path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
					<path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/>
					</svg>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" @click = "deleteAd(ad[0])" width="32" height="32" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16">
					<path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5"/>
					</svg>
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
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" @click = "deleteAd(ad[0])" width="32" height="32" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16">
					<path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5"/>
					</svg>
				</div>
			</div>
		</div>

		<h5>Influencers who have expressed interest</h5>
		<div v-if = "noInterest">
			<p>No influencers have expressed interest in the campaign yet.</p>
		</div>
		<div v-else>
			<div class = "row" v-for = "interest in interested">
				<p>The influencer named "{{ interest[2] }}" has expressed interest in the campaign.</p>
			</div>
		</div>

		<button class = "btn btn-primary" data-bs-toggle = "modal" data-bs-target = "#createAd">Create ad</button>

		<div class = "modal fade" id = "createAd">
			<div class = "modal-dialog">
				<div class = "modal-content bg-dark">
					<div class = "modal-header">
						<h1 class = "modal-title text-primary">
							Create ad request
						</h1>
						<button class = "btn-close bg-danger" data-bs-dismiss = "modal"></button>
					</div>
					<div class = "modal-body text-bg-dark">
						<form >
							<div class = "row">
								<input type = "text" id = "requirements" class = "form-control mt-5" placeholder = "Requirements" v-model = "requirements" />
								<label for = "requirements" class = "form-label">Ad request requirements</label>
							</div>
							<div class = "row">
								<input type = "number" id = "payment_amount" class = "form-control mt-5" placeholder = "1000" v-model = "payment_amount" />
								<label for = "payment_amount" class = "form-label">Payment amount</label>
							</div>
							<div class = "row">
								<label for = "influencer">Choose the influencer:</label>
								<select name = "influencer_id" v-model = "influencer_id" id = "influencer">
									<option v-for = "influencer in influencers" :value = "influencer[0]">{{ influencer[0] }}, {{ influencer[1] }}</option>
								</select>
							</div>
						</form>
					</div>
					<div class = "modal-footer">
						<button class = "btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
						<button class = "btn btn-primary" @click="createAd">Create ad request</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>