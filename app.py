#9.5.1
#Set Up the Flask Weather App

#Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

#Dependencies for SQLAlchemy (access our data in the SQLite database)
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Dependencies for Flask
from flask import Flask, jsonify

#Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")

#Reflect the database into our classes
Base = automap_base()

#Reflect the tables
Base.prepare(engine, reflect=True)

#Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create a session link from Python to our database
session = Session(engine)

#Set Up Flask
app = Flask(__name__)

#9.5.2
#Create the Welcome Route
#Our first task when creating a Flask route is to define what our route will be. 
# #We want our welcome route to be the root, which in our case is essentially the homepage.

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
#When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route
#This line can be updated to support future versions of the app

#Type "flask run" in GitBash (with C:\Users\szewi\Documents\Class\Surfs_Up)


#9.5.3
#Build a second route (Precipitation analysis)
#Make sure that it's aligned all the way to the left as this is a new route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
