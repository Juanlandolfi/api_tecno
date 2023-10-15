from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

USER_DB=os.getenv("USER_DB")
PASSWORD_DB=os.getenv("PASSWORD_DB")
HOST_DB=os.getenv("HOST_DB")
PORT_DB=os.getenv("PORT_DB")
DATABASE_NAME=os.getenv("DATABASE_NAME")


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{DATABASE_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

