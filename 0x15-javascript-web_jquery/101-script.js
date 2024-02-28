// script that adds, remove and clears LI from list
$(document).ready(function() {
	//Event handler for adding a new item
	$('#add_item').on('click', function() {
		//Create a new <li> element wth the text "Item"
		var newItem = $('<li>').text('Item');
		//Append the new <li> to the UL with class 'my_list'
		$('ul.my_list').append(newItem);
	});

	//Event handler for removing the last item
	$('#remove_item').on('click', function() {
		//Remove the last <li> from the UL with class 'my_list'
		$('ul.my_list li:last-child').remove();
	});
	//Event handler for clearing the list
	$('#clear_list').on('click'. function() {
		//Remove all <li> elements from YL with class 'my_list'
		$('ul.my_list').empty();
	});
});
