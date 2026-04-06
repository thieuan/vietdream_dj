document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.querySelector('.nav-menu');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    }));

    // Header Scroll Effect
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-up').forEach((el) => {
        observer.observe(el);
    });

    // Product Carousel Logic
    const prodItems = document.querySelectorAll('.prod-item');
    if (prodItems.length >= 3) {
        let currentIndex = 1; // Middle item active initially
        const updateCarousel = () => {
            prodItems.forEach((item, index) => {
                item.classList.remove('active', 'prev', 'next');
                if (index === currentIndex) {
                    item.classList.add('active');
                } else if (index === (currentIndex - 1 + prodItems.length) % prodItems.length) {
                    item.classList.add('prev');
                } else if (index === (currentIndex + 1) % prodItems.length) {
                    item.classList.add('next');
                }
            });
        };
        updateCarousel();

        document.getElementById('prod-next')?.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % prodItems.length;
            updateCarousel();
        });
        document.getElementById('prod-prev')?.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + prodItems.length) % prodItems.length;
            updateCarousel();
        });
    }
});
