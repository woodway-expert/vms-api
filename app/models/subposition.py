from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, BIT
from sqlalchemy.orm import relationship

from app.database import Base


class SubPosition(Base):
    __tablename__ = "SubPositions"

    SubPositionID = Column(UNIQUEIDENTIFIER, primary_key=True, index=True)
    PositionID = Column(UNIQUEIDENTIFIER, ForeignKey("Orders.OrderID"), nullable=True)
    BreedName = Column(String(50), nullable=True)
    NumberOfInputPallet = Column(String, nullable=True)  # max type
    NumberOfOutputPallet = Column(String(20), nullable=True)
    NecessarySquareMeters = Column(Float, nullable=True)
    ReadySquareMeters = Column(Float, nullable=True)
    Cost = Column(Float, nullable=True)
    Price = Column(Float, nullable=True)
    SalesCurrency = Column(String(3), nullable=True)
    TotalCost = Column(Float, nullable=True)
    DescriptionPos = Column(String(120), nullable=True)
    LinearMeters = Column(Float, nullable=True)
    Discount = Column(Float, nullable=True)
    TotalCostByDiscount = Column(Float, nullable=True)
    FlexOrderPosition = Column(String(255), nullable=True)
    PriceManually = Column(Float, nullable=True)
    IsPriceManually = Column(BIT, nullable=True)
    UnitsOfMeasurement = Column(String(10), nullable=True)
    PositionDiscountId = Column(Integer, nullable=True)
    IsAccrualOfBonus = Column(BIT, nullable=True)
    DirectoryMarkId = Column(Integer, nullable=True)

    # Relationships
    order = relationship("Order", back_populates="sub_positions")

    def __repr__(self):
        return f"<SubPosition(id={self.SubPositionID}, breed={self.BreedName})>"
