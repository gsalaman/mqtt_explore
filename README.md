# mqtt_explore
Random stuff for exploring MQTT and Mosquitto
## Useful sites:
https://appcodelabs.com/introduction-to-iot-build-an-mqtt-server-using-raspberry-pi. ---Has how to install on mac.  
http://www.steves-internet-guide.com/into-mqtt-python-client/ --- Python info.  My favorite reference point.


## Install on Pi
sudo apt update  
sudo apt install -y mosquitto mosquitto-clients

## Make mosquitto enable on boot:
sudo systemctl enable mosquitto.service

## Command line test:
Run Mosquitto in the background as a daemon:  
mosquitto -d

Subscribe to a topic in window #1:  
mosquitto_sub -d -t testTopic

Then, in window #2, send a message:  
mosquitto_pub -d -t testTopic -m "Hello World"

## Stop Mosquitto service
```
sudo service mosquitto stop
sudo systemctl stop mosquito.service
```
## Remove all persistent messages
- First, stop service as above.
- then, remove the mosquitto database:  
```
sudo rm /var/lib/mosquitto/mosquitto.db
```
- Then restart service with either:  
sudo systemctl start mosquitto.service  
or  
sudo service mosquitto start

## Websockets
If you need your mqtt server to enable websockets, you need to do so via a seperate config file.

First, stop the service (sudo service mosquitto stop).
Next, create a config file with the following lines:  (I called mine mqtt_glenn.conf)
```
port 1883
listener 9001
protocol websockets
```

Then, run the mosquitto broker with: mosquitto -c <config_file>
So, for me, it was:
```
mosquitto -c mqtt_glenn.conf
```

You should see a line saying "opening ipv4 listen socket on port 1883" as well as one saying "opening websocketes listen socket on port 9001"

# PYTHON!!!
## Install
sudo pip install paho-mqtt  
## Example scripts
simple_sub_pub.py - one script that acts both as a subscriber and publisher.  

### Dual scripts
To see this running with two scripts, open two windows.
In one, do:  
python simple_subscriber.py  

After that's running, in a seperate window, do:  
python simple_publisher.py  

### matrix example:
In one window, run:  
sudo python matrix_sub.py

In the other, you can run pub_red.py, pub_green.py, or pub_blue.py...don't need to be sudo
Very important:  the two different clients need different names.

## How to use
Start by including the paho-mqtt library:
```
import paho.mqtt.client as mqtt
```

You then need to make a client.  Pass in a unique ID as it's name...I'm using MyExampleClient below:
```
client = mqtt.Client("MyExampleClient")
```
Then you need to connect your client to the broker.  Broker can be either an IP address (like below) or a hostname.
```
broker_address="127.0.0.1"
client.connect(broker_address)
```
At this point, you can publish messages to a topic using the publish method:
```
client.publish("my_topic", "my_message")
```
If you want your client to be able to receive messages, you'll use the subscribe functionalitiy...but to do so, you need to create a message callback.  This function will be called whenever your client recieves a message...but remember that your client will only receive messages on topics it's subscribed to.  The callback looks like this:
```
# Callback for simple message
def on_message(client, userdata, message):
  print("message received: ", str(message.payload.decode("utf-8")))
  print("message topic=", message.topic)

```
It needs to have exactly those three parameters...use those params to do whatever processing you want on that message.  Usually, message.topic and message.payload will be enough, but if you are curious about the other parameters, go to Steve's page above.

Okay, so how do we link that callback to our client?  Before we connect our client to the broker, we need to tell it which callback function to use to processes subscribed messages...oh, and we need to actually subscribe to those messsages.  Which means our client creation code now looks like this:
```
client = mqtt.Client("ExampleClient")
broker_address="127.0.0.1"
client.on_message=on_message
client.connect(broker_address)
client.loop_start()
client.subscribe("testTopic")
```
Note the "loop_start()" call...this tells python to start listening for any subscribed messsages, and then we subscribe to the message topic (or topics) we are interested in.

And, at this point, whenever we get a subscribed message (anything on "testTopic" for the example above), we'll call the callback, which will print the message.
