document.getElementById('login-form').onsubmit = async function (e) {
  e.preventDefault();
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const res = await fetch('http://127.0.0.1:8000/api/v1/auth/login', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({username, password})
  });
  const data = await res.json();
  if (res.ok) {
    localStorage.setItem('access_token', data.access_token);
    alert('Đăng nhập thành công!');
    window.location.href = '../patient/patient.html'; // hoặc dashboard
  } else {
    alert(data.detail);
  }
};
