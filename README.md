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

## 🛠️ Công nghệ sử dụng

- **Frontend**: HTML, CSS, JavaScript (vanilla)
- **Backend**: Python + FastAPI
- **Database**: SQLite / PostgreSQL (tùy chọn)
- **Khác**: PlantUML (sơ đồ ERD), Fetch API (giao tiếp frontend-backend)

---

## 📁 Cấu trúc thư mục

```
📦 medical-system/
├── backend/
│   ├── main.py                  # Điểm khởi động FastAPI
│   ├── core/                    # Cấu hình chung (DB, bảo mật, tiện ích)
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   ├── api/
│   │   ├── v1/
│   │   │   ├── exam/            # Thành viên 1 – Khám bệnh, đơn thuốc
│   │   │   │   ├── routes.py
│   │   │   │   ├── models.py
│   │   │   │   ├── schemas.py
│   │   │   │   └── services.py
│   │   │   ├── patient/         # Thành viên 2 – Bệnh nhân, lịch hẹn
│   │   │   │   ├── routes.py
│   │   │   │   ├── models.py
│   │   │   │   ├── schemas.py
│   │   │   │   └── services.py
│   │   │   ├── auth/            # Thành viên 2 – Đăng nhập
│   │   │   │   └── ...
│   │   │   ├── drug/            # Thành viên 3 – Kho thuốc
│   │   │   │   └── ...
│   │   │   ├── payment/         # Thành viên 3 – Thanh toán
│   │   │   │   └── ...
│   │   │   ├── stats/           # Thành viên 3 – Thống kê & báo cáo
│   │   │   │   └── ...
│   └── requirements.txt

├── frontend/
│   ├── index.html
│   ├── exam/                   # Thành viên 1 – Giao diện khám bệnh
│   │   ├── exam.html
│   │   ├── exam.js
│   │   └── ...
│   ├── patient/                # Thành viên 2 – Bệnh nhân, lịch hẹn
│   │   ├── patient.html
│   │   ├── patient.js
│   │   └── ...
│   ├── auth/                   # Thành viên 2 – Đăng nhập
│   ├── drug/                   # Thành viên 3 – Kho thuốc
│   ├── payment/                # Thành viên 3 – Thanh toán
│   ├── stats/                  # Thành viên 3 – Thống kê
│   └── css/
│       └── style.css

├── database/
│   ├── schema/
│   │   ├── 1_exam.sql          # Thành viên 1 – Phiếu khám, đơn thuốc
│   │   ├── 2_patient.sql       # Thành viên 2 – Bệnh nhân, tài khoản
│   │   ├── 3_drug.sql          # Thành viên 3 – Thuốc, hóa đơn, báo cáo
│   │   └── seed_data.sql       # Dữ liệu mẫu
│   └── erd.puml                # Sơ đồ quan hệ các bảng dùng PlantUML

├── .gitignore
└── README.md
```
-----------------------------
Tên file	Mục đích
models.py	Khai báo model SQLAlchemy cho bảng 
schemas.py	Định nghĩa schema Pydantic
services.py	Xử lý nghiệp vụ CRUD
routes.py	Router FastAPI /api/v1/...
---

## ▶️ Chạy project (demo)

### Backend (FastAPI)
```bash
cd backend/
python -m venv venv
source venv/bin/activate  # hoặc venv\Scripts\activate trên Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
- Mở `index.html` trong trình duyệt 
- Giao tiếp với API bằng `fetch()` từ JS

---

### database
- MySQL
- mysql -u root -p medical_system< database/schema/init.sql
- mysql -u root -p medical_system< database/schema/4_account.sql
* dummy data:
- mysql -u root -p medical_system< database/schema/seed-data.sql

username: admin
password: 123456

---