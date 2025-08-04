from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class CourseCurrencyBase(BaseModel):
    CurrencyDate: datetime = Field(..., description="Currency date")
    CourseEur: Optional[float] = Field(None, description="EUR exchange rate")
    DifferenceCourseEur: Optional[float] = Field(
        None, description="EUR rate difference"
    )
    CourseUsd: Optional[float] = Field(None, description="USD exchange rate")
    DifferenceCourseUsd: Optional[float] = Field(
        None, description="USD rate difference"
    )
    CourseRub: Optional[float] = Field(None, description="RUB exchange rate")
    DifferenceCourseRub: Optional[float] = Field(
        None, description="RUB rate difference"
    )
    Comments: Optional[str] = Field(None, max_length=200, description="Comments")
    NbuEur: Optional[float] = Field(None, description="NBU EUR rate")
    NbuUsd: Optional[float] = Field(None, description="NBU USD rate")
    NbuRub: Optional[float] = Field(None, description="NBU RUB rate")


class CourseCurrencyCreate(CourseCurrencyBase):
    pass


class CourseCurrencyUpdate(BaseModel):
    CurrencyDate: Optional[datetime] = None
    CourseEur: Optional[float] = None
    DifferenceCourseEur: Optional[float] = None
    CourseUsd: Optional[float] = None
    DifferenceCourseUsd: Optional[float] = None
    CourseRub: Optional[float] = None
    DifferenceCourseRub: Optional[float] = None
    Comments: Optional[str] = Field(None, max_length=200)
    NbuEur: Optional[float] = None
    NbuUsd: Optional[float] = None
    NbuRub: Optional[float] = None


class CourseCurrency(CourseCurrencyBase):
    CourseCurrencyID: int = Field(..., description="Currency rate ID")

    class Config:
        from_attributes = True
