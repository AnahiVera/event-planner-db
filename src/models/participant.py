from . import db

class Participant (db.Model):
    __tablename__= 'participants'
    id = db.Column()
    event_id = db.Column()
    user_id =db.Column()
    status = db.Column()

"""  status invitado confirmado rechazado """