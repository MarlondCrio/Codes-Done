tree={'value': 9,
 'children': [{'value': 2, 'children': []},
              {'value': 3, 'children': []},
              {'value': 7, 'children': []}]}

def is_flat(x):
    # returns True if the given list is flat (no nested lists), and False
    # otherwise.
    for i in x:
        if type(i) == list:
            return False
    return True

def flatten_list(x):
    if is_flat(x):
        # base case.  list is already flat, so return it.
        return x
    else:
        # recursive case.  initialize output list and loop over the elements.
        out = []
        for e in x:
            # for each element...
            if type(e) != list:
                # if the element is not a nested list, add it to the output
                # directly.
                out.append(e)
            else:
                # if the element is a nested list, flatten it and add the
                # elements from the flattened list to the output.
                f = flatten_list(e)
                for e2 in f:
                    out.append(e2)
        return out

## next steps use this model to fish out values of the dictionaries using a for loop
