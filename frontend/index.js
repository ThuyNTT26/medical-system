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
