from solid2 import *

valid = False
while not valid:
    name = input("What is your Name? ")
    valid = len(name) > 2 and len(name) < 10

shape = cube(50, 12, 1) - text(text=name).translate(1, 1, 1)
shape.save_as_scad()