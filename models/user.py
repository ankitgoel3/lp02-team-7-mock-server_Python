from utils.to_json import ToJson
from database.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

class User(ToJson, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True)
    admin = Column(Boolean)
    password_digest = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    photo_url = Column(String(500))
    slack_handle = Column(String(255))
    nickname = Column(String(100))
    title = Column(String(500))
    location = Column(String(500))
    manager_id = Column(Integer)
    about_me = Column(String(500))
    interests = Column(String(500))


    def __init__(self, first_name=None, last_name=None, email=None, admin=False, password_digest=None,photo_url=None,slack_handle=None,nickname=None,title=None,location=None,manager_id=None,about_me=None,interests=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.admin = admin
        self.password_digest=password_digest
        self.photo_url = photo_url
        self.slack_handle = slack_handle
        self.nickname = nickname
        self.title = title
        self.location = location
        self.manager_id = manager_id
        self.about_me = about_me
        self.interests = interests

    # @property
    # def createdAt(self):
    #     return self.created_at.isoformat()

    def __repr__(self):
       return '<User %r>' % (self.email)
