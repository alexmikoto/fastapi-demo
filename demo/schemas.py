from pydantic import BaseModel

__all__ = ["Person", "Vehicle", "Officer", "NewTicket"]


class Person(BaseModel):
	id: int | None = None
	name: str
	email: str

	class Config:
		from_attributes = True


class Vehicle(BaseModel):
	id: int | None = None
	license_plate: str
	brand: str
	color: str
	person_id : int | None = None
	person: Person | None = None

	class Config:
		from_attributes = True


class Officer(BaseModel):
	id: int | None = None
	name: str

	class Config:
		from_attributes = True


class NewTicket(BaseModel):
	placa_patente: str
	timestamp: int
	comentarios: str
