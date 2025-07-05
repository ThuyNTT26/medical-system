REATE DATABASE IF NOT EXISTS `clinic_management`;


USE `clinic_management`;


CREATE TABLE IF NOT EXISTS `VaiTro` (
    `MaVaiTro` VARCHAR(50) PRIMARY KEY NOT NULL,
    `TenVaiTro` VARCHAR(100) NOT NULL UNIQUE,
    `MoTa` TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


INSERT IGNORE INTO `VaiTro` (`MaVaiTro`, `TenVaiTro`, `MoTa`) VALUES
('ADMIN', 'Quản trị viên', 'Quyền hạn cao nhất trong hệ thống'),
('BACSI', 'Bác sĩ', 'Quản lý lịch làm việc, thông tin bệnh nhân, kê đơn'),
('NHANVIEN', 'Nhân viên phòng khám', 'Hỗ trợ các công việc hành chính, tiếp đón'),
('LETAN', 'Lễ tân', 'Tiếp đón bệnh nhân, đặt lịch hẹn');


CREATE TABLE IF NOT EXISTS `NhanVien` (
    `MaNhanVien` VARCHAR(50) PRIMARY KEY NOT NULL,
    `TenNhanVien` VARCHAR(255) NOT NULL,
    `NgaySinh` DATE,
    `GioiTinh` ENUM('Nam', 'Nữ', 'Khác'),
    `DiaChi` VARCHAR(255),
    `SoDienThoai` VARCHAR(20),
    `Email` VARCHAR(100) UNIQUE,
    `MaVaiTro` VARCHAR(50) NOT NULL, 
    `NgayVaoLam` DATE DEFAULT CURRENT_DATE,
    `TrangThai` ENUM('Đang làm việc', 'Đã nghỉ việc') DEFAULT 'Đang làm việc',
    FOREIGN KEY (`MaVaiTro`) REFERENCES `VaiTro`(`MaVaiTro`) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


INSERT IGNORE INTO `NhanVien` (`MaNhanVien`, `TenNhanVien`, `NgaySinh`, `GioiTinh`, `DiaChi`, `SoDienThoai`, `Email`, `MaVaiTro`, `NgayVaoLam`, `TrangThai`) VALUES
('NV001', 'Nguyễn Thị Hoa', '1985-05-10', 'Nữ', '123 Đường ABC, Q1, TP.HCM', '0912345678', 'hoa.nguyen@clinic.com', 'LETAN', '2020-01-15', 'Đang làm việc'),
('NV002', 'Lê Văn Cường', '1990-11-22', 'Nam', '456 Đường XYZ, Q3, TP.HCM', '0987654321', 'cuong.le@clinic.com', 'NHANVIEN', '2021-03-01', 'Đang làm việc');



CREATE TABLE IF NOT EXISTS `BacSi` (
    `MaBacSi` VARCHAR(50) PRIMARY KEY NOT NULL,
    `MaNhanVien` VARCHAR(50) NOT NULL UNIQUE,
    `ChuyenKhoa` VARCHAR(255) NOT NULL,
    `HocVi` VARCHAR(100),
    `KinhNghiem` TEXT,
    FOREIGN KEY (`MaNhanVien`) REFERENCES `NhanVien`(`MaNhanVien`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


INSERT IGNORE INTO `NhanVien` (`MaNhanVien`, `TenNhanVien`, `NgaySinh`, `GioiTinh`, `DiaChi`, `SoDienThoai`, `Email`, `MaVaiTro`, `NgayVaoLam`, `TrangThai`) VALUES
('NV003', 'Nguyễn Văn A', '1978-03-15', 'Nam', '789 Đường DEF, Q5, TP.HCM', '0901234567', 'vana@clinic.com', 'BACSI', '2015-07-01', 'Đang làm việc'),
('NV004', 'Trần Thị B', '1982-09-20', 'Nữ', '101 Đường GHI, Q7, TP.HCM', '0907654321', 'thib@clinic.com', 'BACSI', '2018-02-10', 'Đang làm việc');

INSERT IGNORE INTO `BacSi` (`MaBacSi`, `MaNhanVien`, `ChuyenKhoa`, `HocVi`, `KinhNghiem`) VALUES
('BS001', 'NV003', 'Nội tổng quát', 'Thạc sĩ Y khoa', '15 năm kinh nghiệm khám chữa bệnh tổng quát'),
('BS002', 'NV004', 'Nhi khoa', 'Tiến sĩ Y khoa', '10 năm kinh nghiệm trong lĩnh vực nhi khoa');



CREATE TABLE IF NOT EXISTS `LichLamViec` (
    `MaLich` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `MaBacSi` VARCHAR(50) NOT NULL, 
    `NgayLamViec` DATE NOT NULL,
    `GioBatDau` TIME NOT NULL,
    `GioKetThuc` TIME NOT NULL,
    `PhongKham` VARCHAR(100),
    `TrangThai` ENUM('Đã lên lịch', 'Đã hủy', 'Đã hoàn thành') DEFAULT 'Đã lên lịch',
    FOREIGN KEY (`MaBacSi`) REFERENCES `BacSi`(`MaBacSi`) ON UPDATE CASCADE ON DELETE CASCADE,
    UNIQUE (`MaBacSi`, `NgayLamViec`, `GioBatDau`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


INSERT IGNORE INTO `LichLamViec` (`MaBacSi`, `NgayLamViec`, `GioBatDau`, `GioKetThuc`, `PhongKham`, `TrangThai`) VALUES
('BS001', '2025-07-07', '08:00:00', '12:00:00', 'Phòng 101', 'Đã lên lịch'),
('BS001', '2025-07-07', '13:00:00', '17:00:00', 'Phòng 101', 'Đã lên lịch'),
('BS002', '2025-07-08', '09:00:00', '16:00:00', 'Phòng 203', 'Đã lên lịch');
CREATE TABLE IF NOT EXISTS `Benh` (
    `MaBenh` VARCHAR(50) PRIMARY KEY NOT NULL,
    `TenBenh` VARCHAR(255) NOT NULL UNIQUE,
    `MaICD` VARCHAR(50) UNIQUE,
    `MoTa` TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
INSERT IGNORE INTO `Benh` (`MaBenh`, `TenBenh`, `MaICD`, `MoTa`) VALUES
('BENH001', 'Cúm mùa', 'J11', 'Bệnh nhiễm trùng đường hô hấp cấp tính do virus cúm gây ra.'),
('BENH002', 'Viêm họng cấp', 'J02.9', 'Viêm cấp tính của họng, không xác định.'),
('BENH003', 'Đau dạ dày', 'K29.7', 'Viêm dạ dày, không đặc hiệu.');
CREATE TABLE IF NOT EXISTS `LichSuLamViecNhanVien` (
    `MaLichSu` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `MaNhanVien` VARCHAR(50) NOT NULL,
    `ThoiGian` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `LoaiSuKien` VARCHAR(100), 
    `MoTaChiTiet` TEXT,
    FOREIGN KEY (`MaNhanVien`) REFERENCES `NhanVien`(`MaNhanVien`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
INSERT IGNORE INTO `LichSuLamViecNhanVien` (`MaNhanVien`, `ThoiGian`, `LoaiSuKien`, `MoTaChiTiet`) VALUES
('NV001', '2025-07-04 08:00:00', 'Chấm công vào', 'Nhân viên NV001 bắt đầu ca làm việc.'),
('NV001', '2025-07-04 17:00:00', 'Chấm công ra', 'Nhân viên NV001 kết thúc ca làm việc.'),
('NV003', '2025-07-04 08:30:00', 'Đăng nhập hệ thống', 'Bác sĩ NV003 đăng nhập để xem lịch hẹn.');
CREATE TABLE IF NOT EXISTS `BenhNhan` (
    `MaBenhNhan` VARCHAR(50) PRIMARY KEY NOT NULL,
    `TenBenhNhan` VARCHAR(255) NOT NULL,
    `NgaySinh` DATE,
    `GioiTinh` ENUM('Nam', 'Nữ', 'Khác'),
    `DiaChi` VARCHAR(255),
    `SoDienThoai` VARCHAR(20),
    `Email` VARCHAR(100) UNIQUE,
    `NgayDangKy` DATE DEFAULT CURRENT_DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
INSERT IGNORE INTO `BenhNhan` (`MaBenhNhan`, `TenBenhNhan`, `NgaySinh`, `GioiTinh`, `DiaChi`, `SoDienThoai`, `Email`, `NgayDangKy`) VALUES
('BN001', 'Phạm Thị C', '1995-01-20', 'Nữ', '789 Đường K, Q Bình Thạnh, TP.HCM', '0911223344', 'phamc@example.com', '2024-06-01'),
('BN002', 'Đỗ Văn D', '1980-12-05', 'Nam', '101 Đường L, Q Gò Vấp, TP.HCM', '0922334455', 'dod@example.com', '2024-06-15');
CREATE TABLE IF NOT EXISTS `CuocHen` (
    `MaCuocHen` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `MaBenhNhan` VARCHAR(50) NOT NULL,
    `MaBacSi` VARCHAR(50) NOT NULL,
    `ThoiGianHen` DATETIME NOT NULL,
    `LyDoKham` TEXT,
    `TrangThai` ENUM('Đã đặt', 'Đã xác nhận', 'Đã hủy', 'Đã hoàn thành') DEFAULT 'Đã đặt',
    `GhiChu` TEXT,
    FOREIGN KEY (`MaBenhNhan`) REFERENCES `BenhNhan`(`MaBenhNhan`) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (`MaBacSi`) REFERENCES `BacSi`(`MaBacSi`) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
INSERT IGNORE INTO `CuocHen` (`MaBenhNhan`, `MaBacSi`, `ThoiGianHen`, `LyDoKham`, `TrangThai`) VALUES
('BN001', 'BS001', '2025-07-07 09:00:00', 'Khám tổng quát định kỳ', 'Đã đặt'),
('BN002', 'BS002', '2025-07-08 10:30:00', 'Kiểm tra sức khỏe cho bé', 'Đã xác nhận');
CREATE TABLE IF NOT EXISTS `HoSoBenhAn` (
    `MaHoSo` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `MaBenhNhan` VARCHAR(50) NOT NULL,
    `MaBacSi` VARCHAR(50) NOT NULL,
    `NgayKham` DATE NOT NULL,
    `ChuanDoan` TEXT,
    `MaBenh` VARCHAR(50),
    `PhuongPhapDieuTri` TEXT,
    `DonThuoc` TEXT,
    `GhiChu` TEXT,
    FOREIGN KEY (`MaBenhNhan`) REFERENCES `BenhNhan`(`MaBenhNhan`) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (`MaBacSi`) REFERENCES `BacSi`(`MaBacSi`) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (`MaBenh`) REFERENCES `Benh`(`MaBenh`) ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
INSERT IGNORE INTO `HoSoBenhAn` (`MaBenhNhan`, `MaBacSi`, `NgayKham`, `ChuanDoan`, `MaBenh`, `PhuongPhapDieuTri`, `DonThuoc`, `GhiChu`) VALUES
('BN001', 'BS001', '2025-07-07', 'Nhiễm cúm mùa', 'BENH001', 'Nghỉ ngơi, uống thuốc hạ sốt, bù nước.', 'Paracetamol 500mg (1 viên/lần, 2 lần/ngày)', 'Tái khám sau 3 ngày nếu không đỡ.');
