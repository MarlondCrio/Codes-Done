def warehouse_process(x,y):
    if y[1] in x.keys():
        if y[0] == 'receive':
            x[(y[1])] += y[2]

        elif y[0] == 'ship':
            x[(y[1])] -= y[2]
            
    elif y[1] not in x.keys():
        x[y[1]] = y[2]

    return x 
