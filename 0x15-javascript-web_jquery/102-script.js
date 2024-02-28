// script that fetches and print how to say 'Hello' depending on the language
$(document).ready(function() {
	$('#btn_translate').on('click', function() {
		//Get the language code from the input
		var languageCode = $('#language_code').val();
		//fetch the translation using API
		$get.('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function(data) {
			$('#hello').text(data.hello);
		});
	});
});
