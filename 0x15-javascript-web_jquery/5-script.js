$(document).ready(function(){
    $("#add_item").click(function(){
        let add_newList = $("<li>Item</li>");
        $("UL.my_list").append(add_newList);
    });
});