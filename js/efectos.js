$(document).on("mouseenter", "li", function (){
    var title=$(this).attr("title");
    if (typeof title !== "undefined"){
        $(this).css("font-size", "12px");
    }
});