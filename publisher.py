import time
import paho.mqtt.client as mqtt_client
import random
import logging
import sys
import time
from logging.handlers import TimedRotatingFileHandler
import requests

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

logger = get_logger("publisher")

broker="broker.emqx.io"

user_id = requests.get('http://127.0.0.1:8002/auth').json()
logger.info("subs_uid: %s", user_id)

client = mqtt_client.Client(
    mqtt_client.CallbackAPIVersion.VERSION1, 
    user_id
)

logger.info("Connecting to broker %s", broker)
logger.info(client.connect(broker))
client.loop_start() 
logger.info("Publishing")

for i in range(10):
    state = "on" if random.randint(0, 1) == 0 else "off"
    state = state + " привет"
    logger.info(f"state is {state}")
    client.publish("lab/leds/state", state)
    time.sleep(2)
    
client.disconnect()
client.loop_stop()
