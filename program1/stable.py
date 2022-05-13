# Submitter: frasool(Rasool, Farhaan)
# Partner  : anudeeph(Hegde, Anudeep)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import prompt
import goody

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    dict1 = {}
    line = []
    for lines in open_file:
        line.append(lines)
    open_file.close()
    for a in line:
        lines = a.rstrip().split(';')
        dict1[lines[0]] = [None]
        dict1[lines[0]].append(lines[1:])
    return dict1
    

def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    multistring = ''
    for key in sorted(d, key = key, reverse = reverse):
        multistring += "  {} -> {}".format(str(key), str(d[key])) + '\n'
    return multistring


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    index1 = order.index(p1)
    index2 = order.index(p2)
    if index1 < index2:
        return p1
    else:
        return p2


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    set1 = set()
    for a, b in men.items():
        set1.add((a, b[0]))
    return set1

def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    men1 = men.copy()
    women1 = women.copy()
    set1 = set()
    list1 = []

    for a in men1:
        set1.add(a)

    for x, y in men.items():
        if (men1[x][0] == None) and (y[1][0] not in list1):
            c = set1.pop()
            for key, value in men1.items():
                for val in value[1]:
                    for w in women1[val]:
                        if w == None:
                            if men1[key][0] == None:
                                men1[key][0] = val
                                women1[val][0] = key
                        if w != None:
                            current = women1[val][0]
                            new = key
                            for fiance, person in women1.items():
                                if current != None:
                                    if person[1].index(new) < person[1].index(current):
                                        men1[new][0] = val
                                        women1[val][0] = new
                                        men1[current][0] = None
                                        set1.add(current)
                                    else:
                                        set1.add(new)
                                else:
                                    men1[new][0] = val
                                    women1[val][0] = new
                                    set1.add(current)
        
  


  
    
if __name__ == '__main__':
    # Write script here      
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
