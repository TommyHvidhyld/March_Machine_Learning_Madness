import numpy as np

import os
import psycopg2
from flask import Flask, render_template

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify 
from flask_cors import CORS

###############################################
# Database Setup
###############################################
# Create engine for sqlalchemy
engine = create_engine("sqlite:///output/MarchMadnessML.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# print(Base.classes)

# Save reference to the table
Tourney_Lat_Lng = Base.classes.Lat_Lng
MarchMadness = Base.classes.Tournament_Predictions

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config["MarchMadnessML.sqlite"] = "sqlite:///output/MarchMadnessML.sqlite"
# Allow cross origin:
CORS(app) 

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/MarchMadness<br/>"
        f"/api/v1.0/MarchMadnessLatLng<br/>"
    )

# Tourney Predictions data route:
@app.route("/api/v1.0/MarchMadness")
def tourney_data():
   # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a json of the columns below"""
    # Query all columns that we want from the dataset:
    results = session.query(MarchMadness.index, MarchMadness.RK, MarchMadness.TEAM, MarchMadness.CONF, 
    MarchMadness.G, MarchMadness.W, MarchMadness.ADJOE, 
    MarchMadness.ADJDE, MarchMadness.BARTHAG, MarchMadness.EFG_O,
    MarchMadness.EFG_D, MarchMadness.TOR, 
    MarchMadness.TORD, MarchMadness.ORB, MarchMadness.FTR, MarchMadness.FTRD, MarchMadness.TWOP_O, 
    MarchMadness.TWOP_D, MarchMadness.THREEP_O, 
    MarchMadness.THREEP_D, MarchMadness.ADJ_T, 
    MarchMadness.WAB, MarchMadness.POSTSEASON,
    MarchMadness.SEED).all()

    session.close()

    # Create a dictionary from the row data and append to a list of tourney_data
    tourney_data = []
    for index, TEAM, CONF, G, W, ADJOE, ADJDE, BARTHAG, EFG_O, EFG_D, TOR, TORD,ORB, FTR, FTRD, TWOP_O, TWOP_D, THREEP_O, THREEP_D, ADJ_T, WAB, POSTSEASON, SEED, YEAR in results:
        cbbModel = {}
        cbbModel["index"] = index
        cbbModel["TEAM"] = TEAM
        cbbModel["CONF"] = CONF
        cbbModel["G"] = G
        cbbModel["W"] = W
        cbbModel["ADJOE"] = ADJOE
        cbbModel["ADJDE"] = ADJDE
        cbbModel["BARTHAG"] = BARTHAG
        cbbModel["EFG_O"] = EFG_O
        cbbModel["EFG_D"] = EFG_D
        cbbModel["TOR"] = TOR
        cbbModel["TORD"] = TORD
        cbbModel["ORB"] = ORB
        cbbModel["FTR"] = FTR
        cbbModel["FTRD"] = FTRD
        cbbModel["TWOP_O"] = TWOP_O
        cbbModel["TWOP_D"] = TWOP_D
        cbbModel["THREEP_O"] = THREEP_O
        cbbModel["THREEP_D"] = THREEP_D
        cbbModel["ADJ_T"] = ADJ_T
        cbbModel["WAB"] = WAB
        cbbModel["POSTSEASON"] = POSTSEASON
        cbbModel["SEED"] = SEED
        cbbModel["YEAR"] = YEAR
        # Append the cbbModel dictionary to the tourney_data list to make a json:
        tourney_data.append(cbbModel)
    # Return the tourney_data json using jsonify to make it look nice:
    return jsonify(tourney_data)

# Tournament teams lat and lng data route:
@app.route("/api/v1.0/MarchMadnessLatLng")
def tourney_latlng_data():
   # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a json of the columns below"""
    # Query all columns that we want from the dataset:
    results2 = session.query(Tourney_Lat_Lng.index, Tourney_Lat_Lng.RK, Tourney_Lat_Lng.TEAM, Tourney_Lat_Lng.CONF, 
    Tourney_Lat_Lng.G, Tourney_Lat_Lng.W, Tourney_Lat_Lng.ADJOE, 
    Tourney_Lat_Lng.ADJDE, Tourney_Lat_Lng.BARTHAG, Tourney_Lat_Lng.EFG_O,
    Tourney_Lat_Lng.EFG_D, Tourney_Lat_Lng.TOR, 
    Tourney_Lat_Lng.TORD, Tourney_Lat_Lng.ORB, Tourney_Lat_Lng.FTR, Tourney_Lat_Lng.FTRD, Tourney_Lat_Lng.TWOP_O, 
    Tourney_Lat_Lng.TWOP_D, Tourney_Lat_Lng.THREEP_O, 
    Tourney_Lat_Lng.THREEP_D, Tourney_Lat_Lng.ADJ_T, 
    Tourney_Lat_Lng.WAB, Tourney_Lat_Lng.POSTSEASON, Tourney_Lat_Lng.SEED, Tourney_Lat_Lng.LONGITUD, Tourney_Lat_Lng.LATITUDE).all() 

    session.close()

    Lat_Lng_data = []
    for index, RK, TEAM, CONF, G, W, ADJOE, ADJDE, BARTHAG, EFG_O, EFG_D, TOR, TORD,ORB, FTR, FTRD, TWOP_O, TWOP_D, THREEP_O, THREEP_D, ADJ_T, WAB, POSTSEASON, SEED, LONGITUD, LATITUDE in results2:
        MarchMadnessdict = {}
        MarchMadnessdict["index"] = index
        MarchMadnessdict["RK"] = RK
        MarchMadnessdict["TEAM"] = TEAM
        MarchMadnessdict["CONF"] = CONF
        MarchMadnessdict["G"] = G
        MarchMadnessdict["W"] = W
        MarchMadnessdict["ADJOE"] = ADJOE
        MarchMadnessdict["ADJDE"] = ADJDE
        MarchMadnessdict["BARTHAG"] = BARTHAG
        MarchMadnessdict["EFG_O"] = EFG_O
        MarchMadnessdict["EFG_D"] = EFG_D
        MarchMadnessdict["TOR"] = TOR
        MarchMadnessdict["TORD"] = TORD
        MarchMadnessdict["ORB"] = ORB
        MarchMadnessdict["FTR"] = FTR
        MarchMadnessdict["FTRD"] = FTRD
        MarchMadnessdict["TWOP_O"] = TWOP_O
        MarchMadnessdict["TWOP_D"] = TWOP_D
        MarchMadnessdict["THREEP_O"] = THREEP_O
        MarchMadnessdict["THREEP_D"] = THREEP_D
        MarchMadnessdict["ADJ_T"] = ADJ_T
        MarchMadnessdict["WAB"] = WAB
        MarchMadnessdict["POSTSEASON"] = POSTSEASON
        MarchMadnessdict["SEED"] = SEED
        MarchMadnessdict["LONGITUD"] = LONGITUD
        MarchMadnessdict["LATITUDE"] = LATITUDE
        # Append the march madness dictionary to the Lat_Lng_data list to make a json:
        Lat_Lng_data.append(MarchMadnessdict)
        # Return the Lat_Lng_data json using jsonify to make it look nice:
    return jsonify(Lat_Lng_data)  


if __name__ == "__main__":
    app.run(debug=True) 