$(document).ready(function(){
    // add list
    $("#add_item").click(function(){
        $("UL.my_list").append("<li>Item</li>");
    });

    // remove from last item
    $("#remove_item").click(function(){
        $("UL.my_list li:last-child").remove();
    });

    // clear
    $("#clear_list").click(function(){
        $("UL.my_list").empty();
    });
});