from . import db

class Notification(db.Model):
    __tablename__= 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column()
    message = db.Column()
    is_read = db.Column()
    time = db.Column()
    created_at = db.Column()

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