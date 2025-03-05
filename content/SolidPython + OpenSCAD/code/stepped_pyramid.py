#Stepped Pyramid
from solid2 import *
assembly = cube(0,0,0)

levels = 5
for i in range(0, levels):
    side = (i+1) * 2
    c = cube(side, side, 1)
    assembly +=  c.translate(-side/2, -side/2, (levels-i)-1)
    #assembly +=  c.up((levels-i)-1).left(side/2).back(side/2) # Does the same thing

assembly.save_as_scad()