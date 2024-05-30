import datetime
from fastapi import FastAPI
import hashlib
import logging
import sys
import time
from logging.handlers import TimedRotatingFileHandler
import uvicorn

FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
LOG_FILE = "app.log"

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)

    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    logger.addHandler(file_handler)

    return logger

app = FastAPI()
logger = get_logger("my_logger")

@app.get("/auth")
async def gen_id():
    user_id = hashlib.md5(str(datetime.datetime.now()).encode('utf-8')).hexdigest()
    logger.info(f"Generated user_id: {user_id}")
    return user_id

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
