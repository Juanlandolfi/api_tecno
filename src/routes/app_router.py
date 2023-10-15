from fastapi import APIRouter, Query
from sqlalchemy.orm import Session
from ..models.models import ProductModel, CategoriesModel, TagsModel
from ..database.database import engine
from ..schemas.schemas import Product, StringItem


router = APIRouter()

## POST Routes

@router.post("/new_product")
async def create_product(product: Product):
    '''Endpoint for creating new product'''
    with Session(engine) as session:
        session.add(
            ProductModel(
                        **dict(product)
                        )
                    )
        session.commit()
    return 'Product added'

@router.post("/new_category")
async def create_product(item: StringItem):
    '''Endpoint for creating new product'''
    with Session(engine) as session:
        session.add(
            CategoriesModel(
                        category_name = item.name
                        )
                    )
        session.commit()
    return 'Category added'

@router.get('/get_products')
async def get_products(limit: int = Query(None, gt=0)):
    '''Endpoint to retrieve products from database'''
    #TODO: Agregar limit en consulta si es none devolver todo
    with Session(engine) as session:
        result = session.query(ProductModel).all()
    return result


# from sqlalchemy import select

# with Session(engine) as session:
#     result = session.execute(select(ProductModel).where(ProductModel.category_id == 1))
#     for item in result.scalars():
#         print(item.product_name)