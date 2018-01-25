from flask import Flask, jsonify, request
from models.user import User

from sqlalchemy import or_
from database.database import scoped, engine
from controllers.users import UsersController

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Book of Faces Python Server App."

@app.route("/users", methods = ['GET'])
def users():
    usersController = UsersController()
    return jsonify(usersController.getUsers())

@app.route("/search", methods = ['POST'])
def search():
    name = request.json["name"]
    usersController = UsersController()
    return jsonify(usersController.searchByName(name))

@app.route("/user", methods = ['GET'])
def getUserById():
   id = request.args.get('id')
   usersController = UsersController()
   return jsonify(usersController.getUserById(id))
   
@app.teardown_appcontext
def shutdown_session(exception=None):
    scoped.remove()