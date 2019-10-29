erry=[]

tree={'value': 9,
 'children': [{'value': 2, 'children': []},
              {'value': 3, 'children': []},
              {'value': 7, 'children': []}]}
a = []
def list_search(x):
    global a
    for y in x:
        if type(y) == list:
            list_search(y)
        else:
            a.append(y)
    return a
d = []
def search(x):
    def list_search(x):
        global d
        for y in x:
            if type(y) == list:
                list_search(y)
            else:
                d.append(y)
        return d

    a = list(x.values())
    for y in a:
        if type(y) == dict:
            search(y)
        elif type(y) == list:
            list_search(y)
                
        elif type(y) == int:
            erry.append(y)
        else:
            pass
    return erry
Tree ={'value': 13,
 'children': [{'value': 7, 'children': []},
              {'value': 8,
               'children': [{'value': 99, 'children': []},
                            {'value': 16,
                             'children': [{'value': 77, 'children': []}]},
                            {'value': 42, 'children': []}]}]}
print(list_search(Tree.values()))
