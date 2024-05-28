import datetime
from fastapi import FastAPI
import hashlib
import logging
import sys
import time
from logging.handlers import TimedRotatingFileHandler

app = FastAPI()
def generate_hash_for_user_id():
    dt = str(datetime.datetime.now())
    hs = hashlib.md5(dt.encode('utf-8'))
    return hs

@app.get("/auth")
async def gen_id():
    user_id = generate_hash_for_user_id()
    return {"user_id": user_id}
