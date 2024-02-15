#!/usr/bin/python3
"""defines a class for the user to order/ purchase a planner"""
from sqlalchemy import create_engine, Column, Integer, ForeignKey, DateTime
from sqlalchemy import Float
from sqlalchemy.ext.declarative import declarative_base
from db_setup import engine


Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'

    OrderID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey('users.UserID'), nullable=False)
    TotalAmount = Column(Float, nullable=False)
    OrderDate = Column(DateTime, nullable=False)


# Create engine and table
# engine = create_engine('sqlite:///order.db')
Base.metadata.create_all(engine)
