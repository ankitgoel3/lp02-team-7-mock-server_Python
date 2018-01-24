import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

config = configparser.ConfigParser()
config.read('env.ini')
engine = create_engine(config['database']['url'])

Base = declarative_base()
scoped = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base.query = scoped.query_property()
