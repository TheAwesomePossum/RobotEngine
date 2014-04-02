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

class SonarUpdater(Sensor):

    _sensors = []

    def __init__(self):
        Sensor.__init__(self)
        SonarUpdater._sensors.append(sensor)

    def add(sensor):
        SonarUpdater._sensors.append(sensor)

    def update(self):
        pass

class Sonar(Sensor):
    
    _updater = SonarUpdater

    def __init__(self, inpin, outpin):
        Sensor.__init__(self)
        sensorList.remove(self)
        self.inpin = inpin
        self.outpin = outpin
        self.v = 100
        self.step = 0
    
    def update(self):
        pass

class Beacon(Sensor):

    def __init__(self)
        Sensor.__init__(self)
        self.ot13 = string.maketrans( 
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
        self.test=serial.Serial("/dev/ttyAMA0",9600, timeout = 1)
        self.test.open()
        self.updateTime = t.time()

    def update(self):
        ct = t.time()
        if ct > self.updateTime:
            try:
                #print "attempting"
                line = test.readline()
                #inp = string.translate(line, rot13)
                self.value = int(line)
            except KeyboardInterrupt:
                pass
            self.updateTime = ct + 3

def camera():
    return Camera()

def IR(pin):
    return Input(pin)

def button(pin):
    return Input(pin)
