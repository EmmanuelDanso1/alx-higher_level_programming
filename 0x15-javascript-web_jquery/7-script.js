$(document).ready(function(){
    let url_character_fetch = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
    // ajax to fetch data
    $.getJSON(url_character_fetch, function(data){
        $("#character").text(data.name);
    });
});