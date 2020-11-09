import paho.mqtt.client as mqtt
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16) 

# Process servo message
def process_servo_msg(kit, topic,payload):

  print("start of process_servo")

  servo_number = int(topic[6])
  angle = int(payload)

  print("servo: ", str(servo_number))
  print("angle: ", str(angle))

  kit.servo[servo_number].angle  = angle



# Callback for message
def on_message(client, userdata, message):
  global kit

  print("message received: ", str(message.payload.decode("utf-8")))
  print("message topic=", message.topic)
  print("message qos=", message.qos)
  print("message retain flag=", message.retain)

  if (message.topic[:5] == "servo"):
    print("got servo message!!!")
    process_servo_msg(kit, message.topic, message.payload)

broker_address="mqttbroker"
client = mqtt.Client("Simple_subscribe")
client.on_message=on_message
client.connect(broker_address)
client.subscribe("testTopic")
client.subscribe("servo/#")
client.loop_start()

kit = ServoKit(channels=16) 

while True:
  print("Tick!")

  time.sleep(1)

