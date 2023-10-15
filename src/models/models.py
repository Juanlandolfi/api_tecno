'''ORM MODELS'''

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from ..database.database import engine

class Base(DeclarativeBase):
    '''Base'''


class ClientModel(Base):
    '''Client Model for ORM'''
    __tablename__ = "clients"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


class SuppliersModel(Base):
    '''Suppliers Model for ORM'''
    __tablename__ = "suppliers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    address: Mapped[str] = mapped_column(String(100), nullable=True)
    phone1: Mapped[str] = mapped_column(String(30), nullable=True)
    phone2: Mapped[str] = mapped_column(String(30), nullable=True)
    cuit: Mapped[int] = mapped_column(nullable=True)
    

class CategoriesModel(Base):
    '''Categories'''
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column(String(50))
    products: Mapped[List["ProductModel"]] = relationship(back_populates="category")



class TagsModel(Base):
    '''Tags'''
    __tablename__ = 'tags'
    id: Mapped[int] = mapped_column(primary_key=True)
    tag_name: Mapped[str] = mapped_column(String(50))

class MakeModel(Base):
    '''Tags'''
    __tablename__ = 'make'
    id: Mapped[int] = mapped_column(primary_key=True)
    tag_name: Mapped[str] = mapped_column(String(50))


class ProductModel(Base):
    '''Product model for ORM'''
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(90))
    price: Mapped[float]
    code_bar: Mapped[Optional[int]]
    code_prov: Mapped[Optional[str]] = mapped_column(String(15))
    maker_id: Mapped["MakeModel"] = mapped_column(ForeignKey('make.id'),nullable=True)
    stock: Mapped[int]
    description: Mapped[str] = mapped_column(String(500))
    category_id: Mapped["CategoriesModel"] = mapped_column(ForeignKey('categories.id'),nullable=True)
    category: Mapped["CategoriesModel"] = relationship(back_populates="products")

    tag_id: Mapped["TagsModel"] = mapped_column(ForeignKey('tags.id'), nullable=True)
    
    supplier_id: Mapped["SuppliersModel"] = mapped_column(ForeignKey('suppliers.id'), nullable=True)
    
    img_url: Mapped[str] = mapped_column(String(150), nullable=True)


# class 


Base.metadata.create_all(engine)