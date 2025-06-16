-- ============================
-- BỆNH NHÂN
-- ============================
INSERT INTO BenhNhan (id, hoTen, ngaySinh, gioiTinh, soDienThoai, diaChi)
VALUES 
(1, 'Nguyễn Văn A', '1990-01-01', 'Nam', '0909123456', 'Hà Nội'),
(2, 'Trần Thị B', '1985-05-12', 'Nữ', '0912345678', 'TP.HCM');

-- ============================
-- BÁC SĨ
-- ============================
INSERT INTO BacSi (id, hoTen, chuyenKhoa, soDienThoai)
VALUES 
(1, 'Dr. Lê Văn C', 'Nội tổng quát', '0909988776'),
(2, 'Dr. Phạm Thị D', 'Nhi khoa', '0988776655');

-- ============================
-- NHÂN VIÊN
-- ============================
INSERT INTO NhanVien (id, hoTen, chucVu, soDienThoai)
VALUES 
(1, 'Nguyễn Văn E', 'Lễ tân', '0911223344');

-- ============================
-- TÀI KHOẢN
-- user_type: 'benhnhan' / 'bacsi' / 'nhanvien'
-- ============================
INSERT INTO TaiKhoan (id, tenDangNhap, matKhau, vaiTro, user_id, user_type)
VALUES 
(1, 'a_nguyen', 'hashed_pass_1', 'benhnhan', 1, 'benhnhan'),
(2, 'b_tran', 'hashed_pass_2', 'benhnhan', 2, 'benhnhan'),
(3, 'dr_le', 'hashed_pass_3', 'bacsi', 1, 'bacsi'),
(4, 'nv_nguyen', 'hashed_pass_4', 'nhanvien', 1, 'nhanvien');

-- ============================
-- LỊCH HẸN
-- ============================
INSERT INTO LichHen (id, benhNhan_id, ngayHen, gioHen, trangThai)
VALUES 
(1, 1, '2025-06-20', '09:00:00', 'Đã xác nhận'),
(2, 2, '2025-06-21', '14:00:00', 'Đang chờ');

-- ============================
-- PHIẾU KHÁM
-- ============================
INSERT INTO PhieuKham (id, benhNhan_id, bacSi_id, ngayKham, trieuChung, chuanDoan)
VALUES 
(1, 1, 1, '2025-06-20', 'Sốt, ho nhẹ', 'Cảm cúm'),
(2, 2, 2, '2025-06-21', 'Sốt cao, đau họng', 'Viêm họng');

-- ============================
-- KẾT QUẢ KHÁM
-- ============================
INSERT INTO KetQuaKham (id, phieuKham_id, chiTiet)
VALUES 
(1, 1, 'Xét nghiệm máu bình thường. Không dấu hiệu viêm'),
(2, 2, 'Có dấu hiệu nhiễm khuẩn, cần theo dõi thêm');

-- ============================
-- THUỐC
-- ============================
INSERT INTO Thuoc (id, tenThuoc, donVi, gia)
VALUES 
(1, 'Paracetamol 500mg', 'viên', 1000),
(2, 'Amoxicillin 500mg', 'viên', 1500);

-- ============================
-- ĐƠN THUỐC
-- ============================
INSERT INTO DonThuoc (id, phieuKham_id, ngayKe)
VALUES 
(1, 1, '2025-06-20'),
(2, 2, '2025-06-21');

-- ============================
-- CHI TIẾT ĐƠN THUỐC
-- ============================
INSERT INTO ChiTietDonThuoc (id, donThuoc_id, thuoc_id, lieuDung, soLuong)
VALUES 
(1, 1, 1, 'Uống 2 viên/ngày', 10),
(2, 2, 2, 'Uống 1 viên x 3 lần/ngày', 6);

-- ============================
-- THANH TOÁN
-- ============================
INSERT INTO ThanhToan (id, phieuKham_id, tienThuoc, tienKham, tongTien, ngayGio)
VALUES 
(1, 1, 10000, 50000, 60000, '2025-06-20 10:00:00'),
(2, 2, 9000, 50000, 59000, '2025-06-21 15:00:00');
