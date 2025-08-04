from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.sql import func

from app.database import Base


class CourseCurrency(Base):
    __tablename__ = "CourseCurrencies"

    CourseCurrencyID = Column(Integer, primary_key=True, index=True)
    CurrencyDate = Column(DateTime, nullable=False, index=True)
    CourseEur = Column(Float, nullable=True)
    DifferenceCourseEur = Column(Float, nullable=True)
    CourseUsd = Column(Float, nullable=True)
    DifferenceCourseUsd = Column(Float, nullable=True)
    CourseRub = Column(Float, nullable=True)
    DifferenceCourseRub = Column(Float, nullable=True)
    Comments = Column(String(200), nullable=True)
    NbuEur = Column(Float, nullable=True)
    NbuUsd = Column(Float, nullable=True)
    NbuRub = Column(Float, nullable=True)

    def __repr__(self):
        return f"<CourseCurrency(id={self.CourseCurrencyID}, date={self.CurrencyDate})>"
