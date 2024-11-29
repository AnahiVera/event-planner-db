from . import db

class Event(db.Model):
    __tablename__= 'events'
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column()
    description = db.Column()
    date = db.Column()
    time = db.Column()
    location = db.Column()
    organizer_id = db.Column()
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

