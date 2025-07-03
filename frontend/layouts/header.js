// frontend/layouts/header.js
export async function loadHeader() {
  const container = document.getElementById("header-container");
  if (!container) return;

  try {
    const res = await fetch("/frontend/layouts/header.html");
    const html = await res.text();
    container.innerHTML = html;

    // Gắn lại sự kiện logout vì nó nằm trong HTML được inject
    const logoutBtn = container.querySelector("button[onclick='logout()']");
    if (logoutBtn) {
      logoutBtn.addEventListener("click", logout);
    }
  } catch (err) {
    console.error("Không load được header:", err);
  }
}

export function checkAuth() {
  const token = localStorage.getItem("token");
  if (!token) {
    window.location.href = "/frontend/auth/login.html";
  }
}

export function logout() {
  localStorage.removeItem("token");
  window.location.href = "/frontend/auth/login.html";
}
