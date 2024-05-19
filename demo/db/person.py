from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base

__all__ = ["Person"]


class Person(Base):
	__tablename__ = "person"

	id = Column(Integer, primary_key=True, autoincrement=True)
	email = Column(String, unique=True, nullable=False)
	name = Column(String, nullable=False)

	vehicles = relationship("Vehicle", back_populates="person")
