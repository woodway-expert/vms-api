from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class SoldOtherGoodBase(BaseModel):
    GoodsDirectoryId: Optional[int] = Field(None, description="Goods directory ID")
    CostOfArticleId: Optional[UUID] = Field(None, description="Cost of article ID")
    ImportArticleDetailId: Optional[UUID] = Field(
        None, description="Import article detail ID"
    )
    ManagerCreateId: Optional[int] = Field(None, description="Manager create ID")
    StockID: Optional[int] = Field(None, description="Stock ID")
    SupplierID: Optional[int] = Field(None, description="Supplier ID")
    ImportDate: Optional[datetime] = Field(None, description="Import date")
    InitCountItems: Optional[int] = Field(None, description="Initial count of items")
    RealCountItems: Optional[int] = Field(None, description="Real count of items")
    NumberPallet: Optional[str] = Field(
        None, max_length=150, description="Pallet number"
    )
    Comments: Optional[str] = Field(None, max_length=150, description="Comments")
    PercentageOfSoldArticle: Optional[float] = Field(
        None, description="Percentage of sold article"
    )
    IsSold: Optional[bool] = Field(None, description="Is sold")
    SquareMeters: Optional[float] = Field(None, description="Square meters")
    OnePackage: Optional[float] = Field(None, description="One package")
    GoodsAdditionalInformationId: Optional[int] = Field(
        None, description="Goods additional information ID"
    )
    ExpiredDate: Optional[datetime] = Field(None, description="Expiration date")


class SoldOtherGoodCreate(SoldOtherGoodBase):
    pass


class SoldOtherGoodUpdate(BaseModel):
    GoodsDirectoryId: Optional[int] = None
    CostOfArticleId: Optional[UUID] = None
    ImportArticleDetailId: Optional[UUID] = None
    ManagerCreateId: Optional[int] = None
    StockID: Optional[int] = None
    SupplierID: Optional[int] = None
    ImportDate: Optional[datetime] = None
    InitCountItems: Optional[int] = None
    RealCountItems: Optional[int] = None
    NumberPallet: Optional[str] = Field(None, max_length=150)
    Comments: Optional[str] = Field(None, max_length=150)
    PercentageOfSoldArticle: Optional[float] = None
    IsSold: Optional[bool] = None
    SquareMeters: Optional[float] = None
    OnePackage: Optional[float] = None
    GoodsAdditionalInformationId: Optional[int] = None
    ExpiredDate: Optional[datetime] = None


class SoldOtherGood(SoldOtherGoodBase):
    OtherGoodsId: UUID = Field(..., description="Other goods ID")

    class Config:
        from_attributes = True
