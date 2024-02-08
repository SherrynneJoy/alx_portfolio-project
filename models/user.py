#!/usr/bin/python3
"""defines methods & attributes for users / buyers who visit app"""
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    """defines buyers of digital planners from PlanWright"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username},
                      email={self.email})"
