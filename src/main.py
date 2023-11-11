"""Entry point of TECNOPOWER API"""

from fastapi import FastAPI

from src.routes.app_router import router


app = FastAPI()

@app.get("/")
async def home():
    '''First endpoint test'''
    return {'message': 'It seems to work'}


app.include_router(router)