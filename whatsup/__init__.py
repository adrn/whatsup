# -*- coding: utf-8 -*-
""" 
    What's Up?
    ----------
    A web-based, observational astronomy educational tool.
    
"""

from flask import Flask, render_template, request, g, session, flash, redirect, url_for, abort

# Import project-specific database objects
from whatsup.database import db_session, database_url
from whatsup.models import User, AstroObject

import apwlib.geometry as g
import apwlib.convert as c

# setup flask
app = Flask(__name__)
app.config.update(
    DATABASE_URI = database_url,
    SECRET_KEY = "4e5eb5a5-d01e-49e4-868e-0db93cfa30aa",
    DEBUG = True
)

# Views
import whatsup.openid

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

@app.before_request
def before_request():
    g.user = None
    if 'openid' in session:
        g.user = User.query.filter_by(openid=session['openid']).first()

@app.after_request
def after_request(response):
    db_session.remove()
    return response

@app.route('/')
def index():
    return render_template('index.html')

#@app.errorhandler(404)
#def not_found(error):
#    return render_template('error.html'), 404

@app.route('/objects', methods=['POST', 'GET'])
def objects():
    """ Return a list of objects given filter parameters """
    url_parameters = dict(request.args)
    
    main_query = AstroObject.query
    
    if url_parameters.has_key("type"):
        object_types = []
        for object_type in url_parameters["type"]:
            # Validate object type input
            if object_type not in ["star", "galaxy", "nebula", "other"]:
                # some kind of error?
                pass
            else:
                object_types.append(object_type)
        
        main_query = main_query.filter(AstroObject.type.in_(object_types))
    
    if url_parameters.has_key("utc_time"):
        pass
        
    if url_parameters.has_key("date"):
        pass
        
    if url_parameters.has_key("latitude"):
        pass
    
    if url_parameters.has_key("longitude"):
        pass
    
    objects = main_query.all()
    
    return render_template('objects.html', objects=objects)