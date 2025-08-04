from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship

from app.database import Base


class Customer(Base):
    __tablename__ = "Customers"

    CustomerID = Column(Integer, primary_key=True, index=True)
    CompanyName = Column(String(50), nullable=True)
    ContactName = Column(String(30), nullable=True)
    Phone = Column(String(20), nullable=True)
    EMail = Column(String(40), nullable=True)
    City = Column(String(20), nullable=True)
    Address = Column(String(50), nullable=True)
    PostalCode = Column(String(10), nullable=True)
    AddressDetailId = Column(UNIQUEIDENTIFIER, nullable=True)
    ManagerId = Column(Integer, nullable=True)
    LastBuyDate = Column(DateTime, nullable=True)
    CountOrders = Column(Integer, nullable=True)
    SumOfAllOrders = Column(Float, nullable=True)
    LastRecalculationDate = Column(DateTime, nullable=True)
    CustomerStatusId = Column(Integer, nullable=True)
    CustomerSegmentId = Column(Integer, nullable=True)
    DeltaOfOrdersSum = Column(String(128), nullable=True)
    CustomerIdAtBinotel = Column(Integer, nullable=True)
    LastCallingDateAtBinotel = Column(DateTime, nullable=True)
    LastSynchronizationDateWithBinotel = Column(DateTime, nullable=True)

    # Relationships
    orders = relationship("Order", back_populates="customer")

    def __repr__(self):
        return f"<Customer(id={self.CustomerID}, company={self.CompanyName})>"
