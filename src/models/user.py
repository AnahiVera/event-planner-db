from . import db


class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    events = db.relationship('Event', backref='creator', lazy=True)
    tasks = db.relationship('Task', backref='assignee', lazy=True)
    
    def serialize(self):
        return {
            "id":self.id,
            "email":self.email,
            "is_active":self.is_active,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()