from solid2 import *

valid = False
while not valid:
    name = input("What is your Name? ")
    valid = len(name) > 2 and len(name) < 10

length = (len(name) * 7.5) + 7.5
shape = cube(length, 12, 1) - text(text=name).translate(5, 1, 1)
shape -= cylinder(3,1,1,True).translate(2, 8, 0)
shape.save_as_scad()