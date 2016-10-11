from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc

from puppies import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime
import random


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

def PuppyName():
	puppyNames = session.query(Puppy).order_by(Puppy.name.desc()).all()
	for puppy in puppyNames:
		print puppy.name

PuppyName()	
