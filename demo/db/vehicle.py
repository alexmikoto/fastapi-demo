from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

__all__ = ["Vehicle"]


class Vehicle(Base):
	__tablename__ = "vehicle"

	id = Column(Integer, primary_key=True, autoincrement=True)
	license_plate = Column(String, unique=True, nullable=False)
	brand = Column(String, nullable=False)
	color = Column(String, nullable=False)
	person_id = Column(Integer, ForeignKey("person.id"), nullable=False)

	person = relationship("Person", back_populates="vehicles")
	tickets = relationship("Ticket", back_populates="vehicle")
