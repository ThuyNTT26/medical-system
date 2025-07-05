document.addEventListener("DOMContentLoaded", () => {
  const token = localStorage.getItem("token");
  if (!token) {
    window.location.href = "/frontend/auth/login.html";
    return;
  }

  // Gán sự kiện cho các nút
  document.getElementById("btn-patient")?.addEventListener("click", () => {
    window.location.href = "/frontend/patient/patient.html";
  });

  document.getElementById("btn-appointment")?.addEventListener("click", () => {
    window.location.href = "/frontend/appointment/appointment.html";
  });

  document.getElementById("btn-logout")?.addEventListener("click", () => {
    localStorage.removeItem("token");
    window.location.href = "/frontend/auth/login.html";
  });
});

window.addEventListener("DOMContentLoaded", () => {
  const username = localStorage.getItem("username") || "Người dùng";
  document.getElementById("username").innerText = username;

  const slides = document.querySelectorAll(".slide");
  let current = 0;

  setInterval(() => {
    slides[current].classList.remove("active");
    current = (current + 1) % slides.length;
    slides[current].classList.add("active");
  }, 4000);
});

