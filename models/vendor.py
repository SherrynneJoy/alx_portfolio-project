#!/usr/bin/python3
"""defines sellers of digital planners on PlanWright"""
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db_setup import engine


Base = declarative_base()


class Vendor(Base):
    """defines attributes of people selling on PlanWright"""
    __tablename__ = 'vendors'

    id = Column(Integer, primary_key=True)
    vendor_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    products = relationship("Product", back_populates="vendor")

    def __repr__(self):
        return f"Vendor(id={self.id}, vendor_name={self.vendor_name},
                        email={self.email})"
