document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const button = document.querySelector("button");
    const progress = document.querySelector(".progress");

    form.addEventListener("submit", () => {
        button.innerText = "Predicting...";
        button.disabled = true;
    });

    if (progress) {
        const width = progress.getAttribute("data-width");
        progress.style.width = "0%";

        setTimeout(() => {
            progress.style.transition = "width 1s";
            progress.style.width = width + "%";
        }, 200);
    }

});