'''This code is used for testing of the timer trigger mechanism.
It works for detecting rising edge of the signal transmitted by the timer.
The signal is then triggering the camera capture (with 5 second delay - BUG).
    
BUGS:
    - two outputs within one second
    *RESOLVED by adding a pull-down in the GPIO setup*
    
    - adding camera capture takes additional 5 seconds
    *UNRESOLVED
    
    - some images contain no data
    *UNRESOLVED - possibly due to the script interrupt during capture'''

# Load the libraries
import RPi.GPIO as GPIO
from datetime import datetime
from picamera import PiCamera
from time import sleep

# Number of the GPIO receiving signal from the timer
channel = 5

# Initialize the camera
camera = PiCamera()

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the timer GPIO as input with a pull-down (IMPORTANT - prevents bouncing signal!)
GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Look for rising signal
GPIO.add_event_detect(channel, GPIO.RISING)

# MAIN LOOP - capture an image every time rising edge is detected
while True:
    if GPIO.event_detected(channel):
        tstamp = str(datetime.now())
        camera.capture('/home/pi/Timelapse/orange_test_%s.png' %tstamp)
        print(f'Rising edge @{datetime.now()}')