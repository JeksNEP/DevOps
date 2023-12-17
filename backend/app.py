from fastapi import FastAPI
from fastapi.responses import JSONResponse
from parser import get_info
from database.db import create_db


app = FastAPI()


@app.get("/")
async def read_root():
    create_db()
    get_info()
    return JSONResponse(content={"massage": "God help us all"})
