from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from jose import jwt, JWTError

from .db import DB
from . import schemas

api = FastAPI()

# Hardcoded to in-memory db, check_same_thread is required for SQLite
# Normally this would be initialized in an application startup routine
# We also need to put the in-memory DB in a thread pool to not hit a 
# ghost DB in requests.
from sqlalchemy.pool import StaticPool
db = DB(
	"sqlite:///:memory:",
	connect_args={"check_same_thread": False},
	poolclass=StaticPool
)

# As we are connected to a memory sqlite, create schema
db.create_all()

# Insert dummy data
db.create_dummy_data()

static = StaticFiles(packages=[("demo", "static")], html=True)

# You know why this is a bad idea
JWT_KEY = "j9om87yhbsfsadfmnoi3"


# BIG, disgusting pile of CRUD code for admin
@api.get("/api/person/")
def get_persons(
		sess: DB.SessionType = Depends(db.session)
	) -> list[schemas.Person]:
	try:
		persons = sess.query(DB.Person).all()
		return persons
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.get("/api/person/{person_id}")
def get_person(
		person_id: int, sess: DB.SessionType = Depends(db.session)
	) -> schemas.Person:
	try:
		person = (
			sess.query(DB.Person)
				.filter(DB.Person.id == person_id)
				.one()
		)
		return person
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.post("/api/person/")
def create_person(
		data: schemas.Person,
		sess: DB.SessionType = Depends(db.session),
	) -> schemas.Person:
	try:
		person = DB.Person(name=data.name, email=data.email)
		sess.add(person)
		sess.commit()
		sess.refresh(person)
		return person
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.put("/api/person/{person_id}")
def update_person(
		person_id: int,
		data: schemas.Person,
		sess: DB.SessionType = Depends(db.session),
	) -> schemas.Person:
	try:
		person = (
			sess.query(DB.Person)
				.filter(DB.Person.id == officer_id)
				.one()
		)
		person.name = data.name
		person.email = data.email
		sess.commit()
		sess.refresh(person)
		return person
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.delete("/api/person/{person_id}")
def delete_person(
		person_id: int, sess: DB.SessionType = Depends(db.session)
	):
	try:
		person = (
			sess.query(DB.Person)
				.filter(DB.Person.id == person_id)
				.one()
		)
		sess.delete(person)
		sess.commit()
		return {"success": True}
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.get("/api/vehicle/")
def get_vehicles(
		sess: DB.SessionType = Depends(db.session)
	) -> list[schemas.Vehicle]:
	try:
		vehicles = sess.query(DB.Vehicle).all()
		return vehicles
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.get("/api/vehicle/{vehicle_id}")
def get_vehicle(
		vehicle_id: int, sess: DB.SessionType = Depends(db.session)
	) -> schemas.Vehicle:
	try:
		vehicle = (
			sess.query(DB.Vehicle)
				.filter(DB.Vehicle.id == vehicle_id)
				.one()
		)
		return vehicle
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.post("/api/vehicle/")
def create_vehicle(
		data: schemas.Vehicle,
		sess: DB.SessionType = Depends(db.session),
	) -> schemas.Vehicle:
	try:
		vehicle = DB.Vehicle(
			license_plate=data.license_plate,
			brand=data.brand,
			color=data.color,
			person_id=data.person_id,
		)
		sess.add(vehicle)
		sess.commit()
		sess.refresh(vehicle)
		return vehicle
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.put("/api/vehicle/{vehicle_id}")
def update_vehicle(
		officer_id: int,
		data: schemas.Vehicle,
		sess: DB.SessionType = Depends(db.session),
	) -> schemas.Vehicle:
	try:
		vehicle = (
			sess.query(DB.Vehicle)
				.filter(DB.Vehicle.id == vehicle_id)
				.one()
		)
		vehicle.license_plate = data.license_plate
		vehicle.brand = data.brand
		vehicle.color = data.color
		vehicle.person_id = data.person_id
		sess.commit()
		sess.refresh(vehicle)
		return vehicle
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.delete("/api/vehicle/{vehicle_id}")
def delete_vehicle(
		vehicle_id: int, sess: DB.SessionType = Depends(db.session)
	):
	try:
		vehicle = (
			sess.query(DB.Vehicle)
				.filter(DB.Vehicle.id == vehicle_id)
				.one()
		)
		sess.delete(vehicle)
		sess.commit()
		return {"success": True}
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.get("/api/officer/")
def get_officers(
		sess: DB.SessionType = Depends(db.session)
	) -> list[schemas.Officer]:
	try:
		officers = sess.query(DB.Officer).all()
		return officers
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.get("/api/officer/{officer_id}")
def get_officer(
		officer_id: int, sess: DB.SessionType = Depends(db.session)
	) -> schemas.Officer:
	try:
		officer = (
			sess.query(DB.Officer)
				.filter(DB.Officer.id == officer_id)
				.one()
		)
		return officer
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.post("/api/officer/")
def create_officer(
		data: schemas.Officer,
		sess: DB.SessionType = Depends(db.session),
	) -> schemas.Officer:
	try:
		officer = DB.Officer(name=data.name)
		sess.add(officer)
		sess.commit()
		sess.refresh(officer)
		return officer
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.put("/api/officer/{officer_id}")
def update_officer(
		officer_id: int,
		data: schemas.Officer,
		sess: DB.SessionType = Depends(db.session),
	) -> schemas.Officer:
	try:
		officer = (
			sess.query(DB.Officer)
				.filter(DB.Officer.id == officer_id)
				.one()
		)
		officer.name = data.name
		sess.commit()
		sess.refresh(officer)
		return officer
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.delete("/api/officer/{officer_id}")
def delete_officer(
		officer_id: int, sess: DB.SessionType = Depends(db.session)
	):
	try:
		officer = (
			sess.query(DB.Officer)
				.filter(DB.Officer.id == officer_id)
				.one()
		)
		sess.delete(officer)
		sess.commit()
		return {"success": True}
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


