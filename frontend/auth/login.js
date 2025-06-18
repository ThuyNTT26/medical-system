document.getElementById("login-form").onsubmit = async function (e) {
  console.log("JS đã load!");

  e.preventDefault();
  const username = document.getElementById("tenDangNhap").value;
  const password = document.getElementById("matKhau").value;

  const res = await fetch("http://127.0.0.1:8000/api/v1/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      tenDangNhap: username,
      matKhau: password,
    }),
  })
    .then((res) => {
      if (!res.ok) throw new Error("Login failed");
      return res.json();
    })
    .then((data) => {
      localStorage.setItem("token", data.access_token);
      window.location.href = "../index.html";
    })
    .catch((err) => {
      alert("Đăng nhập thất bại: " + err.message);
    });
};
