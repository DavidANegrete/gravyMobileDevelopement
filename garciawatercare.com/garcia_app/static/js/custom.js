$(document).ready(function() {


    var userFeed = new Instafeed({
        get: 'user',
        userId: '508659639',
        limit: 12,
        resolution: 'standard_resolution',
        accessToken: '508659639.1677ed0.da37a230f7e8441292a390d1fee640ec',
        sortBy: 'most-recent',
        template: '<div class="col-lg-3 instaimg"><a href="{{image}}" title="{{caption}}" target="_blank"><img src="{{image}}" alt="{{caption}}" class="img-fluid"/></a></div>',
    });


    userFeed.run();

    
    // This will create a single gallery from all elements that have class "gallery-item"
    $('.gallery').magnificPopup({
        type: 'image',
        delegate: 'a',
        gallery: {
            enabled: true
        }
    });


});