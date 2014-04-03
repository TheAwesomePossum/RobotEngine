'''
Author: Graham Montgomery

This is the main program for the robot, that will be set to run on boot.
We will move this time!
'''

# import engine
from Engine import *


# define Motors

rMotor = Motor('51FF-7106-4980-4956-5739-1387')
lMotot = Motor('51FF-6F06-4980-4956-2739-1387')

# define beacon

b = Beacon()

#define sensors
'''
uncomment lines after debugging
'''

#sFront = Sonar(7, 7)
#sRight = Sonar(6, 6)
#sBack = Sonar(5, 5)
#sLeft = Sonar(4, 4)

#define Motor Behaviors

def move(rSpeed, lSpeed):
    rMotor.set(rSpeed)
    lMotor.set(lSpeed)

#define logic

delta = 89 # used for turning

def logic():
    if b.value is 200:
        move(0,0)
    elif b.value is 0:
        move(1600, 1600)
    elif b.value > 89:
        move(800, -800)
    else:
        move(-800, 800)

engine(logic, .25)
        
    
