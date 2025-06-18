const API_URL = "http://127.0.0.1:8000/api/v1/patient";

document.addEventListener("DOMContentLoaded", function () {
  loadPatients();

  document.getElementById("patient-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const id = document.getElementById("id").value;
    const method = id ? "PUT" : "POST";
    const url = id ? `${API_URL}/${id}` : API_URL;

    const data = {
      hoTen: document.getElementById("hoTen").value,
      ngaySinh: document.getElementById("ngaySinh").value,
      gioiTinh: document.getElementById("gioiTinh").value,
      soDienThoai: document.getElementById("soDienThoai").value,
      email: document.getElementById("email").value,
      diaChi: document.getElementById("diaChi").value,
      cccd: document.getElementById("cccd").value,
      tienSuBenhLy: document.getElementById("tienSuBenhLy").value
    };

    const res = await fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const result = await res.json();
    console.log("DATA TRẢ VỀ:", result);

    if (res.ok) {
      alert("Thành công!");
      document.getElementById("patient-form").reset();
      loadPatients();
    } else {
      alert(result.detail || "Có lỗi xảy ra");
    }
  });
});

async function loadPatients() {
  const res = await fetch(API_URL);
  const data = await res.json();
  console.log("DATA TRẢ VỀ:", data);
  const tbody = document.querySelector("#patient-table tbody");
  tbody.innerHTML = "";

  data.forEach((p) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${p.id}</td>
      <td>${p.hoTen}</td>
      <td>${p.ngaySinh || ""}</td>
      <td>${p.gioiTinh}</td>
      <td>${p.soDienThoai}</td>
      <td>${p.email}</td>
      <td>${p.diaChi}</td>
      <td>${p.cccd}</td>
      <td>${p.tienSuBenhLy}</td>
      <td>
        <button onclick="editPatient(${p.id})">Sửa</button>
        <button onclick="deletePatient(${p.id})">Xoá</button>
        <button onclick="viewPatient(${p.id})">Hồ sơ</button>
      </td>`;
    tbody.appendChild(row);
  });
}

async function editPatient(id) {
  const res = await fetch(`${API_URL}/${id}`);
  const p = await res.json();
  console.log("DATA TRẢ VỀ:", p);
  document.getElementById("id").value = p.id;
  document.getElementById("hoTen").value = p.hoTen;
  document.getElementById("ngaySinh").value = p.ngaySinh;
  document.getElementById("gioiTinh").value = p.gioiTinh;
  document.getElementById("soDienThoai").value = p.soDienThoai;
  document.getElementById("email").value = p.email;
  document.getElementById("diaChi").value = p.diaChi;
  document.getElementById("cccd").value = p.cccd;
  document.getElementById("tienSuBenhLy").value = p.tienSuBenhLy;
}

async function deletePatient(id) {
  if (confirm("Xoá bệnh nhân này?")) {
    const res = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    const result = await res.json();
    console.log("DATA TRẢ VỀ:", result);
    alert(result.message || "Đã xoá");
    loadPatients();
  }
}

function searchPatients() {
  const ma = document.getElementById("searchMa").value.toLowerCase();
  const ten = document.getElementById("searchTen").value.toLowerCase();
  const sdt = document.getElementById("searchSDT").value.toLowerCase();
  const cccd = document.getElementById("searchCCCD").value.toLowerCase();

  const rows = document.querySelectorAll("#patient-table tbody tr");
  rows.forEach((row) => {
    const [idCell, tenCell, , , sdtCell, , , cccdCell] = row.children;
    const matched =
      idCell.textContent.toLowerCase().includes(ma) &&
      tenCell.textContent.toLowerCase().includes(ten) &&
      sdtCell.textContent.toLowerCase().includes(sdt) &&
      cccdCell.textContent.toLowerCase().includes(cccd);
    row.style.display = matched ? "" : "none";
  });
}

function viewPatient(id) {
  alert("Xem hồ sơ bệnh nhân #" + id + "\n(Chức năng này sẽ hiển thị lịch sử khám, đơn thuốc...)");
}

async function viewPatient(id) {
  try {
    console.log("GỌI API:", `${API_URL}/${id}/hosos`);
    const token = localStorage.getItem("access_token");
    const res = await fetch(`${API_URL}/${id}/hosos`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    const data = await res.json();
    console.log("DỮ LIỆU HỒ SƠ:", data);

    const hosoDiv = document.getElementById("hoso-content");

    hosoDiv.innerHTML = `
      <h4>Thông tin bệnh nhân</h4>
      <p><strong>Họ tên:</strong> ${data.benh_nhan.hoTen}</p>
      <p><strong>Ngày sinh:</strong> ${data.benh_nhan.ngaySinh}</p>
      <p><strong>CCCD:</strong> ${data.benh_nhan.cccd}</p>
      <p><strong>Tiền sử bệnh lý:</strong> ${data.benh_nhan.tienSuBenhLy}</p>

      <h4>Lịch sử khám</h4>
      <ul>${data.lich_su_kham.map(l => `<li>${l.ngay_hen}: ${l.noi_dung}</li>`).join("")}</ul>

      <h4>Kết quả điều trị</h4>
      <ul>${data.ket_qua_dieu_tri.map(k => `<li>${k.ngay_ket_qua}: ${k.chan_doan} - ${k.ghi_chu}</li>`).join("")}</ul>

      <h4>Đơn thuốc</h4>
      <ul>${data.don_thuoc.map(d => `<li>${d.ngay_cap}: ${d.thuoc}</li>`).join("")}</ul>
    `;

    // ✅ hiện phần hồ sơ chi tiết
    document.getElementById("hoso-container").style.display = "block";

  } catch (err) {
    console.error("LỖI GỌI HỒ SƠ:", err);
    alert("Không lấy được hồ sơ bệnh nhân.");
  }
}

