#Every 20 counts teleports to a random location on the board
from ball import Ball
from random import random
class Special(Ball):

    def __init__(self, x, y):
        self.counter = 0
        Ball.__init__(self, x, y)
    
    def update(self, model):
        if self.counter == 20:
            mw,mh    = model.world()
            w = int(random()*mw)
            h = int(random()*mh)
            self.set_location(w,h)
            self.counter = 0
        else:
            self.move()
            self.counter += 1