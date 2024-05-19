from sqlalchemy import Column, Integer, String

from .base import Base

__all__ = ["Officer"]


class Officer(Base):
	__tablename__ = "officer"

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String, nullable=False)
