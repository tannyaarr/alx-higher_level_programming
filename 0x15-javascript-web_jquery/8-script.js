//script that fetches and lists the title for all movies by using the URL
$.get('https://swapi-api.alx-tools.com/api/films/?format=json'. function(data) {
	//Iterate through each movie and append its title to the list
	$.each(data.results, function(index, movie) {
		$('#list_movies').append('<li>' + movie.title + '<li>');
}));
