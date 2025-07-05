-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: medical_system
-- ------------------------------------------------------
-- Server version	8.0.41

DROP DATABASE IF EXISTS medical_system;
CREATE DATABASE medical_system;
USE medical_system;

CREATE TABLE `taikhoan` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `tenDangNhap` VARCHAR(100) UNIQUE NOT NULL,
    `matKhau` VARCHAR(255) NOT NULL,
    `vaiTro` VARCHAR(50) NOT NULL
);


-- Table structure for table `bacsi`
DROP TABLE IF EXISTS `bacsi`;
CREATE TABLE `bacsi` (
  `MaBacSi` varchar(10) NOT NULL,
  `HoTen` varchar(100) DEFAULT NULL,
  `NgaySinh` date DEFAULT NULL,
  `ChuyenKhoa` varchar(100) DEFAULT NULL,
  `BangCap` varchar(100) DEFAULT NULL,
  `SoDienThoai` varchar(20) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `TrangThai` varchar(50) DEFAULT NULL,
  `NgayVaoLam` date DEFAULT NULL,
  PRIMARY KEY (`MaBacSi`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `benh`

DROP TABLE IF EXISTS `benh`;
CREATE TABLE `benh` (
  `MaBenh` varchar(10) NOT NULL,
  `TenBenh` varchar(100) DEFAULT NULL,
  `MoTa` text,
  `MaICD` varchar(20) DEFAULT NULL,
  `MaKetQua` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`MaBenh`),
  KEY `MaKetQua` (`MaKetQua`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `benhnhan`

DROP TABLE IF EXISTS `benhnhan`;

CREATE TABLE `benhnhan` (
  `MaBenhNhan` varchar(10) NOT NULL,
  `HoTen` varchar(100) DEFAULT NULL,
  `NgaySinh` date DEFAULT NULL,
  `GioiTinh` enum('F','M') DEFAULT NULL,
  `SoDienThoai` varchar(20) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `DiaChi` text,
  `CCCD` varchar(20) DEFAULT NULL,
  `TienSuBenhLy` text,
  PRIMARY KEY (`MaBenhNhan`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `CCCD` (`CCCD`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `chitietdonthuoc`
DROP TABLE IF EXISTS `chitietdonthuoc`;
CREATE TABLE `chitietdonthuoc` (
  `MaDonThuoc` varchar(10) NOT NULL,
  `MaThuoc` varchar(10) NOT NULL,
  `SoLuong` int DEFAULT NULL,
  `LieuDung` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`MaDonThuoc`,`MaThuoc`),
  KEY `MaThuoc` (`MaThuoc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `donthuoc`
DROP TABLE IF EXISTS `donthuoc`;
CREATE TABLE `donthuoc` (
  `MaDonThuoc` varchar(10) NOT NULL,
  `MaKetQua` varchar(10) DEFAULT NULL,
  `NgayKeDon` date DEFAULT NULL,
  `GhiChu` text,
  PRIMARY KEY (`MaDonThuoc`),
  KEY `MaKetQua` (`MaKetQua`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `ketquakham`
DROP TABLE IF EXISTS `ketquakham`;
CREATE TABLE `ketquakham` (
  `MaKetQua` varchar(10) NOT NULL,
  `MaPhieuKham` varchar(10) DEFAULT NULL,
  `LoaiXetNghiem` varchar(100) DEFAULT NULL,
  `KetQuaXetNghiem` text,
  `NgayThucHien` date DEFAULT NULL,
  `MaBenhNhan` VARCHAR(10),
  PRIMARY KEY (`MaKetQua`),
  UNIQUE KEY `MaPhieuKham` (`MaPhieuKham`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `lichhenkham`
DROP TABLE IF EXISTS `lichhenkham`;
CREATE TABLE `lichhenkham` (
  `MaLichHen` varchar(10) NOT NULL,
  `MaBenhNhan` varchar(10) DEFAULT NULL,
  `MaBacSi` varchar(10) COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `MaLich` varchar(10) DEFAULT NULL,
  `NgayHen` date DEFAULT NULL,
  `GioHen` time DEFAULT NULL,
  `TrangThai` varchar(50) DEFAULT NULL,
  `LyDo` text,
  PRIMARY KEY (`MaLichHen`),
  KEY `MaBenhNhan` (`MaBenhNhan`),
  KEY `MaBacSi` (`MaBacSi`),
  KEY `MaLich` (`MaLich`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `nhanvien`

DROP TABLE IF EXISTS `nhanvien`;
CREATE TABLE `nhanvien` (
  `MaNhanVien` varchar(10) NOT NULL,
  `HoTen` varchar(100) DEFAULT NULL,
  `ChucVu` varchar(50) DEFAULT NULL,
  `SoDienThoai` varchar(20) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `NgayVaoLam` date DEFAULT NULL,
  PRIMARY KEY (`MaNhanVien`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `phieukhambenh`

DROP TABLE IF EXISTS `phieukhambenh`;
CREATE TABLE `phieukhambenh` (
  `MaPhieuKham` varchar(10) NOT NULL,
  `MaBenhNhan` varchar(10) DEFAULT NULL,
  `MaBacSi` varchar(10) DEFAULT NULL,
  `NgayKham` date DEFAULT NULL,
  `TrieuChung` text,
  `ChuanDoan` text,
  `HuongDieuTri` text,
  `MaLichHen` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`MaPhieuKham`),
  KEY `MaBenhNhan` (`MaBenhNhan`),
  KEY `MaBacSi` (`MaBacSi`),
  KEY `MaLichHen` (`MaLichHen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `thanhtoan`

DROP TABLE IF EXISTS `thanhtoan`;

CREATE TABLE `thanhtoan` (
  `MaHoaDon` varchar(10) NOT NULL,
  `MaBenhNhan` varchar(10) DEFAULT NULL,
  `MaKetQua` varchar(10) DEFAULT NULL,
  `LoaiHoaDon` varchar(50) DEFAULT NULL,
  `SoTien` decimal(10,2) DEFAULT NULL,
  `SoTienDaTra` decimal(10,2) DEFAULT NULL,
  `SoTienConNo` decimal(10,2) DEFAULT NULL,
  `ThoiGianThanhToan` datetime DEFAULT NULL,
  `HinhThucThanhToan` varchar(50) DEFAULT NULL,
  `NguoiThuTien` varchar(10) DEFAULT NULL,
  `TrangThai` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`MaHoaDon`),
  KEY `MaBenhNhan` (`MaBenhNhan`),
  KEY `MaKetQua` (`MaKetQua`),
  KEY `NguoiThuTien` (`NguoiThuTien`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `thuoc`

DROP TABLE IF EXISTS `thuoc`;

CREATE TABLE `thuoc` (
  `MaThuoc` varchar(10) NOT NULL,
  `TenThuoc` varchar(100) DEFAULT NULL,
  `DonViTinh` varchar(20) DEFAULT NULL,
  `HamLuong` varchar(50) DEFAULT NULL,
  `CongDung` text,
  `SoLuongTon` int DEFAULT NULL,
  `GiaBan` decimal(10,2) DEFAULT NULL,
  `NgayHetHan` date DEFAULT NULL,
  PRIMARY KEY (`MaThuoc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


ALTER TABLE `chitietdonthuoc`
ADD CONSTRAINT `chitietdonthuoc_ibfk_1` FOREIGN KEY (`MaDonThuoc`) REFERENCES `donthuoc` (`MaDonThuoc`);

ALTER TABLE `chitietdonthuoc`
ADD CONSTRAINT `chitietdonthuoc_ibfk_2` FOREIGN KEY (`MaThuoc`) REFERENCES `thuoc` (`MaThuoc`);

ALTER TABLE `donthuoc`
ADD CONSTRAINT `donthuoc_ibfk_1` FOREIGN KEY (`MaKetQua`) REFERENCES `ketquakham` (`MaKetQua`);

alter table `ketquakham`
add CONSTRAINT `ketquakham_ibfk_1` FOREIGN KEY (`MaPhieuKham`) REFERENCES `phieukhambenh` (`MaPhieuKham`);
ALTER TABLE `ketquakham` ADD CONSTRAINT `fk_benhnhan` FOREIGN KEY (`MaBenhNhan`) REFERENCES `benhnhan`(`MaBenhNhan`);

alter table `benh`
add CONSTRAINT `benh_ibfk_1` FOREIGN KEY (`MaKetQua`) REFERENCES `ketquakham` (`MaKetQua`);
ALTER TABLE `lichhenkham`
ADD CONSTRAINT `lichhenkham_ibfk_1`
FOREIGN KEY (`MaBenhNhan`) REFERENCES `benhnhan` (`MaBenhNhan`);

ALTER TABLE `lichhenkham`
ADD CONSTRAINT `lichhenkham_ibfk_2`
FOREIGN KEY (`MaBacSi`) REFERENCES `bacsi` (`MaBacSi`);

-- ALTER TABLE `lichhenkham`
-- ADD CONSTRAINT `lichhenkham_ibfk_3`
-- FOREIGN KEY (`MaLich`) REFERENCES `lichlamviec` (`MaLich`);

ALTER TABLE `phieukhambenh`
ADD CONSTRAINT `phieukhambenh_ibfk_1`
FOREIGN KEY (`MaBenhNhan`) REFERENCES `benhnhan` (`MaBenhNhan`);

ALTER TABLE `phieukhambenh`
ADD CONSTRAINT `phieukhambenh_ibfk_2`
FOREIGN KEY (`MaBacSi`) REFERENCES `bacsi` (`MaBacSi`);

ALTER TABLE `phieukhambenh`
ADD CONSTRAINT `phieukhambenh_ibfk_3`
FOREIGN KEY (`MaLichHen`) REFERENCES `lichhenkham` (`MaLichHen`)
ON DELETE CASCADE;

ALTER TABLE `thanhtoan`
ADD CONSTRAINT `thanhtoan_ibfk_1`
FOREIGN KEY (`MaBenhNhan`) REFERENCES `benhnhan` (`MaBenhNhan`)
ON DELETE CASCADE;

ALTER TABLE `thanhtoan`
ADD CONSTRAINT `thanhtoan_ibfk_2`
FOREIGN KEY (`MaKetQua`) REFERENCES `ketquakham` (`MaKetQua`)
ON DELETE CASCADE;

ALTER TABLE `thanhtoan`
ADD CONSTRAINT `thanhtoan_ibfk_3`
FOREIGN KEY (`NguoiThuTien`) REFERENCES `nhanvien` (`MaNhanVien`)
ON DELETE CASCADE;
