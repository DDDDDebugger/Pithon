#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Buzzer Controlling module '

__author__ = 'Bruce Deng'

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

buzzerChannel = 4
volume = GPIO.PWM(buzzerChannel, 1000)

def buzzerOn(t=0.2):
    GPIO.output(4, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(4, GPIO.LOW)


def buzzerOnWith(v=10, t=0.5):
    volume.start(v)
    time.sleep(t)
    volume.stop()

# for test

if __name__ == '__main__':
    print('start test')
    print('------------test buzzerOn-------------')
    buzzerOn()
    print('------------test buzzerOnWith-------------')
    time.sleep(0.5)

    print('volume:10')
    time.sleep(0.5)
    buzzerOnWith(10, 0.2)

    print('volume:20')
    time.sleep(0.5)
    buzzerOnWith(20)

    print('volume:40')
    time.sleep(0.5)
    buzzerOnWith(40)

    print('volume:60')
    time.sleep(0.5)
    buzzerOnWith(60)

    print('volume:80')
    time.sleep(0.5)
    buzzerOnWith(80)
    
    GPIO.cleanup()
