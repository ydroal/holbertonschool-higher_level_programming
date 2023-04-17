#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movies = JSON.parse(body);
  const moviesList = movies.results;
  const filteredList = moviesList.filter(movie => movie.characters.some(url => url.endsWith('/18/')));
  console.log(filteredList.length);
});
