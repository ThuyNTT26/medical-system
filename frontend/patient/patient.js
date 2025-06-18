const token = localStorage.getItem('access_token');
if (!token) {
  alert('Hãy đăng nhập!');
  window.location.href = '../auth/login.html';
}

document.getElementById('add-patient-form').onsubmit = async function (e) {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const phone = document.getElementById('phone').value;
  const res = await fetch('http://127.0.0.1:8000/api/v1/patient/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    },
    body: JSON.stringify({name, phone})
  });
  if (res.ok) {
    alert('Thêm thành công!');
    location.reload();
  } else {
    alert('Thêm thất bại!');
  }
};

// Load list
window.onload = async () => {
  const res = await fetch('http://127.0.0.1:8000/api/v1/patient/', {
    headers: {'Authorization': 'Bearer ' + token}
  });
  const patients = await res.json();
  const list = document.getElementById('patient-list');
  patients.forEach(p => {
    const li = document.createElement('li');
    li.textContent = `${p.name} - ${p.phone}`;
    list.appendChild(li);
  });
};
