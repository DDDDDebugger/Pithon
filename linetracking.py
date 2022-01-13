#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Auto Line-tracking '

__author__ = 'Bruce Deng'

from time import sleep
import irsensor
import myWheelControl as WC

def autoTracking():
    while True:
        irValues = irsensor.AnalogRead()
        print('IR values: ' + str(irValues))
        #sleep(3)
        if canGo(irValues):
            print('go straight...')
            WC.Forward(v = 20, t = 0.05)
        else:
            if irValues[4] <= 300:
                print('turn right...')
                WC.Turn(v=10, t=0.1)
            elif irValues[0] <= 300:
                print('turn left...')
                WC.Turn(False, v=10,t=0.1)


        
def canGo(value):
    if value[0] < 300 or value[4] < 300:
        return False
    else:
        return True


if __name__ == '__main__':
    print('start autoTracking...')
    try:
        autoTracking()
    except KeyboardInterrupt as KBI:
        print('Ctrl+C: ', KBI)
        WC.GPIO.cleanup()
    
