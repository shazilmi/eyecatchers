import { createApp } from "vue";

const app = createApp({
	data() {
		return {
			email : "",
			password : ""
		}
	},
	methods : {
		loginUser : async function() {
			const response = await fetch("/api/login", {
				method : 'POST',
				headers : {
					'Content-Type' : 'application/json'
				},
				body : JSON.stringify({"email" : this.email, "password" : this.password})
			});
			const result = await response.json();
			console.log(result);
			if (result.message){
				console.log(result.message);
				alert(result.message);
			}
			else{
				alert("Login successful. Redirecting you to your dashboard.");
				localStorage.setItem("Authentication-Token", result.token);
				if (result.role == 'sponsor'){
					return window.location.href = 'sponsor/dash';
				}
				else if (result.role == 'influencer'){
					return window.location.href = 'influencer/dash';
				}
				else{
					return window.location.href = 'admin/dash';
				}
			}
		}
	}
})
app.mount('#login')