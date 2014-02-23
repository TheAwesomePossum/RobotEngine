'''
Author: Graham Montgomery
Western State Colorado University

This holds the sensor super class for every sensor that is written into the 
Engine. It also holds a list of every sensor that is dieclared for an individual 
project to be used by the Engine heartbeat.
'''

from Engine import pi, t
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
    
    # update will be used by every sensor to update it's value every tick
    def update():
        pass

    # will be used to get the current value of the sensor
    def get_v():
        pass

class Input(Sensor):

    def __init__(self, pin):
        Sensor.__init__(self)
        self.pin = pin + 1
        self.value = 0

    def update(self):
        self.value = pi.digital_read(self.pin)

    def get_v(self):
        return self.value

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

def camera():
    return Camera()

def IR(pin):
    return Input(pin)

def button(pin):
    return Input(pin)
