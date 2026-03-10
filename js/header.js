(function () {
  'use strict';
  var placeholder = document.getElementById('header-placeholder');
  if (!placeholder) return;

  var path = 'partials/header.html';
  fetch(path)
    .then(function (r) { return r.ok ? r.text() : Promise.reject(new Error(r.statusText)); })
    .then(function (html) {
      placeholder.innerHTML = html;
    })
    .catch(function () {
      // Если шапка не загрузилась (например, при открытии по file://),
      // просто не отображаем её. Для работы header нужно открыть сайт через локальный сервер.
    });
})();

(function () {
  'use strict';
  var placeholder = document.getElementById('header-placeholder');
  if (!placeholder) return;

  var path = 'partials/header.html';
  fetch(path)
    .then(function (r) { return r.ok ? r.text() : Promise.reject(new Error(r.statusText)); })
    .then(function (html) {
      placeholder.innerHTML = html;
    })
    .catch(function () {
      // Если шапка не загрузилась (например, при открытии по file://),
      // просто не отображаем её. Для работы header нужно открыть сайт через локальный сервер.
    });
})();
