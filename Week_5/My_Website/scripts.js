$(document).ready(function(){
    $(".letter").hover(ome, oml);
    $
})
//     alert('hi');
// }

// $(document).read(function(){
//     $("T_text").slideToggle();
//     });
// });


function ome(){
    $(this).css("background-color", "gainsboro");
}

function oml(){
    $(this).css("background-color", "transparent");
}

$('h1').hover(function(){
    $('div.letter').text($(this).children())
});

