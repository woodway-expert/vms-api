"""Pydantic schemas for Supplier."""

from pydantic import BaseModel, EmailStr
from typing import Optional


class SupplierBase(BaseModel):
    CompanyName: str
    ContactName: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[EmailStr] = None
    IsActive: bool = True


class SupplierCreate(SupplierBase):
    pass


class SupplierUpdate(BaseModel):
    CompanyName: Optional[str] = None
    ContactName: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[EmailStr] = None
    IsActive: Optional[bool] = None


class Supplier(SupplierBase):
    SupplierID: int

    class Config:
        orm_mode = True
