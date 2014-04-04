'''
Author: Graham Montgomery
Western State Colorado University

This holds the sensor super class for every sensor that is written into the 
Engine. It also holds a list of every sensor that is dieclared for an individual 
project to be used by the Engine heartbeat.
'''

from PiFace import pi
from Motors import outpin
import serial
import string
import time as t
import picamera
import cv

#Global Sensor List
sensorList = []

#Sensor Class
#Super class for every sensor object, act as digital proxies to robot sensors
#IRSensor, SonarSensor, BeaconSensor
class Sensor:

    def __init__(self):
        sensorList.append(self)
        self.value = 0
    
    # update will be used by every sensor to update it's value every tick
    def update():
        pass

class Input(Sensor):

    def __init__(self, pin):
        Sensor.__init__(self)
        self.pin = pin + 1
        self.value = 0

    def update(self):
        self.value = pi.digital_read(self.pin)

class Camera(Sensor):

    def __init__(self):
        Sensor.__init__(self)
        self.camera = picamera.PiCamera()
        self.value = 0 
        self.nexttime = 0

    def update(self):
        time = self.nexttime - t.time()
        if time < 0:
            self.camera.capture("pic" + str(self.value) + ".jpg")
            self.value = (self.value + 1) % 5 
            self.nexttime = t.time() + 3 


class Sonar(Sensor):

    def __init__(self, inpin, outpin):
        Sensor.__init__(self)
        self.inpin = inpin
        self.outpin = outpin
        self.step = 0
    
    def update(self):
        '''print "updating sonar"'''
        piface.digital_write(self.trig, 1)
        time.sleep(0.00001)
        piface.digital_write(self.trig, 0)

        start = time.time()
        test = start

        while piface.digital_read(self.echo) == 1:
            start = time.time()
            if test + .01 > time.time():
                end = -1
                '''print "failure"'''
                self.distance = -1
                return
        
        end = start

        while piface.digital_read(self.echo) == 0:
            end = time.time()
            if end > start + .01:
                end = -1
                '''print "failure to get distance"'''
                self.distance = -1
                return
            time.sleep(.0001)

        timing = end - start
        self.value = (timing*340.29)

        piface.digital_write(self.trig, 0)

class Beacon(Sensor):

    def __init__(self):
        Sensor.__init__(self)
        self.updateTime = t.time()
        self.beac = 0
        self.comp = 0

    def update(self):
        ct = t.time()
        if ct > self.updateTime:
            test=serial.Serial("/dev/ttyAMA0",9600, timeout = 1)
            test.open()
            failed = False
            try:
                #print "attempting"
                line = test.readline()
                snums = line.split(",") # nums[0] beacon, nums[1] compass heading
                #inp = string.translate(line, rot13)
                try:
                    self.beac = int(str(snums[0]))
                    self.comp = int(str(snums[1]))
                except ValueError:
                    Failed = True
            except KeyboardInterrupt:
                pass
            if failed or self.beac >= 200:
                self.value = 200
            else:
                self.value = self.comp - self.beac - 90
            test.close()
            self.updateTime = ct + 3

def camera():
    return Camera()

def IR(pin):
    return Input(pin)

def button(pin):
    return Input(pin)
