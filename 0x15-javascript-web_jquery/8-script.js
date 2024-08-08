$(document).ready(function() {
    // URL to fetch the movie titles
    let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    // Make the AJAX request
    $.getJSON(url, function(data) {
      // Loop through each movie in the response
      $.each(data.results, function(index, movie) {
        // Create a new <li> element with the movie title
        let listItem = $('<li></li>').text(movie.title);
        // Append the <li> element to UL#list_movies
        $('#list_movies').append(listItem);
      });
    });
  });