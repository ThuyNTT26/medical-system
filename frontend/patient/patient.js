const API_URL = "http://127.0.0.1:8000/api/v1/patient";

document.addEventListener("DOMContentLoaded", function () {
  loadPatients();

  document
    .getElementById("patient-form")
    .addEventListener("submit", async (e) => {
      e.preventDefault();

      const id = document.getElementById("MaBenhNhan").value;
      const method = id ? "PUT" : "POST";
      const url = id ? `${API_URL}/${id}` : API_URL;

      const gioiTinhSelect = document.getElementById("gioiTinh");
      const gioiTinh = gioiTinhSelect.value === "Nam" ? "M" : "F";

      const data = {
        hoTen: document.getElementById("hoTen").value,
        ngaySinh: document.getElementById("ngaySinh").value,
        gioiTinh: gioiTinh,
        soDienThoai: document.getElementById("soDienThoai").value,
        email: document.getElementById("email").value,
        diaChi: document.getElementById("diaChi").value,
        cccd: document.getElementById("cccd").value,
        tienSuBenhLy: document.getElementById("tienSuBenhLy").value,
      };

      const res = await fetch(url, {
        method,
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("access_token") || ""}`,
        },
        body: JSON.stringify(data),
      });

      let result;
      try {
        result = await res.json();
      } catch (e) {
        result = { detail: "Lỗi không xác định" };
      }

      if (res.ok) {
        alert("Thêm bệnh nhân thành công!");
        document.getElementById("patient-form").reset();
        document.getElementById("MaBenhNhan").value = "";
        loadPatients();
      } else {
        if (Array.isArray(result.detail)) {
          // Trường hợp trả về dạng danh sách lỗi
          const messages = result.detail.map((err) => err.msg).join("\n");
          alert("Lỗi:\n" + messages);
        } else {
          alert("Lỗi: " + (result.detail || "Có lỗi xảy ra"));
        }
      }
    });
});

async function loadPatients() {
  const res = await fetch(API_URL, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("access_token") || ""}`,
    },
  });
  const data = await res.json();
  console.log("DATA TRẢ VỀ:", data);
  const tbody = document.querySelector("#patient-table tbody");
  tbody.innerHTML = "";

  data.forEach((p) => {
    const row = document.createElement("tr");
    row.innerHTML = `
        <td>${p.MaBenhNhan}</td>
        <td>${p.HoTen}</td>
        <td>${p.NgaySinh || ""}</td>
        <td>${p.GioiTinh}</td>
        <td>${p.SoDienThoai}</td>
        <td>${p.Email}</td>
        <td>${p.DiaChi}</td>
        <td>${p.CCCD}</td>
        <td>${p.TienSuBenhLy}</td>
      <td>
        <button onclick="editPatient('${p.MaBenhNhan}')">Sửa</button>
        <button onclick="deletePatient('${p.MaBenhNhan}')">Xoá</button>
        <button onclick="viewPatient('${p.MaBenhNhan}')">Hồ sơ</button>
      </td>`;
    tbody.appendChild(row);
  });
}

async function editPatient(id) {
  const res = await fetch(`${API_URL}/${id}`, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("access_token") || ""}`,
    },
  });
  const p = await res.json();
  console.log("DATA TRẢ VỀ:", p);
  document.getElementById("MaBenhNhan").value = p.MaBenhNhan;
  document.getElementById("hoTen").value = p.hoTen;
  document.getElementById("ngaySinh").value = p.ngaySinh;
  document.getElementById("gioiTinh").value = p.gioiTinh;
  document.getElementById("soDienThoai").value = p.soDienThoai;
  document.getElementById("email").value = p.email;
  document.getElementById("diaChi").value = p.diaChi;
  document.getElementById("cccd").value = p.cccd;
  document.getElementById("tienSuBenhLy").value = p.tienSuBenhLy;

  document
    .getElementById("patient-form")
    .scrollIntoView({ behavior: "smooth" });
}

async function deletePatient(id) {
  if (confirm("Xoá bệnh nhân này?")) {
    const res = await fetch(`${API_URL}/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${localStorage.getItem("access_token") || ""}`,
      },
    });
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

async function viewPatient(id) {
  try {
    console.log("GỌI API:", `${API_URL}/${id}/hosos`);
    const token = localStorage.getItem("access_token");
    const res = await fetch(`${API_URL}/${id}/hosos`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await res.json();
    console.log("DỮ LIỆU HỒ SƠ:", data);

    const hosoDiv = document.getElementById("hoso-content");

    const content = `
      <h3>Thông tin bệnh nhân</h3>
      <p><strong>Họ tên:</strong> ${data.benh_nhan.hoTen}</p>
      <p><strong>Ngày sinh:</strong> ${data.benh_nhan.ngaySinh || ""}</p>
      <p><strong>Giới tính:</strong> ${data.benh_nhan.gioiTinh || ""}</p>
      <p><strong>SĐT:</strong> ${data.benh_nhan.soDienThoai || ""}</p>
      <p><strong>CCCD:</strong> ${data.benh_nhan.cccd || ""}</p>
      <p><strong>Tiền sử bệnh lý:</strong> ${
        data.benh_nhan.tienSuBenhLy || ""
      }</p>

      <h3>Lịch sử khám</h3>
      <ul>
        ${(data.lich_su || [])
          .map((l) => {
            const ngay = l.NgayHen || l.ngay_kham || "Chưa rõ";
            const lydo = l.LyDo || l.ly_do || "Không có lý do";
            return `<li>${ngay} - ${lydo}</li>`;
          })
          .join("")}
      </ul>

      <h3>Kết quả điều trị</h3>
      <ul>${(data.ket_qua || [])
        .map((k) => `<li>${k.chan_doan} - ${k.ghi_chu}</li>`)
        .join("")}</ul>

      <h3>Đơn thuốc</h3>
      <ul>${(data.don_thuoc || [])
        .map((d) => `<li>${d.thuoc} - ${d.lieu_luong}</li>`)
        .join("")}</ul>
    `;

    document.getElementById("hoso-dialog-content").innerHTML = content;
    document.getElementById("hoso-dialog").style.display = "block";
  } catch (err) {
    console.error("LỖI GỌI HỒ SƠ:", err);
    alert("Không lấy được hồ sơ bệnh nhân.");
  }
}

function closeHosoDialog() {
  document.getElementById("hoso-dialog").style.display = "none";
}

window.editPatient = editPatient;
window.deletePatient = deletePatient;
window.viewPatient = viewPatient;
