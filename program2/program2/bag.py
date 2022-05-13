# Submitter: frasool(Rasool, Farhaan)
# Partner  : Anudeeph(Hegde, Anudeep)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
from collections import defaultdict
from goody import type_as_str
import prompt
from pickle import TRUE, FALSE

class Bag:
    
    def __init__(self, ival = []):
        self.bag = defaultdict(int)
    
        for things in ival:
            self.bag[things] += 1
            
    def __str__(self):
        string1 = 'Bag('
        for key, value in self.bag.items():
            string1 += '.'.join(str(key)) + '[' + str(value) + ']'
        string1 += ')'
        return string1
    
    def __repr__(self):
        list1 = []

        for key, value in self.bag.items():
            e = key * value
            list1.extend(list(e))

        string1 = 'Bag({})'.format(list1)

        return string1
    
    def __len__(self):
        return sum(self.bag.values())
    
    
    def unique(self):
        return len(self.bag.keys())
    
    def __contains__(self, con):
        if con in self.bag:
            return True 
        else:
            return False
    
    def count(self, string2):
        if string2 in self.bag:
            return int(self.bag[string2])
        else:
            return 0

    def add(self, string2):
        self.bag[string2] += 1

    def __add__(self, bag2):
        if type(bag2) is not Bag:
            raise TypeError()
        lst1 = []
        lst2 = []
        for v in self.bag:
            for i in range(self.bag[v]):
                lst1.append(v)
        for v in bag2.bag:
            for i in range(bag2.bag[v]):
                lst2.append(v)
        return Bag(lst1 + lst2)
    
    def remove(self, val):
        if val in self.bag:
            self.bag[val] -= 1
            if self.bag[val] == 0:
                del self.bag[val]
        else:
            raise ValueError
        
    def __eq__(self, right):
        if type(right) != Bag:
            return False
        if self.bag == right.bag:
            return True 
        else:
            return False 
    
    def __ne__(self, right):
        if type(right) != Bag:
            return True
        if self.bag != right.bag:
            return True 
        else:
            return False
        
    def __iter__(self):
        for a,b in self.bag.items():
            for c in range(b):
                yield a
        


if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test Bag before doing the bsc tests
    #Debugging problems with these tests is simpler

    b = Bag(['d','a','d','b','c','b','d'])
    print(repr(b))
    print(all((repr(b).count('\''+v+'\'')==c for v,c in dict(a=1,b=2,c=1,d=3).items())))
    for i in b:
        print(i)
    
    b2 = Bag(['a','a','b','x','d'])
    print(repr(b2+b2))
    print(str(b2+b2))
    print([repr(b2+b2).count('\''+v+'\'') for v in 'abdx'])
    b = Bag(['a','b','a'])
    print(repr(b))
    # print()
    
    import driver
    driver.default_file_name = 'bscp21W22.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
