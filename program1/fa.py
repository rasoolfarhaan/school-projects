# Submitter: frasool(Rasool, Farhaan)
# Partner  : anudeeph(Hegde, Anudeep)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import goody
from pickle import NONE


def read_fa(file : open) -> {str:{str:str}}:
    dict1 = {}
    line = []
    innerdict = {}
    for lines in file:
        line.append(lines)
    file.close()
    for a in line:
        lines = a.rstrip().split(';')
        dict1[lines[0]] = {}
        for i in range(1, len(lines), 2):
            dict1[lines[0]][lines[i]] = lines[i + 1]
    return dict1
        


def fa_as_str(fa : {str:{str:str}}) -> str:
    str1 = ''
    for key,value in sorted(fa.items()):
        str1 += "  {} transitions: {}".format(str(key), str(sorted(value.items()))) + '\n'
    return str1
    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    list1 = []
    state1 = state
    for a in inputs:
        if a in fa[state1]:
            if len(list1) == 0:
                list1.append(state)
                list1.append((a, fa[state][a]))
                state1 = fa[state][a]
            else:
                list1.append((a, fa[state1][a]))
                state1 = fa[state1][a]
        else:
            list1.append((a, None))
    return list1


def interpret(fa_result : [None]) -> str:
    str1 = ""
    for a in fa_result:
        if len(str1) == 0:
                str1 += "Start state = " + str(a) + "\n"
        else:
            if a[1] == None:
                str1 += "  Input = " + str(a[0]) + "; illegal input: simulation terminated\n"
                state = a[1]
                break
            else:
                str1 += "  Input = " + str(a[0]) + "; new state = " + str(a[1]) + "\n"
                state = a[1]
    str1 += "Stop state = " + str(state) + "\n"
        
    return str1
        




if __name__ == '__main__':
    # Write script here
    files = goody.safe_open('Enter file with finite automaton', 'r', 'File cannot be found')
    file = read_fa(files)
    print('\nFinite Automaton Description\n'+ fa_as_str(file))
    fil = goody.safe_open('Enter file with start-states and inputs', 'r', 'File cannot be found')
    lines = []
    for line in fil:
        lines.append(line)
    fil.close()
    print('\nStarting new simulation')
    for a in lines:
        input = a.rstrip().split(';')
        inputs = process(file, input[0], input[1:])
        print(interpret(inputs))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
