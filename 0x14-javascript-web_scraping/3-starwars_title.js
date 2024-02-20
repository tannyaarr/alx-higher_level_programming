const request = require('request'), movieId = process.argv[2];

if (!movieId) console.log("Usage: ./get_movie_title.js <movie_id>");
else request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, { json: true }, (err, res, body) => console.log(body.title));
