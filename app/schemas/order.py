from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class OrderBase(BaseModel):
    CustomerID: Optional[int] = Field(None, description="Customer ID")
    NumberOrder: Optional[str] = Field(None, max_length=30, description="Order number")
    OrderDate: Optional[datetime] = Field(None, description="Order date")
    Descriptions: Optional[str] = Field(
        None, max_length=50, description="Order description"
    )
    ManagerId: Optional[int] = Field(None, description="Manager ID")
    OrderSum: Optional[float] = Field(None, description="Order sum")
    OrderStatus: Optional[int] = Field(None, description="Order status")
    PaymentType: Optional[int] = Field(None, description="Payment type")
    DateOfPayment: Optional[datetime] = Field(None, description="Payment date")
    IsActive: Optional[bool] = Field(None, description="Is active")
    ManagerIdForLastUpdate: Optional[int] = Field(
        None, description="Manager ID for last update"
    )
    IsDeleteReservOrder: Optional[bool] = Field(
        None, description="Is delete reservation order"
    )
    DateOfShipment: Optional[datetime] = Field(None, description="Shipment date")
    ShipmentStatusId: Optional[int] = Field(None, description="Shipment status ID")
    DeliveryMethodId: Optional[int] = Field(None, description="Delivery method ID")
    CountSoldItems: Optional[int] = Field(None, description="Count of sold items")
    ManagerIdForLastOpen: Optional[int] = Field(
        None, description="Manager ID for last open"
    )
    IsClosed: Optional[bool] = Field(None, description="Is closed")
    ExternalComment: Optional[str] = Field(
        None, max_length=100, description="External comment"
    )
    DepositedAmount: Optional[float] = Field(None, description="Deposited amount")
    PaymentFormId: Optional[int] = Field(None, description="Payment form ID")
    IsIndividualOrder: Optional[bool] = Field(None, description="Is individual order")
    IsWholesaleOrder: Optional[bool] = Field(None, description="Is wholesale order")


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    CustomerID: Optional[int] = None
    NumberOrder: Optional[str] = Field(None, max_length=30)
    OrderDate: Optional[datetime] = None
    Descriptions: Optional[str] = Field(None, max_length=50)
    ManagerId: Optional[int] = None
    OrderSum: Optional[float] = None
    OrderStatus: Optional[int] = None
    PaymentType: Optional[int] = None
    DateOfPayment: Optional[datetime] = None
    IsActive: Optional[bool] = None
    ManagerIdForLastUpdate: Optional[int] = None
    IsDeleteReservOrder: Optional[bool] = None
    DateOfShipment: Optional[datetime] = None
    ShipmentStatusId: Optional[int] = None
    DeliveryMethodId: Optional[int] = None
    CountSoldItems: Optional[int] = None
    ManagerIdForLastOpen: Optional[int] = None
    IsClosed: Optional[bool] = None
    ExternalComment: Optional[str] = Field(None, max_length=100)
    DepositedAmount: Optional[float] = None
    PaymentFormId: Optional[int] = None
    IsIndividualOrder: Optional[bool] = None
    IsWholesaleOrder: Optional[bool] = None


class Order(OrderBase):
    OrderID: UUID = Field(..., description="Order ID")
    LastDateChange: Optional[datetime] = Field(None, description="Last change date")

    model_config = ConfigDict(from_attributes=True)


class OrderWithRelations(Order):
    customer: Optional["Customer"] = Field(None, description="Customer information")
    sub_positions: List["SubPosition"] = Field(
        default=[], description="Order sub-positions"
    )

    model_config = ConfigDict(from_attributes=True)
