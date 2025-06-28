const api = "http://localhost:8000/api/v1/drug";
const table = document.querySelector("#thuocTable tbody");

// ✅ Tải danh sách thuốc
function taiDanhSachThuoc() {
  fetch(api)
    .then(res => res.json())
    .then(data => {
      if (!Array.isArray(data)) {
        console.error("API trả về không phải danh sách:", data);
        return;
      }
      table.innerHTML = "";
      data.forEach(thuoc => addRow(thuoc));
    })
    .catch(err => console.error("Lỗi tải dữ liệu:", err));
}

// ✅ Thêm 1 dòng thuốc vào bảng
function addRow(thuoc) {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td>${thuoc.MaThuoc}</td>
    <td contenteditable="false">${thuoc.TenThuoc}</td>
    <td contenteditable="false">${thuoc.DonViTinh}</td>
    <td contenteditable="false">${thuoc.HamLuong}</td>
    <td contenteditable="false">${thuoc.CongDung}</td>
    <td contenteditable="false">${thuoc.SoLuongTon}</td>
    <td contenteditable="false">${thuoc.GiaBan}</td>
    <td contenteditable="false">${thuoc.NgayHetHan || ""}</td>
    <td>
      <button onclick="capNhatThuoc(this)">Sửa</button>
      <button onclick="xoaThuoc('${thuoc.MaThuoc}')">Xóa</button>
    </td>
  `;
  table.appendChild(tr);
}

//  Thêm dòng mới để nhập thuốc
function hienDongThemMoi() {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td>
      <button onclick="luuThuocMoi(this)">Lưu</button>
      <button onclick="this.closest('tr').remove()">Hủy</button>
    </td>
  `;
  table.prepend(tr);
}

// ✅ Gửi API lưu thuốc mới
function luuThuocMoi(btn) {
  const tr = btn.closest("tr");
  const data = {
    MaThuoc: tr.children[0].innerText.trim(),
    TenThuoc: tr.children[1].innerText.trim(),
    DonViTinh: tr.children[2].innerText.trim(),
    HamLuong: tr.children[3].innerText.trim(),
    CongDung: tr.children[4].innerText.trim(),
    SoLuongTon: +tr.children[5].innerText.trim(),
    GiaBan: +tr.children[6].innerText.trim(),
    NgayHetHan: tr.children[7].innerText.trim() || null
  };
  fetch(api, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  }).then(() => taiDanhSachThuoc());
}

// ✅ Gửi API xóa thuốc
function xoaThuoc(ma) {
  fetch(`${api}/${ma}`, { method: "DELETE" })
    .then(() => taiDanhSachThuoc());
}

// ✅ Chế độ sửa / lưu
function capNhatThuoc(btn) {
  const tr = btn.closest("tr");
  const isEditing = btn.innerText === "Sửa";

  // Bật/tắt editable
  for (let i = 1; i <= 7; i++) {
    tr.children[i].setAttribute("contenteditable", isEditing ? "true" : "false");
  }

  if (isEditing) {
    btn.innerText = "Lưu";
  } else {
    const data = {
      TenThuoc: tr.children[1].innerText.trim(),
      DonViTinh: tr.children[2].innerText.trim(),
      HamLuong: tr.children[3].innerText.trim(),
      CongDung: tr.children[4].innerText.trim(),
      SoLuongTon: +tr.children[5].innerText.trim(),
      GiaBan: +tr.children[6].innerText.trim(),
      NgayHetHan: tr.children[7].innerText.trim() || null
    };
    fetch(`${api}/${tr.children[0].innerText}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    }).then(() => taiDanhSachThuoc());
    btn.innerText = "Sửa";
  }
}

// ✅ Tìm kiếm thuốc
function timKiemThuoc() {
  const keyword = document.getElementById("search-input").value.trim();
  if (!keyword) {
    taiDanhSachThuoc();
    return;
  }
  fetch(`${api}/search?keyword=${encodeURIComponent(keyword)}`)
    .then(res => res.json())
    .then(data => {
      table.innerHTML = "";
      data.forEach(thuoc => addRow(thuoc));
    });
}

function hienThiTatCa() {
  document.getElementById("search-input").value = "";
  taiDanhSachThuoc();
}

// ✅ Gọi hàm khi trang load
taiDanhSachThuoc();
