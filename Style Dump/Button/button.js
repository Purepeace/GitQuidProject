$(document).ready(function() {

	$('.btn').delay(400).queue(function(next) {
		$(this).addClass('hover').delay(1800).queue(function(next) {
			$(this).removeClass('hover');
		});
		next();
	});
});