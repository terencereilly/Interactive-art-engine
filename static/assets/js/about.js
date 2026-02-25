// Scroll reveal animation for about sections
function revealSections() {
    const sections = document.querySelectorAll('.about-section');
    const windowHeight = window.innerHeight;
    sections.forEach(section => {
        const sectionTop = section.getBoundingClientRect().top;
        if (sectionTop < windowHeight * 0.85) {
            section.classList.add('revealed');
        }
    });
}

window.addEventListener('scroll', revealSections);
window.addEventListener('load', revealSections);
