#!/usr/bin/python3
"""defines the digital planners to be sold on the planwright app"""
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Product(Base):
    """defines the attributes and methods of digital planners"""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    vendor_id = Column(Integer, ForeignKey('vendors.id'))

    vendor = relationship("Vendor", back_populates="products")

    def __repr__(self):
        return f"Product(id={self.id}, title={self.title}, price={self.price})"
