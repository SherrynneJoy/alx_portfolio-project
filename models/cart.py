#!/usr/bin/python3
"""defines the shoppping cart"""

from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from db_setup import engine

Base = declarative_base()


class Cart(Base):
    __tablename__ = 'carts'

    CartID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey('users.UserID'), nullable=False)
    ProductID = Column(Integer, nullable=False)
    Quantity = Column(Integer, nullable=False)


# Create engine and table
# engine = create_engine('sqlite:///cart.db')
Base.metadata.create_all(engine)
