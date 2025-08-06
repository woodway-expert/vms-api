"""SQLAlchemy models for Supplier."""

from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    SupplierID = Column(Integer, primary_key=True, index=True)
    CompanyName = Column(String(100), nullable=False, unique=True)
    ContactName = Column(String(100))
    Phone = Column(String(50))
    Email = Column(String(100), unique=True)
    IsActive = Column(Boolean, default=True)
