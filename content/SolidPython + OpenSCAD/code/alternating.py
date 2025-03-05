from solid2 import *
assembly = cube(0,0,0)
levels = 5
for i in range(levels, 0, -1):
    side = (i+1) * 2
    c = cube(side, side, side/2).translate(-side/2, -side/2, (levels-i)-1)
    if (i % 2):
        assembly +=  c
    else:
        assembly -=  c
assembly.save_as_scad()