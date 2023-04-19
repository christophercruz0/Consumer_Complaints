from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date


# Create table class 
Base = declarative_base()
class Complaints(Base):
    __tablename__ = 'complaints'
    date_received  = Column(Date)
    product  = Column(String)
    sub_product = Column(String)
    issue = Column(String)
    sub_issue = Column(String)
    company = Column(String)
    state = Column(String)
    zip_code = Column(String)
    consumer_consent_provided = Column(String)
    submitted_via = Column(String)
    date_sent_to_company = Column(Date)
    company_response_to_consumer = Column(String)
    timely_response = Column(String)
    complaint_ID = Column(Integer, primary_key=True)

# path to sqlite database
database_path = "sqlite:///../Resources/complaints.sqlite"

# create engine and databse 
engine = create_engine(database_path)
Base.metadata.create_all(engine)


# Create a Flask object 
app = Flask(__name__)

# enable CORS for API requests with dashboard
CORS(app)

# TODO:create multiple routes for API Request

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/productdata.json<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/names<br/>"
    )


@app.route("/api/v1.0/productdata.json")
def productData():
    session = Session(engine)
    
    productData = session.execute('''SELECT product, COUNT(product) 
                                    FROM complaints 
                                    GROUP BY product ''').fetchall()
    session.close()

    product_count = dict(productData)
    return jsonify(product_count)
 
if __name__ == "__main__":
    app.run(debug=True)