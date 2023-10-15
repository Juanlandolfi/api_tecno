"""Entry point of TECNOPOWER API"""

from fastapi import FastAPI

from .routes.app_router import router


app = FastAPI()

@app.get("/")
async def list_products():
    '''First endpoint test'''
    return {'message': 'It seems to work'}


app.include_router(router)