# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
from pickle import FALSE, NONE


class Hunter(Pulsator, Mobile_Simulton):
    prey_dist = 200
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self.radius, self.radius, 180, 5)
        self.randomize_angle()
        
    def update(self, model):
        list1 = []
        for prey in model.find(Prey):
            if self.distance(prey.get_location()) <= self.prey_dist:
                list1.append(prey)
        
        if len(list1) != 0:
            m = 250
            f_prey = None
            for prey in list1:
                if self.distance(prey.get_location()) <= m:
                    f_prey = prey
                    m = self.distance(prey.get_location())
              
            if f_prey is not None:      
                self.set_angle(atan2(f_prey.get_location()[1] - self.get_location()[1], f_prey.get_location()[0] - self.get_location()[0]))

        
        
        
        self.move()
        return Pulsator.update(self,model)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        