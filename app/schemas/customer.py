from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class CustomerBase(BaseModel):
    CompanyName: Optional[str] = Field(None, max_length=50, description="Company name")
    ContactName: Optional[str] = Field(
        None, max_length=30, description="Contact person name"
    )
    Phone: Optional[str] = Field(None, max_length=20, description="Phone number")
    EMail: Optional[EmailStr] = Field(None, description="Email address")
    City: Optional[str] = Field(None, max_length=20, description="City")
    Address: Optional[str] = Field(None, max_length=50, description="Address")
    PostalCode: Optional[str] = Field(None, max_length=10, description="Postal code")
    AddressDetailId: Optional[UUID] = Field(None, description="Address detail ID")
    ManagerId: Optional[int] = Field(None, description="Manager ID")
    CustomerStatusId: Optional[int] = Field(None, description="Customer status ID")
    CustomerSegmentId: Optional[int] = Field(None, description="Customer segment ID")
    DeltaOfOrdersSum: Optional[str] = Field(
        None, max_length=128, description="Delta of orders sum"
    )
    CustomerIdAtBinotel: Optional[int] = Field(
        None, description="Customer ID at Binotel"
    )


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    CompanyName: Optional[str] = Field(None, max_length=50)
    ContactName: Optional[str] = Field(None, max_length=30)
    Phone: Optional[str] = Field(None, max_length=20)
    EMail: Optional[EmailStr] = None
    City: Optional[str] = Field(None, max_length=20)
    Address: Optional[str] = Field(None, max_length=50)
    PostalCode: Optional[str] = Field(None, max_length=10)
    AddressDetailId: Optional[UUID] = None
    ManagerId: Optional[int] = None
    CustomerStatusId: Optional[int] = None
    CustomerSegmentId: Optional[int] = None
    DeltaOfOrdersSum: Optional[str] = Field(None, max_length=128)
    CustomerIdAtBinotel: Optional[int] = None


class Customer(CustomerBase):
    CustomerID: int = Field(..., description="Customer ID")
    LastBuyDate: Optional[datetime] = Field(None, description="Last purchase date")
    CountOrders: Optional[int] = Field(None, description="Number of orders")
    SumOfAllOrders: Optional[float] = Field(None, description="Sum of all orders")
    LastRecalculationDate: Optional[datetime] = Field(
        None, description="Last recalculation date"
    )
    LastCallingDateAtBinotel: Optional[datetime] = Field(
        None, description="Last calling date at Binotel"
    )
    LastSynchronizationDateWithBinotel: Optional[datetime] = Field(
        None, description="Last sync date with Binotel"
    )

    model_config = ConfigDict(from_attributes=True)


class CustomerWithOrders(Customer):
    orders: List["Order"] = Field(default=[], description="Customer orders")

    model_config = ConfigDict(from_attributes=True)
