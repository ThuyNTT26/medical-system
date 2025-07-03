from backend.core.database import SessionLocal
from backend.api.v1.phieukhambenh.models import PhieuKhamBenh
from backend.api.v1.Ketquakham.models import KetQuaKham
from backend.api.v1.donthuoc.models import DonThuoc
from backend.api.v1.benh.models import Benh
from backend.api.v1.thuoc.models import Thuoc
from datetime import date

def seed():
    db = SessionLocal()

    # 1. Thêm thuốc mẫu
    if not db.query(Thuoc).first():
        thuoc = Thuoc(
            MaThuoc="T001",
            TenThuoc="Paracetamol",
            DonViTinh="viên",
            HamLuong="500mg",
            CongDung="Hạ sốt, giảm đau",
            SoLuongTon=100,
            GiaBan=3000,
            NgayHetHan=date(2026, 1, 1)
        )
        db.add(thuoc)
        print("✅ Thêm thuốc mẫu.")

    # 2. Thêm phiếu khám bệnh
    if not db.query(PhieuKhamBenh).first():
        phieu = PhieuKhamBenh(
            MaPhieuKham="PK001",
            MaBenhNhan="BN001",
            MaBacSi="BS001",
            NgayKham=date.today(),
            TrieuChung="Sốt, ho nhẹ",
            ChuanDoan="Cảm lạnh",
            HuongDieuTri="Nghỉ ngơi, uống nhiều nước",
            MaLichHen="LH001"
        )
        db.add(phieu)
        print("✅ Thêm phiếu khám.")

    # 3. Thêm kết quả khám
    if not db.query(KetQuaKham).first():
        ketqua = KetQuaKham(
            MaKetQua="KQ001",
            MaPhieuKham="PK001",
            LoaiXetNghiem="Xét nghiệm máu",
            KetQuaXetNghiem="Bình thường",
            NgayThucHien=date.today()
        )
        db.add(ketqua)
        print("✅ Thêm kết quả khám.")

    # 4. Thêm đơn thuốc
    if not db.query(DonThuoc).first():
        don = DonThuoc(
            MaDonThuoc="DT001",
            MaKetQua="KQ001",
            NgayKeDon=date.today(),
            GhiChu="Uống sau ăn"
        )
        db.add(don)
        print("✅ Thêm đơn thuốc.")

    # 5. Thêm bệnh liên quan
    if not db.query(Benh).first():
        benh = Benh(
            MaBenh="B001",
            TenBenh="Cảm lạnh",
            MoTa="Bệnh virus thường gặp",
            MaICD="J00",
            MaKetQua="KQ001"
        )
        db.add(benh)
        print("✅ Thêm bệnh mẫu.")

    db.commit()
    db.close()
    print("🎉 Seed dữ liệu hoàn tất.")

if __name__ == "__main__":
    seed()
