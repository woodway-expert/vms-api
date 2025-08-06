from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.models.subposition import SubPosition
from app.schemas.subposition import (
    SubPosition as SubPositionSchema,
    SubPositionCreate,
    SubPositionUpdate,
)
from app.routers.auth import get_current_user
from app.models.user import User as UserModel

router = APIRouter(
    prefix="/subpositions",
    tags=["subpositions"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[SubPositionSchema])
def get_subpositions(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(50, ge=1, le=1000, description="Number of records to return"),
    position_id: Optional[str] = Query(None, description="Filter by position ID"),
    breed_name: Optional[str] = Query(None, description="Filter by breed name"),
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Retrieve all subpositions with pagination and optional filtering.
    """
    try:
        query = db.query(SubPosition)

        if position_id:
            query = query.filter(SubPosition.PositionID == position_id)
        if breed_name:
            query = query.filter(SubPosition.BreedName.contains(breed_name))

        subpositions = query.offset(skip).limit(limit).all()
        return subpositions
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to retrieve subpositions: {str(e)}"
        )


@router.get("/{subposition_id}", response_model=SubPositionSchema)
def get_subposition(
    subposition_id: str,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Retrieve a specific subposition by ID.
    """
    subposition = (
        db.query(SubPosition)
        .filter(SubPosition.SubPositionID == subposition_id)
        .first()
    )
    if not subposition:
        raise HTTPException(status_code=404, detail="Subposition not found")
    return subposition


@router.post("/", response_model=SubPositionSchema)
def create_subposition(
    subposition: SubPositionCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Create a new subposition.
    """
    try:
        db_subposition = SubPosition(**subposition.model_dump())
        db.add(db_subposition)
        db.commit()
        db.refresh(db_subposition)
        return db_subposition
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Subposition creation failed due to constraint violation",
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Failed to create subposition: {str(e)}"
        )


@router.put("/{subposition_id}", response_model=SubPositionSchema)
def update_subposition(
    subposition_id: str,
    subposition_update: SubPositionUpdate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Update an existing subposition.
    """
    subposition = (
        db.query(SubPosition)
        .filter(SubPosition.SubPositionID == subposition_id)
        .first()
    )
    if not subposition:
        raise HTTPException(status_code=404, detail="Subposition not found")

    update_data = subposition_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(subposition, field, value)

    db.commit()
    db.refresh(subposition)
    return subposition


@router.delete("/{subposition_id}")
def delete_subposition(
    subposition_id: str,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Delete a subposition.
    """
    subposition = (
        db.query(SubPosition)
        .filter(SubPosition.SubPositionID == subposition_id)
        .first()
    )
    if not subposition:
        raise HTTPException(status_code=404, detail="Subposition not found")

    db.delete(subposition)
    db.commit()
    return {"message": "Subposition deleted successfully"}
