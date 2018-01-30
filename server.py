from flask import Flask, jsonify, request
import uuid
import hashlib

from models.user import User

from sqlalchemy import or_
from database.database import scoped, engine

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Book of Faces Python Server App."

@app.route("/users", methods=['GET'])
def users():
    users = [u.as_dict() for u in User.query.all()]
    return jsonify(users)

@app.route("/users/searchByName", methods=['POST'])
def search():
    name = request.json["name"]
    users = [u.as_dict() for u in User.query.filter(or_(User.first_name.ilike('%'+name+'%'), 
                                                        User.last_name.ilike('%'+name+'%')))]
    return jsonify(users)

@app.route("/users/create", methods=['POST'])
def createUser():
    try:
        if User.query.filter(User.email == request.json["email"]).count() == 0:
            salt = uuid.uuid4().hex
            password = request.json["password"]
            hash_object = hashlib.sha256(salt.encode() + password.encode())
            hex_dig = hash_object.hexdigest() + ':' + salt
            user = User(
                request.json["first_name"],
                request.json["last_name"],
                request.json["email"],
                request.json["admin"],
                hex_dig,
                request.json["photo_url"],
                request.json["slack_handle"],
                request.json["nickname"],
                request.json["title"],
                request.json["location"],
                request.json["manager_id"],
                request.json["about_me"],
                request.json["interests"],
            )
            scoped.add(user)
            scoped.commit()
            addedUser = [u.as_dict() for u in User.query.filter(
                User.email == request.json["email"]).all()]
            return jsonify(
                StatusCode=201,
                statusMessage="User Added",
                User=addedUser
            )
        else:
            return jsonify(
                StatusCode=400,
                statusMessage="Email already exists."
            ), 400
    except:
        return jsonify(
            StatusCode=500,
            statusMessage='Something went wrong! Please try again.',
            ), 500

@app.teardown_appcontext
def shutdown_session(exception=None):
    scoped.remove()