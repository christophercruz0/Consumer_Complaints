import sqlalchemy
import psycopg2
import datetime as dt
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine , inspect , func, desc
from flask import Flask, jsonify, render_template
from flask_cors import CORS

db_password = 'Project3'

# Path to sqlite
database_path = f"postgresql://postgres:{db_password}@127.0.0.1:5433/Project attempt"

# Create an engine that can talk to the database
engine = create_engine(database_path)

Base = automap_base()
Base.prepare(autoload_with=engine)
Complaints = Base.classes.complaints6

app = Flask(__name__)
CORS(app)

@app.route("/api/v1.0/productData/")
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

@app.route("/api/v1.0/companyData/")
def companyData():
    session = Session(engine)
    sel1 = [Complaints.company, func.count(Complaints.company)]
    companyData = session.query(*sel1).group_by(Complaints.company).all()
    session.close()
    company_count = []
    for name,count in companyData:
        company_count_dict = {}
        company_count_dict["company"] = name
        company_count_dict["count"] = count
        company_count.append(company_count_dict)   
    #return product_count
    return jsonify(company_count)



@app.route("/api/v1.0/top10Company/")
def topcompanyData():
    session = Session(engine)
    sel1 = [Complaints.company, func.count(Complaints.company)]
    topcompanyData = session.query(*sel1).group_by(Complaints.company).all()
    session.close()
    company_count = []
    for name,count in topcompanyData:
        company_count_dict = {}
        company_count_dict["company"] = name
        company_count_dict["count"] = count
        company_count.append(company_count_dict)   
        
    top_10_query = session.query(Complaints.company, func.count(Complaints.company)) \
                        .group_by(Complaints.company) \
                        .order_by(desc(func.count(Complaints.company))) \
                        .limit(10) \
                        .all()
    session.close()
    
    top_10 = []
    for name,count in top_10_query:
        top_10_dict = {}
        top_10_dict["company"] = name
        top_10_dict["count"] = count
        top_10.append(top_10_dict)
    
    return jsonify(top_10)


 
if __name__ == "__main__":

    app.run(debug=True)