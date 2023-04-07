from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv

import os
load_dotenv()
app = FastAPI()


class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    print("CWD is", os.getcwd())
    return {"message": f"Hello World. Welcome to FastAPI! - {os.getenv('MY_VAR')}"}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}


