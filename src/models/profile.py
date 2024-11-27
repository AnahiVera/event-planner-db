from . import db

class Profile(db.Model):
    __tablename__= 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    
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

