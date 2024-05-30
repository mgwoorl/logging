import datetime
from fastapi import FastAPI
import hashlib
import logging
import sys
import time
from logging.handlers import TimedRotatingFileHandler
import uvicorn

app = FastAPI()

@app.get("/auth")
async def gen_id():
    user_id = hashlib.md5(str(datetime.datetime.now()).encode('utf-8')).hexdigest()
    return user_id

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
