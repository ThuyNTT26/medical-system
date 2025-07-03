const donThuocAPI = "http://localhost:8000/api/v1/donthuoc/donthuoc/";
const table = document.querySelector("#donthuoc-body");

// Tải danh sách đơn thuốc
function taiDanhSachDonThuoc() {
  fetch(donThuocAPI)
    .then(res => {
      if (!res.ok) throw new Error("Không thể lấy dữ liệu");
      return res.json();
    })
    .then(data => {
      table.innerHTML = "";
      data.forEach(item => themDong(item));
    })
    .catch(err => console.error("❌ Lỗi tải dữ liệu:", err));
}

// Thêm một dòng đơn thuốc vào bảng
function themDong(item) {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td>${item.MaDonThuoc}</td>
    <td>${item.MaKetQua}</td>
    <td>${item.NgayKeDon}</td>
    <td>${item.GhiChu || ""}</td>
    <td>
      <button onclick="batDauSua(this)">Sửa</button>
      <button onclick="xoaDonThuoc('${item.MaDonThuoc}')">Xóa</button>
    </td>`;
  table.appendChild(tr);
}

// Hiện dòng thêm mới
function hienDongMoiDonThuoc() {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td>
      <button onclick="luuDonThuocMoi(this)">Lưu</button>
      <button onclick="this.closest('tr').remove()">Hủy</button>
    </td>`;
  table.prepend(tr);
}

// Lưu đơn thuốc mới
function luuDonThuocMoi(btn) {
  const tr = btn.closest("tr");
  const data = {
    MaDonThuoc: tr.children[0].innerText.trim(),
    MaKetQua: tr.children[1].innerText.trim(),
    NgayKeDon: tr.children[2].innerText.trim(),
    GhiChu: tr.children[3].innerText.trim(),
  };

  fetch(donThuocAPI, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then(res => {
      if (!res.ok) throw new Error("Thêm thất bại");
      taiDanhSachDonThuoc();
    })
    .catch(err => console.error("❌ Lỗi thêm:", err));
}

// Bắt đầu chỉnh sửa
function batDauSua(btn) {
  const tr = btn.closest("tr");
  for (let i = 2; i <= 3; i++) tr.children[i].contentEditable = "true";
  btn.textContent = "Lưu";
  btn.onclick = () => capNhatDonThuoc(tr);
}

// Cập nhật đơn thuốc
function capNhatDonThuoc(tr) {
  const ma = tr.children[0].innerText.trim();
  const data = {
    MaKetQua: tr.children[1].innerText.trim(),
    NgayKeDon: tr.children[2].innerText.trim(),
    GhiChu: tr.children[3].innerText.trim(),
  };

  fetch(donThuocAPI + ma, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then(res => {
      if (!res.ok) throw new Error("Cập nhật thất bại");
      taiDanhSachDonThuoc();
    })
    .catch(err => console.error("❌ Lỗi cập nhật:", err));
}

// Xóa đơn thuốc
function xoaDonThuoc(ma) {
  if (!confirm(`Xác nhận xoá đơn thuốc "${ma}"?`)) return;

  fetch(donThuocAPI + ma, { method: "DELETE" })
    .then(res => {
      if (!res.ok) throw new Error("Xoá thất bại");
      taiDanhSachDonThuoc();
    })
    .catch(err => console.error("❌ Lỗi xoá:", err));
}

// Tìm kiếm đơn thuốc
function timKiemDonThuoc() {
  const keyword = document.getElementById("searchDonThuoc").value.toLowerCase();

  fetch(donThuocAPI)
    .then(res => res.json())
    .then(data => {
      table.innerHTML = "";
      data
        .filter(item =>
          item.MaDonThuoc.toLowerCase().includes(keyword) ||
          item.MaKetQua.toLowerCase().includes(keyword)
        )
        .forEach(item => themDong(item));
    })
    .catch(err => console.error("❌ Lỗi tìm kiếm:", err));
}

// Tự động tải danh sách khi trang load
document.addEventListener("DOMContentLoaded", () => {
  taiDanhSachDonThuoc();
});
