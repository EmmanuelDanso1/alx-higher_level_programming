$(document).ready(function(){
    let url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
    $.getJSON(url, function(data){
        $("#hello").text(data.hello);
    });
});