import json
from typing import List
# from fastapi import Depends#, Query
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import models
from src.schemas import schemas
from fastapi import HTTPException
from fastapi import status
# from pymysql.err import IntegrityError


# GET
def get_category_by_id(db: Session, category_ids: int) -> List[models.CategoriesModel]:
    '''Return List Of Category ORM objects that match given ids'''
    categories = db.scalars(select(models.CategoriesModel)
                            .filter(models.CategoriesModel.id == category_ids)
                            ).all()
    return categories


def get_tags_by_ids(db: Session, tags_ids: List[int]) -> List[models.TagsModel]:
    '''Return List Of Tags ORM objects that match given ids'''
    tags = db.scalars(select(models.TagsModel).filter(models.TagsModel.id.in_(tags_ids))).all()
    return tags

# CREATE

def create_new_product( db: Session, product: schemas.Product):
    '''Create New Product ORM object and commit to database'''
    dict_new_prod = product.model_dump(exclude_unset=True)
    # Get tags ids and remove form dict. Then get list of ORM Tags
    tag_ids = dict_new_prod.pop('tag', [])
    tags = get_tags_by_ids(db, tags_ids=tag_ids)
    #Create new product
    new_product = models.ProductModel(**dict_new_prod, tag=tags)
    # Add to session and commit
    db.add(new_product)
    db.commit()


def create_new_maker(db: Session, item: schemas.StringItem):
    '''Create New Maker ORM object and commit to database'''

    result = db.scalar(
        select(models.MakerModel)
        .where(models.MakerModel.maker_name ==  item.name))
    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Maker already exists')
    else: 
        db.add(
                models.MakerModel(
                        maker_name = item.name
                        )
                    )
        db.commit()
        return {"message": "Category added"}
    


def create_new_tag(db: Session, item: schemas.StringItem):
    '''Create New Tag ORM object and commit to database'''
    result = db.scalar(
        select(models.TagsModel)
        .where(models.TagsModel.tag_name ==  item.name))
    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Tag already exists')
    else:
        db.add(
            models.TagsModel(
                tag_name = item.name
            )
        )
        db.commit()
        return {"message": "Tag added"}


# DELETE

def delete_category(db: Session, category_id: int):
    category = db.get(models.CategoriesModel, category_id)
    if category:
        db.delete(category)
        db.commit()
        return {'message': 'Category Deleted'}
    else: 
        return {'message': 'Could not find category ID'}



# UPDATE

def update_product(db: Session, product_id: int, product_update: schemas.Product):
    product = db.get(models.ProductModel, product_id)
    product_dict = product_update.model_dump(exclude_unset=True)
    print(product)
    print(product_dict)
    if not product:
        return {'message': 'Could not find product with given id'}
    else:
        tag_ids = product_dict.pop('tag', [])
        tags = get_tags_by_ids(db, tags_ids=tag_ids)
        for key,value in product_dict.items():
            print(key,value)
            setattr(product, key, value)
        setattr(product, 'tag', tags)
        db.add(product)
        db.commit()
        return {'message': 'Product updated'}
    




### For testing  Creating mock data
def create_mock_data(db: Session):
    with open('src/routes/products_mock.json') as file:
        data = json.load(file)
    
    categorias = [models.CategoriesModel(category_name='Auriculares'),
                  models.CategoriesModel(category_name='Celulares')]
    
    makers= [models.MakerModel(maker_name='Samsung'),
             models.MakerModel(maker_name='Apple'),
             models.MakerModel(maker_name='Xiaomi'),
             models.MakerModel(maker_name='Hidrogel'),
             models.MakerModel(maker_name='Pop it'),
             models.MakerModel(maker_name='Lenovo'),]

    for product in data:
        db.add(
            models.ProductModel(product_name=product['product_name'],
                     img_url=product['img'],
                     price=product['price'],
                     stock=product['stock'],
                     description=product['description'],
                     category=categorias[int(product['category_id'])-1],
                     maker=makers[int(product['maker'])-1]
                     )
                 )
    db.commit()
    return {'message': 'Mocked data added'}

