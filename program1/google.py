# Submitter: frasool(Rasool, Farhaan)
# Partner  : anudeeph(Hegde, Anudeep)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    set1 = set()
    li = []
    for x in fq:
        li.append(x)
        set1.add(tuple(li))
    return set1


def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    query[new_query] += 1
    add_query = all_prefixes(new_query)
    for a in add_query:
        prefix[a].add(new_query)
            


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    prefix = defaultdict(set)
    query = defaultdict(int)
    for a in open_file:
        message = tuple(a.rstrip().split(" "))
        add_query(prefix, query, message)
    open_file.close()
    return tuple((prefix, query))


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    str1 = ""
    for key1 in sorted(d, key = key, reverse = reverse):
        str1 += "  " + str(key1) + " -> " + str(d[key1]) + "\n"
    return str1

def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    if a_prefix not in prefix:
        return []
    else:
        list1 = []
        for a in prefix[a_prefix]:
            list1.append(a)
        list1 = sorted(list1, key = lambda x: (query[x], -len(x)), reverse = True)
        return list1[0:n]

# Script

if __name__ == '__main__':
    # Write script here
    file1 = safe_open("Select a file storing multiple full queries", 'r', "File not there")
    read = read_queries(file1)
    print("Prefix dictionary:\n" + dict_as_str(read[0], lambda x : (len(x),x), False))
    print("Query dictionary:\n" + dict_as_str(read[1], lambda x : (-1*read[1][x], x), False))
    while True:
        input1 = prompt.for_string("Select a single prefix sequence (or done to stop)")
        if input1 == "done":
            break
        else:
            print("Matching full queries (up to 3; High->Low frequency) =", top_n(tuple(input1.rstrip().split(" ")), 3, read[0], read[1]))
        input2 = prompt.for_string("Select a single full query sequence (or done to stop)")
        if input2 == "done":
            break
        else:
            add_query(read[0], read[1], tuple(input2.rstrip().split(" ")))
            print("Prefix dictionary:\n" + dict_as_str(read[0], lambda x : (len(x),x), False))
            print("Query dictionary:\n" + dict_as_str(read[1], lambda x : (-1*read[1][x], x), False))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
