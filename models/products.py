from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *

class Product(Base):
        __tablename__ = 'producrs'

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String)
        slug = Column(String, unique=True, index=True)
        desxription = Column(String)
        price = Column(Integer)
        image_url = Column(String)
        stock = Column(Integer)
        category_id = Column(Integer, ForeignKey('category.id'))
        rating = Column(Float)
        is_active = Column(Boolean,default=True)

        category = relationship("Category", back_populates='products')