from sqlalchemy import Boolean, Column, String, Text, Integer

from core.db import Base

class Camera(Base):
    __tablename__ = 'camera'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    pos = Column(String)
