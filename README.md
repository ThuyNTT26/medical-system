# 🏥 HỆ THỐNG QUẢN LÝ KHÁM BỆNH – BÀI TẬP LỚN

## 📌 Tổng quan
Đây là bài tập lớn xây dựng hệ thống quản lý khám bệnh đa chức năng, chia thành 3 phần chính tương ứng với vai trò của 3 thành viên. Hệ thống bao gồm các chức năng quản lý bệnh nhân, lịch hẹn, khám bệnh, kê đơn thuốc, kho thuốc, thanh toán, thống kê và phân quyền người dùng.

---

## 🧩 Phân công chức năng theo nhóm

### 👨‍⚕️ Thành viên 1 – KHÁM BỆNH & ĐƠN THUỐC
- Quản lý phiếu khám (`PhieuKham`)
- Ghi nhận kết quả khám, xét nghiệm (`KetQuaKham`)
- Kê đơn thuốc (`DonThuoc`, `ChiTietDonThuoc`)
- Xem lại lịch sử khám và đơn thuốc

### 👩‍💼 Thành viên 2 – BỆNH NHÂN, LỊCH HẸN, ĐĂNG NHẬP & PHÂN QUYỀN
- Quản lý thông tin bệnh nhân (`BenhNhan`)
- Quản lý lịch hẹn khám bệnh (`LichHen`)
- Quản lý tài khoản người dùng (`TaiKhoan`)
- Đăng nhập, phân quyền bác sĩ, lễ tân, quản trị

### 💊 Thành viên 3 – KHO THUỐC, THANH TOÁN, THỐNG KÊ & BÁO CÁO
- Quản lý danh mục thuốc và kho (`Thuoc`)
- Quản lý hoá đơn thanh toán (`ThanhToan`)
- Thống kê đơn thuốc, doanh thu, thuốc sử dụng
- Báo cáo dữ liệu theo thời gian

---

## ❓ 5W – Phân tích yêu cầu

### ✅ WHAT – Hệ thống gồm những gì?
- Giao diện website HTML/CSS/JS
- Backend API viết bằng FastAPI
- Cơ sở dữ liệu SQL chứa toàn bộ thông tin liên quan đến bệnh nhân, đơn thuốc, thanh toán,...
- Các module phân chia rõ ràng theo chức năng của từng thành viên

### 💡 WHY – Mục đích?
- Hỗ trợ phòng khám quản lý thông tin hiệu quả, giảm thời gian thao tác giấy tờ
- Đảm bảo thông tin được lưu trữ an toàn, truy xuất dễ dàng
- Phân quyền rõ ràng theo chức năng: bác sĩ, lễ tân, quản trị viên
- Tự động hoá quá trình thống kê, báo cáo

### 👥 WHO – Ai sử dụng?
- **Bác sĩ**: khám, kê đơn, tra cứu lịch sử bệnh án
- **Lễ tân**: tạo lịch hẹn, cập nhật hồ sơ bệnh nhân
- **Quản trị viên**: phân quyền, thống kê, báo cáo
- **Nhân viên kho**: xuất nhập thuốc, xử lý đơn thuốc
- **(Mở rộng)**: bệnh nhân truy cập lịch sử và kết quả khám

### 🌐 WHERE – Hệ thống triển khai ở đâu?
- Website nội bộ của phòng khám (local LAN hoặc triển khai cloud)
- Server backend chạy FastAPI
- Giao diện frontend HTML đơn giản, dễ triển khai

### 📅 WHEN – Sử dụng khi nào?
- Mỗi ngày trong hoạt động khám bệnh: tiếp nhận → khám → kê đơn → thanh toán
- Khi cần thống kê doanh thu, số lượng bệnh, thuốc sử dụng
- Khi tra cứu lịch sử khám chữa bệnh

---

## ⚙️ Công nghệ sử dụng

| Thành phần | Công nghệ |
|------------|-----------|
| Frontend   | HTML, CSS, JavaScript |
| Backend    | FastAPI (Python) |
| Database   | SQL (MySQL hoặc PostgreSQL) |

---

