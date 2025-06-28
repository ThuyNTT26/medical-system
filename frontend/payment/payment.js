const paymentAPI = "http://localhost:8000/api/v1/payment";
const table = document.querySelector("#bangThanhToan tbody");

function taiDanhSachThanhToan() {
  fetch(paymentAPI)
    .then(res => {
      if (!res.ok) throw new Error("Không lấy được dữ liệu");
      return res.json();
    })
    .then(data => {
      table.innerHTML = "";
      data.forEach(hoaDon => themDong(hoaDon));
    })
    .catch(err => {
      console.error("Lỗi khi tải dữ liệu:", err);
    });
}

function themDong(hoaDon) {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td contenteditable="false">${hoaDon.MaHoaDon}</td>
    <td contenteditable="false">${hoaDon.MaBenhNhan}</td>
    <td contenteditable="false">${hoaDon.MaKetQua || ""}</td>
    <td contenteditable="false">${hoaDon.LoaiHoaDon}</td>
    <td contenteditable="false">${hoaDon.SoTien}</td>
    <td contenteditable="false">${hoaDon.SoTienDaTra || 0}</td>
    <td contenteditable="false">${hoaDon.SoTienConNo || 0}</td>
    <td contenteditable="false">${hoaDon.ThoiGianThanhToan}</td>
    <td contenteditable="false">${hoaDon.HinhThucThanhToan}</td>
    <td contenteditable="false">${hoaDon.MaNhanVien || ""}</td>
    <td contenteditable="false">${hoaDon.TrangThai}</td>
    <td>
      <button onclick="batDauSua(this)">Sửa</button>
      <button onclick="xoaHoaDon('${hoaDon.MaHoaDon}')">Xóa</button>
    </td>
  `;
  table.appendChild(tr);
}

function hienDongMoiThanhToan() {
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
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td>
      <button onclick="luuHoaDonMoi(this)">Lưu</button>
      <button onclick="this.closest('tr').remove()">Hủy</button>
    </td>
  `;
  table.prepend(tr);
}

function luuHoaDonMoi(btn) {
  const tr = btn.closest("tr");
  const data = {
    MaHoaDon: tr.children[0].innerText,
    MaBenhNhan: tr.children[1].innerText,
    MaKetQua: tr.children[2].innerText || null,
    LoaiHoaDon: tr.children[3].innerText,
    SoTien: +tr.children[4].innerText,
    SoTienDaTra: +tr.children[5].innerText || 0,
    SoTienConNo: +tr.children[6].innerText || 0,
    ThoiGianThanhToan: tr.children[7].innerText,
    HinhThucThanhToan: tr.children[8].innerText,
    MaNhanVien: tr.children[9].innerText || null,
    TrangThai: tr.children[10].innerText
  };
  fetch(paymentAPI, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  }).then(() => taiDanhSachThanhToan());
}

function batDauSua(btn) {
  const tr = btn.closest("tr");
  for (let i = 1; i <= 10; i++) {
    tr.children[i].setAttribute("contenteditable", "true");
  }
  btn.textContent = "Lưu";
  btn.onclick = () => capNhatHoaDon(tr);
}

function capNhatHoaDon(tr) {
  const data = {
    MaBenhNhan: tr.children[1].innerText,
    MaKetQua: tr.children[2].innerText || null,
    LoaiHoaDon: tr.children[3].innerText,
    SoTien: +tr.children[4].innerText,
    SoTienDaTra: +tr.children[5].innerText || 0,
    SoTienConNo: +tr.children[6].innerText || 0,
    ThoiGianThanhToan: tr.children[7].innerText,
    HinhThucThanhToan: tr.children[8].innerText,
    MaNhanVien: tr.children[9].innerText || null,
    TrangThai: tr.children[10].innerText
  };
  fetch(`${paymentAPI}/${tr.children[0].innerText}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  }).then(() => taiDanhSachThanhToan());
}

function xoaHoaDon(ma) {
  fetch(`${paymentAPI}/${ma}`, { method: "DELETE" })
    .then(() => taiDanhSachThanhToan());
}

function timKiemHoaDon() {
  const keyword = document.getElementById("searchBill").value;
  fetch(`${paymentAPI}/search?keyword=${keyword}`)
    .then(res => res.json())
    .then(data => {
      table.innerHTML = "";
      data.forEach(hoaDon => themDong(hoaDon));
    });
}

taiDanhSachThanhToan();
