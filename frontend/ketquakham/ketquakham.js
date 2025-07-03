const ketQuaAPI = "http://localhost:8000/api/v1/ketquakham/ketquakham/";
const table = document.querySelector("#ketqua-body");

function taiDanhSachKetQua() {
  fetch(ketQuaAPI)
    .then(res => {
      if (!res.ok) throw new Error("Không lấy được dữ liệu");
      return res.json();
    })
    .then(data => {
      table.innerHTML = "";
      data.forEach(item => themDong(item));
    })
    .catch(err => console.error("❌ Lỗi:", err));
}

function themDong(item) {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td>${item.MaKetQua}</td>
    <td>${item.MaPhieuKham}</td>
    <td>${item.LoaiXetNghiem}</td>
    <td>${item.KetQuaXetNghiem}</td>
    <td>${item.NgayThucHien}</td>
    <td>
      <button onclick="batDauSua(this)">Sửa</button>
      <button onclick="xoaKetQua('${item.MaKetQua}')">Xóa</button>
    </td>`;
  table.appendChild(tr);
}

function hienDongMoiKetQua() {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td>
      <button onclick="luuKetQuaMoi(this)">Lưu</button>
      <button onclick="this.closest('tr').remove()">Hủy</button>
    </td>`;
  table.prepend(tr);
}

function luuKetQuaMoi(btn) {
  const tr = btn.closest("tr");
  const data = {
    MaKetQua: tr.children[0].innerText.trim(),
    MaPhieuKham: tr.children[1].innerText.trim(),
    LoaiXetNghiem: tr.children[2].innerText.trim(),
    KetQuaXetNghiem: tr.children[3].innerText.trim(),
    NgayThucHien: tr.children[4].innerText.trim()
  };

  fetch(ketQuaAPI, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
    .then(() => taiDanhSachKetQua())
    .catch(err => console.error("❌ Lỗi thêm:", err));
}

function batDauSua(btn) {
  const tr = btn.closest("tr");
  for (let i = 2; i <= 4; i++) tr.children[i].contentEditable = "true";
  btn.textContent = "Lưu";
  btn.onclick = () => capNhatKetQua(tr);
}

function capNhatKetQua(tr) {
  const ma = tr.children[0].innerText.trim();
  const data = {
    LoaiXetNghiem: tr.children[2].innerText.trim(),
    KetQuaXetNghiem: tr.children[3].innerText.trim(),
    NgayThucHien: tr.children[4].innerText.trim()
  };

  fetch(ketQuaAPI + ma, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
    .then(() => taiDanhSachKetQua())
    .catch(err => console.error("❌ Lỗi cập nhật:", err));
}

function xoaKetQua(ma) {
  if (!confirm(`Xác nhận xoá kết quả "${ma}"?`)) return;

  fetch(ketQuaAPI + ma, { method: "DELETE" })
    .then(() => taiDanhSachKetQua())
    .catch(err => console.error("❌ Lỗi xoá:", err));
}

function timKiemKetQua() {
  const keyword = document.getElementById("searchKetQua").value.toLowerCase();

  fetch(ketQuaAPI)
    .then(res => res.json())
    .then(data => {
      table.innerHTML = "";
      data
        .filter(item =>
          item.MaKetQua.toLowerCase().includes(keyword) ||
          item.MaPhieuKham.toLowerCase().includes(keyword)
        )
        .forEach(item => themDong(item));
    })
    .catch(err => console.error("❌ Lỗi tìm kiếm:", err));
}

document.addEventListener("DOMContentLoaded", () => {
  taiDanhSachKetQua();
});
