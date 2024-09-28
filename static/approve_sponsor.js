import { createApp } from "vue";

const app = createApp({
	data() {
		return {
			id : 0,
		}
	},
	methods : {
		approveSponsor : async function() {
			const response = await fetch("/api/admin/approve_sponsor", {
				method : 'POST',
				headers : {
					'Content-Type' : 'application/json',
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
				},
				body : JSON.stringify({"id" : this.id})
			});
			const result = await response.json();
			console.log(result);
			if (result.message){
				console.log(result.message);
				alert(result.message);
			}
			else{
				alert("Sponsor has been approved. Redirecting you to dashboard.");
				return window.location.href = "dash";
			}
		}
	}
})
app.mount('#approve')