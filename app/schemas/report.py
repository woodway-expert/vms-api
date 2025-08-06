"""Pydantic schemas for Reports."""

from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class SalesSummary(BaseModel):
    total_sales: float
    number_of_orders: int
    start_date: date
    end_date: date


class InventoryStatus(BaseModel):
    item_id: int
    item_name: str
    quantity: int
    value: float


class CustomerActivity(BaseModel):
    customer_id: int
    customer_name: str
    total_spent: float
    order_count: int


class ReportBase(BaseModel):
    class Config:
        orm_mode = True
