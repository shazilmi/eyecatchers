<script>
import router from '@/router';
import InfluencerNavbar from '../InfluencerNavbar.vue';

export default {
	components : {
		InfluencerNavbar
	},
	data() {
		return {
			campaigns : [],
			search_criteria : "",
			niche : "",
			description : "",
			name : "",
			budget : "",
			search : false,
		}
	},
	computed : {
		noResults() {
			if(this.search){
				return this.campaigns.length > 0 ? false : true;
			}
			else{
				return false;
			}
		}
	},
	methods : {
		timeoutSearch : async function() {
			setTimeout(function () { this.searchCampaign() }.bind(this), 50);
		},
		searchCampaign : async function() {
			if(this.search_criteria == 'name'){
				const response = await fetch("http://localhost:8000/backend/influencer/search_campaign", {
					method : "POST",
					headers : {
						'Content-Type' : 'application/json',
						'Authentication-Token' : localStorage.getItem('Authentication-Token'),
					},
					body : JSON.stringify({
						"search_criteria" : this.search_criteria,
						"name" : this.name,
					})
				});
				const result = await response.json();
				if (result.message){
					alert(result.message);
				}
				else{
					this.campaigns = result;
				}}
			if(this.search_criteria == 'description'){
				const response = await fetch("http://localhost:8000/backend/influencer/search_campaign", {
					method : "POST",
					headers : {
						'Content-Type' : 'application/json',
						'Authentication-Token' : localStorage.getItem('Authentication-Token'),
					},
					body : JSON.stringify({
						"search_criteria" : this.search_criteria,
						"description" : this.description,
					})
				});
				const result = await response.json();
				if (result.message){
					alert(result.message);
				}
				else{
					this.campaigns = result;
				}}
			if(this.search_criteria == 'niche'){
				const response = await fetch("http://localhost:8000/backend/influencer/search_campaign", {
					method : "POST",
					headers : {
						'Content-Type' : 'application/json',
						'Authentication-Token' : localStorage.getItem('Authentication-Token'),
					},
					body : JSON.stringify({
						"search_criteria" : this.search_criteria,
						"niche" : this.niche,
					})
				});
				const result = await response.json();
				if (result.message){
					alert(result.message);
				}
				else{
					this.campaigns = result;
				}}
			if(this.search_criteria == 'budget'){
				const response = await fetch("http://localhost:8000/backend/influencer/search_campaign", {
					method : "POST",
					headers : {
						'Content-Type' : 'application/json',
						'Authentication-Token' : localStorage.getItem('Authentication-Token'),
					},
					body : JSON.stringify({
						"search_criteria" : this.search_criteria,
						"budget" : this.budget,
					})
				});
				const result = await response.json();
				if (result.message){
					alert(result.message);
				}
				else{
					this.campaigns = result;
				}}
		},
		expressInterest : async function(campaign_id) {
			const response = await fetch("http://localhost:8000/backend/influencer/express_interest", {
				method : "POST",
				headers : {
					'Content-Type' : 'application/json',
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
				},
				body : JSON.stringify({
					"campaign_id" : campaign_id,
					"influencer_id" : localStorage.getItem('UID'),
				})
			});
			const result = await response.json();
			if(result.message){
				alert(result.message);
			}
			else{
				alert("Registered interest successfully.");
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
		<h3>Search for public campaigns</h3>
		<form>
			<div class = "row">
				<p>Choose search criteria:</p>
				<div class = "col">
					<input type = "radio" @click = "search = true" id = "name" class = "form-check-input" value = "name" v-model = "search_criteria">Name of campaign</input>
				</div>
				<div class = "col">
					<input type = "radio" @click = "search = true" id = "description" class = "form-check-input" value = "description" v-model = "search_criteria">Description</input>
				</div>
				<div class = "col">
					<input type = "radio" @click = "search = true" id = "niche" class = "form-check-input" value = "niche" v-model = "search_criteria">Niche</input>
				</div>
				<div class = "col">
					<input type = "radio" @click = "search = true" id = "budget" class = "form-check-input" value = "budget" v-model = "search_criteria">Minimum budget</input>
				</div>
			</div>
			<div class = "row" @keydown="timeoutSearch" v-if = "search_criteria == 'description'">
				<input type = "text" id = "search" class = "form-control mt-2" v-model = "description" placeholder = "Description" />
			</div>
			<div class = "row" @keydown="timeoutSearch" v-if = "search_criteria == 'niche'">
				<input type = "text" id = "search" class = "form-control mt-2" v-model = "niche" placeholder = "Niche" />
			</div>
			<div class = "row" @keydown="timeoutSearch" v-if = "search_criteria == 'name'">
				<input type = "text" id = "search" class = "form-control mt-2" v-model = "name" placeholder = "Name of campaign" />
			</div>
			<div class = "row" @keydown="timeoutSearch" v-if = "search_criteria == 'budget'">
				<input type = "number" id = "search" class = "form-control mt-2" v-model = "budget" placeholder = "1000" />
			</div>
		</form>
		<h5 v-if = "search" class = "mt-5">Search results</h5>
		<p v-if = "noResults">No results were found.</p>
		<div class = "row" v-else v-for="campaign in campaigns">
			<div class = "col">
				{{ campaign[1] }}
			</div>
			<div class = "col">
				{{ campaign[2] }}
			</div>
			<div class = "col">
				{{ campaign[3] }}
			</div>
			<div class = "col">
				{{ campaign[4] }}
			</div>
			<div class = "col">
				{{ campaign[7] }}
			</div>
			<div class = "col">
				<button class = "btn btn-primary" @click = "expressInterest(campaign[0])">Express interest</button>
			</div>
		</div>
	</div>
</template>