# THIS IS WHAT YOU ARE LOOKING FOR, EVERYTHING ELSE IS TO GENERATE /docs UI
@api.get("/api/generate-token")
def generate_token(
		officer_id: str, sess: DB.SessionType = Depends(db.session)
	):
	try:
		officer = (
			sess.query(DB.Officer)
				.filter(DB.Officer.id == officer_id)
				.one_or_none()
		)
		if officer is None:
			raise HTTPException(status_code=401)

		token = jwt.encode(
			{"officer_id": officer.id},
			JWT_KEY,
			algorithm="HS256",
		)
		return token
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))

@api.post("/api/cargar-infraccion")
def cargar_infraccion(
		request: Request,
		data: schemas.NewTicket,
		sess: DB.SessionType = Depends(db.session)
	):
	try:
		oid = jwt.decode(
			(request.headers.get("Authorization") or "")[7:],
			JWT_KEY,
			algorithms=["HS256"],
		)["officer_id"]
		officer = (
			sess.query(DB.Officer)
				.filter(DB.Officer.id == oid)
				.one_or_none()
		)
		if officer is None:
			raise HTTPException(status_code=401)

		vehicle = (
			sess.query(DB.Vehicle)
				.filter(DB.Vehicle.license_plate == data.placa_patente)
				.one_or_none()
		)
		if vehicle is None:
			raise HTTPException(status_code=404)
		ticket = DB.Ticket(
			vehicle_id=vehicle.id,
			timestamp=data.timestamp,
			comments=data.comentarios,
		)
		sess.add(ticket)
		sess.commit()
		return {"success": True}
	except JWTError as exc:
		raise HTTPException(status_code=401)
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


@api.post("/api/generar-informe")
def generar_informe(
		email: str,
		sess: DB.SessionType = Depends(db.session)
	):
	try:
		person = (
			sess.query(DB.Person)
				.filter(DB.Person.email == email)
				.one_or_none()
		)
		if person is None:
			raise HTTPException(status_code=404)

		return [{
			"placa_patente": ticket.vehicle.license_plate,
			"timestamp": ticket.timestamp,
			"comentarios": ticket.comments,
		} for vehicle in person.vehicles for ticket in vehicle.tickets]
	except DB.Error as exc:
		raise HTTPException(status_code=400, detail=str(exc))


# Mount admin UI
api.mount("/", static, name="static")
