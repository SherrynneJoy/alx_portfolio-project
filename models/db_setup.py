#!/usr/bin/python3
"""sqlachemy configuration to establish a conection with the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# establish the db connection url
db_url = 'mysql://root:@localhost:3306/planright_db'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
