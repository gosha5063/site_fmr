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

  // Cookie notice (поддерживаем несколько баннеров на странице)
  var cookieNotices = Array.prototype.slice.call(document.querySelectorAll('.cookie-notice'));
  var cookieButtons = Array.prototype.slice.call(document.querySelectorAll('.cookie-accept'));
  if (cookieNotices.length && cookieButtons.length) {
    if (localStorage.getItem('cookie-accepted')) {
      cookieNotices.forEach(function (n) { n.classList.add('hidden'); });
    }
    cookieButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        localStorage.setItem('cookie-accepted', '1');
        cookieNotices.forEach(function (n) { n.classList.add('hidden'); });
      });
    });
  }

  // Form submit: отправляем лида на бэкенд и показываем сообщение
  var forms = document.querySelectorAll('form[data-lead]');
  forms.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var payload = {};
      var formId = form.getAttribute('data-lead') || 'unknown';

      Array.prototype.forEach.call(
        form.querySelectorAll('input, textarea, select'),
        function (field) {
          if (!field.name) return;
          payload[field.name] = field.value;
        }
      );

      var body = {
        id: Date.now(),
        source: formId,
        data: payload
      };

      // отправляем данные на бэкенд (нужен /api/leads на сервере)
      fetch('/api/leads', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      }).catch(function () {
        // при ошибке сети просто продолжаем, чтобы не ломать UX
      });

      var sent = form.querySelector('.form-sent');
      var fields = form.querySelector('.form-fields');
      if (sent && fields) {
        sent.classList.remove('hidden');
        fields.classList.add('hidden');
      }
    });
  });
})();
