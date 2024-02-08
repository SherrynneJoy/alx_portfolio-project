#!/usr/bin/python3
"""defines the review class for users to leave product reviews"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Review(Base):
    __tablename__ = 'reviews'

    ReviewID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, nullable=False)
    ProductID = Column(Integer, nullable=False)
    Rating = Column(Integer, nullable=False)
    Comment = Column(String(5000), nullable=False)


# Create engine and table
engine = create_engine('sqlite:///reviews.db')
Base.metadata.create_all(engine)
