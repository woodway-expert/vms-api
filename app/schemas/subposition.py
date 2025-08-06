from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class SubPositionBase(BaseModel):
    PositionID: Optional[UUID] = Field(None, description="Position ID (Order ID)")
    BreedName: Optional[str] = Field(None, max_length=50, description="Breed name")
    NumberOfInputPallet: Optional[str] = Field(
        None, description="Number of input pallet"
    )
    NumberOfOutputPallet: Optional[str] = Field(
        None, max_length=20, description="Number of output pallet"
    )
    NecessarySquareMeters: Optional[float] = Field(
        None, description="Necessary square meters"
    )
    ReadySquareMeters: Optional[float] = Field(None, description="Ready square meters")
    Cost: Optional[float] = Field(None, description="Cost")
    Price: Optional[float] = Field(None, description="Price")
    SalesCurrency: Optional[str] = Field(
        None, max_length=3, description="Sales currency"
    )
    TotalCost: Optional[float] = Field(None, description="Total cost")
    DescriptionPos: Optional[str] = Field(
        None, max_length=120, description="Description position"
    )
    LinearMeters: Optional[float] = Field(None, description="Linear meters")
    Discount: Optional[float] = Field(None, description="Discount")
    TotalCostByDiscount: Optional[float] = Field(
        None, description="Total cost by discount"
    )
    FlexOrderPosition: Optional[str] = Field(
        None, max_length=255, description="Flex order position"
    )
    PriceManually: Optional[float] = Field(None, description="Price manually")
    IsPriceManually: Optional[bool] = Field(None, description="Is price manually")
    UnitsOfMeasurement: Optional[str] = Field(
        None, max_length=10, description="Units of measurement"
    )
    PositionDiscountId: Optional[int] = Field(None, description="Position discount ID")
    IsAccrualOfBonus: Optional[bool] = Field(None, description="Is accrual of bonus")
    DirectoryMarkId: Optional[int] = Field(None, description="Directory mark ID")


class SubPositionCreate(SubPositionBase):
    pass


class SubPositionUpdate(BaseModel):
    PositionID: Optional[UUID] = None
    BreedName: Optional[str] = Field(None, max_length=50)
    NumberOfInputPallet: Optional[str] = None
    NumberOfOutputPallet: Optional[str] = Field(None, max_length=20)
    NecessarySquareMeters: Optional[float] = None
    ReadySquareMeters: Optional[float] = None
    Cost: Optional[float] = None
    Price: Optional[float] = None
    SalesCurrency: Optional[str] = Field(None, max_length=3)
    TotalCost: Optional[float] = None
    DescriptionPos: Optional[str] = Field(None, max_length=120)
    LinearMeters: Optional[float] = None
    Discount: Optional[float] = None
    TotalCostByDiscount: Optional[float] = None
    FlexOrderPosition: Optional[str] = Field(None, max_length=255)
    PriceManually: Optional[float] = None
    IsPriceManually: Optional[bool] = None
    UnitsOfMeasurement: Optional[str] = Field(None, max_length=10)
    PositionDiscountId: Optional[int] = None
    IsAccrualOfBonus: Optional[bool] = None
    DirectoryMarkId: Optional[int] = None


class SubPosition(SubPositionBase):
    SubPositionID: UUID = Field(..., description="Sub-position ID")

    model_config = ConfigDict(from_attributes=True)


class SubPositionWithOrder(SubPosition):
    order: Optional["Order"] = Field(None, description="Associated order")

    model_config = ConfigDict(from_attributes=True)
