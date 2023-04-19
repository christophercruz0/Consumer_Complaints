import sqlalchemy
import psycopg2
import datetime as dt
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine , inspect , func
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import pandas as pd

db_password = '!QAZ2wsx'

# Path to sqlite
database_path = f"postgresql://postgres:{db_password}@127.0.0.1:5432/CustomerComplaints"

# Create an engine that can talk to the database
engine = create_engine(database_path)

Base = automap_base()
Base.prepare(autoload_with=engine)
Complaints = Base.classes.complaints6

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
    #return product_count
    return jsonify(product_count)


@app.route("/api/v1.0/barchartmonth/<productType>")
def byMonthCount(productType):
    session = Session(engine)
    sel1 = [func.to_char(Complaints.date_received, 'Mon'),func.date_trunc('month',Complaints.date_received), func.to_char(Complaints.date_received, 'yyyy'), func.count(Complaints.complaint_id)]
    productData = session.query(*sel1).filter(Complaints.product == productType).group_by(func.to_char(Complaints.date_received, 'Mon'), func.to_char(Complaints.date_received, 'yyyy'),func.date_trunc('month',Complaints.date_received)).order_by(func.date_trunc('month',Complaints.date_received).asc()).all()
    session.close()
    by_month = []  
    for m, y, c, mn in productData:
        by_month_count = {}
        by_month_count["month"] = m
        by_month_count["month_2"] = y
        by_month_count["year"] = c
        by_month_count["count"] = mn
        by_month.append(by_month_count)   
    #return product_count
    return jsonify(by_month)



@app.route("/api/v1.0/barchart")
def byMonthCt():
    session = Session(engine)
    sel1 = [func.to_char(Complaints.date_received, 'Mon'),func.date_trunc('month',Complaints.date_received), func.to_char(Complaints.date_received, 'yyyy'), func.count(Complaints.complaint_id)]
    productData = session.query(*sel1).group_by(func.to_char(Complaints.date_received, 'Mon'), func.to_char(Complaints.date_received, 'yyyy'),func.date_trunc('month',Complaints.date_received)).order_by(func.date_trunc('month',Complaints.date_received).asc()).all()
    session.close()
    by_month = []  
    for m, y, c, mn in productData:
        by_month_count = {}
        by_month_count["month"] = m
        by_month_count["month_2"] = y
        by_month_count["year"] = c
        by_month_count["count"] = mn
        by_month.append(by_month_count)   
    #return product_count
    return jsonify(by_month)
 

@app.route("/api/v1.0/productList")
def byuniqueList():
    session = Session(engine)
    sel1 = [Complaints.product]
    productData = session.query(*sel1).group_by(Complaints.product).all()
    session.close()
    by_product = []  
    for m in productData:
        by_product_list = {}
        by_product_list["product"] = m.product
        by_product.append(by_product_list)   
    #return product_count
    return jsonify(by_product)



if __name__ == "__main__":
    app.run(debug=True)