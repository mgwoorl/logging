import time
import paho.mqtt.client as mqtt_client
import random
import logging
import sys
import time
from logging.handlers import TimedRotatingFileHandler

broker = "broker.emqx.io"
def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    print("received message =", data)

#client = mqtt_client.Client('isu10012347')
# FOR new version change ABOVE line to 
client = mqtt_client.Client(
    mqtt_client.CallbackAPIVersion.VERSION1, 
    'isu1004563463412347'
)
client.on_message=on_message

print("Connecting to broker",broker)
client.connect(broker) 
client.loop_start() 
print("Subcribing")
client.subscribe("lab/leds/state")
time.sleep(1800)
client.disconnect()
client.loop_stop()
