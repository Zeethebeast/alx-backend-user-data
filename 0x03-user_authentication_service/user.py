#!/usr/bin/env python3
"""Create a USER Model using sqlalchemy
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String
    )
Base = declarative_base()

class User(Base):
    """
    Definition of a class User
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
        