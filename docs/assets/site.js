// Theme toggle (light <-> dark) — flips [data-theme] so every token-driven element re-themes.
(function () {
  const KEY = 'ds-theme';
  const root = document.documentElement;
  const saved = localStorage.getItem(KEY);
  if (saved === 'dark') root.setAttribute('data-theme', 'dark');

  function label() {
    const dark = root.getAttribute('data-theme') === 'dark';
    document.querySelectorAll('.theme-toggle .lbl').forEach(function (el) {
      el.textContent = dark ? 'Dark' : 'Light';
    });
  }
  document.addEventListener('DOMContentLoaded', function () {
    label();
    document.querySelectorAll('.theme-toggle').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const dark = root.getAttribute('data-theme') === 'dark';
        if (dark) { root.removeAttribute('data-theme'); localStorage.setItem(KEY, 'light'); }
        else { root.setAttribute('data-theme', 'dark'); localStorage.setItem(KEY, 'dark'); }
        label();
      });
    });
    const mb = document.querySelector('.menu-btn');
    const sb = document.querySelector('.sidebar');
    if (mb && sb) mb.addEventListener('click', function () { sb.classList.toggle('open'); });
  });
})();
