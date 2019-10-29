poly = [1, 1, 2]
derivative = []
count= 1
for elements in poly:
    print(count)
    if elements != 0  and (poly[count] == 0) and count < len(poly) :
        derivative.append(0)
        print(derivative)

    elif elements == 0 and poly [count] != 0:
        derivative.append(count*poly[count])
        print(derivative)

    elif elements != 0 and poly [count-1] > 0:
        derivative.append(count*poly[count-1])
        print(derivative)
    if len(poly)-1> count:
        count=count+1
    else:
        poly.append(0)
        a=3
print(derivative)
