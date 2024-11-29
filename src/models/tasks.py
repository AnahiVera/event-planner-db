from . import db

class Task (db.Model):
    __tablename__= 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column()
    description = db.Column()
    status = db.Column()
    event_id = db.Column()
    assignee_id = db.Column()

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