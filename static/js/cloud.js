$(function(){
    var settings = {
        "size" : {
            "grid" : 16
        },
        "options" : {
            "color" : "random-dark",
            "printMultiplier" : 3
        },
        "font" : "Futura, Helvetica, sans-serif",
        "shape" : "square"
    }
    $( "#word_cloud" ).awesomeCloud( settings );
})