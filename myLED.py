#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' LED Controlling module '

__author__ = 'Bruce Deng'

from neopixel import *
from myColor import myColor
import time, threading

# LED strip configuration:
LED_COUNT = 16 # Number of LED pixels
LED_PIN = 18 # GPIO pin connected to the pixels (18 uses PWM)
LED_FREQ_HZ = 800000 # LED signal frequency in Hertz (usually 800kHz)
LED_DMA = 10 # DMA channel to use for generating signal
LED_BRIGHTNESS = 100 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False # NPN transistor needs invert
LED_CHANNEL = 0 # set to '1' for PWM 1
LED_STRIP = ws.WS2812_STRIP

# create NeoPixel object
strip = Adafruit_NeoPixel(
        LED_COUNT ,
        LED_PIN ,
        LED_FREQ_HZ ,
        LED_DMA ,
        LED_INVERT ,
        LED_BRIGHTNESS ,
        LED_CHANNEL
        )
# Intialize the library (must be called once before other functions).
strip.begin()


def setSingleColor(no = 0, color = myColor.BLACK):
    #check input
    def inputCheck(no): 
        if no < 0 or no > 3:
            return False
        else:
            return True    
    
    if inputCheck(no):
        #color = (red << 16)|(green << 8)|blue
        strip.setPixelColor(no, color.getValue())
        # Flash data
        strip.show()

def setColor(color=myColor.BLACK):
    setSingleColor(0, color)
    setSingleColor(1, color)
    setSingleColor(2, color)
    setSingleColor(3, color)

def cleanColor():
    setColor(myColor.BLACK)

def test():
    print('thread %s is running...' % threading.current_thread().name)
    colorList = [myColor.RED, myColor.BLUE, myColor.GREEN, myColor.YELLOW, myColor.MAGENTA, myColor.CYAN, myColor.WHITE]

    times = 50
    i = 0
    while times > 0:
        setSingleColor(0, colorList[i%7])
        setSingleColor(1, colorList[(i+1)%7])
        setSingleColor(2, colorList[(i+2)%7])
        setSingleColor(3, colorList[(i+3)%7])
        time.sleep(0.2)
        i += 1
        times -= 1

    cleanColor()

if __name__ == '__main__':
    print('start LED test')
    test()
