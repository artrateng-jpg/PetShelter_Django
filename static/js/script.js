document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('nav a');
    const sections = document.querySelectorAll('section');
    const petCards = document.querySelectorAll('.pet-card');

    sections.forEach(section => {
        if (section.id === 'home') {
            section.style.display = 'block';
        } else {
            section.style.display = 'none';
        }
    });

    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault(); 

            const targetSectionId = link.getAttribute('data-target');
            if (targetSectionId) {
                sections.forEach(section => {
                    if (section.id === targetSectionId) {
                        section.style.display = 'block';
                    } else {
                        section.style.display = 'none';
                    }
                });
            }

            const filterValue = link.getAttribute('data-filter');
            if (filterValue) {
                petCards.forEach(card => {
                    const category = card.getAttribute('data-category');
                    if (filterValue === 'all' || filterValue === category) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }
        });
    });
});