'''
Author: Graham Montgomery
Western State Colorado University

This is where the motor controllers will be defined along with anykind of output
'''

from PiFace import pi
import os # for speaking to the motor controllers

class Output:

    def __init__(self, pin):
        self.pin = pin + 1

    def set(self, out):
        pi.digital_write(self.pin, out)

def outpin(pin):
    return Output(pin)

class Motor:

    def __init__(self, serialpin):
        self.serialpin = serialpin

    def set(self, speed): 
        os.system('./SmcCmd -d ' + str(self.serialpin) + ' --speed ' + str(speed))

    def brake(self, power):
        os.system('./SmcCmd -d ' + str(self.serialpin) + ' --speed ' + str(power))

    def stop(self):
        os.system('./SmcCmd -d ' + str(self.serialpin) + ' --stop')
        
