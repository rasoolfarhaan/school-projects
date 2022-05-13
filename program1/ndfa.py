import goody
from collections import defaultdict
from multiprocessing.managers import State

def read_ndfa(file : open) -> {str:{str:{str}}}:
    dict2 = {}
    list1 = []
    for open_file in file:
       list1.append(open_file)
    file.close()
    for a in list1:
        lines = a.rstrip().split(";")
        if len(lines) > 1:
            dict1 = defaultdict(set)
            for i in range(1, len(lines), 2):
                dict1[lines[i]].add(lines[i+1])
            dict2[lines[0]] = dict1
        else:
            dict2[lines[0]] = {}
    return dict2


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    str1 = ""
    p_str = ''
    for key in sorted(ndfa):
        p_str += '  ' + str(key) + ' transitions: ['
        for num in sorted(ndfa[key]):
            p_str += '(' + "'" + str(num) + "',"
            p_str += ' ' + str(sorted(ndfa[key][num])) + '), '
        
        p_str = p_str.rstrip(', ')
        p_str += ']\n'
    return p_str       

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    list1 = [state]
    next = set()
    next.add(state)
    for i in inputs: 
        last = set()
        for x in next:
            if i in ndfa[x]:
                curr = last
                for a in ndfa[x][i]:
                    curr.add(a)
                last = curr 
        next = last
        if len(next) == 0:
            list1.append((i,set())) 
            break
        else:
            list1.append((i,next))      
    return list1  

def interpret(result : [None]) -> str:
    print(result)
    
    r_str = ''
    r_str += 'Start state = ' + result[0] + '\n'
    
    for num in range(1, len(result)):
        r_str += '  Input = ' +  str(result[num][0]) + '; new possible states = ' +  str(sorted(result[num][1])) + '\n'
    r_str += "Stop state(s) = " + str(sorted(result[-1][1])) + "\n"
    return r_str
    
    
    
    
    
    





if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
