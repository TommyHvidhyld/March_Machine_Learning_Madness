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
# Tourney_Lat_Lng = Base.classes.Lat_Lng
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
    )

# Tourney Predictions data route:
@app.route("/api/v1.0/MarchMadness")
def tourney_data():
   # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a json of the columns below"""
    # Query all columns that we want from the dataset:
    results = session.query(MarchMadness.RK, MarchMadness.TEAM, MarchMadness.CONF, 
    MarchMadness.G, MarchMadness.W, MarchMadness.ADJOE, 
    MarchMadness.ADJDE, MarchMadness.BARTHAG, MarchMadness.EFG_O,
    MarchMadness.EFG_D, MarchMadness.TOR, 
    MarchMadness.TORD, MarchMadness.ORB, MarchMadness.FTR, MarchMadness.FTRD, MarchMadness.TWOP_O, 
    MarchMadness.TWOP_D, MarchMadness.THREEP_O, 
    MarchMadness.THREEP_D, MarchMadness.ADJ_T, 
    MarchMadness.WAB, MarchMadness.POSTSEASON,
    MarchMadness.SEED, MarchMadness.LATITUDE, MarchMadness.LONGITUD).all()

    session.close()

    # Create a dictionary from the row data and append to a list of tourney_data
    tourney_data = []
    for RK, TEAM, CONF, G, W, ADJOE, ADJDE, BARTHAG, EFG_O, EFG_D, TOR, TORD, ORB, FTR, FTRD, TWOP_O, TWOP_D, THREEP_O, THREEP_D, ADJ_T, WAB, POSTSEASON, SEED, LAT, LNG in results:
        cbbModel = {}
        cbbModel["RK"] = RK
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
        cbbModel['LATITUDE'] = LAT
        cbbModel['LONGITUD'] = LNG
        # Append the cbbModel dictionary to the tourney_data list to make a json:
        tourney_data.append(cbbModel)
    # Return the tourney_data json using jsonify to make it look nice:
    return jsonify(tourney_data)


if __name__ == "__main__":
    app.run(debug=True) 