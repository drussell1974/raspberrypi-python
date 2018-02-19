#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

def go():
    for i in range(4):
        GPIO.output(23, 1)
        time.sleep(5)
        GPIO.output(24, 1)
        time.sleep(0.5)
        GPIO.output(23, 0)
        GPIO.output(24, 0)
        GPIO.output(25, 1)
        time.sleep(5)
        GPIO.output(25, 0)
        GPIO.output(24, 1)
        time.sleep(0.5)
        GPIO.output(24, 0)
    GPIO.cleanup()

go()
	
