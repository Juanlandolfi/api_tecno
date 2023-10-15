"""Pydantic models for TECNOPOWER API"""
from typing import List
from pydantic import BaseModel, Field, HttpUrl


class Product(BaseModel):
    """Product schema for products in TECNOPOWER"""
    product_name: str
    price: float = Field(gt=0)
    code_bar: str | None = None
    code_prov: str | None = None
    maker_id: int  | None = None
    stock: int | None = 0
    description: str | None = 'Producto sin descripción'
    category_id: int  | None = None
    tag_id: int | None = None
    supplier_id: int | None = None
    img_url: HttpUrl | None = None



class Supplier(BaseModel):
    """Supplier schema"""
    supplier_id: int
    supplier_name: str
    supplier_address: str
    supplier_phone1: int
    supplier_phone2: int
    supplier_cuit: int


class ItemOrder(BaseModel):
    """Item schema for items in orders"""
    product: Product
    discount: int
    quantity: int | float


class Order(BaseModel):
    """Order schema for client orders"""
    order_id: int
    client_id: int
    product_id: int
    shipment_id: int
    items: List[ItemOrder]


class Client(BaseModel):
    """Client schema for clients table"""
    client_id: int
    client_name: str
    client_birth_date: str

class StringItem(BaseModel):
    '''Category schema for categories table'''
    name: str