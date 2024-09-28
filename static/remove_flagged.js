import { createApp } from "vue";

const app = createApp({
	methods : {
		async removeUser(id){
			console.log("I was called.");
			const response = await fetch('/api/admin/remove_user', {
				method : 'POST',
				headers : {
					'Content-Type' : 'application/json',
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
				},
				body : JSON.stringify({"id" : id})
			});
			const result = await response.json();
			console.log(result);
			if (result.message){
				console.log(result.message);
				alert(result.message);
			}
			else{
				alert("User has been removed.");
				window.location.reload();
			}
		},
		async removeFlag(id){
			console.log("I was called.");
			const response = await fetch('/api/admin/remove_flag', {
				method : 'POST',
				headers : {
					'Content-Type' : 'application/json',
					'Authentication-Token' : localStorage.getItem('Authentication-Token'),
				},
				body : JSON.stringify({"id" : id})
			});
			const result = await response.json();
			console.log(result);
			if (result.message){
				console.log(result.message);
				alert(result.message);
			}
			else{
				alert("Flag has been removed.");
				window.location.reload();
			}
		}
	}
})
app.mount("#removed")