<script>
import CommonNavbar from './CommonNavbar.vue'

export default {
	components: {
		CommonNavbar
	}
}
</script>

<template>
	<div class = "container-fluid">
		<header>
			<CommonNavbar />
		</header>
		<h3 class = "text-center position-relative start-50 mt-4 bg-dark-subtle text-success">
			Welcome to Eyecatchers!
		</h3>
		<p class = "lead position-relative start-50 pt-4 text-center bg-primary-subtle">
			This is an app that connects sponsors who want to advertise their products in the best way possible with the influencers who have the reach and the nous to do just that.
		</p>
	</div>
</template>