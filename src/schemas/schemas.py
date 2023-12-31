"""Pydantic models for TECNOPOWER API"""
from typing import List
from pydantic import BaseModel, Field


class Product(BaseModel):
    """Product schema for products in TECNOPOWER"""
    product_name: str
    price: float = Field(gte=0)
    maker_id: int  | None = None
    stock: int | None = 0
    description: str | None = 'Producto sin descripción'
    category_id: int  | None 
    tag: List[int] | None = []
    img_url: str | None = None
    
    class Config:
        from_attributes = True


class ItemOrder(BaseModel):
    """Item schema for items in orders"""
    product: Product
    discount: int
    quantity: int | float
    class Config:
        '''pydantic config'''
        from_attributes = True


class Order(BaseModel):
    """Order schema for client orders"""
    order_id: int
    client_id: int
    product_id: int
    shipment_id: int
    items: List[ItemOrder]
    class Config:
        from_attributes = True


class Client(BaseModel):
    """Client schema for clients table"""
    client_id: int
    client_name: str
    client_birth_date: str
    class Config:
        from_attributes = True

class StringItem(BaseModel):
    '''Category schema for categories table'''
    name: str
    class Config:
        from_attributes = True


class Tags(BaseModel):
    id: int
    tag_name: str
    class Config:
        from_attributes = True


class Category(BaseModel):
    id: int
    category_name: str
    class Config:
        from_attributes = True

class Maker(BaseModel):
    id: int
    maker_name: str


class MakeCreate(BaseModel):
    make_name: str

class ResponseGetProducts(Product):
    id_product: int
    category: Category | None= None
    tag: List[Tags] | None = []
    maker: Maker | None = None
    class Config:
        from_attributes = True

