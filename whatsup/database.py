# -*- coding: utf-8 -*-
""" 
    Database for What's Up?
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = "sqlite:///flask-openid.db"

engine = create_engine(database_url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """ Create any tables that subclass Base """
    import models
    Base.metadata.create_all(bind=engine)
    
    # THIS IS JUST FOR MY INITIAL TESTS!
    import apwlib.geometry as g
    print "CALLED"
    albireo = models.AstroObject()
    albireo.name = "albireo a"
    albireo.ra = g.RA("19h30m43.2915s").degrees
    albireo.dec = g.Dec("+27:57:34.73").degrees
    albireo.type = "star"
    db_session.add(albireo)
    
    andromeda = models.AstroObject()
    andromeda.name = "andromeda"
    andromeda.ra = g.RA("00h42m44.3s").degrees
    andromeda.dec = g.Dec("+41:16:09").degrees
    andromeda.type = "galaxy"
    db_session.add(andromeda)
    
    db_session.commit()