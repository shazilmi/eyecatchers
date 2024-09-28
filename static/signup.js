import { createApp, ref } from "vue";

const app = createApp({
	data() {
		return {
			email: "",
			password1: "",
			name: "",
			password2: "",
			industry: "",
			category: "",
			niche: "",
			yt: 0,
			x: 0,
			ig: 0,
			choice : ""
		}
	},
	methods: {
		toggleSponsor: function () {
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
					const response = await fetch("/api/signup", {
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
						setTimeout(function(){
							window.location.href = "/";
						}, 2000);
					}
				}
				else if (this.choice == 'influencer'){
					const response = await fetch("/api/signup", {
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
						setTimeout(function(){
							window.location.href = "signin";
						}, 2000);
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
})
app.mount('#signup')
