document.addEventListener('DOMContentLoaded', () => {
    const popup = document.getElementById('construction-popup');
    const closeButton = document.getElementById('close-popup');

    // Check if the popup has been closed during the current session
    if (!sessionStorage.getItem('popupClosed')) {
        if (popup) {
            popup.style.display = 'flex';
        }
    }

    if (closeButton) {
        closeButton.addEventListener('click', () => {
            if (popup) {
                popup.style.display = 'none';
            }
            // Store the fact that the popup has been closed for this session
            sessionStorage.setItem('popupClosed', 'true');
        });
    }
});
