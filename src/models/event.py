from . import db
from datetime import datetime

class Event(db.Model):
    __tablename__= 'events'
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False )
    location = db.Column(db.String)
    organizer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.DateTime, onupdate=datetime.now(datetime.timezone.utc))
    
    def serialize(self):
        return {
            "id":self.id,
            "tittle": self.tittle,
            "description": self.description,
            "date": self.date,
            "location": self.location,
            "organizer_id": self.user.serialize()
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

