<script>
export default {
	data(){
		return {
			isWaiting : false,
		}
	},
	methods: {
		async downloadCSV() {
			this.isWaiting = true;
			const res = await fetch('/backend/sponsor/download_csv');
			const data = await res.json();
			if(res.ok){
				const taskId = data["task-id"];
				const intv = setInterval(async ()=>{
					const csv_res = await fetch("/backend/sponsor/get_csv/$(taskId)");
					if(csv_res.ok){
						this.isWaiting = false;
						clearInterval(intv);
						window.location.href = "/backend/sponsor/get_csv/$(taskId)";
					}
				})
			}
		}
	}
}
</script>

<template>
	<div>
		<button @click = "downloadResource">Download Resource</button>
		<span v-if = "isWaiting">Waiting...</span>
	</div>
</template>