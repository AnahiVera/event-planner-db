from . import db

class Notification(db.Model):
    __tablename__= 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column()
    message = db.Column()
    is_read = db.Column()
    time = db.Column()
    created_at = db.Column()