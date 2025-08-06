"""SQLAlchemy models for Warehouse."""

from sqlalchemy import Column, Integer, String
from app.database import Base


class Warehouse(Base):
    __tablename__ = "warehouses"

    WarehouseID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100), nullable=False, unique=True)
    Location = Column(String(255))
