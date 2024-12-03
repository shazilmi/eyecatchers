<script>
import CommonNavbar from './CommonNavbar.vue';
import router from '@/router';

export default {
	components: {
		CommonNavbar
	},
	data() {
		return {
			email : "",
			password1: "",
			name: "",
			password2: "",
			industry: "",
			category: "",
			niche: "",
			yt: 0,
			x: 0,
			ig: 0,
			choice: "",
		}
	},
	methods : {
		toggleSponsor : function() {
			let sponsors = document.querySelectorAll(".sponsor");
			let influencers = document.querySelectorAll(".influencer");
			for (let i = 0; i < sponsors.length; i++){
				if (sponsors[i].classList.contains('invisible')){
					sponsors[i].classList.remove('invisible');
					sponsors[i].classList.add('visible');
				}
			}
			for (let j = 0; j < influencers.length; j++){
				if (influencers[j].classList.contains('visible')){
					influencers[j].classList.remove('visible');
					influencers[j].classList.add("invisible");
				}
			}
			this.choice = 'sponsor';
		},
		toggleInfluencer: function () {
			let sponsors = document.querySelectorAll(".sponsor");
			let influencers = document.querySelectorAll(".influencer");
			for (let i = 0; i < sponsors.length; i++){
				if (sponsors[i].classList.contains('visible')){
					sponsors[i].classList.remove('visible');
					sponsors[i].classList.add('invisible');
				}
			}
			for (let j = 0; j < influencers.length; j++){
				if (influencers[j].classList.contains('invisible')){
					influencers[j].classList.remove('invisible');
					influencers[j].classList.add("visible");
				}
			}
		this.choice = "influencer";
		},
		signupUser: async function () {
			if (this.password1 == this.password2){
				if (this.choice == 'sponsor'){
					const response = await fetch("http://localhost:8000/backend/signup", {
						method : 'POST',
						headers : {
							'Content-Type' : 'application/json',
						},
						body : JSON.stringify({
							"email" : this.email,
							"password" : this.password1,
							"name" : this.name,
							"industry" : this.industry,
							"choice" : this.choice,
						})
					});
					const result = await response.json();
					this.email =  "";
					this.password1 = "";
					this.name = "";
					this.password2 = "";
					this.industry = "";
					this.category = "";
					this.niche = "";
					this.yt = 0;
					this.x = 0;
					this.ig = 0;
					console.log(result);
					if (result.message){
						console.log(result.message);
						alert(result.message);
					}
					else{
						alert("Account has been created. You can log in after admin has approved your account. Automatically redirecting to home.");
						router.push('/');
					}
				}
				else if (this.choice == 'influencer'){
					const response = await fetch("http://localhost:8000/backend/signup", {
						method : 'POST',
						headers : {
							'Content-Type' : 'application/json',
						},
						body : JSON.stringify({
							"email" : this.email,
							"password" : this.password1,
							"name" : this.name,
							"category" : this.category,
							"choice" : this.choice,
							"niche" : this.niche,
							"x" : this.x,
							"ig" : this.ig,
							"yt" : this.yt
						})
					});
					const result = await response.json();
					this.email =  "";
					this.password1 = "";
					this.name = "";
					this.password2 = "";
					this.industry = "";
					this.category = "";
					this.niche = "";
					this.yt = 0;
					this.x = 0;
					this.ig = 0;
					console.log(result);
					if (result.message){
						console.log(result.message);
						alert(result.message);
					}
					else{
						alert("Account has been created. You may log in to your account. Automatically redirecting to login page.");
						router.push('/signin');
					}
				}
				else{
					alert("Error. You must choose to register as either sponsor or influencer.");
				}
			}
			else{
				alert("Error. Given passwords do not match.");
			}
		},
	},
}
</script>

