# mqtt_explore
Random stuff for exploring MQTT and Mosquitto
## Useful sites:
https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/. --- Note, may have malware!!!


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
