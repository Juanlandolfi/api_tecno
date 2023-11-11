"""Pydantic models for TECNOPOWER API"""
from typing import List
from pydantic import BaseModel, Field


class Product(BaseModel):
    """Product schema for products in TECNOPOWER"""
    product_name: str
    price: float = Field(gte=0)
    code_bar: str | None = None
    code_prov: str | None = None
    maker_id: int  | None = None
    stock: int | None = 0
    description: str | None = 'Producto sin descripción'
    category_id: int  | None 
    tag: List[int] | None = []
    supplier_id: int | None = None
    img_url: str | None = None
    
    class Config:
        from_attributes = True


class Supplier(BaseModel):
    """Supplier schema"""
    supplier_id: int
    supplier_name: str
    supplier_address: str
    supplier_phone1: int
    supplier_phone2: int
    supplier_cuit: int
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


class ResponseGetProducts(Product):
    id_product: int
    category: Category = []
    tag: List[Tags] = []
    class Config:
        from_attributes = True


class MakeCreate(BaseModel):
    make_name: str