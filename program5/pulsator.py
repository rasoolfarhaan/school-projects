# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    counter = 30
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.time_between_meals = 0
        
    def update(self, model):
        the_set = Black_Hole.update(self, model)
        if len(the_set) > 0:
            self.time_between_meals = 0
            self.radius += 1
        else:
            self.time_between_meals += 1
            if self.time_between_meals == self.counter:
                self.radius -= 1
                self.time_between_meals = 0
            
        if self.radius == 0:
            the_set.add(self)
            model.remove(self)
        
        return the_set
                