from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from core.db import engine

from app.user.model import Base as user_model

user_model.metadata.create_all(bind=engine)