#! /usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12,GPIO.OUT)



while True:

# SET HIGH PIN

    GPIO.output(21,1)

    sleep(0.5)

# SET LOW

    GPIO.output(21,0)

    sleep(0.5)