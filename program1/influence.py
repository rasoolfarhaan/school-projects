# Submitter: frasool(Rasool, Farhaan)
# Partner  : anudeeph(Hegde, Anudeep)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import prompt
from goody       import safe_open
from math        import ceil 
from collections import defaultdict
from pickle import TRUE


def read_graph(open_file : open) -> {str:{str}}:
    dict1 = defaultdict(set)
    list1 = []
    line = []
    for lines in open_file:
        line.append(lines)
    open_file.close()
    line = [a.strip() for a in line]
    for a in line:
        if ";" in a:
            lines = a.split(";")
            list1.append((lines[0], lines[1]))
        else:
            list1.append(a)
    for a in list1:
        if type(a) is tuple:
            dict1[a[0]].add(a[1])
            dict1[a[1]].add(a[0])
        else:
            dict1[a[0]]
    return dict1
        

def graph_as_str(graph : {str:{str}}) -> str:
    # str1 = "  "
    # for a, b in sorted(graph.items()):
    #     str1 += str(a) + ' -> ' + str(sorted(b)) + '\n  '
    # return str1[0:-2]
    multistring = ''
    for key, value in sorted(graph.items()):
        multistring += "  {} -> {}".format(str(key), str(sorted(value))) + '\n'
    return multistring


def find_influencers(graph : {str:{str}}, trace : bool = False) -> {str}:
    infl_dict = {}
    for a, b in graph.items():
        if len(b) != 0:
            infl_dict[a] = [len(b)-ceil(len(b)/2), len(b), a]
        else:
            infl_dict[a] = [-1, 0, a]
    removal_list = []
    for b in infl_dict.values():
        if b[0] >= 0:
            removal_list.append(tuple(b))
    while len(removal_list) > 0:
        if trace:
            print("influencer dictionary =", infl_dict)
            print("removal candidates", removal_list)
        minimum = min(removal_list)
        for a in removal_list:
            if a[0] < 0:
                removal_list.remove(a)
        if trace:
            print(minimum, "is the smallest candidate")
            print('Removing', minimum[2], "as key from influencer dictionary; decrementing every friend's value\n")
        removal_list.remove(minimum)
        del infl_dict[minimum[2]]
        var = graph[minimum[2]]
        for a in var:
            if a in infl_dict:
                infl_dict[a][0] -= 1
                infl_dict[a][1] -= 1
        removal_list = []
        for b in infl_dict.values():
            if b[0] >= 0:
                removal_list.append(tuple(b))
    if trace:
        print("influencer dictionary =", infl_dict)
        print("removal candidates", removal_list)
    set1 = set()
    for a in infl_dict:
        set1.add(a)
    return set1

def all_influenced(graph : {str:{str}}, influencers : {str}) -> {str}:
    n_dict = {}
    tval = len(influencers)
    for key, value in graph.items():
        if key in influencers:
            n_dict[key] = True
        else:
            n_dict[key] = False

    f_dict = {}
    while f_dict != n_dict:
        for key, value in graph.items():
            if n_dict[key] == False:
                count = 0
                for val in value:
                    friends = len(graph[key])
                    needed = ceil(friends/2)
                    if n_dict[val] == True:
                        count += 1
                    if count >= needed:
                        n_dict[key] = True
            f_dict = n_dict.copy()
    set1 = set()
    for a, b in n_dict.items():
        if n_dict[a] == True:
            set1.add(a)

    for key, value in graph.items():
        if n_dict[key] == False:
            count = 0
            for val in value:
                friends = len(graph[key])
                needed = ceil(friends/2)
                if n_dict[val] == True:
                    count += 1
                if count >= needed:
                    set1.add(key)
    return set1


       
            
    
if __name__ == '__main__':
    # Write script here
    files = safe_open("Select a file storing a friendship graph", 'r', 'File cannot be found')
    influence = read_graph(files)
    print("Graph: person -> [sorted friends of person]\n" + graph_as_str(influence)) 
    tracer = prompt.for_string("Select Tracing of Execution[true]: ")
    print()
    if tracer == "True":
        tracer1 = True
    else:
        tracer1 = False
    
    print("The influencers set calculated is", find_influencers(influence, tracer1))
    
    while True:
        input1 = input("Select a subset of persons(or enter done to stop)[{'g', 'k', 'd'}]: ")
        if input1 == 'done':
            break
        else:
            percent = (len(all_influenced(influence, input1))/len(influence)) * 100
            print("People influenced by selected subset", "({})".format(percent), '=', all_influenced(influence, input1))
    
    # For running batch sef-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()

