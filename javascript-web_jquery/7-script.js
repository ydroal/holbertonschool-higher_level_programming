$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/people/5/?',
    success: function (data) {
      $('#character').text(data.name);
    }
  });
});
