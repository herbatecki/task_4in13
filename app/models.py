# app/models.py
from app import db

class Project(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), index=True, unique=True)
   start_date = db.Column(db.String(200))
   end_date = db.Column(db.String(128))

   def __str__(self):
       return f"<Project {self.name}>"
