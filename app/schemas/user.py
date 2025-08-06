"""Pydantic schemas for User model."""

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    Username: str
    Email: EmailStr


class UserCreate(UserBase):
    Password: str


class UserUpdate(UserBase):
    Password: str | None = None
    IsActive: bool | None = None
    IsAdmin: bool | None = None


class User(UserBase):
    UserID: int
    IsActive: bool
    IsAdmin: bool

    class Config:
        orm_mode = True
