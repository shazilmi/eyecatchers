<script>
import router from '@/router';
import SponsorNavbar from '../SponsorNavbar.vue';

export default {
	components : {
		SponsorNavbar
	},
	data() {
		return {
			influencers : [],
			search_criteria : "",
			niche : "",
			category : "",
			name : "",
			followers : "",
			search : false,
		}
	},
	computed : {
		noResults() {
			if(this.search){
				return this.influencers.length > 0 ? false : true;
			}
			else{
				return false;
			}
		}
	},
	methods : {
		timeoutSearch : async function() {
			setTimeout(function () { this.searchInfluencer() }.bind(this), 50);
		},
		searchInfluencer : async function() {
			if(this.search_criteria == 'name'){
				const response = await fetch("http://localhost:8000/backend/sponsor/search_influencer", {
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
					this.influencers = result;
				}}
			if(this.search_criteria == 'category'){
				const response = await fetch("http://localhost:8000/backend/sponsor/search_influencer", {
					method : "POST",
					headers : {
						'Content-Type' : 'application/json',
						'Authentication-Token' : localStorage.getItem('Authentication-Token'),
					},
					body : JSON.stringify({
						"search_criteria" : this.search_criteria,
						"category" : this.category,
					})
				});
				const result = await response.json();
				if (result.message){
					alert(result.message);
				}
				else{
					this.influencers = result;
				}}
			if(this.search_criteria == 'niche'){
				const response = await fetch("http://localhost:8000/backend/sponsor/search_influencer", {
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
					this.influencers = result;
				}}
			if(this.search_criteria == 'followers'){
				const response = await fetch("http://localhost:8000/backend/sponsor/search_influencer", {
					method : "POST",
					headers : {
						'Content-Type' : 'application/json',
						'Authentication-Token' : localStorage.getItem('Authentication-Token'),
					},
					body : JSON.stringify({
						"search_criteria" : this.search_criteria,
						"followers" : this.followers,
					})
				});
				const result = await response.json();
				if (result.message){
					alert(result.message);
				}
				else{
					this.influencers = result;
				}}
		}
	}
}
</script>

<template>
	<div class = "container-fluid">
		<header>
			<SponsorNavbar/>
		</header>
		<h3>Search for influencer</h3>
		<form>
			<div class = "row">
				<p>Choose search criteria:</p>
				<div class = "col">
					<input type = "radio" @click = "search = true" id = "name" class = "form-check-input" value = "name" v-model = "search_criteria">Name of Influencer</input>
				</div>
				<div class = "col">
					<input type = "radio" @click = "search = true" id = "category" class = "form-check-input" value = "category" v-model = "search_criteria">Category</input>
				</div>
				<div class = "col">
					<input type = "radio" @click = "search = true" id = "niche" class = "form-check-input" value = "niche" v-model = "search_criteria">Niche</input>
				</div>
				<div class = "col">
					<input type = "radio" @click = "search = true" id = "followers" class = "form-check-input" value = "followers" v-model = "search_criteria">Minimum number of followers</input>
				</div>
			</div>
			<div class = "row" @keydown="timeoutSearch" v-if = "search_criteria == 'category'">
				<input type = "text" id = "search" class = "form-control mt-2" v-model = "category" placeholder = "Category" />
			</div>
			<div class = "row" @keydown="timeoutSearch" v-if = "search_criteria == 'niche'">
				<input type = "text" id = "search" class = "form-control mt-2" v-model = "niche" placeholder = "Niche" />
			</div>
			<div class = "row" @keydown="timeoutSearch" v-if = "search_criteria == 'name'">
				<input type = "text" id = "search" class = "form-control mt-2" v-model = "name" placeholder = "Name of influencer" />
			</div>
			<div class = "row" @keydown="timeoutSearch" v-if = "search_criteria == 'followers'">
				<input type = "number" id = "search" class = "form-control mt-2" v-model = "followers" placeholder = "1000" />
			</div>
		</form>
		<h5 v-if = "search" class = "mt-5">Search results</h5>
		<p v-if = "noResults">No results were found.</p>
		<div class = "row" v-else v-for="influencer in influencers">
			<div class = "col">
				{{ influencer[1] }}
			</div>
			<div class = "col">
				{{ influencer[2] }}
			</div>
			<div class = "col">
				{{ influencer[3] }}
			</div>
			<div class = "col">
				{{ influencer[4] }}
			</div>
			<div class = "col">
				{{ influencer[5] }}
			</div>
			<div class = "col">
				{{ influencer[6] }}
			</div>
		</div>
	</div>
</template>