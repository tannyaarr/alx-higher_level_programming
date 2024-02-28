// script that adds a <li> element
$('#add_item').on('click', function () {
  // Create a new <li> element with the text item
  const newItem = $('<li>').text('Item');
  // Append the new <li> element to the UL with class 'my_list'
  $('ul.my_list').append(newItem);
});
