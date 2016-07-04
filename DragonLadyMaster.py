"""
Dragon Lady master code. Dragon lady is a ndvi camera consisting of a master and slave raspberry pi. Each raspberry pi has its own camera. The master is connected to the PiNOIR camera while the slave is connected to the RGB camera.

Hardie Pienaar
June 2016
"""

# Import dependencies
import picamera
import time

# Setup GPIO pins
#TODO

# Set status to busy (Red)
#TODO

# Create camera object
camera = picamera.PiCamera()
camera.resolution = (2592, 1944)

# Read camera settings
#TODO

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
#TODO

# Wait for camera trigger 
#TODO

# Set state to shutter (Blue)
#TODO

# Send trigger to slave 
#TODO

# Take photo 
camera.capture("foo.jpg")

# Wait for trigger
#TODO
