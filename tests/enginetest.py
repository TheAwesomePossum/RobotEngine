from Engine import *

global e
b1 = button(0)
b2 = button(1)
b3 = button(2)
b4 = button(3)
l1 = light(7)
l2 = light(6)
l3 = light(5)
b = Beacon()

def logic():
    print b.value
    l1.set(b1.value)
    l2.set(b2.value)
    l3.set(b3.value)
    if b4.value == 1:
        e.stop()

e = engine(logic, .1)
e.spin()
