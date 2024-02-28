// script that updates the text color of <header> element to red
// when the user clicks on the tag DIV#red_header
$('#red_header').on('click', function () {
  // Update the text color of the header to red
  $('header').css('color', '#FF0000');
});
