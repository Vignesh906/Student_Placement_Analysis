document.addEventListener("DOMContentLoaded", () => {

  const form = document.getElementById("predict-form");
  const btn = document.getElementById("submit-btn");

  // Animate progress bar on page load if result exists
  const fill = document.querySelector(".progress-fill");
  if (fill) {
    const width = fill.getAttribute("data-width");
    fill.style.width = "0%";
    setTimeout(() => {
      fill.style.width = width + "%";
    }, 300);
  }

  // Button loading state on submit
  if (form) {
    form.addEventListener("submit", (e) => {
      // Basic validation check
      const selects = form.querySelectorAll("select[required]");
      let valid = true;
      selects.forEach(sel => {
        if (!sel.value) valid = false;
      });
      if (!valid) return;

      btn.textContent = "Predicting...";
      btn.disabled = true;
    });
  }

  // Staggered field entrance animation
  const fields = document.querySelectorAll(".field");
  fields.forEach((field, i) => {
    field.style.opacity = "0";
    field.style.transform = "translateY(10px)";
    field.style.transition = "opacity 0.3s ease, transform 0.3s ease";
    setTimeout(() => {
      field.style.opacity = "1";
      field.style.transform = "translateY(0)";
    }, 60 + i * 30);
  });

});
