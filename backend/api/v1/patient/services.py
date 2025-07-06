from sqlalchemy.orm import Session
from sqlalchemy import text
from . import schemas
from backend.api.v1.appointment.schemas import LichHenCreate
from fastapi import HTTPException

def get_all(db: Session):
    rows = db.execute(text("SELECT * FROM `benhnhan`")).mappings().all()
    return [schemas.BenhNhanOut(**row) for row in rows]

def get_by_id(db: Session, ma_benh_nhan: str):
    result = db.execute(
        text("SELECT * FROM `benhnhan` WHERE `MaBenhNhan` = :ma"),
        {"ma": ma_benh_nhan}
    ).mappings().first()
    return result

def create(db: Session, data: schemas.BenhNhanCreate):
    max_code = db.execute(text("SELECT `MaBenhNhan` FROM `benhnhan` ORDER BY `MaBenhNhan` DESC LIMIT 1")).scalar()
    if max_code:
        max_number = int(max_code[2:])
    else:
        max_number = 0

    new_code = f"BN{max_number + 1:03d}"

    db.execute(text('''
        INSERT INTO `benhnhan` (
            `MaBenhNhan`, `hoTen`, `ngaySinh`, `gioiTinh`, `soDienThoai`,
            `email`, `diaChi`, `cccd`, `tienSuBenhLy`
        ) VALUES (
            :ma, :hoTen, :ngaySinh, :gioiTinh, :soDienThoai,
            :email, :diaChi, :cccd, :tienSuBenhLy
        )
    '''), {
        "ma": new_code,
        **data.dict()
    })
    db.commit()
    return get_by_id(db, new_code)

def update(db: Session, ma_benh_nhan: str, data: schemas.BenhNhanUpdate):
    update_fields = ", ".join([f"{key} = :{key}" for key in data.dict(exclude_unset=True).keys()])
    values = data.dict(exclude_unset=True)
    values["ma"] = ma_benh_nhan

    db.execute(
        text(f"UPDATE `benhnhan` SET {update_fields} WHERE `MaBenhNhan` = :ma"),
        values
    )
    db.commit()
    return get_by_id(db, ma_benh_nhan)

def delete(db: Session, ma_benh_nhan: str):
    result = get_by_id(db, ma_benh_nhan)
    if result:
        db.execute(
            text("DELETE FROM `benhnhan` WHERE `MaBenhNhan` = :ma"),
            {"ma": ma_benh_nhan}
        )
        db.commit()
    return result

def get_hoso_chi_tiet(db: Session, ma_benh_nhan: str):
    print("🔍 Lấy hồ sơ cho:", ma_benh_nhan)
    bn = get_by_id(db, ma_benh_nhan)
    if not bn:
        raise HTTPException(status_code=404, detail="Không tìm thấy bệnh nhân")

    try:
        lich_su_raw = db.execute(text('''
            SELECT `MaLichHen`, `NgayHen`, `LyDo` FROM `lichhenkham`
            WHERE `MaBenhNhan` = :ma
        '''), {"ma": ma_benh_nhan}).mappings().all()

        lich_su = [
            schemas.LichHenOutHistory(
                MaLichHen=row["MaLichHen"],
                ngay_kham=row["NgayHen"],
                ly_do=row["LyDo"]
            ) for row in lich_su_raw
        ]
    except Exception as e:
        print("❌ Lỗi lịch sử khám:", e)
        lich_su = []

    try:
        ket_qua = db.execute(text('''
        SELECT `ChanDoan`, `GhiChu` FROM `ketquakham`
        WHERE `MaPhieuKham` IN (
            SELECT `MaLichHen` FROM `lichhenkham`
            WHERE `MaBenhNhan` = :ma
        )
    '''), {"ma": ma_benh_nhan}).mappings().all()

    except Exception as e:
        print("❌ Lỗi kết quả khám:", e)
        ket_qua = []

    try:
        don_thuoc = db.execute(text('''
        SELECT `Thuoc`, `LieuLuong` FROM `donthuoc`
        WHERE `MaKetQua` IN (
            SELECT `MaKetQua` FROM `ketquakham`
            WHERE `MaPhieuKham` IN (
                SELECT `MaLichHen` FROM `lichhenkham`
                WHERE `MaBenhNhan` = :ma
            )
        )
    '''), {"ma": ma_benh_nhan}).mappings().all()
    except Exception as e:
        print("❌ Lỗi đơn thuốc:", e)
        don_thuoc = []

    

    return {
        "benh_nhan": bn,
        "lich_su": lich_su,
        "ket_qua": ket_qua,
        "don_thuoc": don_thuoc,
    }









def get_lichhen(db: Session):
    return db.execute(text("SELECT * FROM `lichhenkham`"))\
             .mappings().all()

def create_lichhen(db: Session, lichhen: LichHenCreate):
    db.execute(text('''
        INSERT INTO `lichhenkham` (
            `MaLichHen`, `MaBenhNhan`, `MaBacSi`, `MaLich`, `NgayHen`,
            `GioHen`, `TrangThai`, `LyDo`
        ) VALUES (
            :MaLichHen, :MaBenhNhan, :MaBacSi, :MaLich, :NgayHen,
            :GioHen, :TrangThai, :LyDo
        )
    '''), lichhen.dict())
    db.commit()
    return db.execute(text("SELECT * FROM `lichhenkham` WHERE `MaLichHen` = :ma"),
                      {"ma": lichhen.MaLichHen}).mappings().first()
