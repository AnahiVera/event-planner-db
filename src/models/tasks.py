from . import db

class Task (db.Model):
    __tablename__= 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column()
    description = db.Column()
    status = db.Column()
    event_id = db.Column()
    assignee_id = db.Column()