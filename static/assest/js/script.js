// Loan Calculator Logic
document.addEventListener('DOMContentLoaded', function () {
    const loanAmount = document.getElementById('loanAmount');
    const interestRate = document.getElementById('interestRate');
    const loanTerm = document.getElementById('loanTerm');

    const amountDisplay = document.getElementById('amountDisplay');
    const rateDisplay = document.getElementById('rateDisplay');
    const termDisplay = document.getElementById('termDisplay');

    const totalRepayment = document.getElementById('totalRepayment');
    const totalInterest = document.getElementById('totalInterest');
    const monthlyRepayment = document.getElementById('monthlyRepayment');

    // Format currency
    function formatCurrency(num) {
        return new Intl.NumberFormat('en-AU', {
            style: 'currency',
            currency: 'AUD',
            maximumFractionDigits: 0
        }).format(num);
    }

    // Calculate loan
    function calculateLoan() {
        const P = parseInt(loanAmount.value);
        const r = parseFloat(interestRate.value) / 100 / 12;
        const n = parseInt(loanTerm.value) * 12;

        // Monthly payment formula: P * (r(1+r)^n) / ((1+r)^n - 1)
        const monthly = P * (r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
        const total = monthly * n;
        const interest = total - P;

        // Update displays
        amountDisplay.textContent = formatCurrency(P);
        rateDisplay.textContent = interestRate.value + '%';
        termDisplay.textContent = loanTerm.value + ' years';

        monthlyRepayment.textContent = formatCurrency(monthly || 0);
        totalRepayment.textContent = formatCurrency(total || 0);
        totalInterest.textContent = formatCurrency(interest || 0);
    }

    // Update range track background (fill effect)
    function updateRangeTrack(input) {
        const val = input.value;
        const min = input.min ? input.min : 0;
        const max = input.max ? input.max : 100;
        const percent = (val - min) / (max - min) * 100;
        input.style.background = `linear-gradient(to right, #0d3b9c 0%, #0d3b9c ${percent}%, #F1F4E3 ${percent}%, #F1F4E3 100%)`;
    }

    // Event listeners
    [loanAmount, interestRate, loanTerm].forEach(input => {
        input.addEventListener('input', () => {
            calculateLoan();
            updateRangeTrack(input);
        });
        // Initial track update
        updateRangeTrack(input);
    });

    // Initial calculation
    calculateLoan();

    // Loan type buttons
    const typeButtons = document.querySelectorAll('[data-type]');
    typeButtons.forEach(btn => {
        btn.addEventListener('click', function () {
            typeButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // Set default values based on type
            const type = this.getAttribute('data-type');
            switch (type) {
                case 'home':
                    loanAmount.value = 500000;
                    interestRate.value = 5.5;
                    break;
                case 'refinance':
                    loanAmount.value = 750000;
                    interestRate.value = 5.2;
                    break;
                case 'investment':
                    loanAmount.value = 1000000;
                    interestRate.value = 4.9;
                    break;
            }
            [loanAmount, interestRate, loanTerm].forEach(input => {
                updateRangeTrack(input);
            });
            calculateLoan();
        });
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe cards
    document.querySelectorAll('.service-card, .testimonial-card, .guide-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
});



// Mega Menu behavior
document.addEventListener('DOMContentLoaded', function () {
    const megaMenus = document.querySelectorAll('.mega-menu');

    megaMenus.forEach(menu => {
        const toggle = menu.querySelector('.dropdown-toggle');
        const dropdown = menu.querySelector('.dropdown-menu');

        if (toggle && dropdown) {
            toggle.addEventListener('click', function (e) {
                if (window.innerWidth > 991) {
                    e.preventDefault();
                    e.stopPropagation();

                    const isOpen = dropdown.classList.contains('show');

                    // Close all other mega menus
                    megaMenus.forEach(otherMenu => {
                        const otherDropdown = otherMenu.querySelector('.dropdown-menu');
                        if (otherDropdown && otherDropdown !== dropdown) {
                            closeMenu(otherDropdown);
                        }
                    });

                    if (isOpen) {
                        closeMenu(dropdown);
                    } else {
                        openMenu(dropdown);
                    }
                }
            });
        }
    });

    function openMenu(dropdown) {
        dropdown.style.display = 'block';

        dropdown.classList.add('show');

        setTimeout(() => {
            dropdown.style.opacity = '1';
            dropdown.style.transform = 'translate(-50%, 0)';
        }, 10);
    }

    function closeMenu(dropdown) {
        dropdown.style.opacity = '0';
        dropdown.style.transform = 'translate(-50%, 10px)';
        dropdown.classList.remove('show');
        setTimeout(() => {
            if (!dropdown.classList.contains('show')) {
                dropdown.style.display = 'none';
            }
        }, 300); // Wait for transition
    }

    // Close on click outside
    document.addEventListener('click', function (e) {
        if (window.innerWidth > 991) {
            megaMenus.forEach(menu => {
                const dropdown = menu.querySelector('.dropdown-menu');
                if (dropdown && !menu.contains(e.target)) {
                    closeMenu(dropdown);
                }
            });
        }
    });

    // Handle window resize
    window.addEventListener('resize', () => {
        const dropdowns = document.querySelectorAll('.mega-menu .dropdown-menu');
        dropdowns.forEach(d => {
            if (window.innerWidth <= 991) {
                d.style = ''; // Reset inline styles for mobile
                d.classList.remove('show');
            }
        });
    });
});

// Slick Slider Initialization for Lenders Section
$(document).ready(function () {

    // First row: Left → Right
    $('.scroller-ltr .scroller-track').slick({
        autoplay: true,
        autoplaySpeed: 0,
        speed: 5000,
        cssEase: 'linear',
        infinite: true,
        variableWidth: true,
        arrows: false,
        dots: false,
        pauseOnHover: false,
        pauseOnFocus: false
    });

    // Second row: Right → Left
    $('.scroller-rtl-two .scroller-track').slick({
        autoplay: true,
        autoplaySpeed: 0,
        speed: 5000,
        cssEase: 'linear',
        infinite: true,
        variableWidth: true,
        arrows: false,
        dots: false,
        rtl: true,
        pauseOnHover: false,
        pauseOnFocus: false
    });

});




const btn = document.getElementById('selectBtn');
const dropdown = document.getElementById('dropdown');

btn.addEventListener('click', (e) => {
    e.stopPropagation(); // 🔥 IMPORTANT
    dropdown.classList.toggle('active');
});

dropdown.addEventListener('click', (e) => {
    e.stopPropagation(); // allow clicking inside dropdown
});

document.addEventListener('click', () => {
    dropdown.classList.remove('active');
});



const btn1 = document.getElementById('selectBtntwo');
const dropdown1 = document.getElementById('dropdowntwo');

btn1.addEventListener('click', (e) => {
    e.stopPropagation(); // 🔥 IMPORTANT
    dropdown1.classList.toggle('active');
});

dropdown1.addEventListener('click', (e) => {
    e.stopPropagation(); // allow clicking inside dropdown
});

document.addEventListener('click', () => {
    dropdown1.classList.remove('active');
});



const ctx = document.getElementById('stackedChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['0', '2', '3', '4', '6', '7', '8'],
        datasets: [
            {
                label: 'Base Amount',
                data: [30, 45, 60, 75, 95, 110, 130],
                backgroundColor: '#041E42'
            },
            {
                label: 'Growth',
                data: [10, 12, 15, 18, 20, 22, 25],
                backgroundColor: '#15489D'
            },
            {
                label: 'Bonus',
                data: [5, 6, 7, 8, 9, 10, 12],
                backgroundColor: '#CFE0FF'
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false
            }
        },
        scales: {
            x: {
                stacked: true,
                title: {
                    display: true,
                    text: 'Years',
                    font: { size: 14 }
                },
                grid: {
                    display: false
                }
            },
            y: {
                stacked: true,
                title: {
                    display: true,
                    text: 'Amount'
                },
                ticks: {
                    stepSize: 60,
                    callback: value => `$${value}k`
                },
                grid: {
                    color: '#BFBFBF'
                },
                suggestedMax: 150
            }
        },
        borderRadius: 6,
        barThickness: 45
    }
});


Chart.defaults.font.family = "Poppins";
Chart.defaults.font.size = 12;
Chart.defaults.color = '#4A4A4A';




document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector(".navbar");
    if (!navbar) return;

    window.addEventListener("scroll", () => {
        const scrollTop = window.scrollY;
        console.log("scroll:", scrollTop);

        if (scrollTop >= 10) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });
});





