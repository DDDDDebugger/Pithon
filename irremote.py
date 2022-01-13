#!/usr/bin/python3
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

IR = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR, GPIO.IN, GPIO.PUD_UP)

keymap = {
0x45: 'CH-', 0x46: 'CH ', 0x47: 'CH+',
0x44: '<<<', 0x40: '>>>', 0x43: '>>|',
0x07: ' - ', 0x15: ' + ', 0x09: 'EQ ',
0x16: ' 0 ', 0x19: '100+', 0x0D: '200+',
0x0C: ' 1 ', 0x18: ' 2 ', 0x5E: ' 3 ',
0x08: ' 4 ', 0x1C: ' 5 ', 0x5A: ' 6 ',
0x42: ' 7 ', 0x52: ' 8 ', 0x4A: ' 9 '}

def getkey():
    if GPIO.input(IR) == GPIO.HIGH:
        return
    channel = GPIO.wait_for_edge(IR, GPIO.RISING , timeout=8)
    GPIO.remove_event_detect(IR)
    if channel is not None: # less than 9ms, maybe noise
        return

    time.sleep(0.0045) # wait 4.5ms

    data = 0
    for shift in range(0, 32):
        # 0.56ms low level
        while GPIO.input(IR) == GPIO.LOW:
            time.sleep(0.0001)

        count = 0
        while GPIO.input(IR) == GPIO.HIGH and count < 10:
            count += 1
            time.sleep(0.0005)

        # "0": 0.56ms, "1": 1.69ms
        if (count > 1):
            data |= 1<<shift

    a1 = (data >> 24) & 0xff
    a2 = (data >> 16) & 0xff
    a3 = (data >> 8) & 0xff
    a4 = (data) & 0xff
    if ((a1+a2) == 0xff) and ((a3+a4) == 0xff):
        return a2
    else: print("repeat key")

print('IRremote Test Start ...')
while True:
    key = getkey()
    if(key != None):
        print('key = ', keymap[key])
