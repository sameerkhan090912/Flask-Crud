from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///table1.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]="sqlite:///table1.db"
db=SQLAlchemy(app)

class Table1(db.Model):
    srno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    age=db.Column(db.Integer,nullable=False)

with app.app_context():
    db.create_all()