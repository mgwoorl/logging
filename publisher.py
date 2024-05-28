import time
import paho.mqtt.client as mqtt_client
import random
import logging
import sys
import time
from logging.handlers import TimedRotatingFileHandler

broker="broker.emqx.io"

#client = mqtt_client.Client('isu10012300')
# FOR new version change ABOVE line to 
client = mqtt_client.Client(
    mqtt_client.CallbackAPIVersion.VERSION1, 
    'isu1001234645678987654312'
)

print("Connecting to broker",broker)
print(client.connect(broker))
client.loop_start() 
print("Publishing")

for i in range(10):
    state = "on" if random.randint(0, 1) == 0 else "off"
    state = state + " 🍄"
    print(f"state is {state}")
    client.publish("lab/leds/state", state)
    time.sleep(2)
    
client.disconnect()
client.loop_stop()
