def second_largest_number(x):           ##Function
    count = 0
    if len(x) <= 1:                     ## If for when nothing or just one value
        return (None)

    else:
        best = 0
        secondbest = 0
        lowest = 0
        for elements in x:              ##finding lowest as reference point
            if elements < 0:
                lowest = elements
            else:
                pass
        for pings in x:
            if  pings > best: 
                best = pings
        secondbest = lowest
        for tings in x:
            if tings > secondbest and tings < best:
                secondbest = tings

        for items in x:
            if items == best:
                count = count + 1
            else:
                pass
            
        if count <= 1:
            secondbest = secondbest
        else:
            secondbest = best
    return secondbest

print(second_largest_number([]))
print(second_largest_number([2]))
print(second_largest_number([94, 87, 20, 35]))
print(second_largest_number([1, 2, 3, 3, 3]))
print(second_largest_number([20,100,-100, -1, -10]))
