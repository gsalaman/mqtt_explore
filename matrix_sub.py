import paho.mqtt.client as mqtt
import time

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# this is the size of ONE of our matrixes. 
matrix_rows = 64 
matrix_columns = 64 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 1 
matrix_vertical = 1

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 

#options.hardware_mapping = 'adafruit-hat-pwm' 
#options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.hardware_mapping = 'regular'  

options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

screen = Image.new("RGB", (total_columns, total_rows))
draw = ImageDraw.Draw(screen)

def set_color(message):
  global draw
  global total_columns
  global total_rows

  if (message == "red"):
    print "Setting red"
    color = (255,0,0)
  elif (message == "green"):
    print "Setting green"
    color = (0,255,0)
  elif (message == "blue"):
    print "Setting blue"
    color = (0,0,255)
  else:
    print "unknown color received"
    print message
    color = (0,0,0)

  draw.rectangle((0,0,total_columns-1,total_rows-1), fill = color)
  matrix.SetImage(screen,0,0)

# Callback for message
def on_message(client, userdata, message):
  set_color(message.payload)   

broker_address="10.0.0.17"
client = mqtt.Client("matrix")
client.on_message=on_message
client.connect(broker_address)
client.subscribe("matrix")
client.loop_start()

while True:
  print "Tick!"

  time.sleep(1)

