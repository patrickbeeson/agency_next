$(function() {

  // Hamburger menu icon
  $("#js-hamburger").click(function (e) {
    e.preventDefault();
    $(this).toggleClass("is-open");
  });

  // Project list parallax
  if ($(window).width()>980 && !Modernizr.touch) {
    
  }

  // Project videos
  $(".panel-video--full").click(function () {
    $(this).append('<div class="video"><iframe src="//player.vimeo.com/video/' + $(this).data('video-id') + '?title=0&amp;byline=0&amp;portrait=0&amp;wmode=opaque&amp;api=1&amp;&autoplay=1" width="1004" height="565" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div>');
  });

  // Project carousels
  $(".slides--full").slick({
    centerMode: true,
    centerPadding: '60px',
    arrows: false,
    focusOnSelect: true,
    slidesToShow: 1,
    responsive: [
    {
      breakpoint: 480,
      settings: {
        centerPadding: '30px'
      }
    }
  ]
  });

});