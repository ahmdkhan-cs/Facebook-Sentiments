// Hero text animation
$('document').ready(function(){
    var text = ["Know what people are saying about your products.", "Generate Graphs and PDF reports.", "Fetch your customers reviews."];
    var counter = 0;
    setInterval(function() {
        $("#js--hero-text").fadeOut(function() {
            $(this).text(text[counter])
          }).fadeIn();
        
        counter++;
        if (counter >= text.length) {
            counter = 0;
        }
    }, 5000);


    $('.js--scroll-to-features').click(function(){
        $('html, body').animate({scrollTop: $('#js--features').offset().top - 100}, 1000);
    });


    $('#js--features').waypoint(function(direction){
        $('#js--features').addClass('animated fadeIn');
    },{
        offset: '30%'
    });

});

