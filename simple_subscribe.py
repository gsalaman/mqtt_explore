import paho.mqtt.client as mqtt
import time

# Callback for message
def on_message(client, userdata, message):
  print("message received: ", str(message.payload.decode("utf-8")))
  print("message topic=", message.topic)
  print("message qos=", message.qos)
  print("message retain flag=", message.retain)

broker_address="10.0.0.17"
client = mqtt.Client("Simple_subscribe")
client.on_message=on_message
client.connect(broker_address)
client.subscribe("testTopic")
client.loop_start()

while True:
  print "Tick!"

  time.sleep(1)

