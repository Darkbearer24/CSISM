/*
  Navbar Component Behavior
  - Handles menu toggle and basic keyboard accessibility
*/
(function () {
  const toggle = document.querySelector('.navbar__toggle');
  const menu = document.getElementById('navbar-menu');
  if (!toggle || !menu) return;

  function setOpen(open) {
    toggle.setAttribute('aria-expanded', String(open));
    menu.setAttribute('data-open', String(open));
    if (open) {
      menu.querySelector('.navbar__link')?.focus();
    }
  }

  toggle.addEventListener('click', function () {
    const isOpen = toggle.getAttribute('aria-expanded') === 'true';
    setOpen(!isOpen);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      setOpen(false);
      toggle.focus();
    }
  });

  document.addEventListener('click', function (e) {
    const isOpen = toggle.getAttribute('aria-expanded') === 'true';
    if (!isOpen) return;
    if (!menu.contains(e.target) && !toggle.contains(e.target)) {
      setOpen(false);
    }
  });
})();

