/*  ---------------------------------------------------
    Template Name: Sona
    Description: Sona Hotel Html Template
    Author: Colorlib
    Author URI: https://colorlib.com
    Version: 1.0
    Created: Colorlib
---------------------------------------------------------  */

'use strict';

(function ($) {
    let en_path = true
    if(window.location.pathname.includes("/en/")){
        en_path = false
    }

   
    $('a.eng').on('click', function(e) {
        $('body').removeClass('rtl');
        $('body').addClass('ltr');
        //$('.owl-carousel').owlCarousel({ rtl:false });
       
      });

      $('a.arb').on('click', function(e) {
        $('body').removeClass('ltr');
        $('body').addClass('rtl');
        //$('.owl-carousel').owlCarousel({ rtl:true });
       
      });

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    //Offcanvas Menu
    $(".canvas-open").on('click', function () {
        $(".offcanvas-menu-wrapper").addClass("show-offcanvas-menu-wrapper");
        $(".offcanvas-menu-overlay").addClass("active");
    });

    $(".canvas-close, .offcanvas-menu-overlay").on('click', function () {
        $(".offcanvas-menu-wrapper").removeClass("show-offcanvas-menu-wrapper");
        $(".offcanvas-menu-overlay").removeClass("active");
    });

    // Search model
    $('.search-switch').on('click', function () {
        $('.search-model').fadeIn(400);
    });

    $('.search-close-switch').on('click', function () {
        $('.search-model').fadeOut(400, function () {
            $('#search-input').val('');
        });
    });

    /*------------------
		Navigation
	--------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*------------------
        Hero Slider
    --------------------*/
   $(".hero-slider").owlCarousel({
        loop: true,
        rtl: en_path,
        margin: 0,
        items: 1,
        dots: true,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        mouseDrag: true
    });
    

    /*------------------------
		Testimonial Slider
    ----------------------- */
    $(".testimonial-slider").owlCarousel({
      
        dots: false,
        margin: 25,
        rtl: en_path,
        autoplay: true,
        loop: true,
        smartSpeed: 1200,
        nav: false,
        onInitialized  : counter, //When the plugin has initialized.
        onTranslated : counter, //When the translation of the stage has finished.
        responsive:{
            0:{
                items:1
                
            },
            600:{
                items:1
                
            },
            1000:{
                items:1
                
            }
        }
    });


    $(".testimonial-slider-content").owlCarousel({
      
        dots: false,
        margin: 25,
        rtl: en_path,
        autoplay: true,
        loop: false,
        smartSpeed: 800,
        nav: true,
        responsive:{
            0:{
                items:1
                
            },
            600:{
                items:2
                
            },
            1000:{
                items:3
                
            }
        }
    });


    function counter(event) {
        var element   = event.target;         // DOM element, in this example .owl-carousel
         var items     = event.item.count;     // Number of items
         var item      = event.item.index + 1;     // Position of the current item
       
       // it loop is true then reset counter from 1
        if(item > items) {
            item = item - items
        }
        if(en_path){
            $('.counters').html (item + " " + items +"of")
        }else{
            $('.counters').html (""+item+" of "+items)
        }
     }

    /*------------------
        Magnific Popup
    --------------------*/
    $('.video-popup').magnificPopup({
        type: 'iframe'
    });

    /*------------------
		Date Picker
	--------------------*/
    $(".date-input").datepicker({
        minDate: 0,
        dateFormat: 'dd MM, yy'
    });

    /*------------------
		Nice Select
	--------------------*/
    $("select").niceSelect();

})(jQuery);