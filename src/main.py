"""Entry point of TECNOPOWER API"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.app_router import router



app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:4200",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    '''First endpoint test'''
    return {'message': 'It seems to work'}


app.include_router(router)