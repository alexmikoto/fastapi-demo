from typing import Callable

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

from .base import Base
from .officer import Officer
from .person import Person
from .vehicle import Vehicle
from .ticket import Ticket

__all__ = ["DB"]

# Only here for dummy data, it's "password""
DEFAULT_PW = "$2b$12$L0HB8pyXEi0b5RkL9HiD4.Q.l2ls9f032NYCBetQvEWvw4CIMey7m"


class DB:
	engine: Engine
	Session: Callable[..., Session]
	SessionType = Session

	# nicer API facing out of this module
	Base = Base
	Officer = Officer
	Person = Person
	Vehicle = Vehicle
	Ticket = Ticket

	Error = SQLAlchemyError

	def __init__(self, uri: str, *args, **kwargs) -> None:
		self.engine = create_engine(uri, *args, **kwargs)
		self.Session = sessionmaker(
			autocommit=False,
			autoflush=False,
			bind=self.engine,
		)

	def create_all(self):
		Base.metadata.create_all(self.engine)

	def session(self):
		sess = self.Session()
		try:
			yield sess
		finally:
			sess.close()

	def create_dummy_data(self):
		with self.Session() as sess:
			persons = [
				Person(name="Mark", email="mark@example.com"),
				Person(name="Alex", email="alex@example.com"),
				Person(name="John", email="john@example.com"),
			]
			officers = [
				Officer(name="Richard"),
				Officer(name="James"),
				Officer(name="Michael"),
			]
			vehicles = [
				Vehicle(
					license_plate="AAA-123",
					brand="Toyota",
					color="Red",
					person=persons[0],
				),
				Vehicle(
					license_plate="BBB-456",
					brand="Ford",
					color="Black",
					person=persons[1],
				),
			]
			
			sess.add_all(persons)
			sess.add_all(officers)
			sess.add_all(vehicles)
			
			sess.commit()
