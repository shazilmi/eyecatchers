<script>
import router from '@/router';
import SponsorNavbar from '../SponsorNavbar.vue';

export default {
	components: {
		SponsorNavbar
	},
	data() {
		return {
			basics : {},
			id : 0,
			name : "",
			niche : "",
			description : "",
			start_date : "",
			end_date : "",
			budget : 0,
			goals : "",
			visibility : "",
		}
	},
	computed : {
		noCampaigns() {
			return this.basics.campaigns.length > 0 ? false : true;
		}
	},
	async created() {
		const response = await fetch("http://localhost:8000/backend/sponsor/sponsor_basic_stats", {
			method : 'GET',
			headers : {
				'Content-Type' : 'application/json',
				'Authentication-Token' : localStorage.getItem('Authentication-Token'),
			}
		});
		const result = await response.json();
		this.basics =  result;
	},
	methods : {
		createCampaign : async function() {
			const response = await fetch("http://localhost:8000/backend/sponsor/create_campaign", {
				method : "POST",
				headers : {
					'Content-Type' : 'application/json',
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
				},
				body : JSON.stringify({
					"name" : this.name,
					"sponsor" : localStorage.getItem('UID'),
					"niche" : this.niche,
					"description" : this.description,
					"start_date" : this.start_date,
					"end_date" : this.end_date,
					"budget" : this.budget,
					"goals" : this.goals,
					"visibility" : this.visibility,
				}),
			});
			const result = await response.json();
			if (result.message){
				alert(result.message);
			}
			else{
				alert("Campaign created successfully.");
				router.go(0);
			}
		},
		viewDetails : async function(id) {
			this.id = id;
			const response = await fetch("http://localhost:8000/backend/sponsor/campaign_details", {
				method : "POST",
				headers : {
					'Content-Type' : 'application/json',
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
				},
				body : JSON.stringify({"id" : id}),
			});
			const result = await response.json();
			if (result.message) {
				alert(result.message);
			}
			else{
				this.name = result[1];
				this.niche = result[2];
				this.description = result[3];
				this.sponsor = result[4];
				this.start_date = result[5];
				this.end_date = result[6];
				this.budget = result[7];
				this.visibility = result[8];
				this.goals = result[9];
			}
		},
		editCampaign : async function() {
			const response = await fetch("http://localhost:8000/backend/sponsor/update_campaign", {
				method : "POST",
				headers : {
					'Content-Type' : 'application/json',
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
				},
				body : JSON.stringify({
					"name" : this.name,
					"sponsor" : localStorage.getItem('UID'),
					"campaign" : this.id,
					"niche" : this.niche,
					"description" : this.description,
					"start_date" : this.start_date,
					"end_date" : this.end_date,
					"budget" : this.budget,
					"goals" : this.goals,
					"visibility" : this.visibility,
				}),
			});
			const result = await response.json();
			if (result.message){
				alert(result.message);
			}
			else{
				alert("Campaign modified successfully.");
				router.go(0);
			}
		},
		deleteCampaign: async function(id) {
			const response = await fetch("http://localhost:8000/backend/sponsor/delete_campaign", {
				method: "POST",
				headers : {
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
					'Content-Type' : 'application/json',
				},
				body : JSON.stringify({
					"campaign_id" : id,
					"sponsor_id" : localStorage.getItem('UID'),
				}),
			});
			const result = await response.json();
			if(result.message){
				alert(result.message);
			}
			else{
				alert("Campaign deleted successfully");
				router.go(0);
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
		<h3>Campaign details</h3>
		<p class = "lead text-center" v-if = "noCampaigns">There are no current campaigns.</p>
		<div v-else>
			<div class = "row" v-for="campaign in basics.campaigns">
				<div class="col">
							<p>Campaign name : {{ campaign[2] }}, Campaign niche : {{ campaign[3] }},
								Campaign budget : {{ campaign[4] }}
							</p>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" @click = "viewDetails(campaign[0])" data-bs-toggle = "modal" data-bs-target = "#viewDetails" width="32" height="32" fill="currentColor" class="bi bi-info-circle" viewBox="0 0 16 16">
					<path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
					<path d="m8.93 6.588-2.29.287-.082.38.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246-.275 0-.375-.193-.304-.533zM9 4.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0"/>
					</svg>
				</div>
				<div class = "modal" id = "viewDetails">
					<div class = "modal-dialog">
						<div class = "modal-content bg-dark">
							<div class = "modal-header">
								<h1 class = "modal-title text-bg-dark">Details of campaign "{{ this.name }}"</h1>
								<button class = "btn-close bg-danger" data-bs-dismiss = "modal"></button>
							</div>
							<div class = "modal-body text-bg-dark">
								<div class = "row">
									<p class = "lead">Campaign id: {{ this.id }}</p>
									<p class = "lead">Campaign name : {{ this.name }}</p>
									<p class = "lead">Campaign description : {{ this.description }}</p>
									<p class = "lead">Niche : {{ this.niche }}</p>
									<p class = "lead">Campaign budget: {{ this.budget }}</p>
									<p class = "lead">Campaign goals : {{ this.goals }}</p>
									<p class = "lead">Campaign start date : {{ this.start_date }}</p>
									<p class = "lead">Campaign end date : {{ this.end_date }}</p>
									<p class = "lead">Campaign visibility : {{ this.visibility }}</p>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" @click = "viewDetails(campaign[0])" data-bs-toggle = "modal" data-bs-target = "#editCampaign" width="32" height="32" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
					<path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
					<path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
					</svg>
				</div>
				<div class = "modal fade" id = "editCampaign">
					<div class = "modal-dialog">
						<div class = "modal-content bg-dark">
							<div class = "modal-header">
								<h1 class = "modal-title text-primary">
									Edit campaign
								</h1>
								<button class = "btn-close bg-danger" data-bs-dismiss = "modal"></button>
							</div>
							<div class = "modal-body text-bg-dark">
								<form >
									<div class = "row">
										<input type = "text" id = "name" class = "form-control mt-5" :placeholder = "this.name" v-model = "name" />
										<label for = "name" class = "form-label">Campaign name</label>
									</div>
									<div class = "row">
										<input type = "text" id = "niche" class = "form-control mt-5" :placeholder = "this.niche" v-model = "niche" />
										<label for = "niche" class = "form-label">Niche</label>
									</div>
									<div class = "row">
										<input type = "text" id = "description" class = "form-control mt-5" :placeholder = "this.description" v-model = "description" />
										<label for = "description" class = "form-label">Description</label>
									</div>
									<div class = "row">
										<input type = "date" id = "start_date" class = "form-control mt-5" v-model = "start_date"/>
										<label for = "start_date" class = "form-label">Campaign start date</label>
									</div>
									<div class = "row">
										<input type = "date" id = "end_date" class = "form-control mt-5" v-model = "end_date" />
										<label for = "end_date" class = "form-label">Campaign end date</label>
									</div>
									<div class = "row">
										<input type = "number" id = "budget" class = "form-control mt-5" :placeholder = "this.budget" v-model = "budget" />
										<label for = "budget" class = "form-label">Budget</label>
									</div>
									<div class = "row">
										<div class = "col">
											<input type = "radio" id = "public" class = "form-control mt-5" value = "public" v-model = "visibility" />
											<label for = "public" class = "form-label">Public</label>
										</div>
										<div class = "col">
											<input type = "radio" id = "private" class = "form-control mt-5" value = "private" v-model = "visibility" />
											<label for = "private" class = "form-label">Private</label>
										</div>
										<div class = "row">
										<input type = "text" id = "goals" class = "form-control mt-5" :placeholder = "this.goals" v-model = "goals" />
										<label for = "goals" class = "form-label">Campaign Goals</label>
									</div>
									</div>
								</form>
							</div>
							<div class = "modal-footer">
								<button class = "btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
								<button class = "btn btn-primary" @click="editCampaign">Edit campaign</button>
							</div>
						</div>
					</div>
				</div>
				<div class = "col">
					<svg xmlns="http://www.w3.org/2000/svg" @click = "deleteCampaign(campaign[0])" width="32" height="32" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16">
					<path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5"/>
					</svg>
				</div>
				<div class = "col">
					<RouterLink class = "btn btn-primary" :to = "'/sponsor/campaign/' + campaign[0]">Ad requests</RouterLink>
				</div>
			</div>
		</div>
		<button class = "btn btn-primary" data-bs-toggle = "modal" data-bs-target = "#createCampaign">Create campaign</button>

		<div class = "modal fade" id = "createCampaign">
			<div class = "modal-dialog">
				<div class = "modal-content bg-dark">
					<div class = "modal-header">
						<h1 class = "modal-title text-primary">
							Create campaign
						</h1>
						<button class = "btn-close bg-danger" data-bs-dismiss = "modal"></button>
					</div>
					<div class = "modal-body text-bg-dark">
						<form >
							<div class = "row">
								<input type = "text" id = "name" class = "form-control mt-5" placeholder = "Name" v-model = "name" />
								<label for = "name" class = "form-label">Campaign name</label>
							</div>
							<div class = "row">
								<input type = "text" id = "niche" class = "form-control mt-5" placeholder = "Niche" v-model = "niche" />
								<label for = "niche" class = "form-label">Niche</label>
							</div>
							<div class = "row">
								<input type = "text" id = "description" class = "form-control mt-5" placeholder = "Description" v-model = "description" />
								<label for = "description" class = "form-label">Description</label>
							</div>
							<div class = "row">
								<input type = "date" id = "start_date" class = "form-control mt-5" placeholder = "Start date" v-model = "start_date" />
								<label for = "start_date" class = "form-label">Campaign start date</label>
							</div>
							<div class = "row">
								<input type = "date" id = "end_date" class = "form-control mt-5" placeholder = "End date" v-model = "end_date" />
								<label for = "end_date" class = "form-label">Campaign end date</label>
							</div>
							<div class = "row">
								<input type = "number" id = "budget" class = "form-control mt-5" placeholder = "1000" v-model = "budget" />
								<label for = "budget" class = "form-label">Budget</label>
							</div>
							<div class = "row">
								<div class = "col">
									<input type = "radio" id = "public" class = "form-control mt-5" value = "public" v-model = "visibility" />
									<label for = "public" class = "form-label">Public</label>
								</div>
								<div class = "col">
									<input type = "radio" id = "private" class = "form-control mt-5" value = "private" v-model = "visibility" />
									<label for = "private" class = "form-label">Private</label>
								</div>
								<div class = "row">
								<input type = "text" id = "goals" class = "form-control mt-5" placeholder = "Goals" v-model = "goals" />
								<label for = "goals" class = "form-label">Campaign Goals</label>
							</div>
							</div>
						</form>
					</div>
					<div class = "modal-footer">
						<button class = "btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
						<button class = "btn btn-primary" @click="createCampaign">Create campaign</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>