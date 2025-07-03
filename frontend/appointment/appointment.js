const API_URL = "http://127.0.0.1:8000/api/v1/appointments";

document.addEventListener("DOMContentLoaded", () => {
  loadAppointments();

  document.getElementById("appointment-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const maLichHen = document.getElementById("MaLichHen").value;
    const method = maLichHen ? "PUT" : "POST";
    const url = maLichHen ? `${API_URL}/${maLichHen}` : API_URL;

    const data = {
      MaBenhNhan: document.getElementById("MaBenhNhan").value,
      MaBacSi: document.getElementById("MaBacSi").value,
      NgayHen: document.getElementById("NgayHen").value,
      GioHen: document.getElementById("GioHen").value,
      TrangThai: document.getElementById("TrangThai").value,
      LyDo: document.getElementById("LyDo").value,
    };
    console.log("DỮ LIỆU GỬI:", data);

    const res = await fetch(url, {
      method,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("access_token") || ""}`,
      },
      body: JSON.stringify(data),
    });

    const result = await res.json();
    if (res.ok) {
      alert("Thành công!");
      document.getElementById("appointment-form").reset();
      loadAppointments();
    } else {
      alert(result.detail || "Có lỗi xảy ra");
    }
  });
});

async function loadAppointments() {
  const res = await fetch(API_URL, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("access_token") || ""}`,
    },
  });
  const data = await res.json();
  const tbody = document.querySelector("#appointment-table tbody");
  tbody.innerHTML = "";

  data.forEach((a) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${a.MaLichHen}</td>
      <td>${a.MaBenhNhan}</td>
      <td>${a.MaBacSi}</td>
      <td>${a.MaLich}</td>
      <td>${a.NgayHen}</td>
      <td>${a.GioHen}</td>
      <td>${a.TrangThai}</td>
      <td>${a.LyDo || ""}</td>
      <td>
        <button onclick="editAppointment('${a.MaLichHen}')">Sửa</button>
        <button onclick="deleteAppointment('${a.MaLichHen}')">Xoá</button>
      </td>`;
    tbody.appendChild(row);
  });
}

async function editAppointment(id) {
  const res = await fetch(`${API_URL}/${id}`, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("access_token") || ""}`,
    },
  });
  const a = await res.json();

  document.getElementById("MaLichHen").value = a.MaLichHen;
  document.getElementById("MaBenhNhan").value = a.MaBenhNhan;
  document.getElementById("MaBacSi").value = a.MaBacSi;
  document.getElementById("MaLich").value = a.MaLich;
  document.getElementById("NgayHen").value = a.NgayHen;
  document.getElementById("GioHen").value = a.GioHen;
  document.getElementById("TrangThai").value = a.TrangThai;
  document.getElementById("LyDo").value = a.LyDo;
}

async function deleteAppointment(id) {
  if (confirm("Xoá lịch hẹn này?")) {
    const res = await fetch(`${API_URL}/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${localStorage.getItem("access_token") || ""}`,
      },
    });
    const result = await res.json();
    alert(result.message || "Đã xoá");
    loadAppointments();
  }
}

function searchAppointments() {
  const ma = document.getElementById("searchMa").value.toLowerCase();
  const bn = document.getElementById("searchBN").value.toLowerCase();
  const bs = document.getElementById("searchBS").value.toLowerCase();
  const ngay = document.getElementById("searchNgay").value;

  const rows = document.querySelectorAll("#appointment-table tbody tr");
  rows.forEach((row) => {
    const [maCell, bnCell, bsCell, , ngayCell] = row.children;
    const matched =
      maCell.textContent.toLowerCase().includes(ma) &&
      bnCell.textContent.toLowerCase().includes(bn) &&
      bsCell.textContent.toLowerCase().includes(bs) &&
      (!ngay || ngayCell.textContent.includes(ngay));
    row.style.display = matched ? "" : "none";
  });
}

function resetForm() {
  document.getElementById("appointment-form").reset();
}

async function loadBenhNhanAndBacSi() {
  const token = localStorage.getItem("token");

  // Load bệnh nhân
  const benhnhanRes = await fetch("http://127.0.0.1:8000/api/v1/patient", {
    headers: { Authorization: `Bearer ${token}` },
  });
  const benhnhans = await benhnhanRes.json();

  const benhNhanList = document.getElementById("ds-benhnhan");
  benhNhanList.innerHTML = "";
  benhnhans.forEach((bn) => {
    const opt = document.createElement("option");
    opt.value = bn.MaBenhNhan;
    opt.label = bn.hoTen;
    benhNhanList.appendChild(opt);
  });

  // Load bác sĩ
  const bacsiRes = await fetch("http://127.0.0.1:8000/api/v1/doctor/all", {
    headers: { Authorization: `Bearer ${token}` },
  });
  const bacsis = await bacsiRes.json();

  const bacSiList = document.getElementById("ds-bacsi");
  bacSiList.innerHTML = "";
  bacsis.forEach((bs) => {
    const opt = document.createElement("option");
    opt.value = bs.MaBacSi;
    opt.label = bs.hoTen;
    bacSiList.appendChild(opt);
  });
}

window.addEventListener("DOMContentLoaded", () => {
  loadBenhNhanAndBacSi();
});


window.editAppointment = editAppointment;
window.deleteAppointment = deleteAppointment;
window.searchAppointments = searchAppointments;
window.loadAppointments = loadAppointments;
