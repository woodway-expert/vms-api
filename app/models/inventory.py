from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, BIT
from sqlalchemy.orm import relationship

from app.database import Base


class SoldOtherGood(Base):
    __tablename__ = "SoldOtherGoods"

    OtherGoodsId = Column(UNIQUEIDENTIFIER, primary_key=True, index=True)
    GoodsDirectoryId = Column(Integer, nullable=True)
    CostOfArticleId = Column(UNIQUEIDENTIFIER, nullable=True)
    ImportArticleDetailId = Column(UNIQUEIDENTIFIER, nullable=True)
    ManagerCreateId = Column(Integer, nullable=True)
    StockID = Column(Integer, nullable=True)
    SupplierID = Column(Integer, nullable=True)
    ImportDate = Column(DateTime, nullable=True)
    InitCountItems = Column(Integer, nullable=True)
    RealCountItems = Column(Integer, nullable=True)
    NumberPallet = Column(String(150), nullable=True)
    Comments = Column(String(150), nullable=True)
    PercentageOfSoldArticle = Column(Float, nullable=True)
    IsSold = Column(BIT, nullable=True)
    SquareMeters = Column(Float, nullable=True)
    OnePackage = Column(Float, nullable=True)
    GoodsAdditionalInformationId = Column(Integer, nullable=True)
    ExpiredDate = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<SoldOtherGood(id={self.OtherGoodsId}, pallet={self.NumberPallet})>"
