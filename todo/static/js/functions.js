// remap jQuery to $
(function($){})(window.jQuery);

var mouse_is_inside = false;
/* trigger when page is ready */
$(document).ready(function (){
    $(".loginbutton").click(function() {
        var loginBox = $("#login_box");
        if (loginBox.is(":visible"))
            loginBox.fadeOut("fast");
        else
            loginBox.fadeIn("fast");
        return false;
    });
    
    $("#login_box").hover(function(){ 
        mouse_is_inside=true; 
    }, function(){ 
        mouse_is_inside=false; 
    });

    $("body").click(function(){
        if(! mouse_is_inside) $("#login_box").fadeOut("fast");
    });

    $(".registrationbutton").click(function() {
        var registrationBox = $("#registration_box");
        if (registrationBox.is(":visible"))
            registrationBox.fadeOut("fast");
        else
            registrationBox.fadeIn("fast");
        return false;
    });
    
    $("#registration_box").hover(function(){ 
        mouse_is_inside=true; 
    }, function(){ 
        mouse_is_inside=false; 
    });

    $("body").click(function(){
        if(! mouse_is_inside) $("#registration_box").fadeOut("fast");
    });

		$('.default-value').each(function() {
    		var default_value = this.value;
    		$(this).css('color', '#666');
   		 $(this).focus(function() {
      		  if(this.value == default_value) {
         	  this.value = '';
         	  $(this).css('color', '#333');
       		  }
    		 });
   		$(this).blur(function() {
        		if(this.value == '') {
        			$(this).css('color', '#666');
            	this.value = default_value;
        		}
    		});
		});
		
});


/* optional triggers

$(window).load(function() {
	
});

$(window).resize(function() {
	
});

*/