<template>
	<div class = "container-fluid" id = "signup">
		<header>
			<CommonNavbar />
		</header>
		<div class = "row">
			<div class = "col 6">
				<h3 class = "display-5 text-centre">Register on Eyecatchers</h3>
			</div>
		</div>
		<div class = "row">
			<div class = "col"></div>
			<div class = "col">
				<p class = "lead text-centre">Choose whether to register as a sponsor or as an influencer</p>
			</div>
			<div class = "col"></div>
		</div>
		<div class="btn-group start-50 translate-middle" role="group"
		aria-label="Basic radio toggle button group">
			<div class="row">
				<div class="col"></div>
				<div class="col">
					<input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off"
						v-on:click="toggleSponsor">
					<label class="btn btn-outline-primary" for="btnradio1">Sponsor</label>
				</div>
				<div class="col"></div>
			</div>
			<div class="row">
				<div class="col"></div>
				<div class="col">
					<input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off"
						v-on:click="toggleInfluencer">
					<label class="btn btn-outline-primary" for="btnradio2">Influencer</label>
				</div>
				<div class="col"></div>
			</div>
		</div>
		<form name="details" class="position-relative">
			<div class="row">
				<div class="col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible sponsor">
						<input type="email" class="form-control" id="email" v-model="email" />
						<label for="email" class="form-label">Email</label>
					</div>
				</div>
				<div class="col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible influencer">
						<input type="email" class="form-control" id="email2" v-model="email" />
						<label for="email2" class="form-label">Email</label>
					</div>
				</div>
				<div class="col"></div>
			</div>
			<div class="row">
				<div class="col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible sponsor">
						<input type="password" class="form-control" id="password1" v-model="password1" />
						<label for="password1" class="form-label">Password</label>
					</div>
				</div>
				<div class="col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible influencer">
						<input type="password" class="form-control" id="password11" v-model="password1" />
						<label for="password11" class="form-label">Password</label>
					</div>
				</div>
				<div class="col"></div>
			</div>
			<div class="row">
				<div class="col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible sponsor">
						<input type="password" class="form-control" id="password2" v-model="password2" />
						<label for="password2" class="form-label">Confirm password</label>
					</div>
				</div>
				<div class="col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible influencer">
						<input type="password" class="form-control" id="password21" v-model="password2" />
						<label for="password21" class="form-label">Confirm password</label>
					</div>
				</div>
				<div class="col"></div>
			</div>
			<div class="row">
				<div class="col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible sponsor">
						<input type="text" class="form-control" id="name" v-model="name" />
						<label for="name" class="form-label">Name</label>
					</div>
				</div>
				<div class="col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible influencer">
						<input type="text" class="form-control" id="name1" v-model="name" />
						<label for="name1" class="form-label">Name</label>
					</div>
				</div>
				<div class="col"></div>
			</div>
			<div class="row">
				<div class="col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible sponsor">
						<input type="text" class="form-control" id="industry" v-model="industry" />
						<label for="industry" class="form-label">Industry</label>
					</div>
				</div>
				<div class="col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible influencer">
						<input type="text" class="form-control" id="category" v-model="category" />
						<label for="category" class="form-label">Category</label>
					</div>
				</div>
				<div class="col"></div>
			</div>
			<div class="row">
				<div class="col"></div>
				<div class="col">
					<button type="button" class="btn btn-primary position-relative translate-middle start-50 invisible sponsor"
						v-on:click="signupUser" name="button">Sign up</button>
				</div>
				<div class="col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible influencer">
						<input type="text" class="form-control" id="niche" v-model="niche" />
						<label for="niche" class="form-label">Niche</label>
					</div>
				</div>
				<div class = "col"></div>
			</div>
			<div class="row">
				<div class="col"></div>
				<div class = "col"></div>
				<div class = "col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible influencer">
						<input type="number" class="form-control" id="yt" v-model="yt" />
						<label for="yt" class="form-label">YouTube Followers</label>
					</div>
				</div>
				<div class="col"></div>
			</div>
			<div class="row">
				<div class="col"></div>
				<div class = "col"></div>
				<div class = "col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible influencer">
						<input type="number" class="form-control" id="x" v-model="x" />
						<label for="x" class="form-label">X Followers</label>
					</div>
				</div>
				<div class="col"></div>
			</div>
			<div class="row">
				<div class="col"></div>
				<div class = "col"></div>
				<div class = "col"></div>
				<div class="col">
					<div class="form-outline mb-4 invisible influencer">
						<input type="number" class="form-control" id="ig" v-model="ig" />
						<label for="ig" class="form-label">Instagram Followers</label>
					</div>
				</div>
				<div class="col"></div>
			</div>
		</form>
		<div class="row">
			<div class="col"></div>
			<div class = "col"></div>
			<div class = "col"></div>
			<div class="col">
				<button type="button" class="btn btn-primary position-relative translate-middle start-50 invisible influencer"
					v-on:click="signupUser" name="button">Sign up</button>
			</div>
			<div class="col"></div>
		</div>
	</div>
	</template>