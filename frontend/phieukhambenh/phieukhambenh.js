const API_URL = "http://localhost:8000/api/v1/phieukhambenh/phieukhambenh/";
const tableBody = document.querySelector("#phieu-body");

// Tải dữ liệu
function taiDanhSachPhieu() {
  fetch(API_URL)
    .then(res => {
      if (!res.ok) throw new Error("Không thể lấy dữ liệu phiếu khám");
      return res.json();
    })
    .then(data => {
      tableBody.innerHTML = "";
      data.forEach(phieu => themDong(phieu));
    })
    .catch(err => console.error("❌ Lỗi khi tải phiếu khám:", err));
}

// Thêm dòng vào bảng
function themDong(phieu) {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td>${phieu.MaPhieuKham}</td>
    <td>${phieu.MaBenhNhan}</td>
    <td>${phieu.MaBacSi}</td>
    <td>${phieu.NgayKham}</td>
    <td>${phieu.TrieuChung || ""}</td>
    <td>${phieu.ChuanDoan || ""}</td>
    <td>${phieu.HuongDieuTri || ""}</td>
    <td>${phieu.MaLichHen || ""}</td>
    <td>
      <button onclick="batDauSua(this)">Sửa</button>
      <button onclick="xoaPhieu('${phieu.MaPhieuKham}')">Xóa</button>
    </td>`;
  tableBody.appendChild(tr);
}

// Thêm dòng mới để nhập
function hienDongMoiPhieu() {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td><input type="date" /></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td>
      <button onclick="luuPhieuMoi(this)">Lưu</button>
      <button onclick="this.closest('tr').remove()">Hủy</button>
    </td>`;
  tableBody.prepend(tr);
}

// Lưu phiếu mới
function luuPhieuMoi(btn) {
  const tr = btn.closest("tr");
  const data = {
    MaPhieuKham: tr.children[0].innerText.trim(),
    MaBenhNhan: tr.children[1].innerText.trim(),
    MaBacSi: tr.children[2].innerText.trim(),
    NgayKham: tr.children[3].querySelector("input").value,
    TrieuChung: tr.children[4].innerText.trim(),
    ChuanDoan: tr.children[5].innerText.trim(),
    HuongDieuTri: tr.children[6].innerText.trim(),
    MaLichHen: tr.children[7].innerText.trim()
  };

  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
    .then(() => taiDanhSachPhieu())
    .catch(err => console.error("❌ Lỗi lưu phiếu mới:", err));
}

// Bắt đầu sửa
function batDauSua(btn) {
  const tr = btn.closest("tr");
  for (let i = 4; i <= 6; i++) {
    tr.children[i].contentEditable = "true";
  }
  btn.textContent = "Lưu";
  btn.onclick = () => capNhatPhieu(tr);
}

// Cập nhật
function capNhatPhieu(tr) {
  const maPhieu = tr.children[0].innerText.trim();
  const data = {
    TrieuChung: tr.children[4].innerText.trim(),
    ChuanDoan: tr.children[5].innerText.trim(),
    HuongDieuTri: tr.children[6].innerText.trim()
  };

  fetch(`${API_URL}${maPhieu}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
    .then(() => taiDanhSachPhieu())
    .catch(err => console.error("❌ Lỗi cập nhật:", err));
}

// Xoá phiếu
function xoaPhieu(maPhieu) {
  fetch(`${API_URL}${maPhieu}`, { method: "DELETE" })
    .then(() => taiDanhSachPhieu())
    .catch(err => console.error("❌ Lỗi xoá:", err));
}

// Tìm kiếm
function timKiemPhieu() {
  const keyword = document.getElementById("searchPhieu").value.toLowerCase();
  fetch(API_URL)
    .then(res => res.json())
    .then(data => {
      const filtered = data.filter(p =>
        p.MaPhieuKham.toLowerCase().includes(keyword) ||
        p.MaBenhNhan.toLowerCase().includes(keyword) ||
        p.MaBacSi.toLowerCase().includes(keyword)
      );
      tableBody.innerHTML = "";
      filtered.forEach(themDong);
    });
}

// Khởi động
document.addEventListener("DOMContentLoaded", taiDanhSachPhieu);
