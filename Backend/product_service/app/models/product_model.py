from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.shared.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500))
    photo_url = Column(String(500))
    size = Column(String(50))
    weight = Column(String(50))
    unit_price = Column(Float, nullable=False)
    iva = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category")
