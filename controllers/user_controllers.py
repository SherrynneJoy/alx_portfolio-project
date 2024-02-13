#!/usr/bin/python3
"""creates CRUD functions for the user"""
# from db_setup import session
from models.user import User


# create the user
def create_user(username, email, password):
    new_user = User(username=username, email=email, password=password)
    session.add(new_user)
    session.commit()
    return new_user


# get the user(lookup) through their username/email
def get_user_by_id(user_id):
    session.query(User).filter_by(id=user_id).first()


def get_user_by_email(email):
    session.query(User).filter_by(email=email).first()


def get_all_users():
    return session.query(User).all()


# update user in the record db
def update_user(user_id, new_email):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.email = new_email
        session.commit()
        return True
    return False


# delete a record from a db
def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    return False
