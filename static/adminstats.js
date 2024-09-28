import { createApp, onMounted } from "vue";

const app = createApp({
	data() {
		return {
			users: 0,
			sponsors: 0,
			influencers: 0,
			unapproved: 0,
			campaigns: 0,
			ads: 0,
			flagged: 0,
			public: 0
		}
	},
	methods: {
		getStats: async function () {
			console.log("Something happened.");
			const response = await fetch("/api/admin/stats", {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					'Authentication-Token': localStorage.getItem('Authentication-Token'),
				},
			});
			const result = await response.json();
			console.log(result);
			this.users = result.users;
			this.sponsors = result.sponsors;
			this.influencers = result.influencers;
			this.ads = result.ads;
			this.campaigns = result.campaigns;
			this.public = result.public_campaigns;
			this.flagged = result.flagged;
			this.unapproved = result.unapproved;
			let statistics = document.querySelectorAll(".card");
			for (let i = 0; i < statistics.length; i++){
				if (statistics[i].classList.contains('invisible')){
					statistics[i].classList.remove('invisible');
				}
			}
			let buttons = document.getElementById('buttons');
			if (buttons.classList.contains('visible')){
				buttons.classList.remove('visible');
				buttons.classList.add('invisible');
			}
		}
	}
})
app.mount('#stats')