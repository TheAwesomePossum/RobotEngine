'''
Author: Graham Montgomery

This holds the sensor super class for every sensor that is written into the 
Engine. It also holds a list of every sensor that is dieclared for an individual 
project to be used by the Engine heartbeat.
'''

from Engine import pi

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

def IR(pin):
    return Input(pin)

def button(pin):
    return Input(pin)
