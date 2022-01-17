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
        return "__repr__ not set"
