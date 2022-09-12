# in this file, we want to define the data model. 
# thus, the data object must be imported here
from app import db


# create a class which describes your data model

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    # method to represent the data
    def __repr__(self):
        return f'{self.title} created on {self.date}'