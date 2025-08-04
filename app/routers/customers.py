from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.customer import Customer
from app.schemas.customer import (
    Customer as CustomerSchema,
    CustomerCreate,
    CustomerUpdate,
)

router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[CustomerSchema])
def get_customers(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(50, ge=1, le=1000, description="Number of records to return"),
    company_name: str = Query(None, description="Filter by company name"),
    city: str = Query(None, description="Filter by city"),
    db: Session = Depends(get_db),
):
    """
    Retrieve all customers with pagination and optional filtering.
    """
    query = db.query(Customer)

    if company_name:
        query = query.filter(Customer.CompanyName.contains(company_name))
    if city:
        query = query.filter(Customer.City == city)

    customers = query.offset(skip).limit(limit).all()
    return customers


@router.get("/{customer_id}", response_model=CustomerSchema)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific customer by ID.
    """
    customer = db.query(Customer).filter(Customer.CustomerID == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.post("/", response_model=CustomerSchema)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """
    Create a new customer.
    """
    db_customer = Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


@router.put("/{customer_id}", response_model=CustomerSchema)
def update_customer(
    customer_id: int, customer_update: CustomerUpdate, db: Session = Depends(get_db)
):
    """
    Update an existing customer.
    """
    customer = db.query(Customer).filter(Customer.CustomerID == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    update_data = customer_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(customer, field, value)

    db.commit()
    db.refresh(customer)
    return customer


@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Delete a customer.
    """
    customer = db.query(Customer).filter(Customer.CustomerID == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    db.delete(customer)
    db.commit()
    return {"message": "Customer deleted successfully"}
