from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_confession(nickname, confession, age):
	confession = Confessions(nickname = nickname, confession = confession, age = age)
	session.add(confession)
	session.commit()

def get_all_confessions():
	confession = session.query(Confessions).all()
	return confession

