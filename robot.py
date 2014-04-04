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

sFront = Sonar(7, 7)
#sRight = Sonar(6, 6)
#sLeft = Sonar(5, 5)
#sLeft = Sonar(4, 4)

#define Motor Behaviors

def move(rSpeed, lSpeed):
    rMotor.set(rSpeed)
    lMotor.set(lSpeed)

#define special behaviors for avoidance

def avoidFront():
    move(-1600, -800)
    t.sleep(.5)
    move(1600, 1600)
    t.sleep(.25)

def turnToBeacon(deg):
    speed = 1600
    if deg > 89:
        deg -= 89*2
        speed *= -1
    move(speed, -speed)
    t.sleep(deg/89)

#define logic

def logic():
    if b.value is 200:
        move(0,0)
    elif b.value is 0:
        move(1600, 1600)
    elif b.value > 89:
        move(800, -800)
    else:
        move(-800, 800)

def dunes():
    if b.value < 170 or b.value > 10:
        turnToBeacon(b.value)
    elif sFront.value < .3:
        avoidFront()
    else:
        move(3000, 3000)

e = engine(logic, .25)

e.spin() 
