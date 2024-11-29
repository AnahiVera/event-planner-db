from . import db
"""  status invitado confirmado rechazado """
class Participant (db.Model):
    __tablename__= 'participants'
    id = db.Column()
    event_id = db.Column()
    user_id =db.Column()
    status = db.Column()

    def serialize(self):
        return {
            "id":self.id
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()