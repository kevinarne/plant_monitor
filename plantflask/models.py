from plantflask import db
from datetime import datetime

class PlantEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    val = db.Column(db.Integer, nullable=False)
    plant = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f"PlantEvent (id = {self.id}, code = {self.code}, plant = {self.plant}, val = {self.val})"

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(30), nullable=False)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f"Plant ({self.id}, {self.nickname})"

class EventCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return f"EventCode (id = {self.id}, description = {self.description})"

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.String(1), nullable=False, default="n")
    type = db.Column(db.Integer, nullable=False)
    schedule = db.Column(db.String(20), nullable=False)
    units = db.Column(db.String(20), nullable=False)
    subscribed = db.Column(db.String(30))
    
    def __repr__(self):
        return f"Sensor ID: {self.id}"
