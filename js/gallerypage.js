document.addEventListener("DOMContentLoaded", () => {
    const overlay = document.createElement("div");
    overlay.className = "img-overlay";
    overlay.innerHTML = `<img><span class="close">×</span>`;
    document.body.appendChild(overlay);

    const overlayImg = overlay.querySelector("img");
    const desktopQuery = window.matchMedia("(min-width: 651px)");

    document.querySelectorAll(".gallery-img").forEach(img => {
        img.addEventListener("click", () => {
            // Only allow lightbox in 3-column mode
            if (!desktopQuery.matches) return;
            overlayImg.src = img.src;
            overlay.classList.add("show");
            // Disable background scrolling
            document.body.style.overflow = 'hidden';
        });
    });

    overlay.addEventListener("click", () => {
        overlay.classList.remove("show");
        // Re-enable background scrolling
        document.body.style.overflow = '';
    });

    // overlay.addEventListener("click", (e) => { // can only click close button
    //     if (e.target.classList.contains("close")) {
    //         overlay.classList.remove("show");
    //         document.body.style.overflow = '';
    //     }
    // });
});
