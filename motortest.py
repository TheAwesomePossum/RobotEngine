from LMotors import Motor

r = Motor('51FF-7106-4980-4956-5739-1387')
l = Motor('51FF-6F06-4980-4956-2739-1387')

def move(speedl, speedr):
    r.set(speedr)
    l.set(speedl)

def fullfor():
    r.set(-1600)
    l.set(-1600)

def fullback():
    r.set(1600)
    l.set(1600)

def left():
    r.set(-1600)
    l.set(1600)

def right():
    r.set(1600)
    l.set(-1600)

def stop():
    r.stop()
    l.stop()
