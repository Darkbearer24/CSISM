(function () {
  const back = document.querySelector('.timeline__back');
  if (!back) return;
  back.addEventListener('click', function (e) {
    if (window.history.length > 1) {
      e.preventDefault();
      history.back();
    }
  });
})();

