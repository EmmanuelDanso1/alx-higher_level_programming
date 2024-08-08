// DOMContentLoaded event to ensure that the DOM is fully loaded before trying to select and modify the
// <header> element. This is important since the script is included in the <head> tag
document.addEventListener("DOMContentLoaded", function(){
    let headerEL = document.querySelector("header");
    headerEL.style.color = "#FF0000";
})