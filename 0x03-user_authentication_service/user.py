#!/usr/bin/env python3
"""
This module contains the SQLAlchemy model for the User entity.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    User model for the users table.

    Attributes:
        id (int): The primary key for the user.
        email (str): The email of the user.
        hashed_password (str): The hashed password of the user.
        session_id (str): The session ID associated with the user.
        reset_token (str): The token for password reset.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
