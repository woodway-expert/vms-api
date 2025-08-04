from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.order import Order
from app.schemas.order import Order as OrderSchema, OrderCreate, OrderUpdate

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[OrderSchema])
def get_orders(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(50, ge=1, le=1000, description="Number of records to return"),
    customer_id: int = Query(None, description="Filter by customer ID"),
    status: int = Query(None, description="Filter by order status"),
    db: Session = Depends(get_db),
):
    """
    Retrieve all orders with pagination and optional filtering.
    """
    query = db.query(Order)

    if customer_id:
        query = query.filter(Order.CustomerID == customer_id)
    if status is not None:
        query = query.filter(Order.OrderStatus == status)

    orders = query.offset(skip).limit(limit).all()
    return orders


@router.get("/{order_id}", response_model=OrderSchema)
def get_order(order_id: UUID, db: Session = Depends(get_db)):
    """
    Retrieve a specific order by ID.
    """
    order = db.query(Order).filter(Order.OrderID == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.post("/", response_model=OrderSchema)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """
    Create a new order.
    """
    db_order = Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@router.put("/{order_id}", response_model=OrderSchema)
def update_order(
    order_id: UUID, order_update: OrderUpdate, db: Session = Depends(get_db)
):
    """
    Update an existing order.
    """
    order = db.query(Order).filter(Order.OrderID == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    update_data = order_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(order, field, value)

    db.commit()
    db.refresh(order)
    return order


@router.delete("/{order_id}")
def delete_order(order_id: UUID, db: Session = Depends(get_db)):
    """
    Delete an order.
    """
    order = db.query(Order).filter(Order.OrderID == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    db.delete(order)
    db.commit()
    return {"message": "Order deleted successfully"}
