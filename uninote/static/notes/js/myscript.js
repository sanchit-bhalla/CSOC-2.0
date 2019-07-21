window.onload=function(){
	
	$('.se-pre-con').fadeOut(2000);
	
	
	var url=window.location.href;
	console.log(url);
	
	$('.nav a').each(function(){
		
		
		if(url==(this.href)){
			
			$(this).closest('li').addClass(' active');
			
		}
		
	});
	
	var url2=window.location.href;
	console.log(url2);
	
	$('.base a').each(function(){
		
		
		if(url2==(this.href)){
			
			$(this).closest('li').addClass(' active');
			
		}
		
	});
	
	
};


$(document).ready(function(){


var a=document.querySelectorAll('.rowa');
console.log(a)


$(a[0]).children('.notesaThumbnail').click(function(){
	
	$(a[0]).children('.getnotes').slideToggle('slow');
	$(a[0]).children('.getnotes').css('visibility','visible');
	
    $(a[1]).children('.getnotes').slideToggle('slow');
    $(a[1]).children('.getnotes').css('visibility','hidden');
						
    $(a[2]).children('.getnotes').slideToggle('slow');
    $(a[2]).children('.getnotes').css('visibility','hidden');
						
});

$(a[1]).children('.notesaThumbnail').click(function(){
	
	$(a[1]).children('.getnotes').slideToggle('slow');
	$(a[1]).children('.getnotes').css('visibility','visible');
	
	
    $(a[0]).children('.getnotes').slideToggle('slow');
    $(a[0]).children('.getnotes').css('visibility','hidden');
						
    $(a[2]).children('.getnotes').slideToggle('slow');
    $(a[2]).children('.getnotes').css('visibility','hidden');
						
});	

$(a[2]).children('.notesaThumbnail').click(function(){
	
	$(a[2]).children('.getnotes').slideToggle('slow');
	$(a[2]).children('.getnotes').css('visibility','visible');
	
    $(a[0]).children('.getnotes').slideToggle('slow');
    $(a[0]).children('.getnotes').css('visibility','hidden');
						
    $(a[1]).children('.getnotes').slideToggle('slow');
    $(a[1]).children('.getnotes').css('visibility','hidden');
						
});				   
				   
			   



var b=document.querySelectorAll('.rowb');
console.log(b);	

 

$(b[0]).children('.notesaThumbnail').click(function(){
	
	$(b[0]).children('.getnotes').slideToggle('slow');
	$(b[0]).children('.getnotes').css('visibility','visible');
	
    $(b[1]).children('.getnotes').slideToggle('slow');
    $(b[1]).children('.getnotes').css('visibility','hidden');
						
    $(b[2]).children('.getnotes').slideToggle('slow');
    $(b[2]).children('.getnotes').css('visibility','hidden');
						
});

$(b[0]).find('.closebutton').click(function(){
	
	 $(b[0]).children('.getnotes').slideUp('slow');
	 
	 
	 $(b[1]).children('.getnotes').slideUp('slow');
	 $(b[1]).children('.getnotes').css('visibility','hidden');
	 
	 
	 $(b[2]).children('.getnotes').siblings('#getnotes2').slideUp('slow');
	 $(b[2]).children('.getnotes').css('visibility','hidden');
	 
});


$(b[1]).children('.notesaThumbnail').click(function(){
	
	$(b[1]).children('.getnotes').slideToggle('slow');
	$(b[1]).children('.getnotes').css('visibility','visible');
	
	
    $(b[0]).children('.getnotes').slideToggle('slow');
    $(b[0]).children('.getnotes').css('visibility','hidden');
						
    $(b[2]).children('.getnotes').slideToggle('slow');
    $(b[2]).children('.getnotes').css('visibility','hidden');
						
});	

$(b[2]).children('.notesaThumbnail').click(function(){
	
	$(b[2]).children('.getnotes').slideToggle('slow');
	$(b[2]).children('.getnotes').css('visibility','visible');
	
    $(b[0]).children('.getnotes').slideToggle('slow');
    $(b[0]).children('.getnotes').css('visibility','hidden');
						
    $(b[1]).children('.getnotes').slideToggle('slow');
    $(b[1]).children('.getnotes').css('visibility','hidden');
						
});				   



$('.notes-header').find('span').click(function(){
	
	$(this).toggleClass(' glyphicon glyphicon-search glyphicon glyphicon-remove');
	
	$('.notes-header').find('.form-search').fadeToggle();
	
	
	
});


});