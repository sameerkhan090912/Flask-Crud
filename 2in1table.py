from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///1table.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
db=SQLAlchemy(app)

class Table2in1(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    rollno=db.Column(db.Integer,nullable=False)
    name=db.Column(db.String(200),nullable=False)
    AddmisionDate=db.Column(db.Date,nullable=True)

class Table2in2(db.Model):
    empId=db.Column(db.Integer,primary_key=True)
    address=db.Column(db.String(300),nullable=False)
    salary=db.Column(db.Float,nullable=False)

with app.app_context():
    db.create_all()