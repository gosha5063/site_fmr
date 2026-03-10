(function () {
  'use strict';

  // Mobile menu (event delegation — работает и для шапки, подгруженной из partials/header.html)
  document.body.addEventListener('click', function (e) {
    if (!e.target.closest('.menu-toggle')) return;
    var navMobile = document.querySelector('.nav-mobile');
    if (navMobile) {
      navMobile.classList.toggle('open');
      document.body.style.overflow = navMobile.classList.contains('open') ? 'hidden' : '';
    }
  });

  // Cookie notice
  var cookieNotice = document.querySelector('.cookie-notice');
  var cookieAccept = document.querySelector('.cookie-accept');
  if (cookieAccept && cookieNotice) {
    if (localStorage.getItem('cookie-accepted')) cookieNotice.classList.add('hidden');
    cookieAccept.addEventListener('click', function () {
      localStorage.setItem('cookie-accepted', '1');
      cookieNotice.classList.add('hidden');
    });
  }

  // Form submit (demo — без бэкенда показываем сообщение)
  var forms = document.querySelectorAll('form[data-lead]');
  forms.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var sent = form.querySelector('.form-sent');
      if (sent) {
        sent.classList.remove('hidden');
        form.querySelector('.form-fields')?.classList.add('hidden');
      }
    });
  });
})();
