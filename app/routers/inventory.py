from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.models.inventory import SoldOtherGood
from app.schemas.inventory import (
    SoldOtherGood as SoldOtherGoodSchema,
    SoldOtherGoodCreate,
    SoldOtherGoodUpdate,
)

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[SoldOtherGoodSchema])
def get_inventory_items(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(50, ge=1, le=1000, description="Number of records to return"),
    is_sold: Optional[bool] = Query(None, description="Filter by sold status"),
    stock_id: Optional[int] = Query(None, description="Filter by stock ID"),
    db: Session = Depends(get_db),
):
    """
    Retrieve all inventory items with pagination and optional filtering.
    """
    try:
        query = db.query(SoldOtherGood)

        if is_sold is not None:
            query = query.filter(SoldOtherGood.IsSold == is_sold)
        if stock_id is not None:
            query = query.filter(SoldOtherGood.StockID == stock_id)

        items = query.offset(skip).limit(limit).all()
        return items
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to retrieve inventory items: {str(e)}"
        )


@router.get("/{item_id}", response_model=SoldOtherGoodSchema)
def get_inventory_item(item_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific inventory item by ID.
    """
    item = (
        db.query(SoldOtherGood).filter(SoldOtherGood.SoldOtherGoodId == item_id).first()
    )
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return item


@router.post("/", response_model=SoldOtherGoodSchema)
def create_inventory_item(item: SoldOtherGoodCreate, db: Session = Depends(get_db)):
    """
    Create a new inventory item.
    """
    try:
        db_item = SoldOtherGood(**item.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Inventory item creation failed due to constraint violation",
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Failed to create inventory item: {str(e)}"
        )


@router.put("/{item_id}", response_model=SoldOtherGoodSchema)
def update_inventory_item(
    item_id: str, item_update: SoldOtherGoodUpdate, db: Session = Depends(get_db)
):
    """
    Update an existing inventory item.
    """
    item = (
        db.query(SoldOtherGood).filter(SoldOtherGood.SoldOtherGoodId == item_id).first()
    )
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")

    try:
        update_data = item_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(item, field, value)

        db.commit()
        db.refresh(item)
        return item
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, detail="Update failed due to constraint violation"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Failed to update inventory item: {str(e)}"
        )


@router.delete("/{item_id}")
def delete_inventory_item(item_id: str, db: Session = Depends(get_db)):
    """
    Delete an inventory item.
    """
    item = (
        db.query(SoldOtherGood).filter(SoldOtherGood.SoldOtherGoodId == item_id).first()
    )
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")

    try:
        db.delete(item)
        db.commit()
        return {"message": "Inventory item deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Failed to delete inventory item: {str(e)}"
        )
