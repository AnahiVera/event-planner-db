from . import db
from datetime import datetime

""" status completed or pending """

class Task (db.Model):
    __tablename__= 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    due_date = db.Column(db.DateTime)

    def serialize(self):
        return {
            "id":self.id,
            "event_id": self.event.serialize(),
            "tittle": self.tittle,
            "status": self.status,
            "assigned_to": self.user.serialize(),
            "due_date": self.due_date
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()