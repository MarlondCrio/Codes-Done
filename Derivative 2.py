poly=[5403103293403]
derivative = []
count=1
if len(poly)== 1:
    print ([])
elif poly != []:
    for elements in poly:
        if len(poly) != count and count > 1:
            if elements != 0  and poly[count] == 0 : ##for when there is no exponent left but there still is list
                derivative.append(0)
                count= count + 1
            elif elements == 0 and poly [count] != 0:
                derivative.append(count*poly[count])
                count= count + 1
            elif elements != 0 and poly [count] != 0:
                derivative.append(count*poly[count])
                count= count + 1
            elif elements != 0  and poly[count] == 0 and (len(poly)> count):
                a=3
        elif elements == poly[0] and count == 1:
         
            derivative.append(poly[count])
            count = count + 1
        else:
            print(derivative)
else:
    print ([])
