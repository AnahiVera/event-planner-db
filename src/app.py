import os
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db
from dotenv import load_dotenv
from routes.auth import bp_auth 
from routes.tasks import bp_tasks
from routes.event import bp_event
from models import User

load_dotenv()

path = os.path.abspath("instance")

app = Flask(__name__, instance_path=path)
app.config['DEBUG'] = True 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

db.init_app(app)
Migrate(app, db)
jwt = JWTManager(app)
CORS(app)

app.register_blueprint(bp_auth, url_prefix="/api")
app.register_blueprint(bp_event, url_prefix="/api")
app.register_blueprint(bp_tasks, url_prefix="/api")

@app.route('/')
def main():
    return jsonify({"msg": "Server running correctly"}), 200

@app.route('/api/users')
def get_users():

    users = User.query.all()
    users= {user.name for user in users}

    return jsonify({"users": users}), 200

@app.route('/api/users', methods=['POST'])
def add_user():

    name = request.json.get('name')

    if not name:
        return jsonify({"status": "error", "message": "Name is required"}), 422
    
    found = User.query.filter_by(name=name).first()

    if found: 
        return jsonify({"status": "error", "message": "User already exists"}), 422
    
    user = User()
    user.name = name

    db.session.add(user)
    db.session.commit()

    return jsonify({"status": "success", "message": "User added successfully"}), 201


if __name__ == '__main__':
    app.run()

    