// script that fetches the translation of 'hello' in French
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Display the translated 'hello in the DIV#hello
    $('#hello').text(data.hello);
  });
});
