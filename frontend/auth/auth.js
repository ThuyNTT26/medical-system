window.addEventListener("DOMContentLoaded", function () {
  const token = localStorage.getItem("token");
  console.log("token", token);
  if (!token) {
    window.location.href = "/frontend/auth/login.html";
  }
});

function showDialog(message) {
  const dialog = document.getElementById("custom-dialog");
  const msg = document.getElementById("dialog-message");
  msg.innerText = message;
  dialog.classList.remove("hidden");
}

function closeDialog() {
  const dialog = document.getElementById("custom-dialog");
  dialog.classList.add("hidden");
}

