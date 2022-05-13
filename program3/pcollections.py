# Submitter: frasool(Rasool, Farhaan)
# Partner  : Anudeeph(Hegde, Anudeep)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import re, traceback, keyword
from dataclasses import field

def pnamedtuple(type_name, field_names, mutable = False,  defaults =  {}):
    def show_listing(s):
        for line_number, text_of_line in enumerate(s.split('\n'),1):         
            print(f' {line_number: >3} {text_of_line.rstrip()}')

    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    class_definition = ""
    def valid(n):
        strings = r'^[a-zA-Z]\w*$'
        patterns = re.compile(strings)
        if patterns.match(str(n)) == None:
            raise SyntaxError()
        
        else:
            if type(n) is str and n not in keyword.kwlist:
                return True
            else:
                raise SyntaxError()

    def unique(container):
        list1 = []
        for i in container:
            if i not in list1:
                list1.append(i)
        return list1
    
    if not valid(type_name):
        raise SyntaxError()
    
    if type(field_names) is str:
        field_names = field_names.replace(',', ' ').split()
        list1 = []
        for word in unique(field_names):
            list1.append(word)
        
        for a in list1:
            if valid(a) == True:
                pass
            else:
                raise SyntaxError()
    
    elif type(field_names) is list:
        list1 = []
        for word in unique(field_names):
            list1.append(word)
        for a in list1:
            if valid(a) == True:
                pass
            else:
                raise SyntaxError()
            
    else:
        raise SyntaxError()
    
    class_definition += '''
class {type_name}:
    _fields = {_fields}
    _mutable = {_mutable}
    '''.format(type_name = type_name, _fields = list1, _mutable = mutable)
        
    class_definition += '''
    def __init__(self, {vars}):'''.format(vars = ', '.join(a + " = " + str(defaults[a]) if a in defaults else a for a in list1))
    for fieldvar in list1:
        class_definition += '''
        self.{fieldvar} = {fieldvar}'''.format(fieldvar = fieldvar)
    
   
    rep = '''
    
    def __repr__(self):
        return '{type_name}('''.format(type_name = type_name)
    for val in list1:
        rep += val + '={'+val+'},'
    rep = rep[0:-1] + ")'.format("
    for val in list1:
        rep += val + '=' + 'self.' + val + ','
    rep = rep[0:-1]
    class_definition += rep + ")"
    
    for x in list1:
        class_definition += '''
        
    def get_{x}(self):
        return self.{x}'''.format(x = x)
            
    class_definition += '''
    
    def __getitem__(self, var):
        if type(var) == int:
            if 0 <= var and var < len(self._fields):
                return eval("self.get_" + self._fields[var] + "()")
            else:
                raise IndexError('Int is out of bounds')
        
        elif type(var) != int and var in self._fields:
            return eval("self.get_" + var + "()")
            
        else:
            raise IndexError('string var does not name a field')'''
    
    class_definition += '''
    
    def __eq__(self, other):
        if type(other) == {type_name}:
            for a in self._fields:
                if self.__getitem__(a) != other.__getitem__(a):
                    return False
            
            return True
        else:
            return False'''.format(type_name = type_name)
            
    class_definition += '''
    
    def _asdict(self):
        return dict((x, self[x]) for x in self._fields)'''
    

    print(class_definition)
    
    
    
    
    
    
    
    
    # For initial debugging, always show the source code of the class
    #show_listing(class_definition)
    
    # Execute the class_definition string in a local name_space and bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   show the error
    name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name=type_name))
    try:
        exec(class_definition, name_space)
        name_space[type_name].source_code = class_definition
    except [TypeError, SyntaxError]:
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test simple pnamedtuple below in script: Point=pnamedtuple('Point','x,y')
    # Point = pnamedtuple('Point','x,y',mutable=True,defaults=dict(y=[4,'4'],x=0))

    #driver tests
    import driver  
    driver.default_file_name = 'bscp3W22.txt'
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
