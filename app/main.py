from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(
    title='Pix Mock - BACEN'
)

from app.presentation.routes import *
