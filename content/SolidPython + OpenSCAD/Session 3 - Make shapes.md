## Session 3 - Make shapes

---
![[Pasted image 20250226150345.png]]


```python
from solid2.extensions.bosl2 import heightfield
import re

def get_data():
  from math import sqrt,sin
  data = []
  for y in range(50):
    yrow = []
    data.append(yrow)
    for x in range(50):
      yrow.append(sin(sqrt((y-25)**2+(x-25)**2)))
  return data

assembly = heightfield(size=[100,100], bottom=-1, data=get_data())

assembly.save_as_scad() #this fails in NixOS, delete this and uncomment below
'''
from solid2 import scad_render
rendered_string = re.sub(r'<.*BOSL2', '<BOSL2', scad_render(assembly))
with open("heightmap.scad","w") as file:
  file.write(rendered_string)
'''
```

---

## Code Ideas - Shape along a path


```python
#! /usr/bin/env python
from solid2.extensions.bosl2 import circle
path = [ [0, 0, 0], [33, 33, 33], [66, 33, 40], [100, 0, 0], [150,0,0] ]

assembly = circle(r=10, _fn=6).path_extrude(path)
assembly.save_as_scad()
```

![[Pasted image 20250226150506.png|300]]

---

## What do you want to make?


---

# Next Week
[[Session 4 - Print Art]]