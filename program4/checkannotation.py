# Submitter: frasool(Rasool, Farhaan)
# Partner  : Anudeeph(Hegde, Anudeep)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation:
    # Initially bind the class attribute to True allowing checking to occur (but
    #   only if the object's self._checking_on attribute is also bound to True)
    checking_on  = True
  
    # Initially bind self._checking_on = True, to check the decorated function f
    def __init__(self, f):
        self._f = f
        self._checking_on = True

    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Initially compare check's function annotation with its arguments
        def checklist(types):
            assert isinstance(value, types), "'" + check_history + "' failed annotation check(wrong type): value = " + str(value) + ' was type ' + type_as_str(value) + ' ...should be type ' + str(type(annot).__name__)
            if len(annot) == 1:
                for a in value:
                    self.check(param, annot[0], a, check_history)
            else:
                assert len(annot) == len(value), "'" + check_history + "' failed annotation check(wrong type): value = " + str(value) + ' was type ' + type_as_str(value) + ' ...should be type ' + str(type(annot).__name__)
                for a in value:
                    self.check(param, annot[value.index(a)%len(annot)], a, check_history)
                    
        def checkdict(types):
            assert isinstance(value, types), "'" + check_history + "' failed annotation check(wrong type): value = " + str(value) + ' was type ' + type_as_str(value) + ' ...should be type ' + str(type(annot).__name__)
            if len(annot) == 1:
                for a, b in annot.items():
                    for c, d in value.items():
                        self.check(param,a, c, check_history)
                        self.check(param,b, d, check_history)
            else:
                raise AssertionError("'" + check_history + "' annotation inconsistency: dict should have 1 item but had " + str(len(annot)) + "\n    annotation = " + str(annot))
            
        def checkset(types):
            assert isinstance(value, types), "'" + check_history + "' failed annotation check(wrong type): value = " + str(value) + ' was type ' + type_as_str(value) + ' ...should be type ' + str(type(annot).__name__)
            if len(annot) == 1:
                for a in annot:
                    for b in value:
                        self.check(param, a, b, check_history)
            else:
                if types == set:
                    raise AssertionError("'" + check_history + "' annotation inconsistency: set should have 1 value but had " + str(len(annot)) + "\n    annotation = " + str(annot))
                if types == frozenset:
                    raise AssertionError("'" + check_history + "' annotation inconsistency: frozenset should have 1 value but had " + str(len(annot)) + "\n    annotation = " + str(annot))
                
        def checklambda():
            assert len(annot.__code__.co_varnames), "'" + check_history + "' annotation inconsistency: predicate should have 1 parameter but had " + str(annot.__code__.co_argcount) + '\n  Predicate = ' + str(annot)
            try:
                val = annot(value)
            except:
                raise AssertionError("'" + check_history + "' failed annotation check: value = " + str(value) + '\n  Predicate = ' + str(annot))
            else:
                assert val, "'" + check_history + "' failed annotation check: value = " + str(value) + '\n  Predicate = ' + str(annot)
            
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
        if annot == None:
            pass
        elif type(annot) is type:
            assert isinstance(value, annot), "'" + check_history + "' failed annotation check(wrong type): value = " + str(value) + ' was type ' + type_as_str(value) + ' ...should be type ' + str(annot.__name__) 
        elif type(annot) is list:
            checklist(list)
        elif type(annot) is tuple:
            checklist(tuple)
        elif type(annot) is dict:
            checkdict(dict)
        elif type(annot) is set:
            checkset(set)
        elif type(annot) is frozenset:
            checkset(frozenset)
        elif inspect.isfunction(annot):
            checklambda()
        else:
            try:
                annot.__check_annotation__(self.check, param, value, check_history)
            except AttributeError:
                raise AssertionError("'" + check_history + "' annotation undecipherable: " + str(annot))
            except:
                raise AssertionError("'" + check_history + "' annotation protocol(" + str(annot) + ") raised exception")
            
    def __call__(self, *args, **kargs):
        
        # Return argument/parameter bindings in an OrderedDict (derived from a
        #   regular dict): bind the function header's parameters with that order
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if not (param.name in bound_f_signature.arguments):
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        
        try:
        # For each detected annotation, check it using its argument's value
            
        #The param_arg_bindings function (written locally in this method) returns an 
        #ordered dictionary of parameter/value bindings;
            
            ordereddict = param_arg_bindings()
            
            for key, value in self._f.__annotations__.items():
                kstring = str(key) # only saved in case of recursions or key == return 
                if key == "return": #must be converted to str(_return)
                    pass
                else:
                    #Peuntes - Key is often/always string, so is param and check_history
                    self.check(key, value, ordereddict[key], kstring)
                    
                    #When param: param = key, SyntaxError: positional argument follows keyword argument
                    
            # Compute/remember the value of the decorated function
            
            # If 'return' is in the annotation, check it - Self Note: does Check mean the method Check?
            for key in self._f.__annotations__:
                if key == 'return':
                    self.check("_return", self.__f__annotations__["return"], self._f(args))
            # Return the decorated answer
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            # print(80*'-')
            # for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
            #     print(l.rstrip())
            # print(80*'-')
            raise
  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
    # def f(x:int): pass
    # f = Check_Annotation(f)
    # f(3)
    # f('a')
        
    #driver tests
    import driver
    driver.default_file_name = 'bscp4W22.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
