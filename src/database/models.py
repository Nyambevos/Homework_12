from sqlalchemy import Column, Integer, String, func
from sqlalchemy.sql.sqltypes import Date, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    email = Column(String(50))
    phone = Column(String(15), nullable=False)
    birthday = Column(Date)
    created_at = Column('created_at', DateTime, default=func.now())
