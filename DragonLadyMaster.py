"""
Dragon Lady master code. Dragon lady is a ndvi camera consisting of a master and slave raspberry pi. Each raspberry pi has its own camera. The master is connected to the PiNOIR camera while the slave is connected to the RGB camera.

Hardie Pienaar
June 2016
"""

# Import dependencies
import picamera
import time
import RPi.GPIO as GPIO

# Setup GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

# General Definitions
RED = 27
GREEN = 10 
BLUE = 22 

# Status led functions
def ledOn(led):
    GPIO.output(led, False)

def ledOff(led):
    GPIO.output(led, True)

def setStatus(status):
    if status == "busy":
        ledOn(RED) 
        ledOff(GREEN) 
        ledOff(BLUE) 
    elif status == "idle":
        ledOn(GREEN)
        ledOff(RED) 
        ledOff(BLUE) 
    elif status == "shutter":
        ledOn(BLUE)
        ledOff(RED) 
        ledOff(GREEN) 

# Set status to busy (Red)
setStatus("busy")

# Create camera object
camera = picamera.PiCamera()
camera.resolution = (2592, 1944)

# Read camera settings
#TODO
time.sleep(1)

# Set camera settings
#TODO
# camera.shutter_speed
# camera.iso
# camera.analog_gain
# camera.digital_gain
# camera.exposure_mode = 'off'
# camera.awb_mode = 'off'
# camera.awb_gains red,blue

# Wait for slave ready
#TODO

# Set state to idle (Green)
setStatus("idle")

# Wait for camera trigger 
#TODO
time.sleep(1)

# Set state to shutter (Blue)
setStatus("shutter")


# Send trigger to slave 
#TODO

# Take photo 
#TODO
time.sleep(1)
#camera.capture("foo.jpg")

# Wait for trigger
setStatus("idle")
#TODO
