/* ═══════════════════════════════════════════════════════════════
   SNOWL — Global JavaScript (Original Style)
   ═══════════════════════════════════════════════════════════════ */

(function () {
  /* ── Loader ──────────────────────────────────────────────── */
  const loader = document.getElementById('loader');
  if (loader) {
    setTimeout(function () { loader.classList.add('hidden'); }, 500);
  }

  /* ── Navbar scroll ──────────────────────────────────────── */
  window.addEventListener('scroll', function () {
    var navbar = document.querySelector('.navbar');
    if (navbar) navbar.classList.toggle('scrolled', window.scrollY > 50);
  });

  /* ── Mobile menu ─────────────────────────────────────────── */
  var menuToggle = document.querySelector('.menu-toggle');
  var mobileMenu = document.querySelector('.mobile-menu');
  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', function () {
      mobileMenu.classList.toggle('active');
    });
    document.querySelectorAll('.mobile-menu a').forEach(function (a) {
      a.addEventListener('click', function () {
        mobileMenu.classList.remove('active');
      });
    });
  }

  /* ── Fade-in on scroll ───────────────────────────────────── */
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
  document.querySelectorAll('.fade-in').forEach(function (el) { observer.observe(el); });

  /* ── Contact Form ─────────────────────────────────────────── */
  var form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      if (!btn) return;
      btn.disabled = true;
      btn.textContent = '...';
      var success = document.getElementById('formSuccess');
      setTimeout(function () {
        if (success) success.classList.add('show');
        form.reset();
        btn.disabled = false;
        btn.textContent = 'Send Inquiry';
      }, 1000);
    });
  }

  /* ── Lucide icons ─────────────────────────────────────────── */
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }

})();
