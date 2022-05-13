# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Floater.radius*2, Floater.radius*2, 180, 5)
        self.randomize_angle()
        
    def update(self, model):
        if random()*10 > 7:
            self._speed += random()*10-5
            self._angle += random()*10-5
            if self._speed < 3:
                self._speed = 3
            elif self._speed > 7:
                self._speed = 7
            else:
                pass
        self.move()
        self.wall_bounce()
    
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill="RED")
