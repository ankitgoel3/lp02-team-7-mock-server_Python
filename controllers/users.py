from models.user import User

from sqlalchemy import or_ ,desc
from database.database import scoped, engine
import random

class UsersController:
      def __init__(self):
          self.sortArray= ['id','first_name','last_name','photo_url','password_digest','created_at','updated_at']
          self.userLimit =3

      def getUsers(self):
          sortKey =  random.choice(self.sortArray)
          users=  [u.as_dict() for u in User.query.order_by(desc(sortKey)).limit(self.userLimit).all()] 
          return users  

      def searchByName(self,name):
          sortKey =  random.choice(self.sortArray)
          users=[u.as_dict() for u in User.query.order_by(desc(sortKey)).filter(or_(User.first_name.ilike('%'+name+'%'), User.last_name.ilike('%'+name+'%'))).limit(self.userLimit).all()]
          return users

      def getUserById(self,userId):
          users = [u.as_dict() for u in User.query.filter_by(id=userId)]
          return users
      
