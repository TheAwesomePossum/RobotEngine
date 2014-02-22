'''
Author: Graham Montgomery

This is where the motor controllers will be defined along with anykind of output
'''

from Engine import pi

class Output:

    def __init__(self, pin):
        self.pin = pin + 1

    def set(self, out):
        pi.digital_write(self.pin, out)

def light(pin):
    return Output(pin)
