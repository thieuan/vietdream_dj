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

        // Click on prev/next item → bring it to center
        // Click on active (center) item → navigate to services page
        prodItems.forEach((item, index) => {
            item.addEventListener('click', () => {
                if (item.classList.contains('active')) {
                    // Active item clicked → go to services
                    window.location.href = document.querySelector('a[href*="services"]')?.href || '/dich-vu/';
                } else {
                    // Side item clicked → make it active
                    currentIndex = index;
                    updateCarousel();
                }
            });

            // Change cursor to pointer for better UX hint
            item.style.cursor = 'pointer';
        });

        document.getElementById('prod-next')?.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % prodItems.length;
            updateCarousel();
        });
        document.getElementById('prod-prev')?.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + prodItems.length) % prodItems.length;
            updateCarousel();
        });

        // Touch swipe for mobile
        const prodCarousel = document.getElementById('product-carousel');
        if (prodCarousel) {
            let prodTouchStartX = 0;
            prodCarousel.addEventListener('touchstart', (e) => {
                prodTouchStartX = e.touches[0].clientX;
            }, { passive: true });

            prodCarousel.addEventListener('touchend', (e) => {
                const diff = prodTouchStartX - e.changedTouches[0].clientX;
                if (Math.abs(diff) > 50) {
                    if (diff > 0) {
                        currentIndex = (currentIndex + 1) % prodItems.length; // swipe left → next
                    } else {
                        currentIndex = (currentIndex - 1 + prodItems.length) % prodItems.length; // swipe right → prev
                    }
                    updateCarousel();
                }
            }, { passive: true });
        }
    }

    // ============ PROJECT INFO BOX SLIDER ============
    const projDots = document.querySelectorAll('.project-dots .dot');
    const projBgImg = document.getElementById('projectBgImg');
    const projTitle = document.getElementById('projectTitle');
    const projScale = document.getElementById('projectScale');
    const projDesc = document.getElementById('projectDesc');

    if (projDots.length && projBgImg) {
        let currentProj = 0;

        const goToProject = (index) => {
            const dot = projDots[index];
            if (!dot) return;

            // Fade out
            projBgImg.style.opacity = '0';
            projTitle.style.opacity = '0';
            projScale.style.opacity = '0';
            projDesc.style.opacity = '0';

            setTimeout(() => {
                // Swap content
                projBgImg.src = dot.dataset.img;
                projBgImg.alt = dot.dataset.title;
                projTitle.textContent = dot.dataset.title;
                projScale.innerHTML = '<strong>Quy mô:</strong> ' + dot.dataset.scale;
                projDesc.innerHTML = '<strong>Hạng mục PCCC:</strong> ' + dot.dataset.desc;

                // Update active dot
                projDots.forEach(d => d.classList.remove('active'));
                dot.classList.add('active');
                currentProj = index;

                // Fade in
                projBgImg.style.opacity = '1';
                projTitle.style.opacity = '1';
                projScale.style.opacity = '1';
                projDesc.style.opacity = '1';
            }, 300);
        };

        // CSS transition for fade
        [projBgImg, projTitle, projScale, projDesc].forEach(el => {
            el.style.transition = 'opacity 0.3s ease';
        });

        // Dot click
        projDots.forEach((dot, i) => {
            dot.style.cursor = 'pointer';
            dot.addEventListener('click', () => goToProject(i));
        });

        // Swipe on the section
        const projSection = document.getElementById('projectFeatured');
        if (projSection) {
            let projTouchStartX = 0;
            projSection.addEventListener('touchstart', (e) => {
                projTouchStartX = e.touches[0].clientX;
            }, { passive: true });
            projSection.addEventListener('touchend', (e) => {
                const diff = projTouchStartX - e.changedTouches[0].clientX;
                if (Math.abs(diff) > 50) {
                    const next = diff > 0
                        ? (currentProj + 1) % projDots.length
                        : (currentProj - 1 + projDots.length) % projDots.length;
                    goToProject(next);
                }
            }, { passive: true });
        }
    }

    // ============ HERO HORIZONTAL SLIDER ============
    const heroTrack = document.getElementById('heroTrack');
    const heroSlides = document.querySelectorAll('.hero-slide');
    const heroDots = document.querySelectorAll('.hero-dot');
    const totalSlides = heroSlides.length;

    if (heroTrack && totalSlides > 0) {
        let currentSlide = 0;
        let autoTimer;

        const goToSlide = (index) => {
            // Deactivate old
            heroSlides[currentSlide].classList.remove('active');
            heroDots[currentSlide].classList.remove('active');

            // Update index
            currentSlide = (index + totalSlides) % totalSlides;

            // Activate new
            heroSlides[currentSlide].classList.add('active');
            heroDots[currentSlide].classList.add('active');

            // Move track: each slide takes 1/3 of the full 300% track
            heroTrack.style.transform = `translateX(-${currentSlide * (100 / totalSlides)}%)`;
        };

        // Initialise first slide
        heroSlides[0].classList.add('active');

        // Arrows
        document.getElementById('heroPrev')?.addEventListener('click', () => {
            goToSlide(currentSlide - 1);
            resetTimer();
        });
        document.getElementById('heroNext')?.addEventListener('click', () => {
            goToSlide(currentSlide + 1);
            resetTimer();
        });

        // Dots
        heroDots.forEach(dot => {
            dot.addEventListener('click', () => {
                goToSlide(parseInt(dot.dataset.index));
                resetTimer();
            });
        });

        // Touch swipe support for mobile (replaces arrow buttons)
        let touchStartX = 0;
        heroTrack.addEventListener('touchstart', (e) => {
            touchStartX = e.touches[0].clientX;
        }, { passive: true });

        heroTrack.addEventListener('touchend', (e) => {
            const diff = touchStartX - e.changedTouches[0].clientX;
            if (Math.abs(diff) > 50) { // swipe threshold 50px
                if (diff > 0) {
                    goToSlide(currentSlide + 1); // swipe left → next
                } else {
                    goToSlide(currentSlide - 1); // swipe right → prev
                }
                resetTimer();
            }
        }, { passive: true });

        // Auto-play every 5s
        const startTimer = () => {
            autoTimer = setInterval(() => goToSlide(currentSlide + 1), 5000);
        };
        const resetTimer = () => {
            clearInterval(autoTimer);
            startTimer();
        };
        startTimer();
    }
});

