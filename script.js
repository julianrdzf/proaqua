(function () {
  const navToggle = document.querySelector('[data-nav-toggle]');
  const nav = document.querySelector('[data-nav]');
  const year = document.getElementById('year');

  if (year) year.textContent = String(new Date().getFullYear());

  function setNav(open) {
    if (!navToggle || !nav) return;
    nav.classList.toggle('is-open', open);
    navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  if (navToggle && nav) {
    navToggle.addEventListener('click', () => {
      const open = nav.classList.contains('is-open');
      setNav(!open);
    });

    nav.addEventListener('click', (e) => {
      const t = e.target;
      if (t && t.tagName === 'A') setNav(false);
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') setNav(false);
    });

    document.addEventListener('click', (e) => {
      if (!nav.classList.contains('is-open')) return;
      const target = e.target;
      if (!target) return;
      if (nav.contains(target) || navToggle.contains(target)) return;
      setNav(false);
    });
  }

  const toast = document.querySelector('[data-toast]');
  const toastText = document.querySelector('[data-toast-text]');
  const toastClose = document.querySelector('[data-toast-close]');
  const fakeSubmit = document.querySelector('[data-fake-submit]');

  function showToast(message) {
    if (!toast || !toastText) return;
    toastText.textContent = message;
    toast.hidden = false;
  }

  function hideToast() {
    if (!toast) return;
    toast.hidden = true;
  }

  if (toastClose) toastClose.addEventListener('click', hideToast);

  if (fakeSubmit) {
    fakeSubmit.addEventListener('click', () => {
      showToast('Gracias. Tu consulta fue registrada (demo).');
      window.setTimeout(hideToast, 5000);
    });
  }
})();
