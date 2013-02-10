// remap jQuery to $
(function($){})(window.jQuery);


/* trigger when page is ready */
$(document).ready(function (){
   
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
