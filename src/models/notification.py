from . import db
from datetime import datetime

class Notification(db.Model):
    __tablename__= 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String)
    is_read = is_active = db.Column(db.Boolean, default=False)
    time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now(datetime.timezone.utc))

    def serialize(self):
        return {
            "id":self.id,
            "user_id": self.user.serialize(),
            "message": self.message,
            "is_read": self.is_read,
            "time": self.time,
            "created_at": self.created_at
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()