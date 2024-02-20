#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
    console.log("Usage: ./count_wedge_movies.js <api_url>");
} else {
    const characterId = 18;

    request.get(apiUrl, { json: true }, (error, response, body) => {
        if (!error && response.statusCode === 200) {
            const wedgeMovies = body.results.filter(movie => movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
            console.log(wedgeMovies.length);
        }
    });
}
