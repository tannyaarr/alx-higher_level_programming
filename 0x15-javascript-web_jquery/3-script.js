// script that adds the class red to the <header> element when the user
// clicks on the tag DIV#red_header
$('#red_header').on('click', function () {
  // Add the 'red' class to the header
  $('header').addClass('red');
});
