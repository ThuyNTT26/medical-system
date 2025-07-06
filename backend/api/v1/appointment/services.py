from sqlalchemy import text
from sqlalchemy.orm import Session
from . import schemas

def _convert_time_fields(rows):
    from datetime import timedelta, time
    new_rows = []
    for row in rows:
        row_dict = dict(row)
        gio_hen = row_dict.get("GioHen")
        if isinstance(gio_hen, timedelta):
            total_seconds = int(gio_hen.total_seconds())
            row_dict["GioHen"] = time(
                hour=total_seconds // 3600,
                minute=(total_seconds % 3600) // 60,
                second=(total_seconds % 60)
            )
        new_rows.append(row_dict)
    return new_rows


def get_all(db: Session):
    result = db.execute(text("SELECT * FROM `lichhenkham`")).mappings().all()
    return _convert_time_fields(result)


def get_by_id(db: Session, id: str):
    result = db.execute(
        text("SELECT * FROM `lichhenkham` WHERE `MaLichHen` = :id"),
        {"id": id}
    ).mappings().first()
    if result:
        return _convert_time_fields([result])[0]
    return None


def create(db: Session, data: schemas.LichHenCreate):
    # Sinh mã mới duy nhất
    result = db.execute(text("SELECT MAX(CAST(SUBSTRING(`MaLichHen`, 3) AS UNSIGNED)) AS max_ma FROM `lichhenkham`")).mappings().first()
    max_ma = result["max_ma"] or 0
    maLH = f"LH{max_ma + 1:03d}"

    db.execute(
        text("""
            INSERT INTO `lichhenkham` (`MaLichHen`, `MaBenhNhan`, `MaBacSi`, `MaLich`, `NgayHen`, `GioHen`, `TrangThai`, `LyDo`)
            VALUES (:ma, :ma_benh_nhan, :ma_bac_si, :ma_lich, :ngay_hen, :gio_hen, :trang_thai, :ly_do)
        """),
        {
            "ma": maLH,
            "ma_benh_nhan": data.MaBenhNhan,
            "ma_bac_si": data.MaBacSi,
            "ma_lich": data.MaLich or maLH,
            "ngay_hen": data.NgayHen,
            "gio_hen": data.GioHen,
            "trang_thai": data.TrangThai,
            "ly_do": data.LyDo
        }
    )
    db.commit()
    return get_by_id(db, maLH)



def update(db: Session, ma_lich_hen: str, data: schemas.LichHenCreate):
    db.execute(
        text("""
            UPDATE `lichhenkham`
            SET `MaBenhNhan` = :ma_benh_nhan,
                `MaBacSi` = :ma_bac_si,
                `MaLich` = :ma_lich,
                `NgayHen` = :ngay_hen,
                `GioHen` = :gio_hen,
                `TrangThai` = :trang_thai,
                `LyDo` = :ly_do
            WHERE `MaLichHen` = :ma
        """),
        {
            "ma": ma_lich_hen,
            "ma_benh_nhan": data.MaBenhNhan,
            "ma_bac_si": data.MaBacSi,
            "ma_lich": data.MaLich,
            "ngay_hen": data.NgayHen,
            "gio_hen": data.GioHen,
            "trang_thai": data.TrangThai,
            "ly_do": data.LyDo
        }
    )
    db.commit()
    return get_by_id(db, ma_lich_hen)


def delete(db: Session, id: str):
    db.execute(
        text("DELETE FROM `lichhenkham` WHERE `MaLichHen` = :id"),
        {"id": id}
    )
    db.commit()
    return True
