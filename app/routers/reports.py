"""FastAPI router for generating reports."""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from app import schemas
from app.database import get_db
from app.routers.auth import get_current_user
from app.models import (
    order as order_model,
    customer as customer_model,
    subposition as subposition_model,
)

router = APIRouter()


@router.get(
    "/reports/sales-summary",
    response_model=schemas.report.SalesSummary,
    tags=["Reports"],
    summary="Get Sales Summary Report / Отримати звіт по продажам",
)
def get_sales_summary(
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db),
    current_user: models.user.User = Depends(get_current_user),
):
    """
    Generate a summary of sales within a given date range.
    """
    query = db.query(order_model.Order).filter(
        order_model.Order.OrderDate >= start_date,
        order_model.Order.OrderDate <= end_date,
    )
    total_sales = sum(o.OrderSum for o in query.all())
    number_of_orders = query.count()

    return {
        "total_sales": total_sales,
        "number_of_orders": number_of_orders,
        "start_date": start_date,
        "end_date": end_date,
    }
