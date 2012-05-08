# -*- coding: utf-8 -*-
""" 
    Database model classes for What's Up?
"""

from sqlalchemy import Column, Integer, Float, String
from database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    email = Column(String(200))
    openid = Column(String(200))

    def __init__(self, name, email, openid):
        self.name = name
        self.email = email
        self.openid = openid
    
    def __repr__(self):
        return '<User %r>' % (self.name)

class AstroObject(Base):
    __tablename__ = 'astro_object'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    ra = Column(Float)
    dec = Column(Float)
    type = Column(String(20))