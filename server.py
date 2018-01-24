from flask import Flask, jsonify, request
from models.user import User

from sqlalchemy import or_
from database.database import scoped, engine

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Book of Faces Python Server App."

@app.route("/users", methods = ['GET'])
def users():
    users = [u.as_dict() for u in User.query.all()]
    return jsonify(users)

@app.route("/users/searchByName", methods = ['POST'])
def search():
    name=request.json["name"]
    users=[u.as_dict() for u in User.query.filter(or_(User.first_name.ilike('%'+name+'%'), User.last_name.ilike('%'+name+'%')))]
    return jsonify(users)

@app.teardown_appcontext
def shutdown_session(exception=None):
    scoped.remove()