## Session 3 - Make shapes

---

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



---

# Next Week
[[Session 4 - Print Art]]