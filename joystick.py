#!/usr/bin/python3
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO

import time

CENTER , FRONT , RIGHT , LEFT, BACK = 7, 8, 9, 10, 11
pingroup = (LEFT, RIGHT , CENTER , FRONT , BACK)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pingroup , GPIO.IN, GPIO.PUD_UP)

message = {CENTER: 'center', LEFT: 'left', RIGHT: 'right',
FRONT: 'front', BACK: 'back'}

def pin_catched(channel):
    print (message[channel])

for pin in pingroup:
    GPIO.add_event_detect(pin, GPIO.FALLING , callback=pin_catched)

while True:
    time.sleep(5)
