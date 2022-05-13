import controller
import model   # Calling update in update_all passes a reference to this model

# Use the reference to this module to pass it to update methods

from ball       import  Ball
from blackhole  import  Black_Hole
from floater    import  Floater
from hunter     import  Hunter
from pulsator   import  Pulsator
from concurrent.futures._base import RUNNING
from special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
objects = set()
kinds = ""



#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,objects
    running = False
    cycle_count = 0
    objects = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count
    global running
    running = False 
    cycle_count += 1
    for a in objects:
        a.update(model)


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global kinds
    kinds = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global kinds
    if kinds == "Remove":
        objects_copy = objects.copy()
        for a in objects_copy:
            if a.contains([x, y]):
                remove(a)
    else:
        str_object = str(kinds) + "({},{})".format(str(x),str(y))
        object = eval(str_object)
        add(object)
                

#add simulton s to the simulation
def add(s):
    objects.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    objects.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    set1 = set()
    for a in objects:
        if isinstance(a, p):
            set1.add(a)
    return set1


#Simulation: for each simulton in the model, call its update, passing it model
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's update do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def update_all():
    objects_copy = objects.copy()
    global cycle_count
    global running 
    if running == True:
        cycle_count += 1
        for a in objects_copy:
            a.update(model)
#Animation: clear then canvas; for each simulton in the model, call display
#  (a) delete all simultons on the canvas; (b) call display on all simultons
#  being simulated, adding back each to the canvas, often in a new location;
#  (c) update the label defined in the controller showing progress 
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's display do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    for b in objects:
        b.display(controller.the_canvas)
    controller.the_progress.config(text=str(len(objects))+" simultons/"+str(cycle_count)+" cycles")