document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector(
        '.input-body-e input[type="text"]'
    );
    const cards = document.querySelectorAll(".Calculator-cardrs");

    searchInput.addEventListener("input", function () {
        const query = searchInput.value.toLowerCase().trim();

        cards.forEach(card => {
            const text = card.innerText.toLowerCase();
            const col = card.closest(".col-md-4");

            if (text.includes(query)) {
                col.style.display = "block";
            } else {
                col.style.display = "none";
            }
        });
    });
});




document.addEventListener("DOMContentLoaded", function () {
    const exploreBtn = document.getElementById("explore-calculor-button");
    const heroPic = document.getElementById("calulator-hero-pic");
    const mainCalculators = document.querySelectorAll(".main-calulator");
    const searchBar = document.querySelector(".serchbar");

    exploreBtn.addEventListener("click", function (e) {
        e.preventDefault(); // stop anchor jump

        // hide hero image
        heroPic.classList.add("d-none");

        // show ALL calculator sections
        mainCalculators.forEach(section => {
            section.classList.remove("d-none");
        });

        // hide search bar
        searchBar.classList.add("d-none");
    });
});



document.addEventListener("DOMContentLoaded", function () {
    const hasInfoSplit = document.querySelector(".info-split-section");
    const footer = document.querySelector(".footer-section");

    if (hasInfoSplit && footer) {
        footer.style.paddingTop = "10px";
    }
});
