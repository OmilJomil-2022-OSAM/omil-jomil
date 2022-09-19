from sqlalchemy import Boolean, Column, String, Text, Integer

from core.db import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    uid = Column(String)
    password = Column(String)
    number = Column(String)
