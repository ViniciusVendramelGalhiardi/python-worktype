from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.utils.config_files import ConfigFiles
import os

engine = create_engine(ConfigFiles.Conn(), echo=True)
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine) 
Base = declarative_base() 

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()
