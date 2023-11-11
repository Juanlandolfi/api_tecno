from typing import List
from enum import Enum
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.database.database import get_db, engine
from src.schemas import schemas
from src.routes import crud
from src.models.models import ProductModel, CategoriesModel, TagsModel, MakerModel, Base
from pymysql.err import IntegrityError


router = APIRouter()

class RouteTags(Enum):
    '''Enum for tags in routes decorators'''
    PRODUCTS = 'Products'
    CATEGORIES = 'Categories'
    TAGS = 'Tags'
    MAKERS = 'Makers'


## POST Routes

@router.post("/new_product",
             status_code=status.HTTP_201_CREATED,
             tags=[RouteTags.PRODUCTS])
async def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    '''Endpoint for creating new product'''
    # __import__("pdb").set_trace()
    try:
        crud.create_new_product(db, product)
        return {"message": "Product added"}
    except IntegrityError:
        return {"message": "Algo no salio bien"}



@router.post("/new_category",
             status_code=status.HTTP_201_CREATED,
             tags=[RouteTags.CATEGORIES])
async def create_category(item: schemas.StringItem, db: Session = Depends(get_db)):
    '''Endpoint for creating new Category'''
    result = db.execute(
        select(CategoriesModel)
        .where(CategoriesModel.category_name ==  item.name))
    if result.scalar():
        return {'messagge': 'Ya existe una categoría con ese nombre'}
    db.add(
        CategoriesModel(
                    category_name = item.name
                    )
                )
    db.commit()
    return {"message": "Category added"}


@router.post("/new_tag",
             status_code=status.HTTP_201_CREATED,
             tags=[RouteTags.TAGS])
async def create_tag(item: schemas.StringItem, session: Session = Depends(get_db)):
    '''Endpoint for creating new tag'''
    return crud.create_new_tag(session, item)


@router.post("/new_maker",
             status_code=status.HTTP_201_CREATED,
             tags=[RouteTags.MAKERS])
async def create_maker(item: schemas.StringItem, db: Session = Depends(get_db)):
    ''''Endpoint to create new maker'''
    return crud.create_new_maker(db, item)


## GET Routes

@router.get('/get_products',
            response_model=List[schemas.ResponseGetProducts],
            tags=[RouteTags.PRODUCTS])
async def get_products(session: Session = Depends(get_db)):
    '''Endpoint to retrieve products from database'''
    result = session.query(ProductModel).all()
    return result


@router.get('/get_categories', tags=[RouteTags.CATEGORIES])
async def get_categories(session: Session = Depends(get_db)):
    '''Endpoint to retrieve categories from database'''
    return session.query(CategoriesModel).all()


@router.get('/get_tags', tags=[RouteTags.TAGS])
async def get_tags(session: Session = Depends(get_db)):
    '''Endpoint to retrieve tags from database'''
    return session.query(TagsModel).all()


@router.get('/get_makers', tags=[RouteTags.MAKERS])
async def get_makers(session: Session = Depends(get_db)):
    '''Endpoint to retrieve tags from database'''
    return session.query(MakerModel).all()

@router.patch('/drop_all')
async def drop_all():
    '''Only While Testing. Drop Everything'''
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

@router.put('/load_mock')
async def load_mock(session: Session = Depends(get_db)):
    '''Only While Testing. Drop Everything'''
    return crud.create_mock_data(session)