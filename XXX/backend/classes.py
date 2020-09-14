#dont use  backend.py 
from datetime import datetime
from backend import db

class Citizen(db.Model):
    __tablename__ = 'flasksqlalchemy_citizen_db'
    ID = db.Column( db.Integer, primary_key=True )
    citizenname = db.Column( db.String(50), index=False, unique=True, nullable=False)
    citizencin = db.Column( db.String(80), index=False, unique=True, nullable=False)
    citizenpass = db.Column( db.String(80), nullable=False, unique=True)



    #magic method : here's how our project are printed 
    def __repr__(self):
    	return "Citizen({},{},{})".format(self.ID, self.citizenname, self.citizencin)
