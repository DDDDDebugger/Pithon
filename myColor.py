#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' myColor module '

__author__ = 'Bruce Deng'

from enum import Enum

class myColor(Enum):

    BLACK = (0, 0, 0)
    RED = (128, 0, 0)
    BRIGHTRED = (255, 0, 0)
    GREEN = (0, 128, 0)
    BLUE = (0, 0, 128)
    YELLOW = (128, 128, 0)
    MAGENTA = (128, 0, 128)
    CYAN = (0, 128, 128)
    WHITE = (192, 192, 192)
    
    
    def __init__(self, r, g, b) -> None:
        super().__init__()
        self.__red, self.__green, self.__blue = 0, 0, 0
        if r>=0 and r<=255 and g>=0 and g<=255 and b>=0 and b<=255:
            self.__red, self.__green, self.__blue = r, g, b
    
    def getValue(self):
        return (self.__red<<16)|(self.__green<<8)|self.__blue

    def getRed(self):
        return self.__red

    def getGreen(self):
        return self.__green
        
    def getBlue(self):
        return self.__blue

    
    

def test():
    print('Test function!\n')
    color1 = myColor.RED
    color2 = myColor.BLUE
    print("red: ", color1, "\nblue: ", color2)
    print('r = {}, g = {}, b = {}'.format(color1.getRed(), color1.getGreen(), color1.getBlue()))

if __name__=='__main__':
    test()