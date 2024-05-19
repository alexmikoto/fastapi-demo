from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

__all__ = ["Ticket"]


class Ticket(Base):
	__tablename__ = "ticket"

	id = Column(Integer, primary_key=True, autoincrement=True)
	vehicle_id = Column(Integer, ForeignKey("vehicle.id"), nullable=False)
	timestamp = Column(Integer, nullable=False)
	comments = Column(String, nullable=False)

	vehicle = relationship("Vehicle", back_populates="tickets")
