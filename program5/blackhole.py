# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    def __init__(self, x, y):
        self.radius = 10
        Simulton.__init__(self, x, y, self.radius*2, self.radius*2)
    def contains(self, xy):
        return self.distance(xy) <= self.radius
   
    def update(self, model):
        grubbed = set()
        for a in model.find(Prey):
            if self.contains(a.get_location()):
                grubbed.add(a)
        for a in grubbed:
            model.remove(a)
        return grubbed
    
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill="BLACK")
        
