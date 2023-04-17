import sqlalchemy
import psycopg2
import datetime as dt
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine , inspect , func
from flask import Flask, jsonify, render_template
from flask_cors import CORS

db_password = 'postgres'

# Path to sqlite
database_path = f"postgresql://postgres:{db_password}@127.0.0.1:5432/Consumer_complaints_db"

# Create an engine that can talk to the database
engine = create_engine(database_path)

Base = automap_base()
Base.prepare(autoload_with=engine)
Complaints = Base.classes.complaints

app = Flask(__name__)
CORS(app)

@app.route("/api/v1.0/productdata")
def productData():
    session = Session(engine)
    sel1 = [Complaints.product, func.count(Complaints.product)]
    productData = session.query(*sel1).group_by(Complaints.product).all()
    session.close()
    product_count = []
    for name,count in productData:
        product_count_dict = {}
        product_count_dict["name"] = name
        product_count_dict["count"] = count
        product_count.append(product_count_dict)   
    return product_count
 
if __name__ == "__main__":
    app.run(debug=True)