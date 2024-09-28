import { createApp, onMounted } from "vue";

const app = createApp({
	methods: {
		logoutUser: async function () {
			const response = await fetch("/api/logout", {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					'Authentication-Token': localStorage.getItem('Authentication-Token'),
				},
			});
			const result = await response.json();
			console.log(result);
			if (result.message) {
				alert("You have successfully been logged out. Redirecting you to home.");
				localStorage.removeItem('Authentication-Token');
				setTimeout(() => window.location.href = '/', 2000);
			}
			else {
				alert("Some error occurred. Redirecting you to home.");
				setTimeout(() => window.location.href = '/', 2000);
			}
		}
	}
})
app.mount('#logout')