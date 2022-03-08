from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ecomerce.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(255), unique=True)