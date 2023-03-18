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
# reflect=True
# print(Base.classes)

# Save reference to the table
# cbbModel = Base.classes.MarchMadnessML
MarchMadness = Base.classes.Tournament_Predictions
# cbbModel_Predictions = Base.classes.MarchMadnessML

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

# ZHVI and Risk Index data route:
# @app.route("/api/v1.0/cbbModel")
# def home_risk():
#    # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a json of the columns below"""
#     # Query all columns that we want from the dataset:
#     results = session.query(cbbModel.TEAM, cbbModel.CONF, 
#     cbbModel.G, cbbModel.W, cbbModel.ADJOE, 
#     cbbModel.ADJDE, cbbModel.BARTHAG, cbbModel.EFG_O,
#     cbbModel.EFG_D, cbbModel.TOR, 
#     cbbModel.TORD, cbbModel.ORB, cbbModel.FTR, cbbModel.FTRD, cbbModel.TWOP_O, 
#     cbbModel.TWOP_D, cbbModel.THREEP_O, 
#     cbbModel.THREEP_D, cbbModel.ADJ_T, 
#     cbbModel.WAB, cbbModel.POSTSEASON,
#     cbbModel.SEED, cbbModel.YEAR).all() 
    

# ZHVI and Risk Index data route:
@app.route("/api/v1.0/MarchMadness")
def home_risk():
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
    MarchMadness.SEED).all() 

# ZHVI and Risk Index data route:
# @app.route("/api/v1.0/cbbModel_Predictions")
# def home_risk():
#    # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a json of the columns below"""
#     # Query all columns that we want from the dataset:
#     results = session.query(cbbModel_Predictions.RK, cbbModel_Predictions.TEAM, cbbModel_Predictions.CONF, 
#     cbbModel_Predictions.G, cbbModel_Predictions.W, cbbModel_Predictions.ADJOE, 
#     cbbModel_Predictions.ADJDE, cbbModel_Predictions.BARTHAG, cbbModel_Predictions.EFG_O,
#     cbbModel_Predictions.EFG_D, cbbModel_Predictions.TOR, 
#     cbbModel_Predictions.TORD, cbbModel_Predictions.ORB, cbbModel_Predictions.FTR, cbbModel_Predictions.FTRD, cbbModel_Predictions.TWOP_O, 
#     cbbModel_Predictions.TWOP_D, cbbModel_Predictions.THREEP_O, 
#     cbbModel_Predictions.THREEP_D, cbbModel_Predictions.ADJ_T, 
#     cbbModel_Predictions.WAB, cbbModel_Predictions.POSTSEASON).all() 

    session.close()

    # Create a dictionary from the row data and append to a list of all_hv_risk
    # cbbModelModel1 = []
    # for TEAM, CONF, G, W, ADJOE, ADJDE, BARTHAG, EFG_O, EFG_D, TOR, TORD,ORB, FTR, FTRD, TWOP_O, TWOP_D, THREEP_O, THREEP_D, ADJ_T, WAB, POSTSEASON, SEED, YEAR in results:
    #     cbbModel = {}
    #     cbbModel["TEAM"] = TEAM
    #     cbbModel["CONF"] = CONF
    #     cbbModel["G"] = G
    #     cbbModel["W"] = W
    #     cbbModel["ADJOE"] = ADJOE
    #     cbbModel["ADJDE"] = ADJDE
    #     cbbModel["BARTHAG"] = BARTHAG
    #     cbbModel["EFG_O"] = EFG_O
    #     cbbModel["EFG_D"] = EFG_D
    #     cbbModel["TOR"] = TOR
    #     cbbModel["TORD"] = TORD
    #     cbbModel["ORB"] = ORB
    #     cbbModel["FTR"] = FTR
    #     cbbModel["FTRD"] = FTRD
    #     cbbModel["TWOP_O"] = TWOP_O
    #     cbbModel["TWOP_D"] = TWOP_D
    #     cbbModel["THREEP_O"] = THREEP_O
    #     cbbModel["THREEP_D"] = THREEP_D
    #     cbbModel["ADJ_T"] = ADJ_T
    #     cbbModel["WAB"] = WAB
    #     cbbModel["POSTSEASON"] = POSTSEASON
    #     cbbModel["SEED"] = SEED
    #     cbbModel["YEAR"] = YEAR
    #     # Append the cbbModel dictionary to the all_hv_risk list to make a json:
    #     cbbModelModel1.append(cbbModel)
    # Return the all_hv_risk json using jsonify to make it look nice:
    # return jsonify(cbbModelModel1)  


    Tournament_PredictionsModel2 = []
    for RK, TEAM, CONF, G, W, ADJOE, ADJDE, BARTHAG, EFG_O, EFG_D, TOR, TORD,ORB, FTR, FTRD, TWOP_O, TWOP_D, THREEP_O, THREEP_D, ADJ_T, WAB, POSTSEASON, SEED in results:
        MarchMadnessdict = {}
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
        # Append the cbbModel dictionary to the all_hv_risk list to make a json:
        Tournament_PredictionsModel2.append(MarchMadnessdict)
    # Return the all_hv_risk json using jsonify to make it look nice:
    return jsonify(Tournament_PredictionsModel2)  

# cbbModel_PredictionsModel3 = []
# for RK, TEAM, CONF, G, W, ADJOE, ADJDE, BARTHAG, EFG_O, EFG_D, TOR, TORD,ORB, FTR, FTRD, TWOP_O, TWOP_D, THREEP_O, THREEP_D, ADJ_T, WAB, POSTSEASON, SEED in results:
#         cbbModel_Predictions = {}
#         cbbModel_Predictions["RK"] = RK
#         cbbModel_Predictions["TEAM"] = TEAM
#         cbbModel_Predictions["CONF"] = CONF
#         cbbModel_Predictions["G"] = G
#         cbbModel_Predictions["W"] = W
#         cbbModel_Predictions["ADJOE"] = ADJOE
#         cbbModel_Predictions["ADJDE"] = ADJDE
#         cbbModel_Predictions["BARTHAG"] = BARTHAG
#         cbbModel_Predictions["EFG_O"] = EFG_O
#         cbbModel_Predictions["EFG_D"] = EFG_D
#         cbbModel_Predictions["TOR"] = TOR
#         cbbModel_Predictions["TORD"] = TORD
#         cbbModel_Predictions["ORB"] = ORB
#         cbbModel_Predictions["FTR"] = FTR
#         cbbModel_Predictions["FTRD"] = FTRD
#         cbbModel_Predictions["TWOP_O"] = TWOP_O
#         cbbModel_Predictions["TWOP_D"] = TWOP_D
#         cbbModel_Predictions["THREEP_O"] = THREEP_O
#         cbbModel_Predictions["THREEP_D"] = THREEP_D
#         cbbModel_Predictions["ADJ_T"] = ADJ_T
#         cbbModel_Predictions["WAB"] = WAB
#         cbbModel_Predictions["POSTSEASON"] = POSTSEASON
#         cbbModel_Predictions["SEED"] = SEED
#         # Append the cbbModel dictionary to the all_hv_risk list to make a json:
#         cbbModel_PredictionsModel3.append(cbbModel_Predictions)
#     # Return the all_hv_risk json using jsonify to make it look nice:
# return jsonify(cbbModel_PredictionsModel3)  

if __name__ == "__main__":
    app.run(debug=True) 