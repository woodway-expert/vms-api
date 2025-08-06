"""FastAPI router for administrative tasks."""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db
from app.routers.auth import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["Administration"],
    responses={403: {"description": "Operation not permitted"}},
)


def require_admin(current_user: models.user.User = Depends(get_current_user)):
    """Dependency to require admin privileges."""
    if not current_user.IsAdmin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges",
        )
    return current_user


# --- User Management ---
@router.get(
    "/users",
    response_model=List[schemas.user.User],
    dependencies=[Depends(require_admin)],
)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all users."""
    users = db.query(models.user.User).offset(skip).limit(limit).all()
    return users


# --- Supplier Management ---
@router.post(
    "/suppliers",
    response_model=schemas.supplier.Supplier,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_admin)],
)
def create_supplier(
    supplier: schemas.supplier.SupplierCreate, db: Session = Depends(get_db)
):
    """Create a new supplier."""
    db_supplier = models.supplier.Supplier(**supplier.model_dump())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier


@router.get(
    "/suppliers",
    response_model=List[schemas.supplier.Supplier],
    dependencies=[Depends(require_admin)],
)
def get_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all suppliers."""
    suppliers = db.query(models.supplier.Supplier).offset(skip).limit(limit).all()
    return suppliers


# --- Warehouse Management ---
@router.post(
    "/warehouses",
    response_model=schemas.warehouse.Warehouse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_admin)],
)
def create_warehouse(
    warehouse: schemas.warehouse.WarehouseCreate, db: Session = Depends(get_db)
):
    """Create a new warehouse."""
    db_warehouse = models.warehouse.Warehouse(**warehouse.model_dump())
    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse


@router.get(
    "/warehouses",
    response_model=List[schemas.warehouse.Warehouse],
    dependencies=[Depends(require_admin)],
)
def get_warehouses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all warehouses."""
    warehouses = db.query(models.warehouse.Warehouse).offset(skip).limit(limit).all()
    return warehouses
