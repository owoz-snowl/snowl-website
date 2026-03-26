// SNOWL main.js - Essential site functionality
document.addEventListener('DOMContentLoaded', function() {
    // Hide the loader/spinner
    var loader = document.getElementById('loader');
    if (loader) {
        loader.style.display = 'none';
    }

    // Mobile menu toggle
    var menuToggle = document.getElementById('menuToggle');
    var mobileMenu = document.getElementById('mobileMenu');
    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });
    }

    // Navbar scroll effect
    var navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Close mobile menu on link click
    var mobileLinks = document.querySelectorAll('.mobile-menu a');
    mobileLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            if (mobileMenu) mobileMenu.classList.remove('active');
            if (menuToggle) menuToggle.classList.remove('active');
        });
    });

    // Dropdown for products (mobile)
    var dropdownTriggers = document.querySelectorAll('.dropdown-trigger');
    dropdownTriggers.forEach(function(trigger) {
        trigger.addEventListener('click', function(e) {
            e.preventDefault();
            var menu = trigger.nextElementSibling;
            if (menu) menu.classList.toggle('active');
        });
    });

    // Fade-in animations on scroll
    var fadeElements = document.querySelectorAll('.fade-in');
    if (fadeElements.length > 0) {
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        fadeElements.forEach(function(el) {
            observer.observe(el);
        });
    }
});
