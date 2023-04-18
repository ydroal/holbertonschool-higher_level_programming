$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      data.results.forEach(function (movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});

