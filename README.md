# mqtt_explore
Random stuff for exploring MQTT and Mosquitto
## Useful sites:
https://appcodelabs.com/introduction-to-iot-build-an-mqtt-server-using-raspberry-pi. --- Better...has how to install on mac.  
http://www.steves-internet-guide.com/into-mqtt-python-client/ --- Python info.  


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

