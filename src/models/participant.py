from . import db

"""  status invitado, confirmado, rechazado """

class Participant (db.Model):
    __tablename__= 'participants'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    user_id =db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(20), default='invited')

    def serialize(self):
        return {
            "id":self.id,
            "event_id": self.event.serialize(),
            "user_id": self.user.serialize(),
            "status": self.status

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()