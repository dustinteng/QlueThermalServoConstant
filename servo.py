# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:35:06 2020

@author: Dustin Tengdyantono

for servo using bus 0 (pins 28 and 27 for scl and sda)
"""
import time
from adafruit_servokit import ServoKit
import busio
import board

class shervo:
    
    def __init__(self):
        self.dpixels= 0
        self.angle= 90
        self.angle0= 90
        self.angle0p= 90
        self.i2c_bus0=(busio.I2C(board.SCL_1, board.SDA_1))
        self.kit= ServoKit(channels=16, reference_clock_speed=25000000, i2c=self.i2c_bus0)
        self.kit.servo[15].angle = self.angle
        self.kit.servo[14].angle = self.angle
        self.ts= 0.005 #time sleep yang diperuntukkan untuk forloop kecepatan daripada servo itu sendiri
        self.norm = 10
    def converter(self,pix_in):
        self.dpixels= int(pix_in)*-1
        if -1.5<self.dpixels<1.5:

            time.sleep(0.01)
            self.angle0p =  self.angle0p - (self.dpixels)
            print("currently it's at "+ str(self.angle0p)+"degree, nothing changed")
            pass
        else:
            time.sleep(1)
            self.angle = self.dpixels + self.angle
            self.angle0p =  self.angle0p - (self.dpixels)
            deltaangle = self.angle-self.angle0
            if deltaangle >=-3 and deltaangle <=3:
                if self.angle0 < self.angle:
                    for t in range (self.angle0*self.norm,self.angle*self.norm,1):
                        self.kit.servo[15].angle = t/self.norm
                        self.kit.servo[14].angle = t/self.norm
                        time.sleep (self.ts)
                elif self.angle0 > self.angle:
                    for t in range (self.angle0*self.norm,self.angle*self.norm,-1):
                        self.kit.servo[15].angle = t/self.norm
                        self.kit.servo[14].angle = t/self.norm
                        time.sleep (self.ts)
                self.angle0 = self.angle

            else:
                if self.angle0 < self.angle:
                    for t in range (self.angle0*self.norm,self.angle*self.norm,1):
                        self.kit.servo[15].angle = t/self.norm
                        self.kit.servo[14].angle = t/self.norm
                        time.sleep (self.ts)
                elif self.angle0 > self.angle:
                    for t in range (self.angle0*self.norm,self.angle*self.norm,-1):
                        self.kit.servo[15].angle = t/self.norm
                        self.kit.servo[14].angle = t/self.norm
                        time.sleep (self.ts)
                self.angle0 = self.angle

            print("currently it's at "+ str(self.angle0p)+" degree")
            return self.angle0p

    def reset_(self):
        self.kit.servo[15].angle = 90
        self.kit.servo[14].angle = 90
        print('reset')
            
    def return_to_ninety(self,angle0):
        if self.angle0 >= 89.5 and self.angle0<=90.5:
            print('let it pass')
            time.sleep(0.5)
            pass

        elif self.angle0 < 89.5:  
        #self.angle = self.angle0 + self.angle
        
            for t in range (self.angle0*self.norm,90*self.norm,1):
                self.kit.servo[15].angle = t/self.norm
                self.kit.servo[14].angle = t/self.norm
                time.sleep (self.ts)
            print('return to 90 naik from the angle '+ str(self.angle0))
            self.angle0= 90
            return(self.angle0)
        elif self.angle0 > 90.5:
            for t in range (self.angle0*self.norm,90*self.norm,-1):
                self.kit.servo[15].angle = t/self.norm
                self.kit.servo[14].angle = t/self.norm
                time.sleep (self.ts)
            print('return to 90 turun from the angle '+ str(self.angle0))
            self.angle0 = 90
            return(self.angle0)

    #def n_provider (self, angle0,angle,n):
       # self.niteration = abs(self.angle0-self.angle)*self.norm
