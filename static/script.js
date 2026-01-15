// Forest FinTech theme interactions

// Smooth fade for alerts
document.addEventListener("DOMContentLoaded", () => {
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.style.transition = "opacity 0.6s ease";
      alert.style.opacity = "0";
      setTimeout(() => alert.remove(), 600);
    }, 4000); // auto-dismiss after 4s
  });
});

// Button ripple effect
document.addEventListener("click", e => {
  const btn = e.target.closest(".btn");
  if (!btn) return;

  const circle = document.createElement("span");
  const diameter = Math.max(btn.clientWidth, btn.clientHeight);
  const radius = diameter / 2;

  circle.style.width = circle.style.height = `${diameter}px`;
  circle.style.left = `${e.clientX - btn.offsetLeft - radius}px`;
  circle.style.top = `${e.clientY - btn.offsetTop - radius}px`;
  circle.classList.add("ripple");

  const ripple = btn.getElementsByClassName("ripple")[0];
  if (ripple) ripple.remove();

  btn.appendChild(circle);
});

// Ripple CSS
const style = document.createElement("style");
style.textContent = `
  .btn { position: relative; overflow: hidden; }
  .ripple {
    position: absolute;
    border-radius: 50%;
    transform: scale(0);
    animation: ripple 600ms linear;
    background-color: rgba(255, 255, 255, 0.7);
  }
  @keyframes ripple {
    to { transform: scale(4); opacity: 0; }
  }
`;
document.head.appendChild(style);