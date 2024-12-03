<script>
import router from '@/router';
import CommonNavbar from './CommonNavbar.vue';

export default {
	components: {
		CommonNavbar
	},
	data() {
		return {
			email : "",
			password : "",
		}
	},
	methods: {
		loginUser : async function() {
			const response = await fetch("http://localhost:8000/backend/login", {
				method: 'POST',
				headers: {
					'Content-Type' : 'application/json',
				},
				body : JSON.stringify({"email" : this.email, "password" : this.password})
			});
			const result = await response.json();
			if (result.message){
				alert(result.message);
			}
			else{
				alert("Login successful. Redirecting you to your dashboard.");
				localStorage.setItem("Authentication-Token", result.token);
				localStorage.setItem("Role", result.role);
				localStorage.setItem("UID", result.id);
				if (result.role == "sponsor"){
					router.push('/sponsor/dash');
				}
				else if(result.role == "influencer"){
					router.push('/influencer/dash');
				}
				else {
					router.push('/admin/dash');
				}
			}
		},
	}
}
</script>

<template>
	<div class = "container-fluid" id = "login">
		<header>
			<CommonNavbar />
		</header>
		<form class = "position-absolute top-50 start-50 bg-dark-subtle translate-middle w-25">
			<div class = "row">
				<div class = "col"></div>
				<div class = "col-8">
					<div class = "form-floating">
						<input type = "email" id = "email" class = "form-control mt-5" placeholder = "apassword" v-model = "email" />
						<label for = "email" class = "form-label">Email</label>
					</div>
				</div>
				<div class = "col"></div>
			</div>
			<div class = "row">
				<div class = "col"></div>
				<div class = "col-8">
					<div class = "form-floating mt-3">
						<input type = "password" id = "password" class = "form-control" placeholder = "name@example.com" v-model = "password"/>
						<label for = "password" class = "form-label">Password</label>
					</div>
				</div>
				<div class = "col"></div>
			</div>
			<div class = "row">
				<div class = "col"></div>
				<div class = "col">
					<button type = "button" class = "btn btn-primary mb-4 mt-3" @click = "loginUser">Sign in</button>
				</div>
				<div class = "col"></div>
			</div>
		</form>
	</div>
</template>