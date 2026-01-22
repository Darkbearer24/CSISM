/*
  Hero Component Behavior
  - Progressive enhancement: fade-in on intersection
*/
(function () {
  const hero = document.querySelector('.hero');
  if (!hero) return;
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) return;
  hero.style.opacity = '0';
  hero.style.transform = 'translateY(24px)';
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        hero.style.transition = 'opacity 600ms ease, transform 600ms ease';
        hero.style.opacity = '1';
        hero.style.transform = 'translateY(0)';
        observer.unobserve(hero);
      }
    });
  }, { threshold: 0.2 });
  observer.observe(hero);
})();

