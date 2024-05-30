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

logger = get_logger("subscriber")

broker = "broker.emqx.io"

user_id = requests.get('http://127.0.0.1:8002/auth').json()
logger.info("subs_uid %s", user_id)

def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    logger.info("received message = %s", data)

client = mqtt_client.Client(
    mqtt_client.CallbackAPIVersion.VERSION1, 
    user_id
)
client.on_message = on_message

print("Connecting to broker",broker)
client.connect(broker) 
client.loop_start() 
print("Subcribing")
client.subscribe("lab/leds/state")
time.sleep(1800)
client.disconnect()
client.loop_stop()
