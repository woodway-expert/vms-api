from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.currency import CourseCurrency
from app.schemas.currency import (
    CourseCurrency as CourseCurrencySchema,
    CourseCurrencyCreate,
    CourseCurrencyUpdate,
)
from app.routers.auth import get_current_user
from app.models.user import User as UserModel

router = APIRouter(
    prefix="/currencies",
    tags=["currencies"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[CourseCurrencySchema])
def get_currencies(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(50, ge=1, le=1000, description="Number of records to return"),
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Retrieve all currency rates with pagination.
    """
    currencies = db.query(CourseCurrency).offset(skip).limit(limit).all()
    return currencies


@router.get("/{currency_id}", response_model=CourseCurrencySchema)
def get_currency(
    currency_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Retrieve a specific currency rate by ID.
    """
    currency = (
        db.query(CourseCurrency)
        .filter(CourseCurrency.CourseCurrencyID == currency_id)
        .first()
    )
    if not currency:
        raise HTTPException(status_code=404, detail="Currency rate not found")
    return currency


@router.post("/", response_model=CourseCurrencySchema)
def create_currency(
    currency: CourseCurrencyCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Create a new currency rate.
    """
    db_currency = CourseCurrency(**currency.model_dump())
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency


@router.put("/{currency_id}", response_model=CourseCurrencySchema)
def update_currency(
    currency_id: int,
    currency_update: CourseCurrencyUpdate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Update an existing currency rate.
    """
    currency = (
        db.query(CourseCurrency)
        .filter(CourseCurrency.CourseCurrencyID == currency_id)
        .first()
    )
    if not currency:
        raise HTTPException(status_code=404, detail="Currency rate not found")

    update_data = currency_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(currency, field, value)

    db.commit()
    db.refresh(currency)
    return currency


@router.delete("/{currency_id}")
def delete_currency(
    currency_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Delete a currency rate.
    """
    currency = (
        db.query(CourseCurrency)
        .filter(CourseCurrency.CourseCurrencyID == currency_id)
        .first()
    )
    if not currency:
        raise HTTPException(status_code=404, detail="Currency rate not found")

    db.delete(currency)
    db.commit()
    return {"message": "Currency rate deleted successfully"}
