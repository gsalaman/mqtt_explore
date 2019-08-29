import paho.mqtt.client as mqtt
import time

# Callback for simple message
def on_message(client, userdata, message):
  print("message received: ", str(message.payload.decode("utf-8")))
  print("message topic=", message.topic)
  print("message qos=", message.qos)
  print("message retain flag=", message.retain)

broker_address="10.0.0.17"
client = mqtt.Client("P1")
client.on_message=on_message
client.connect(broker_address)
client.loop_start()
client.subscribe("testTopic")
client.publish("testTopic", "Hello")
time.sleep(4)
client.loop_stop()
