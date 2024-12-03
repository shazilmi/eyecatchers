<script>
import router from '@/router';

export default {
	logoutUser: async function() {
		const response = await fetch("http://localhost:8000/backend/logout", {
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
			localStorage.removeItem('Role');
			localStorage.removeItem('UID');
			router.push('/');
		}
		else {
			alert("Some error occurred. Redirecting you to home.");
			router.push('/');
		}
	},

	acceptAd: async function(ad_id, sponsor_id, influencer_id) {
		const response = await fetch("http://localhost:8000/backend/accept_ad", {
			method : 'POST',
			headers : {
				'Content-Type' : 'application/json',
				'Authentication-Token' : localStorage.getItem('Authentication-Token'),
			},
			body : JSON.stringify({
				"ad_id" : ad_id,
				"influencer_id" : influencer_id,
				"sponsor_id" : sponsor_id,
			})
		});
		const result = await response.json();
		if(result.message){
			alert(result.message);
		}
		else{
			alert("Ad request was accepted successfully.");
			router.go(0);
		}
	},

	rejectAd: async function(ad_id, sponsor_id, influencer_id) {
		const response = await fetch("http://localhost:8000/backend/reject_ad", {
			method : 'POST',
			headers : {
				'Content-Type' : 'application/json',
				'Authentication-Token' : localStorage.getItem('Authentication-Token'),
			},
			body : JSON.stringify({
				"ad_id" : ad_id,
				"influencer_id" : influencer_id,
				"sponsor_id" : sponsor_id,
			})
		});
		const result = await response.json();
		if(result.message){
			alert(result.message);
		}
		else{
			alert("Ad request was rejected successfully.");
			router.go(0);
		}
	}
}
</script>