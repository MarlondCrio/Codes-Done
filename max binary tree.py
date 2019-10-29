a =[]
import sys
sys.setrecursionlimit(100000)
def binary_tree_max(tree):
    global a
    a.append(tree['value'])
    for x in tree['children'] :
        if x != []:
             binary_tree_max(x)
    
    return max(a)

