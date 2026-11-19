
// ==========================
// MOBILE NAVIGATION
// ==========================

const menuToggle = document.getElementById("menuToggle");
const navMenu = document.getElementById("navMenu");

menuToggle.addEventListener("click", function () {

    navMenu.classList.toggle("active");

    const isOpen = navMenu.classList.contains("active");

    menuToggle.textContent = isOpen ? "✕" : "☰";

    menuToggle.setAttribute("aria-expanded", isOpen);

});


// Close menu after clicking a navigation link

const navLinks = document.querySelectorAll("#navMenu a");

navLinks.forEach(function (link) {

    link.addEventListener("click", function () {

        navMenu.classList.remove("active");

        menuToggle.textContent = "☰";

        menuToggle.setAttribute("aria-expanded", "false");

    });

});


// ==========================
// SCROLL REVEAL ANIMATION
// ==========================

const revealElements = document.querySelectorAll(
    ".section-heading, .about-content, " +
    ".skill-card, .project-card, " +
    ".timeline-item, .achievement-card, " +
    ".hackathon-card, .contact-form"
);

if ("IntersectionObserver" in window) {

    revealElements.forEach(function (element) {

        element.classList.add("reveal");

    });

    const observer = new IntersectionObserver(

        function (entries) {

            entries.forEach(function (entry) {

                if (entry.isIntersecting) {

                    entry.target.classList.add("visible");

                    observer.unobserve(entry.target);

                }

            });

        },

        {
            threshold: 0.12
        }

    );

    revealElements.forEach(function (element) {

        observer.observe(element);

    });

}


// ==========================
// CONTACT FORM
// ==========================

const contactForm = document.getElementById("contactForm");

contactForm.addEventListener("submit", function (event) {

    event.preventDefault();

    const name = document.getElementById("name").value.trim();

    const email = document.getElementById("email").value.trim();

    const message = document.getElementById("message").value.trim();

    const result = document.getElementById("formResult");


    if (!name || !email || !message) {

        result.style.color = "red";

        result.textContent = "Please fill in all fields.";

        return;

    }


    const subject = "Portfolio Contact - " + name;

    const body =
        "Name: " + name + "\n" +
        "Email: " + email + "\n\n" +
        "Message:\n" + message;


    const mailtoLink =
        "mailto:prathikshahn07@gmail.com" +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);


    result.style.color = "green";

    result.textContent =
        "Opening your email application...";


    window.location.href = mailtoLink;

});


// ==========================
// AUTOMATIC COPYRIGHT YEAR
// ==========================

document.getElementById("year").textContent =
    new Date().getFullYear();
