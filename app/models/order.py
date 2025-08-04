from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, TINYINT, BIT
from sqlalchemy.orm import relationship

from app.database import Base


class Order(Base):
    __tablename__ = "Orders"

    OrderID = Column(UNIQUEIDENTIFIER, primary_key=True, index=True)
    CustomerID = Column(Integer, ForeignKey("Customers.CustomerID"), nullable=True)
    NumberOrder = Column(String(30), nullable=True)
    OrderDate = Column(DateTime, nullable=True)
    Descriptions = Column(String(50), nullable=True)
    ManagerId = Column(Integer, nullable=True)
    LastDateChange = Column(DateTime, nullable=True)
    OrderSum = Column(Float, nullable=True)
    OrderStatus = Column(TINYINT, nullable=True)
    PaymentType = Column(TINYINT, nullable=True)
    DateOfPayment = Column(DateTime, nullable=True)
    IsActive = Column(BIT, nullable=True)
    ManagerIdForLastUpdate = Column(Integer, nullable=True)
    IsDeleteReservOrder = Column(BIT, nullable=True)
    DateOfShipment = Column(DateTime, nullable=True)
    ShipmentStatusId = Column(Integer, nullable=True)
    DeliveryMethodId = Column(Integer, nullable=True)
    CountSoldItems = Column(Integer, nullable=True)
    ManagerIdForLastOpen = Column(Integer, nullable=True)
    IsClosed = Column(BIT, nullable=True)
    ExternalComment = Column(String(100), nullable=True)
    DepositedAmount = Column(Float, nullable=True)
    PaymentFormId = Column(Integer, nullable=True)
    IsIndividualOrder = Column(BIT, nullable=True)
    IsWholesaleOrder = Column(BIT, nullable=True)

    # Relationships
    customer = relationship("Customer", back_populates="orders")
    sub_positions = relationship("SubPosition", back_populates="order")

    def __repr__(self):
        return f"<Order(id={self.OrderID}, number={self.NumberOrder})>"
