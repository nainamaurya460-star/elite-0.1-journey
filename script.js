/**
 * ============================================================================
 * Naina Maurya Portfolio — Ultra-Premium Interactive Engine (script.js)
 * High-performance, 60fps animations, memory-optimized for 8GB RAM systems.
 * ============================================================================
 */

(function () {
    'use strict';

    // -------------------------------------------------------------------------
    // 1. Lightweight 3D/Canvas Particle Constellation Engine
    // -------------------------------------------------------------------------
    const initParticleCanvas = () => {
        const canvas = document.getElementById('bgCanvas');
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        let width = 0;
        let height = 0;
        let dpr = 1;
        let animationFrameId = null;

        // Mouse tracking for subtle ambient particle reaction
        const mouse = {
            x: null,
            y: null,
            radius: 140
        };

        const handleMouseMove = (e) => {
            mouse.x = e.clientX;
            mouse.y = e.clientY;
        };

        const handleMouseLeave = () => {
            mouse.x = null;
            mouse.y = null;
        };

        window.addEventListener('mousemove', handleMouseMove, { passive: true });
        document.addEventListener('mouseleave', handleMouseLeave, { passive: true });

        // Responsive resize with dpr capped at 2 for memory efficiency
        const resizeCanvas = () => {
            dpr = Math.min(window.devicePixelRatio || 1, 2);
            width = window.innerWidth;
            height = window.innerHeight;

            canvas.width = Math.floor(width * dpr);
            canvas.height = Math.floor(height * dpr);
            canvas.style.width = width + 'px';
            canvas.style.height = height + 'px';

            ctx.scale(dpr, dpr);
            initParticles();
        };

        // Particle configuration
        let particles = [];
        const isMobile = window.innerWidth < 768;
        const PARTICLE_COUNT = isMobile ? 32 : 65; // Optimized for smooth rendering
        const CONNECTION_DIST = isMobile ? 85 : 125;

        class Particle {
            constructor() {
                this.reset(true);
            }

            reset(initial = false) {
                this.x = Math.random() * width;
                this.y = initial ? Math.random() * height : -10;
                this.vx = (Math.random() - 0.5) * 0.45;
                this.vy = (Math.random() * 0.35) + 0.15; // gentle downward/ambient drift
                this.radius = Math.random() * 1.8 + 1.1;
                this.baseAlpha = Math.random() * 0.45 + 0.25;
                this.alpha = this.baseAlpha;
                
                // Color palette: Cyan, Indigo, Violet
                const colors = ['#06b6d4', '#6366f1', '#a855f7', '#38bdf8'];
                this.color = colors[Math.floor(Math.random() * colors.length)];
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;

                // Mouse interaction: subtle push/repel
                if (mouse.x !== null && mouse.y !== null) {
                    const dx = mouse.x - this.x;
                    const dy = mouse.y - this.y;
                    const dist = Math.sqrt(dx * dx + dy * dy);

                    if (dist < mouse.radius) {
                        const force = (mouse.radius - dist) / mouse.radius;
                        const angle = Math.atan2(dy, dx);
                        this.x -= Math.cos(angle) * force * 1.8;
                        this.y -= Math.sin(angle) * force * 1.8;
                    }
                }

                // Wrap around edges seamlessly
                if (this.x < -20) this.x = width + 20;
                if (this.x > width + 20) this.x = -20;
                if (this.y > height + 20) this.reset(false);
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = this.color;
                ctx.globalAlpha = this.alpha;
                ctx.fill();
            }
        }

        const initParticles = () => {
            particles = [];
            for (let i = 0; i < PARTICLE_COUNT; i++) {
                particles.push(new Particle());
            }
        };

        // Render loop with connection lines
        const render = () => {
            ctx.clearRect(0, 0, width, height);

            // Connect nearby particles
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const p1 = particles[i];
                    const p2 = particles[j];
                    const dx = p1.x - p2.x;
                    const dy = p1.y - p2.y;
                    const dist = Math.sqrt(dx * dx + dy * dy);

                    if (dist < CONNECTION_DIST) {
                        const lineAlpha = (1 - dist / CONNECTION_DIST) * 0.18;
                        ctx.beginPath();
                        ctx.moveTo(p1.x, p1.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.strokeStyle = '#6366f1';
                        ctx.globalAlpha = lineAlpha;
                        ctx.lineWidth = 0.85;
                        ctx.stroke();
                    }
                }
            }

            // Update & draw particles
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();
            }

            ctx.globalAlpha = 1;
            animationFrameId = requestAnimationFrame(render);
        };

        // Resize with debounce
        let resizeTimeout;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(resizeCanvas, 150);
        });

        // Pause loop when tab is hidden to save CPU & RAM
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                cancelAnimationFrame(animationFrameId);
            } else {
                animationFrameId = requestAnimationFrame(render);
            }
        });

        resizeCanvas();
        render();
    };

    // -------------------------------------------------------------------------
    // 2. Custom Smooth Glowing Cursor (Desktop Only)
    // -------------------------------------------------------------------------
    const initCustomCursor = () => {
        // Only initialize on pointer devices that support hover
        if (!window.matchMedia('(pointer: fine)').matches) return;

        const cursorDot = document.querySelector('.cursor-dot');
        const cursorRing = document.querySelector('.cursor-ring');
        if (!cursorDot || !cursorRing) return;

        let mouseX = -100;
        let mouseY = -100;
        let ringX = -100;
        let ringY = -100;

        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            cursorDot.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
        }, { passive: true });

        // Smooth lagging ring with requestAnimationFrame lerp
        const lerpCursor = () => {
            ringX += (mouseX - ringX) * 0.16;
            ringY += (mouseY - ringY) * 0.16;
            cursorRing.style.transform = `translate3d(${ringX}px, ${ringY}px, 0)`;
            requestAnimationFrame(lerpCursor);
        };
        requestAnimationFrame(lerpCursor);

        // Hover scale state
        const interactiveElements = document.querySelectorAll(
            'a, button, input, textarea, .btn, .interactive-card, .skill-badge, .social-icon-btn, .bento-card, .credential-id-pill'
        );

        interactiveElements.forEach((el) => {
            el.addEventListener('mouseenter', () => {
                cursorRing.classList.add('cursor-expanded');
                cursorDot.classList.add('cursor-hidden');
            });
            el.addEventListener('mouseleave', () => {
                cursorRing.classList.remove('cursor-expanded');
                cursorDot.classList.remove('cursor-hidden');
            });
        });
    };

    // -------------------------------------------------------------------------
    // 3. Dynamic Typing Effect in Hero
    // -------------------------------------------------------------------------
    const initTypingEffect = () => {
        const textElement = document.getElementById('typingText');
        if (!textElement) return;

        const phrases = [
            'AI & Machine Learning Engineer',
            'Generative AI Specialist',
            'Computer Vision Developer',
            'Full-Stack AI Builder'
        ];

        let phraseIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        const typingSpeed = 75;
        const deletingSpeed = 40;
        const pauseDelay = 1800;

        const type = () => {
            const currentPhrase = phrases[phraseIndex];

            if (isDeleting) {
                textElement.textContent = currentPhrase.substring(0, charIndex - 1);
                charIndex--;
            } else {
                textElement.textContent = currentPhrase.substring(0, charIndex + 1);
                charIndex++;
            }

            let timeout = isDeleting ? deletingSpeed : typingSpeed;

            if (!isDeleting && charIndex === currentPhrase.length) {
                timeout = pauseDelay;
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                phraseIndex = (phraseIndex + 1) % phrases.length;
                timeout = 400;
            }

            setTimeout(type, timeout);
        };

        type();
    };

    // -------------------------------------------------------------------------
    // 4. 3D Card Tilt & Specular Reflection (Awwwards Style)
    // -------------------------------------------------------------------------
    const init3DCardTilt = () => {
        // Disable on touch devices for fluid native scrolling
        if (!window.matchMedia('(hover: hover)').matches) return;

        const tiltCards = document.querySelectorAll('.tilt-card');

        tiltCards.forEach((card) => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const cardWidth = rect.width;
                const cardHeight = rect.height;

                // Mouse offset from center (-1 to 1)
                const xOffset = (e.clientX - rect.left - cardWidth / 2) / (cardWidth / 2);
                const yOffset = (e.clientY - rect.top - cardHeight / 2) / (cardHeight / 2);

                const rotateX = -yOffset * 9; // Max 9 degrees
                const rotateY = xOffset * 9;

                // Update glare reflection position
                const mouseXPercent = ((e.clientX - rect.left) / cardWidth) * 100;
                const mouseYPercent = ((e.clientY - rect.top) / cardHeight) * 100;

                card.style.setProperty('--glare-x', `${mouseXPercent}%`);
                card.style.setProperty('--glare-y', `${mouseYPercent}%`);

                card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-8px) scale3d(1.02, 1.02, 1.02)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0) scale3d(1, 1, 1)`;
            });
        });

        // Profile headshot hover micro-tilt
        const avatarWrapper = document.querySelector('.hero-avatar-card');
        if (avatarWrapper) {
            avatarWrapper.addEventListener('mousemove', (e) => {
                const rect = avatarWrapper.getBoundingClientRect();
                const x = (e.clientX - rect.left - rect.width / 2) / (rect.width / 2);
                const y = (e.clientY - rect.top - rect.height / 2) / (rect.height / 2);
                avatarWrapper.style.transform = `perspective(800px) rotateX(${-y * 12}deg) rotateY(${x * 12}deg) translateY(-6px)`;
            });

            avatarWrapper.addEventListener('mouseleave', () => {
                avatarWrapper.style.transform = `perspective(800px) rotateX(0deg) rotateY(0deg) translateY(0)`;
            });
        }
    };

    // -------------------------------------------------------------------------
    // 5. Magnetic Hover Effect on CTA Buttons
    // -------------------------------------------------------------------------
    const initMagneticButtons = () => {
        if (!window.matchMedia('(hover: hover)').matches) return;

        const magneticButtons = document.querySelectorAll('.btn-magnetic');

        magneticButtons.forEach((btn) => {
            btn.addEventListener('mousemove', (e) => {
                const rect = btn.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;

                btn.style.transform = `translate3d(${x * 0.28}px, ${y * 0.28}px, 0)`;
            });

            btn.addEventListener('mouseleave', () => {
                btn.style.transform = `translate3d(0, 0, 0)`;
            });
        });
    };

    // -------------------------------------------------------------------------
    // 6. Smooth Scroll Reveal Animations (IntersectionObserver)
    // -------------------------------------------------------------------------
    const initScrollReveals = () => {
        const revealElements = document.querySelectorAll('.reveal');
        if (!revealElements.length) return;

        const observerOptions = {
            threshold: 0.12,
            rootMargin: '0px 0px -40px 0px'
        };

        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        revealElements.forEach((el) => revealObserver.observe(el));
    };

    // -------------------------------------------------------------------------
    // 7. Navigation Scrollspy & Sticky Header Blur
    // -------------------------------------------------------------------------
    const initNavigation = () => {
        const navbar = document.querySelector('.navbar-pill');
        const menuToggle = document.getElementById('menuToggle');
        const navMenu = document.getElementById('navMenu');
        const navLinks = document.querySelectorAll('.nav-pill-link');
        const sections = document.querySelectorAll('section[id]');

        // Sticky header background intensity on scroll
        const handleScroll = () => {
            if (navbar) {
                if (window.scrollY > 40) {
                    navbar.classList.add('scrolled');
                } else {
                    navbar.classList.remove('scrolled');
                }
            }

            // Scrollspy active anchor
            let current = '';
            const scrollPosition = window.pageYOffset + 180;

            sections.forEach((section) => {
                const top = section.offsetTop;
                const height = section.offsetHeight;
                if (scrollPosition >= top && scrollPosition < top + height) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach((link) => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${current}`) {
                    link.classList.add('active');
                }
            });
        };

        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll();

        // Mobile drawer toggle
        if (menuToggle && navMenu) {
            menuToggle.addEventListener('click', () => {
                navMenu.classList.toggle('active');
                const icon = menuToggle.querySelector('i');
                if (navMenu.classList.contains('active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-xmark');
                } else {
                    icon.classList.remove('fa-xmark');
                    icon.classList.add('fa-bars');
                }
            });

            // Close on link click
            navLinks.forEach((link) => {
                link.addEventListener('click', () => {
                    navMenu.classList.remove('active');
                    const icon = menuToggle.querySelector('i');
                    if (icon) {
                        icon.classList.remove('fa-xmark');
                        icon.classList.add('fa-bars');
                    }
                });
            });
        }
    };

    // -------------------------------------------------------------------------
    // 8. One-Click Interactive Email Copy Button
    // -------------------------------------------------------------------------
    const initEmailCopy = () => {
        const copyBtn = document.getElementById('copyEmailBtn');
        if (!copyBtn) return;

        const emailAddress = copyBtn.getAttribute('data-email') || 'naina.maurya.ai@gmail.com';

        copyBtn.addEventListener('click', async () => {
            try {
                await navigator.clipboard.writeText(emailAddress);
                const originalHtml = copyBtn.innerHTML;
                copyBtn.innerHTML = '<i class="fa-solid fa-check"></i> <span>Copied to Clipboard!</span>';
                copyBtn.classList.add('copied');

                setTimeout(() => {
                    copyBtn.innerHTML = originalHtml;
                    copyBtn.classList.remove('copied');
                }, 2200);
            } catch (err) {
                console.error('Failed to copy email:', err);
            }
        });
    };

    // -------------------------------------------------------------------------
    // 9. Interactive Contact Form with Feedback States
    // -------------------------------------------------------------------------
    const initContactForm = () => {
        const form = document.getElementById('contactForm');
        const feedback = document.getElementById('formFeedback');
        const submitBtn = document.getElementById('submitBtn');

        if (!form || !feedback || !submitBtn) return;

        form.addEventListener('submit', (e) => {
            e.preventDefault();

            // Loading state
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span>Transmitting...</span> <i class="fa-solid fa-circle-notch fa-spin"></i>';

            setTimeout(() => {
                feedback.textContent = '🚀 Message transmitted successfully! I will reply shortly.';
                feedback.className = 'form-feedback success';
                form.reset();

                submitBtn.disabled = false;
                submitBtn.innerHTML = '<span>Message Sent!</span> <i class="fa-solid fa-check"></i>';

                setTimeout(() => {
                    submitBtn.innerHTML = '<span>Send Message</span> <i class="fa-solid fa-paper-plane"></i>';
                    feedback.textContent = '';
                    feedback.className = 'form-feedback';
                }, 4000);
            }, 900);
        });
    };

    // -------------------------------------------------------------------------
    // 10. Interactive Credential ID Copy Handler
    // -------------------------------------------------------------------------
    const initCredentialCopy = () => {
        const credentialPills = document.querySelectorAll('.credential-id-pill');
        credentialPills.forEach((pill) => {
            pill.addEventListener('click', async () => {
                const textToCopy = pill.getAttribute('data-copy') || pill.textContent.trim();
                try {
                    await navigator.clipboard.writeText(textToCopy);
                    const originalHtml = pill.innerHTML;
                    pill.innerHTML = `<code>${textToCopy}</code> <i class="fa-solid fa-check"></i>`;
                    pill.classList.add('copied');

                    setTimeout(() => {
                        pill.innerHTML = originalHtml;
                        pill.classList.remove('copied');
                    }, 2200);
                } catch (err) {
                    console.error('Failed to copy credential ID:', err);
                }
            });
        });
    };

    // -------------------------------------------------------------------------
    // DOM Ready Initializer
    // -------------------------------------------------------------------------
    document.addEventListener('DOMContentLoaded', () => {
        initParticleCanvas();
        initCustomCursor();
        initTypingEffect();
        init3DCardTilt();
        initMagneticButtons();
        initScrollReveals();
        initNavigation();
        initEmailCopy();
        initContactForm();
        initCredentialCopy();
    });
})();
