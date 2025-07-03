const detailAPI = "http://localhost:8000/api/v1/chitiet-donthuoc";
const table = document.querySelector("#bangChiTiet tbody");

function taiDanhSachChiTiet() {
  console.log("✅ Gọi 'taiDanhSachChiTiet'");
  fetch(detailAPI)
    .then(res => {
      console.log("HTTP status:", res.status);
      if (!res.ok) throw new Error("Không lấy được dữ liệu");
      return res.json();
    })
    .then(data => {
      console.log("📦 Dữ liệu nhận được:", data);
      table.innerHTML = "";
      data.forEach(item => themDong(item));
    })
    .catch(err => console.error("❌ Lỗi tải dữ liệu:", err));
}

function themDong(item) {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td>${item.MaThuoc}</td>
    <td>${item.MaDonThuoc}</td>
    <td>${item.SoLuong}</td>
    <td>${item.LieuDung}</td>
    <td>
      <button onclick="batDauSua(this)">Sửa</button>
      <button onclick="xoaChiTiet('${item.MaDonThuoc}', '${item.MaThuoc}')">Xóa</button>
    </td>`;
  table.appendChild(tr);
}

function hienDongMoiChiTiet() {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td>
      <button onclick="luuChiTietMoi(this)">Lưu</button>
      <button onclick="this.closest('tr').remove()">Hủy</button>
    </td>`;
  table.prepend(tr);
}

function luuChiTietMoi(btn) {
  const tr = btn.closest("tr");
  const data = {
    MaThuoc: tr.children[0].innerText,
    MaDonThuoc: tr.children[1].innerText,
    SoLuong: +tr.children[2].innerText,
    LieuDung: tr.children[3].innerText
  };
  fetch(detailAPI, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  }).then(() => taiDanhSachChiTiet());
}

function batDauSua(btn) {
  const tr = btn.closest("tr");
  for (let i = 2; i <= 3; i++) tr.children[i].contentEditable = "true";
  btn.textContent = "Lưu";
  btn.onclick = () => capNhatChiTiet(tr);
}

function capNhatChiTiet(tr) {
  const MaThuoc = tr.children[0].innerText;
  const MaDonThuoc = tr.children[1].innerText;
  const data = {
    SoLuong: +tr.children[2].innerText,
    LieuDung: tr.children[3].innerText
  };
  fetch(`${detailAPI}${MaDonThuoc}/${MaThuoc}`, {
    method: "PUT",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  }).then(() => taiDanhSachChiTiet());
}

function xoaChiTiet(maDon, maThuoc) {
  fetch(`${detailAPI}${maDon}/${maThuoc}`, { method: "DELETE" })
    .then(() => taiDanhSachChiTiet());
}

function timKiemChiTiet() {
  const keyword = document.getElementById("searchDetail").value.toLowerCase();
  fetch(detailAPI)
    .then(res => res.json())
    .then(data => {
      table.innerHTML = "";
      data.filter(item =>
        item.MaThuoc.toLowerCase().includes(keyword) ||
        item.MaDonThuoc.toLowerCase().includes(keyword)
      ).forEach(item => themDong(item));
    });
}

document.addEventListener("DOMContentLoaded", () => {
  taiDanhSachChiTiet();
});
