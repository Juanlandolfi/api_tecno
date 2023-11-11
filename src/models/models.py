'''ORM MODELS'''

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from src.database.database import engine

class Base(DeclarativeBase):
    '''Base'''

product_tags_table = Table(
    "products_tags_table",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id_product"), primary_key=True),
)

product_categories_table = Table(
    "products_categories_table",
    Base.metadata,
    Column("category_id", ForeignKey("categories.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id_product"), primary_key=True),
)



class ClientModel(Base):
    '''Client Model for ORM'''
    __tablename__ = "clients"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    other: Mapped[str] = mapped_column(String(50))


class SuppliersModel(Base):
    '''Suppliers Model for ORM'''
    __tablename__ = "suppliers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    address: Mapped[str] = mapped_column(String(100), nullable=True)
    phone1: Mapped[str] = mapped_column(String(30), nullable=True)
    phone2: Mapped[str] = mapped_column(String(30), nullable=True)
    cuit: Mapped[int] = mapped_column(nullable=True)
    products: Mapped[List["ProductModel"]] = relationship(back_populates='supplier')


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
    products: Mapped[List["ProductModel"]] = relationship(secondary=product_tags_table, back_populates="tag") #nuevo


class MakerModel(Base):
    '''Maker'''
    __tablename__ = 'make'
    id: Mapped[int] = mapped_column(primary_key=True)
    maker_name: Mapped[str] = mapped_column(String(50))
    products: Mapped[List["ProductModel"]] = relationship(back_populates="maker") #nuevo


class ProductModel(Base):
    '''Product model for ORM'''
    __tablename__ = 'products'
    #Columns
    id_product: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(90))
    price: Mapped[float]
    code_bar: Mapped[Optional[str]] = mapped_column(String(13), nullable=True)
    code_prov: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    stock: Mapped[int]
    description: Mapped[str] = mapped_column(String(500))
    maker_id: Mapped[int] = mapped_column(ForeignKey("make.id"), nullable=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"), nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=True)
    img_url: Mapped[str] = mapped_column(String(150), nullable=True)
    #Relationships
    maker: Mapped["MakerModel"] = relationship(back_populates="products")
    supplier: Mapped["SuppliersModel"] = relationship(back_populates="products")
    category: Mapped["CategoriesModel"] = relationship(back_populates="products")
    tag: Mapped[List["TagsModel"]] = relationship(secondary=product_tags_table, back_populates="products") # nuevo
    


Base.metadata.create_all(engine)