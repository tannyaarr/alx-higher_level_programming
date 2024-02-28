// script that fetches and print the translation of "hello" based on the
// language code
$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').on('click', fetchTranslation);
  $('#language_code').on('keypress', function (event) {
    if (event.which === 13) { // 13 corresponds to the ENTER key
      fetchTranslation();
    }
	  });
});
