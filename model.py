from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Confessions(Base):
	__tablename__ = "confessions"
	id = Column(Integer, primary_key = True)
	nickname = Column(String)
	confession = Column(String)
	age = Column(Integer)

