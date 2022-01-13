import RPi.GPIO as GPIO
import time, threading

leftChannelList = [13,12]
leftCONTROL = 6
rightChannelList = [21,20]
rightCONTROL = 26
GPIO.setmode(GPIO.BCM)

GPIO.setup((leftCONTROL, rightCONTROL), GPIO.OUT)
GPIO.setup(leftChannelList, GPIO.OUT)
GPIO.setup(rightChannelList, GPIO.OUT)

leftSpeed = GPIO.PWM(leftCONTROL, 1000)
rightSpeed = GPIO.PWM(rightCONTROL, 1000)
# forward, 50% maxspeed
def Forward(t = 0.5, v = 50):
    #print('thread %s is running...' % threading.current_thread().name)
    GPIO.output(leftChannelList, (1, 0))
    GPIO.output(rightChannelList, (1, 0))
    leftSpeed.start(v)
    rightSpeed.start(v)
    time.sleep(t)
    leftSpeed.stop()
    rightSpeed.stop()
# backward, 30% maxspeed
def Backward(t = 0.5, v = 30):
    #print('thread %s is running...' % threading.current_thread().name)
    GPIO.output(leftChannelList, (0, 1))
    GPIO.output(rightChannelList, (0, 1))
    leftSpeed.start(v)
    rightSpeed.start(v)
    time.sleep(t)
    leftSpeed.stop()
    rightSpeed.stop()

def Turn(isRight = True, t = 0.5, v = 10):
    #print('thread %s is running...' % threading.current_thread().name)
    if isRight == False:
        GPIO.output(rightChannelList, (1,0))
        GPIO.output(leftChannelList, (0,1))
    else:
        GPIO.output(rightChannelList, (0,1))
        GPIO.output(leftChannelList, (1,0))
    leftSpeed.start(v)
    rightSpeed.start(v)
    time.sleep(t)
    leftSpeed.stop()
    rightSpeed.stop()

def test():
    print('start wheel testing...')
    print('forward')
    Forward()
    time.sleep(1)
   
    print('backward')
    Backward()
    time.sleep(1)
    
    print('turn right')
    Turn()
    time.sleep(1)

    print('turn left')
    Turn(False)
    GPIO.cleanup()

if __name__ == '__main__':
    test()
