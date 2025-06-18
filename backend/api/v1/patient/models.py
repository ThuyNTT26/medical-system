from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.core.database import Base

class BenhNhan(Base):
    __tablename__ = "benhnhan"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=True)

    appointments = relationship("LichHen", back_populates="patient")

class LichHen(Base):
    __tablename__ = "lichhen"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("benhnhan.id"))
    date = Column(DateTime, nullable=False)
    reason = Column(String, nullable=True)

    patient = relationship("BenhNhan", back_populates="appointments")
