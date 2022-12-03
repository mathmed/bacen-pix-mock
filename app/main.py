from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

from app.presentation.routes import *
