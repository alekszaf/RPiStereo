from picamera import PiCamera
import RPi.GPIO as GPIO
from gpiozero import Button
from time import sleep
from datetime import datetime
from signal import pause

camera = PiCamera()

button = Button(17)
channel = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.add_event_detect(channel, GPIO.RISING)

timelapse_on = False

def captureTimelapse():
    global timelapse_on
    
    if timelapse_on:
        pass
    else:
        if GPIO.event_detected(channel):
            tstamp = datetime.now()
            print(f'Rising edge @{datetime.now()}')
            camera.capture('/home/pi/Timelapse/orange_test_%s.png' %tstamp)
    timelapse_on = not timelapse_on
    
# def capture():
#     tstamp = datetime.now()
#     camera.capture('/home/pi/Timelapse/%s.jpg' %tstamp)
    
try:
    button.when_pressed = captureTimelapse
    pause()

finally:
    pass