// script that fetches the character name from the URL
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  // Extract the character name from the fecthed data
  const characterName = data.name;
  // Display the character name in the HTML tag with ID 'character'
  $('#character').text(characterName);
});
