#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time
from time import sleep


GPIO.setmode(GPIO.BMC) 
GPIO.setup(17,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(22,GPIO.OUT,initial=GPIO.LOW)
#GPIO.setup(26,GPIO.OUT,initial=GPIO.LOW)
GPIO.cleanup()


time = time.time()

while (time-(time.time()< 5)):

# SET HIGH PIN

    GPIO.output(17,1)
    GPIO.output(22,1)
    GPIO.output(27,1)

    sleep(0.1)

    GPIO.output(17,0)
    GPIO.output(22,0)
    GPIO.output(27,0)
