'''This code works for detecting rising edge
of the signal transmitted by the timer.
    
BUGS:
    - two outputs within one second
    *RESOLVED by adding a pull-down in the GPIO setup* '''

import RPi.GPIO as GPIO
from datetime import datetime
from picamera import PiCamera
from time import sleep

channel = 4

camera = PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.add_event_detect(channel, GPIO.RISING)

while True:
    if GPIO.event_detected(channel):
        print(f'Rising edge @{datetime.now()}')