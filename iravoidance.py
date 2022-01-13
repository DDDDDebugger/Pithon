#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Auto Obstacle-Avoidance module '

__author__ = 'Bruce Deng'

import sys
from myColor import myColor
import myWheelControl as WC
import RPi.GPIO as GPIO
import myLED
import myBuzzer
from time import sleep
import threading

GPIO.setmode(GPIO.BCM)
IR_frontR = 19
IR_frontL = 16
GPIO.setup((IR_frontL, IR_frontR), GPIO.IN)


def LEDflash(color, t = 0.2):
    myLED.setColor(color)
    sleep(t)
    myLED.cleanColor()

def autoObstacleAvoiding():
    warning = False
    CL = False
    if len(sys.argv) >= 2:
        if 'warning' in sys.argv or '-W' in sys.argv:
            warning = True
        if 'CL' in sys.argv or '-CL' in sys.argv:
            CL = True


    try:
        Left, Right = 0, 0
        thrd1 = None #thread of buzzer
        thrd2 = None #thread of LED
        while True:
            Left = GPIO.input(IR_frontL)
            Right = GPIO.input(IR_frontR)

            if Left == 1 and Right == 1:
                #Go straight
                if CL:
                    myLED.setColor(myColor.GREEN)
                    myLED.cleanColor()
               
                WC.Forward(t=0.1, v=10)
                
            elif Left == 1 and Right == 0:
                #Turn left
                if thrd2 != None and thrd2.is_alive():
                    print('{} is still alive!'.format(thrd2.getName()))
                elif warning:
                    thrd2 = threading.Thread(target=LEDflash, kwargs={'color':myColor.BLUE}, name='LEDThread', daemon=False)
                    thrd2.start()
                    
                WC.Turn(False)
               
            elif Left == 0 and Right == 1:
                #Turn right
                if thrd2 != None and thrd2.is_alive():
                    print('{} is still alive!'.format(thrd2.getName()))
                elif warning:
                    thrd2 = threading.Thread(target=LEDflash, kwargs={'color':myColor.YELLOW}, name='LEDThread', daemon=False)
                    thrd2.start()
                
                WC.Turn()

            else:
                #Turn back
                if thrd1 != None and thrd1.is_alive():
                    print('{} is still alive!'.format(thrd1.getName()))
                else:
                    thrd1 = threading.Thread(target = myBuzzer.buzzerOnWith, kwargs={'t':0.2}, name = 'Buzzerthread', daemon = False)
                    thrd1.start()

                if thrd2 != None and thrd2.is_alive():
                    print('{} is still alive!'.format(thrd2.getName()))
                elif warning:
                    thrd2 = threading.Thread(target=LEDflash, kwargs={'color':myColor.BRIGHTRED}, name='LEDThread', daemon=False)
                    thrd2.start()

                WC.Turn(True, 0.2, 30)
                
    except KeyboardInterrupt as e:
        print("CTRL + 'C':")
        print(e)
        myLED.cleanColor()
        GPIO.cleanup()

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-test':
        print('start test...')  
        try:
            Left, Right = 0, 0
            while True:
                Left = GPIO.input(IR_frontL)
                Right = GPIO.input(IR_frontR)
                print('LIR: {}, RIR: {}'.format(Left, Right))
                if Left == 1 and Right == 1:
                    print('go straight')
                    WC.Forward(t=0.1, v=10)
                elif Left == 1 and Right == 0:
                    #Turn left
                    print('turn left')
                    WC.Turn(False)
                elif Left == 0 and Right == 1:
                    print('turn right')
                    WC.Turn()
                else:
                    print('turn back')
                    WC.Turn(True, 0.2, 30)
                    #turn back
                sleep(0.5)
        except KeyboardInterrupt as e:
            print("CTRL + 'C':")
            print(e)
            GPIO.cleanup()
    else:
        print('start auto obstacle-avoiding...')
        autoObstacleAvoiding()

