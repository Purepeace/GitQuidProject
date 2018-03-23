// $(document).ready(function () {
//     $("#about-btn").click(function (event) {
//         $().button('toggle')
//         // alert("You clicked the button using JQuery!");
//     });
//     $("#aaaa").click(function (event) {
//         // $("#Z>A").button('toggle')
//         $().button('toggle')
//         // alert("You clicked the button using JQuery!");
//     });
// });

$(document).ready(function() {
       $("#test").submit(function(event){
            $.ajax({
                 type:"POST",
                 url:"/edit_favorites/",
                 data: {
                        'video': $('#test').val() // from form
                        },
                 success: function(){
                     $('#message').html("<h2>Contact Form Submitted!</h2>")
                 }
            });
            return false; //<---- move it here
       });

});