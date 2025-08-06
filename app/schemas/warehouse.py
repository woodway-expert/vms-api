"""Pydantic schemas for Warehouse."""

from pydantic import BaseModel
from typing import Optional


class WarehouseBase(BaseModel):
    Name: str
    Location: Optional[str] = None


class WarehouseCreate(WarehouseBase):
    pass


class WarehouseUpdate(BaseModel):
    Name: Optional[str] = None
    Location: Optional[str] = None


class Warehouse(WarehouseBase):
    WarehouseID: int

    class Config:
        orm_mode = True
